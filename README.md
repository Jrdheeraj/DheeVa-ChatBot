# 🤖 Offline AI Voice & Text Chatbot

A lightweight, offline-first AI chatbot built with Python that combines **text-based conversations** and **voice input/output capabilities**. No internet required! Uses GPT-2 for text generation and runs entirely on your local machine.

## ✨ Features

- **Offline AI Processing**: Uses GPT-2 model for completely offline text generation
- **Voice Input**: Speak naturally and the chatbot will understand you (via speech recognition)
- **Text-to-Speech Output**: Chatbot responds with synthesized voice
- **Text Input**: Type messages directly into the chat interface
- **Clean GUI**: Modern tkinter-based interface with real-time chat display
- **Threading**: Responsive UI with background processing for AI responses
- **Status Indicators**: Real-time feedback on what the chatbot is doing
- **Chat History**: Scrollable chat display to review conversation

## 🎯 Use Cases

- Personal AI assistant for offline environments
- Educational projects learning AI/ML fundamentals
- Testing chatbot logic without cloud dependencies
- Privacy-focused conversations (no data sent to servers)
- Development and prototyping

## 📋 Prerequisites

- **Python 3.8+** installed on your system
- **Microphone** (for voice input feature)
- **Speakers/Headphones** (for voice output)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/offline-ai-chatbot.git
cd offline-ai-chatbot
```

### 2. Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install tkinter
pip install SpeechRecognition
pip install pyttsx3
pip install transformers
pip install torch
```

### 4. (Optional) Download spaCy Language Model

For enhanced text processing:

```bash
python -m spacy download en_core_web_sm
```

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `tkinter` | Built-in | GUI framework |
| `SpeechRecognition` | 3.10+ | Speech-to-text processing |
| `pyttsx3` | 2.90+ | Text-to-speech engine |
| `transformers` | 4.30+ | GPT-2 text generation model |
| `torch` | 2.0+ | Deep learning framework |

## 🚀 Usage

### Run the Chatbot

```bash
python dhee.py
```

The GUI window will open with the following interface:

### Interface Guide

- **Chat Display**: Shows conversation history
- **Text Input**: Type your message and press Enter or click "Send"
- **🎤 Voice Button**: Click to enable/disable voice input
- **Send Button**: Send text message
- **Clear Button**: Clear chat history
- **Status Label**: Shows current state (listening, thinking, ready)

### Keyboard Shortcuts

- **Enter Key**: Send text message
- **Click Voice Button**: Toggle voice listening mode

## 📝 How It Works

### Text Input Flow
```
User Types Message → Enter Key → Message Added to Chat
→ Threading Spawned → GPT-2 Generates Response → Display Result
→ Text-to-Speech Plays Audio
```

### Voice Input Flow
```
User Clicks Voice Button → Listening Starts → Audio Captured
→ Speech Recognition API Processes → Text Extracted
→ AI Response Generated → Text-to-Speech Output
```

## ⚙️ Configuration

Edit `dhee.py` to customize:

```python
# GUI Size
self.root.geometry("800x600")  # Change window size

# Text-to-Speech Speed (150 = default)
self.tts_engine.setProperty('rate', 150)  # Increase/decrease speech rate

# AI Response Length
max_length=100  # Maximum tokens in response (line in get_ai_response)

# Voice Recognition Timeout
timeout=5  # Seconds to listen before timeout
phrase_time_limit=10  # Max duration of single phrase
```

## 🐛 Troubleshooting

### Issue: "No module named 'tkinter'"
**Solution**: Tkinter is usually built-in. For Linux:
```bash
sudo apt-get install python3-tk
```

### Issue: Microphone not detected
**Solution**: 
- Check if microphone is connected and enabled in system settings
- Run audio tests to verify microphone functionality
- Try different microphone input in speech recognition settings

### Issue: GPT-2 model not loading
**Solution**: 
- First run will download ~500MB model automatically
- Ensure stable internet for first initialization only
- Model is cached locally after first download

### Issue: Text-to-speech not working
**Solution**:
- Check speaker/headphone connection
- Verify pyttsx3 is properly installed
- Try: `python -c "import pyttsx3; engine = pyttsx3.init(); engine.say('test'); engine.runAndWait()"`

### Issue: GUI appears frozen
**Solution**: 
- Freezing during AI thinking is normal (GPT-2 inference takes time)
- Wait 10-30 seconds depending on your hardware
- Upgrade CPU/GPU or increase RAM for better performance

## 📊 Project Structure

```
offline-ai-chatbot/
├── dhee.py                 # Main chatbot application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
└── .gitignore             # Git ignore rules
```

## 🔍 Code Overview

### Main Class: `LocalAIVoiceChatbot`

#### Key Methods:

| Method | Purpose |
|--------|---------|
| `__init__()` | Initialize GUI and AI models |
| `create_widgets()` | Build GUI components |
| `send_text_message()` | Handle text input |
| `listen_for_voice()` | Capture and process voice input |
| `get_ai_response()` | Generate AI response using GPT-2 |
| `speak_response()` | Convert response to audio |
| `clear_chat()` | Reset conversation |

## 🎓 Learning Resources

- **Transformers Library**: https://huggingface.co/transformers/
- **Speech Recognition**: https://github.com/Uberi/speech_recognition
- **pyttsx3 Documentation**: https://pyttsx3.readthedocs.io/
- **Tkinter GUI**: https://docs.python.org/3/library/tkinter.html

## 🚀 Future Enhancements

- [ ] Support for multiple AI models (GPT-2, BERT, DistilBERT)
- [ ] Custom training on domain-specific data
- [ ] Conversation memory/context retention
- [ ] Export chat history to file
- [ ] Theme customization (dark/light mode)
- [ ] Sentiment analysis integration
- [ ] Multi-language support
- [ ] Docker containerization
- [ ] Web interface version

## 💡 Tips for Better Performance

1. **First Run**: First execution will download GPT-2 model (~500MB). Plan for 5-10 minutes
2. **Hardware**: More RAM = faster AI responses. SSD recommended for model caching
3. **Voice Quality**: Speak clearly in quiet environments for better recognition
4. **Response Quality**: GPT-2 is lightweight but basic. Fine-tuning improves responses
5. **Batch Processing**: Process multiple requests asynchronously for efficiency

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions welcome! 

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 👨‍💻 Author

**Dhee** - AI/ML Enthusiast & Developer

## 🙏 Acknowledgments

- Hugging Face for Transformers library
- OpenAI for GPT-2 model
- Python speech recognition community
- Tkinter documentation and examples

## 📞 Support

For issues, questions, or suggestions:
1. Open an Issue on GitHub
2. Check existing issues for solutions
3. Provide detailed error messages and system info

## 🎯 Project Status

- ✅ Core functionality complete
- ✅ Voice input/output working
- ✅ Offline AI processing stable
- 🔄 Actively maintained

---

**Happy Chatting! 🚀**

*Made with ❤️ for the AI community*