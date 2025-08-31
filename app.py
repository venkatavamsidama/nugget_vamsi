from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os
import tiktoken

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    st.error("GOOGLE_API_KEY environment variable is not set.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=google_api_key)

st.title("💼 LinkedIn Post Generator (Gemini 1.5 Flash)")

# Function to count tokens using tiktoken (using a GPT-like encoding)
def count_tokens_exact(text, model_encoding="cl100k_base"):
    encoding = tiktoken.get_encoding(model_encoding)
    tokens = encoding.encode(text)
    return len(tokens)

# Function to calculate exact tokens and cost (cost_rate per 1,000 tokens)
def compute_exact_tokens_and_cost(text, cost_rate=0.03):
    token_count = count_tokens_exact(text)
    estimated_cost = (token_count / 1000) * cost_rate
    return token_count, estimated_cost

# Multi-step: Planning phase for post structure
def plan_post_structure(topic, tone, audience, length, post_format, additional_details, hashtags, cta, industry, goal):
    plan_prompt = f"""
You are an expert LinkedIn strategist. Based on the following details, outline a clear structure for a LinkedIn post that maximizes engagement.

Inputs:
- Topic: {topic}
- Tone: {tone}
- Audience: {audience if audience else "General professional audience"}
- Length: {length}
- Post Format: {post_format}
- Additional Details: {additional_details if additional_details else "None"}
- Hashtags: {hashtags if hashtags else "Generate relevant hashtags"}
- Call-to-Action: {cta if cta else "Generate an engaging CTA"}
- Industry/Niche: {industry if industry else "General"}
- Primary Goal: {goal}

Please produce an outline with the following sections in bullet points:
• Hook
• Key Content/Points
• Call-to-Action or Engagement Tactic
• Best Posting Time Suggestion
"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        plan_response = model.generate_content(
            plan_prompt,
            generation_config={"temperature": 0.7}
        )
        if plan_response.candidates:
            return "".join(
                [cand.content.parts[0].text for cand in plan_response.candidates if cand.content.parts]
            ).strip()
        else:
            return "No plan generated."
    except Exception as e:
        return f"Error generating plan: {e}"

# Multi-step: Drafting phase that uses the outline plan from above
def generate_linkedin_posts(topic, tone, audience, length, post_count, additional_details, hashtags, cta, post_format, industry, goal):
    # Step 1: Generate a post outline first
    plan = plan_post_structure(topic, tone, audience, length, post_format, additional_details, hashtags, cta, industry, goal)
    
    # Step 2: Use the outline to generate complete posts
    draft_prompt = f"""
You are an expert LinkedIn strategist. Use the outline below to generate {post_count} complete LinkedIn posts.

Outline:
{plan}

Now, based on this outline and the details provided, generate the posts with the following inputs:

- Topic: {topic}
- Tone: {tone}
- Audience: {audience if audience else "General professional audience"}
- Length: {length}
- Post Format: {post_format}
- Additional Details: {additional_details if additional_details else "None"}
- Hashtags: {hashtags if hashtags else "Generate relevant hashtags"}
- Call-to-Action: {cta if cta else "Generate an engaging CTA"}
- Industry/Niche: {industry if industry else "General"}
- Primary Goal: {goal}

Output the posts in exactly the following format for each post:

===POST===
Title: <Post Title>
Content: <Main post content>
Strategy: <Explanation on engagement tactic>
Best Posting Time: <Suggestion for posting time>
===ENDPOST===
"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            draft_prompt,
            generation_config={"temperature": 0.8}
        )
        if response.candidates:
            return "".join(
                [cand.content.parts[0].text for cand in response.candidates if cand.content.parts]
            ).strip()
        else:
            return "No result generated."
    except Exception as e:
        return f"Error generating posts: {e}"

# Initialize chat history if not already in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Inputs
topic = st.text_input("Enter your topic (required):", "")
tone = st.selectbox("Select the tone of your post:", [
    "Professional", "Casual", "Formal", "Friendly",
    "Inspirational", "Educational", "Thought-provoking"
])
audience = st.text_input("Enter your target audience:", "")
length = st.radio("Select post length:", [
    "Short (50-100 words)", "Medium (100-200 words)", "Long (200-300 words)"
])
post_format = st.selectbox("Select post format:", [
    "Story/Narrative", "List/Tips", "Question/Discussion",
    "Industry Insight", "Personal Experience", "How-to Guide", "Opinion/Commentary"
])
post_count = st.number_input("Number of posts to generate:", min_value=1, max_value=10, value=3, step=1)
additional_details = st.text_area("Additional details or context:")
hashtags = st.text_input("Suggested hashtags (comma separated):", "")
cta = st.text_input("Call-to-action (optional):", "")
industry = st.text_input("Your industry/niche (optional):", "")
goal = st.selectbox("Primary goal of the post:", [
    "Generate engagement", "Share knowledge", "Build thought leadership",
    "Promote content/service", "Start a discussion", "Share personal experience"
])

if st.button("🚀 Generate LinkedIn Posts"):
    if not topic:
        st.error("⚠️ Please enter a topic.")
    else:
        with st.spinner("✨ Crafting engaging LinkedIn posts..."):
            result = generate_linkedin_posts(
                topic, tone, audience, length, post_count,
                additional_details, hashtags, cta, post_format, industry, goal
            )
            # Compute exact tokens and cost for the generated result
            token_count, cost = compute_exact_tokens_and_cost(result)
            # Save conversation history with token and cost info
            st.session_state.chat_history.append({
                "topic": topic,
                "result": result,
                "tokens": token_count,
                "cost": cost
            })

            # Split posts by the delimiter
            raw_posts = result.split("===POST===")
            posts = []
            for raw in raw_posts:
                if "===ENDPOST===" in raw:
                    post_content = raw.split("===ENDPOST===")[0].strip()
                    if post_content:
                        posts.append(post_content)

            if posts:
                for i, post in enumerate(posts, start=1):
                    st.subheader(f"📝 Post {i}")
                    # Extract sections with fallback in case formatting is off
                    title = ""
                    content = ""
                    strategy = ""
                    posting_time = ""
                    for line in post.splitlines():
                        if line.startswith("Title:"):
                            title = line.replace("Title:", "").strip()
                        elif line.startswith("Content:"):
                            content = line.replace("Content:", "").strip()
                        elif line.startswith("Strategy:"):
                            strategy = line.replace("Strategy:", "").strip()
                        elif line.startswith("Best Posting Time:"):
                            posting_time = line.replace("Best Posting Time:", "").strip()
                    display_text = f"**{title}**\n\n{content}\n\n*Strategy:* {strategy}\n\n*Best Posting Time:* {posting_time}"
                    st.text_area(f"Post {i} Content", display_text, height=200, key=f"post_{i}")
                    st.button(f"📋 Copy Post {i}", key=f"copy_{i}", help="Copy this post manually")
                    st.divider()
            else:
                st.subheader("📝 Generated Content")
                st.text_area("Generated Content:", result, height=400)

# Sidebar: Display chat history with exact tokens and cost
with st.sidebar:
    st.header("💬 Chat History")
    if st.session_state.chat_history:
        for idx, chat in enumerate(reversed(st.session_state.chat_history), start=1):
            tokens = chat.get("tokens", 0)
            cost = chat.get("cost", 0)
            st.markdown(f"**Chat {idx}:** Topic – {chat['topic']}")
            st.markdown(f"*Exact Tokens:* {tokens} | *Est. Cost:* ${cost:.4f}")
            st.text_area("Result", chat["result"], height=150, key=f"history_{idx}")
            st.divider()
    else:
        st.write("No chats yet. Generate a post to see history.")