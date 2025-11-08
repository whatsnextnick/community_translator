import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch

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
    .download-button>button {
        background-color: #00b894;
        color: white;
    }
    .download-button>button:hover {
        background-color: #00a383;
    }
    </style>
""", unsafe_allow_html=True)

# Language mappings for NLLB-200
LANGUAGES = {
    "English": "eng_Latn",
    "Spanish": "spa_Latn",
    "French": "fra_Latn",
    "Haitian Creole": "hat_Latn",
    "Arabic": "arb_Arab",
    "Mandarin Chinese": "zho_Hans",
    "Portuguese": "por_Latn",
    "Russian": "rus_Cyrl",
    "Vietnamese": "vie_Latn",
    "Tagalog": "tgl_Latn",
    "Bengali": "ben_Beng",
    "Hindi": "hin_Deva",
    "Korean": "kor_Hang",
    "Japanese": "jpn_Jpan",
    "Swahili": "swh_Latn",
    "Amharic": "amh_Ethi",
    "Somali": "som_Latn",
    "Urdu": "urd_Arab",
    "Polish": "pol_Latn",
    "German": "deu_Latn"
}

# Document templates for community organizing
TEMPLATES = {
    "Community Assembly Invitation": """Dear Neighbors,

You are invited to our Community Assembly on [DATE] at [TIME] at [LOCATION].

We will discuss:
• Community safety and mutual aid
• Resource sharing and collective support
• Upcoming neighborhood initiatives
• Open forum for community concerns

Your voice matters. Together we are stronger.

In solidarity,
[ORGANIZATION NAME]""",

    "Mutual Aid Resource List": """COMMUNITY MUTUAL AID RESOURCES

Food Assistance:
• Community Pantry: [ADDRESS]
• Hot Meal Program: [DAYS/TIMES]

Housing Support:
• Tenant Rights Hotline: [PHONE]
• Emergency Shelter: [LOCATION]

Healthcare:
• Free Clinic: [ADDRESS]
• Mental Health Support: [PHONE]

Legal Aid:
• Know Your Rights Workshops: [SCHEDULE]
• Free Legal Consultation: [CONTACT]

We take care of each other. Solidarity forever.""",

    "Worker Rights Information": """KNOW YOUR RIGHTS AS A WORKER

You have the right to:
✓ Fair wages for all hours worked
✓ Safe working conditions
✓ Form or join a union
✓ Refuse unsafe work
✓ Breaks and meal periods
✓ Protection from discrimination

If your rights are violated:
1. Document everything
2. Contact worker center: [PHONE]
3. File complaint with labor board
4. Seek legal support

An injury to one is an injury to all.
Workers united will never be divided.""",

    "Food Co-op Announcement": """JOIN OUR COMMUNITY FOOD CO-OP!

What: Cooperative grocery buying for fresh, affordable food
When: Every [DAY] at [TIME]
Where: [LOCATION]

How it works:
• Members pool resources to buy bulk food
• Everyone pays wholesale prices
• Volunteer 2 hours per month
• Democratic decision-making

Benefits:
✓ Save 30-50% on groceries
✓ Fresh, healthy food
✓ Support local farmers
✓ Build community

First meeting: [DATE]
Contact: [EMAIL/PHONE]

Food is a human right, not a privilege.""",

    "Custom Template": ""
}

# Initialize the model
@st.cache_resource
def load_translation_model():
    """Load the NLLB translation model"""
    model_name = "facebook/nllb-200-distilled-600M"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

def translate_text(text, source_lang, target_lang, tokenizer, model):
    """Translate text from source to target language"""
    tokenizer.src_lang = source_lang
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

    # Get the target language token ID
    target_lang_token = tokenizer.convert_tokens_to_ids(target_lang)

    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=target_lang_token,
        max_length=512
    )

    translation = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    return translation

# Header
st.markdown("""
    <div class="solidarity-banner">
        <h1>🌍 Community Organizing Translation Hub</h1>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            Breaking language barriers • Building solidarity • Empowering communities
        </p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("✊ Language Justice")

    st.markdown("""
        ### Why Translation Matters

        Language justice means ensuring everyone can participate in their community
        regardless of the language they speak.

        **Our Principles:**
        - Everyone deserves information in their language
        - Communication is a human right
        - Multilingual organizing is stronger organizing
        - Translation builds trust and inclusion

        **This Tool Helps:**
        - Reach more community members
        - Ensure accessibility
        - Build multicultural solidarity
        - Strengthen grassroots movements
    """)

    st.divider()

    st.markdown("""
        ### 🌐 Supported Languages

        English, Spanish, French, Haitian Creole, Arabic,
        Mandarin Chinese, Portuguese, Russian, Vietnamese,
        Tagalog, Bengali, Hindi, Korean, Japanese, Swahili,
        Amharic, Somali, Urdu, Polish, German
    """)

    st.divider()

    st.info("""
        **Powered by:**
        Meta's NLLB-200 Model
        (No Language Left Behind)

        Supporting 200+ languages for global communication.
    """)

