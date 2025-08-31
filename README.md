# 💼 LinkedIn Post Generator

A powerful Streamlit application that generates engaging LinkedIn posts using Google's Gemini 1.5 Flash AI model.

## ✨ Features

- **AI-Powered Generation**: Uses Google Gemini 1.5 Flash for intelligent post creation
- **Multi-Step Process**: First plans post structure, then generates complete posts
- **Customizable Inputs**: Topic, tone, audience, length, format, hashtags, call-to-action
- **Token Tracking**: Shows exact token usage and estimated costs
- **Chat History**: Keeps track of all generated posts
- **Multiple Formats**: Story, list, question, industry insight, personal experience, how-to, opinion

## 🚀 Live Demo

[Deployed on Streamlit Cloud](https://your-app-name.streamlit.app)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd nugget_vamsi
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file
GOOGLE_API_KEY=your_google_api_key_here
```

4. Run the app:
```bash
streamlit run app.py
```

## 🔑 Environment Variables

- `GOOGLE_API_KEY`: Your Google AI API key (required)

## 📦 Dependencies

- streamlit
- google-generativeai
- requests
- python-dotenv
- tiktoken

## 📱 Usage

1. Enter your topic and customize post parameters
2. Select tone, audience, length, and format
3. Click "Generate LinkedIn Posts"
4. Review and copy the generated posts
5. Check chat history for previous generations

## 🌐 Deployment

This app is deployed on Streamlit Cloud. The deployment automatically:
- Installs dependencies from `requirements.txt`
- Sets up environment variables
- Deploys the app to a public URL

## 📄 License

MIT License
