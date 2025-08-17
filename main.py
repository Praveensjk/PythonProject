import streamlit as st
from config import load_api_key
from services.translation import translate_text
from services.tts import text_to_speech
from services.file_extractor import extract_text_from_file
from utils.text_cleaner import clean_text_for_tts

LANGUAGES = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-cn",
    "Hindi": "hi",
    "Arabic": "ar",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Kannada": "kn"
}

def main():
    st.title("Multilingual Text Translator & Speech Synthesizer")
    st.write("Translate text, convert to speech, and download audio.")

    st.sidebar.markdown("[App Setup & Documentation](README.md)")

    api_key = load_api_key()
    if not api_key:
        st.error("Gemini API key not found. Please check your .env file.")
        return

    text = st.text_area("Enter text to translate:")
    st.write("Upload a text, PDF, CSV, or Excel file for translation (optional):")
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "csv", "xls", "xlsx"])
    target_language = st.selectbox("Select target language:", list(LANGUAGES.keys()))
    file_text = extract_text_from_file(uploaded_file) if uploaded_file else ""
    combined_text = "\n".join([text, file_text]).strip()
    if st.button("Translate"):
        if combined_text and target_language:
            with st.spinner("Translating..."):
                translated = translate_text(combined_text, target_language, api_key)
            if translated:
                st.success(f"Translated Text ({target_language}):")
                st.write(translated)
                lang_code = LANGUAGES[target_language]
                cleaned_text = clean_text_for_tts(translated)
                tts = text_to_speech(cleaned_text, lang_code)
                audio_file = f"output_{lang_code}.mp3"
                tts.save(audio_file)
                with open(audio_file, "rb") as f:
                    audio_bytes = f.read()
                    st.audio(audio_bytes, format="audio/mp3")
                    st.download_button(
                        label="Download Audio",
                        data=audio_bytes,
                        file_name=audio_file,
                        mime="audio/mp3"
                    )
            else:
                st.error(f"Translation failed. Please try again. {translated}")

if __name__ == "__main__":
    main()
