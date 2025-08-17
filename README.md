# Multilingual Text Translator & Speech Synthesizer

This application allows users to translate text or uploaded files (TXT, PDF, CSV, Excel) into multiple languages, convert the translated text to speech, and download the resulting audio. It leverages Google's Gemini API for translation and gTTS for speech synthesis.

## Features
- Translate free text or uploaded files (TXT, PDF, CSV, Excel)
- Convert translated text to speech (audio)
- Download the audio file
- Supports multiple languages

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd CapstoneProject
```

### 2. Create a Virtual Environment (Recommended)
```
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```
If `requirements.txt` is missing, install manually:
```
pip install streamlit gtts python-dotenv requests pandas PyPDF2 openpyxl
```

### 4. Set Up the Gemini API Key
- Obtain a Gemini API key from Google (https://aistudio.google.com/app/apikey)
- Create a `.env` file in the project root:
```
GEMINI_API_KEY="your-gemini-api-key"
```

### 5. Run the Application
```
streamlit run main.py
```

## Usage
- Enter text in the text area or upload a file (TXT, PDF, CSV, Excel)
- Select the target language
- Click the "Translate" button
- View the translated text, listen to the audio, and download the audio file

## Considerations & Limitations
- **Gemini API**: Free tier may have usage limits. API response time may vary.
- **gTTS**: Limited voice/tone control. Only supports languages available in Google TTS.
- **File Uploads**: Large files or complex PDFs may not extract text perfectly.
- **Security**: Do not expose your API key publicly.
- **Error Handling**: The app provides basic error messages for failed translations or unsupported file types.

## Development Challenges
- Ensuring robust text extraction from various file formats (especially PDFs)
- Handling special characters and formatting for TTS
- Managing API errors and rate limits
- Keeping the code modular and maintainable

## Project Structure
- `main.py`: Streamlit UI and app logic
- `config.py`: Loads environment variables
- `services/translation.py`: Translation logic
- `services/tts.py`: Text-to-speech logic
- `services/file_extractor.py`: File reading and text extraction
- `utils/text_cleaner.py`: Text cleaning utilities

---

For more details, see the [full documentation](README.md).
