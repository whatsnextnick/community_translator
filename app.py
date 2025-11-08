import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="Community Translation Hub",
    page_icon="🌍",
    layout="wide"
)

# Custom CSS for social justice theme
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #6c5ce7;
        color: white;
        border-radius: 5px 5px 0 0;
        padding: 0 24px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #5f27cd;
    }
    .translation-box {
        background-color: white;
        border-left: 4px solid #6c5ce7;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .language-header {
        color: #5f27cd;
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    .solidarity-banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #6c5ce7;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #5f27cd;
    }
    </style>
""", unsafe_allow_html=True)

# Simplified language mappings (Helsinki-NLP models use ISO codes)
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Hindi": "hi"
}

# Simple translation using Helsinki-NLP models (much smaller, ~300MB each)
@st.cache_resource
def load_translator(source_lang, target_lang):
    """Load a specific translation model for language pair"""
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    try:
        translator = pipeline("translation", model=model_name)
        return translator
    except Exception as e:
        st.error(f"Model not available for {source_lang} → {target_lang}")
        return None

def translate_text(text, source_lang, target_lang):
    """Translate text using Helsinki-NLP models"""
    translator = load_translator(source_lang, target_lang)
    if translator is None:
        return None

    try:
        result = translator(text, max_length=512)
        return result[0]['translation_text']
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return None

# Header
st.markdown("""
    <div class="solidarity-banner">
        <h1>🌍 Community Translation Hub - Lite</h1>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            Breaking language barriers • Building solidarity • Empowering communities
        </p>
        <p style="font-size: 0.9rem; margin-top: 0.5rem; opacity: 0.9;">
            Lightweight version optimized for Streamlit Cloud
        </p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("✊ Language Justice")

    st.markdown("""
        ### About This Version

        This is a **lightweight version** optimized for cloud deployment.
        Uses Helsinki-NLP translation models (smaller, faster).

        **Features:**
        - Single translation between supported languages
        - Lower memory usage
        - Faster loading times

        **Limitations:**
        - Fewer language pairs
        - No multi-language broadcast
        - Simpler interface

        For full features, run the main app locally.
    """)

    st.divider()

    st.markdown("""
        ### 🌐 Supported Languages

        English, Spanish, French, German, Portuguese,
        Russian, Chinese, Japanese, Korean, Arabic, Hindi

        *Note: Not all language pairs available*
    """)

st.header("🔄 Translation")
st.markdown("Translate text between languages")

col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox(
        "From:",
        options=list(LANGUAGES.keys()),
        index=0
    )

with col2:
    target_lang_name = st.selectbox(
        "To:",
        options=list(LANGUAGES.keys()),
        index=1
    )

input_text = st.text_area(
    "Enter text to translate:",
    height=200,
    placeholder="Type or paste your message here..."
)

if st.button("🔄 Translate"):
    if not input_text.strip():
        st.warning("⚠️ Please enter text to translate.")
    elif source_lang_name == target_lang_name:
        st.warning("⚠️ Source and target languages are the same!")
    else:
        source_code = LANGUAGES[source_lang_name]
        target_code = LANGUAGES[target_lang_name]

        with st.spinner(f"Translating from {source_lang_name} to {target_lang_name}..."):
            translation = translate_text(input_text, source_code, target_code)

            if translation:
                st.markdown("### ✅ Translation Result")
                st.markdown(f"""
                    <div class="translation-box">
                        <div class="language-header">{target_lang_name}</div>
                        <div style="font-size: 1.1rem; line-height: 1.6;">
                            {translation}
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                st.code(translation, language=None)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p><strong>✊ Built for organizers, by organizers</strong></p>
        <p>Language justice is social justice • Solidarity forever</p>
        <p style="font-size: 0.9rem; margin-top: 1rem;">
            Powered by Helsinki-NLP OPUS-MT • Built with Streamlit
        </p>
    </div>
""", unsafe_allow_html=True)
