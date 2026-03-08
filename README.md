# Bank Support Bot - AI-Powered Customer Assistant

Bank Support Bot is an AI-driven conversational agent built on top of ChatterBot, designed specifically for banking customer support. It leverages machine learning and Groq's Llama 3.3 model to provide fast, intelligent, and accurate responses to common banking inquiries.

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.9 - 3.13
- Groq API Key (Optional, for advanced AI responses)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/your-repo/BankSupportBot.git
cd BankSupportBot

# Install dependencies
pip install -e .
pip install openai  # Required for Groq/OpenAI adapters
```

### 3. Setup Groq (Optional)
To use high-speed AI responses, set your Groq API key:
```powershell
$env:OPENAI_API_KEY="your_groq_api_key_here"
```

### 4. Run the Django Web App
```bash
cd examples/django_example
python manage.py migrate
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to start chatting!

---

## 🏗️ Project Structure

- **`chatterbot/`**: The core logic of the dialog engine.
  - **`logic/`**: Adapters for processing input (e.g., `BestMatch`, `OpenAILogicAdapter` for Groq).
  - **`storage/`**: Adapters for data persistence (SQL, Redis, MongoDB).
- **`data/`**: Banking-specific training data (`banking.yml`).
- **`examples/django_example/`**: A complete web interface for the bank bot.
- **`docs/`**: Comprehensive documentation and tutorials.
- **`tests/`**: Unit and integration tests.

---

## 🛠️ Configuration

The bot's behavior is configured in `examples/django_example/django_example/settings.py` under the `CHATTERBOT` dictionary:

```python
CHATTERBOT = {
    'name': 'Bank Support Bot',
    'logic_adapters': [
        'chatterbot.logic.BestMatch',  # First priority: Local banking data
        {
            'import_path': 'chatterbot.logic.OpenAILogicAdapter',
            'model': 'llama-3.3-70b-versatile',
            'host': 'https://api.groq.com/openai/v1',
            'api_key': 'your_key_here'
        }
    ]
}
```

---

## 📚 Features
- **Hybrid Intelligence**: Combines local rule-based matching with advanced LLM fallback.
- **High Performance**: Powered by Groq for near-instantaneous responses.
- **Extensible**: Easily add new banking knowledge by updating `data/banking.yml`.
- **Admin Dashboard**: Built-in Django admin at `/admin` (User: `admin`, Pass: `admin123`).

---

## 🤝 Contributing
Contributions are welcome! Please check our [Contributing Guidelines](CONTRIBUTING.md) and [Security Policy](SECURITY.md).

---

## 📄 License
This project is licensed under the [BSD 3-Clause License](LICENSE).