# Main content with tabs
tab1, tab2, tab3 = st.tabs(["🔄 Single Translation", "📢 Multi-Language Broadcast", "📄 Document Templates"])

# TAB 1: Single Translation
with tab1:
    st.header("Single Translation")
    st.markdown("Translate text between any two languages")

    col1, col2 = st.columns(2)

    with col1:
        source_lang_name = st.selectbox(
            "Source Language",
            options=list(LANGUAGES.keys()),
            index=0,
            key="single_source"
        )

    with col2:
        target_lang_name = st.selectbox(
            "Target Language",
            options=list(LANGUAGES.keys()),
            index=1,
            key="single_target"
        )

    input_text = st.text_area(
        "Enter text to translate:",
        height=200,
        placeholder="Type or paste your message here...",
        key="single_input"
    )

    if st.button("🔄 Translate", key="single_translate"):
        if input_text.strip():
            if source_lang_name == target_lang_name:
                st.warning("⚠️ Source and target languages are the same!")
            else:
                with st.spinner(f"Translating from {source_lang_name} to {target_lang_name}..."):
                    try:
                        tokenizer, model = load_translation_model()
                        source_code = LANGUAGES[source_lang_name]
                        target_code = LANGUAGES[target_lang_name]

                        translation = translate_text(input_text, source_code, target_code, tokenizer, model)

                        st.markdown("### ✅ Translation Result")
                        st.markdown(f"""
                            <div class="translation-box">
                                <div class="language-header">{target_lang_name}</div>
                                <div style="font-size: 1.1rem; line-height: 1.6;">
                                    {translation}
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

                        # Copy button
                        st.code(translation, language=None)

                    except Exception as e:
                        st.error(f"Translation error: {str(e)}")
                        st.info("Please check your internet connection for model download on first run.")
        else:
            st.warning("⚠️ Please enter text to translate.")

# TAB 2: Multi-Language Broadcast
with tab2:
    st.header("Multi-Language Broadcast")
    st.markdown("Translate one message into multiple languages at once")

    broadcast_text = st.text_area(
        "Enter your message:",
        height=200,
        placeholder="Type your announcement or message that needs to reach multiple language communities...",
        key="broadcast_input"
    )

    st.markdown("### Select Target Languages:")

    # Create checkbox grid
    num_cols = 4
    lang_list = list(LANGUAGES.keys())
    selected_languages = []

    # Remove English as source and create checkboxes for others
    target_langs = [lang for lang in lang_list if lang != "English"]

    cols = st.columns(num_cols)
    for idx, lang in enumerate(target_langs):
        col_idx = idx % num_cols
        with cols[col_idx]:
            if st.checkbox(lang, key=f"broadcast_{lang}"):
                selected_languages.append(lang)

    st.markdown(f"**Selected: {len(selected_languages)} languages**")

    if st.button("📢 Broadcast Translation", key="broadcast_button"):
        if not broadcast_text.strip():
            st.warning("⚠️ Please enter a message to broadcast.")
        elif len(selected_languages) == 0:
            st.warning("⚠️ Please select at least one target language.")
        else:
            st.markdown("### 🌍 Broadcasting to Multiple Languages")

            tokenizer, model = load_translation_model()
            source_code = LANGUAGES["English"]

            # Progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()

            translations = {}

            for idx, target_lang_name in enumerate(selected_languages):
                status_text.text(f"Translating to {target_lang_name}...")
                progress_bar.progress((idx + 1) / len(selected_languages))

                try:
                    target_code = LANGUAGES[target_lang_name]
                    translation = translate_text(broadcast_text, source_code, target_code, tokenizer, model)
                    translations[target_lang_name] = translation
                except Exception as e:
                    translations[target_lang_name] = f"[Translation Error: {str(e)}]"

            status_text.text("✅ All translations completed!")
            st.balloons()

            # Display all translations
            st.markdown("### 📋 All Translations")

            for lang_name, translation in translations.items():
                st.markdown(f"""
                    <div class="translation-box">
                        <div class="language-header">{lang_name}</div>
                        <div style="font-size: 1.05rem; line-height: 1.6;">
                            {translation}
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            # Create downloadable text file
            download_content = f"MULTI-LANGUAGE BROADCAST\n{'='*50}\n\n"
            download_content += f"ORIGINAL (English):\n{broadcast_text}\n\n"
            download_content += f"{'='*50}\n\nTRANSLATIONS:\n\n"

            for lang_name, translation in translations.items():
                download_content += f"{lang_name.upper()}:\n{translation}\n\n{'-'*50}\n\n"

            st.download_button(
                label="📥 Download All Translations",
                data=download_content,
                file_name="community_broadcast_translations.txt",
                mime="text/plain",
                key="download_broadcast"
            )

# TAB 3: Document Templates
with tab3:
    st.header("Document Templates")
    st.markdown("Pre-built organizing templates ready for translation")

    template_choice = st.selectbox(
        "Select a template:",
        options=list(TEMPLATES.keys()),
        key="template_choice"
    )

    st.markdown("### Edit Template")
    template_text = st.text_area(
        "Template content:",
        value=TEMPLATES[template_choice],
        height=300,
        key="template_text",
        help="You can edit this template before translating"
    )

    col1, col2 = st.columns(2)

    with col1:
        template_source_lang = st.selectbox(
            "Source Language",
            options=list(LANGUAGES.keys()),
            index=0,
            key="template_source"
        )

    with col2:
        template_target_lang = st.selectbox(
            "Target Language",
            options=list(LANGUAGES.keys()),
            index=1,
            key="template_target"
        )

    col_a, col_b = st.columns([1, 1])

    with col_a:
        translate_template = st.button("🔄 Translate Template", key="translate_template_btn")

    if translate_template:
        if not template_text.strip():
            st.warning("⚠️ Template is empty.")
        elif template_source_lang == template_target_lang:
            st.warning("⚠️ Source and target languages are the same!")
        else:
            with st.spinner(f"Translating template to {template_target_lang}..."):
                try:
                    tokenizer, model = load_translation_model()
                    source_code = LANGUAGES[template_source_lang]
                    target_code = LANGUAGES[template_target_lang]

                    translation = translate_text(template_text, source_code, target_code, tokenizer, model)

                    st.markdown("### ✅ Translated Template")
                    st.markdown(f"""
                        <div class="translation-box">
                            <div class="language-header">{template_target_lang} - {template_choice}</div>
                            <div style="font-size: 1.05rem; line-height: 1.6; white-space: pre-wrap;">
                                {translation}
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

                    # Download button for translated template
                    download_filename = f"{template_choice.lower().replace(' ', '_')}_{template_target_lang.lower().replace(' ', '_')}.txt"

                    st.download_button(
                        label=f"📥 Download {template_target_lang} Version",
                        data=translation,
                        file_name=download_filename,
                        mime="text/plain",
                        key="download_template"
                    )

                except Exception as e:
                    st.error(f"Translation error: {str(e)}")
                    st.info("Please check your internet connection for model download on first run.")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p><strong>✊ Built for organizers, by organizers</strong></p>
        <p>Language justice is social justice • Solidarity forever</p>
        <p style="font-size: 0.9rem; margin-top: 1rem;">
            Powered by Meta's NLLB-200 Model • Built with Streamlit
        </p>
    </div>
""", unsafe_allow_html=True)
