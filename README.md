# 💼 LinkedIn Post Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nuggetvamsi-eshrymtffv6amqz4peq7no.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/venkatavamsidama/nugget_vamsi)

A powerful **Streamlit application** that generates engaging LinkedIn posts using Google's **Gemini 1.5 Flash AI** model.

**🎯 Status: LIVE & DEPLOYED** ✅

## ✨ Features

- **AI-Powered Generation**: Uses Google Gemini 1.5 Flash for intelligent post creation
- **Multi-Step Process**: First plans post structure, then generates complete posts
- **Customizable Inputs**: Topic, tone, audience, length, format, hashtags, call-to-action
- **Token Tracking**: Shows exact token usage and estimated costs
- **Chat History**: Keeps track of all generated posts
- **Multiple Formats**: Story, list, question, industry insight, personal experience, how-to, opinion

## 🚀 Live Demo

**🎯 Live App:** [LinkedIn Post Generator](https://nuggetvamsi-eshrymtffv6amqz4peq7no.streamlit.app/)

Your LinkedIn Post Generator is now live and accessible to everyone!

## 🚀 Quick Start

**Try the app now:** [https://nuggetvamsi-eshrymtffv6amqz4peq7no.streamlit.app/](https://nuggetvamsi-eshrymtffv6amqz4peq7no.streamlit.app/)

## 🛠️ Local Installation

1. Clone the repository:
```bash
git clone https://github.com/venkatavamsidama/nugget_vamsi.git
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

- `GOOGLE_API_KEY`: Your Google AI API key (required for AI functionality)

### Setting up in Streamlit Cloud:
1. Go to your app's **Settings** → **Secrets**
2. Add in TOML format:
```toml
GOOGLE_API_KEY = "your_actual_api_key_here"
```

### Getting a Google AI API Key:
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API key"
4. Create and copy your API key

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

This app is successfully deployed on **Streamlit Cloud** and is live at:
**https://nuggetvamsi-eshrymtffv6amqz4peq7no.streamlit.app/**

### Deployment Features:
- ✅ **Automatic deployment** from GitHub repository
- ✅ **Dependencies** automatically installed from `requirements.txt`
- ✅ **Environment variables** managed through Streamlit Cloud secrets
- ✅ **Auto-updates** on every push to main branch
- ✅ **Public access** for anyone with the link

### Repository:
- **GitHub:** [venkatavamsidama/nugget_vamsi](https://github.com/venkatavamsidama/nugget_vamsi)
- **Branch:** `main`
- **Main file:** `app.py`

## 📄 License

MIT License
