# 🌍 Community Organizing Translation Hub

A multilingual translation web application designed specifically for community organizers, activists, and grassroots movements. Built with Streamlit and Meta's NLLB-200 model.

## Overview

Language justice is social justice. This tool helps community organizers break down language barriers and ensure everyone in the community can participate regardless of the language they speak.

## Features

### 🔄 Tab 1: Single Translation
- Translate text between any two supported languages
- Simple, intuitive interface
- Real-time translation with confidence
- Copy-to-clipboard functionality

### 📢 Tab 2: Multi-Language Broadcast
- Translate one message into **multiple languages simultaneously**
- Perfect for community announcements, flyers, and mass communications
- Progress tracking for batch translations
- Download all translations in a single text file
- Checkbox interface to select target languages

### 📄 Tab 3: Document Templates
- Pre-built templates for common organizing needs:
  - Community Assembly Invitations
  - Mutual Aid Resource Lists
  - Worker Rights Information
  - Food Co-op Announcements
  - Custom templates
- Edit templates before translation
- Download translated documents
- Professional formatting maintained

## Supported Languages (20+)

- English
- Spanish (Español)
- French (Français)
- Haitian Creole (Kreyòl)
- Arabic (العربية)
- Mandarin Chinese (中文)
- Portuguese (Português)
- Russian (Русский)
- Vietnamese (Tiếng Việt)
- Tagalog
- Bengali (বাংলা)
- Hindi (हिंदी)
- Korean (한국어)
- Japanese (日本語)
- Swahili (Kiswahili)
- Amharic (አማርኛ)
- Somali (Soomaali)
- Urdu (اردو)
- Polish (Polski)
- German (Deutsch)

## Model Information

**Model**: `facebook/nllb-200-distilled-600M`

NLLB (No Language Left Behind) is Meta's state-of-the-art translation model supporting 200+ languages with a focus on low-resource languages often ignored by commercial translation services.

**Key Features**:
- Trained on 200+ languages
- Optimized for cross-lingual communication
- Distilled version for faster inference
- Strong performance on low-resource languages

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- 4GB+ RAM recommended (for model loading)
- Stable internet connection (for first-time model download)

### Setup

1. **Navigate to the project directory**
   ```bash
   cd community-translator-app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: First installation will download the NLLB model (~2.4GB). This may take several minutes depending on your internet connection.

## Running the App

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the interface**
   - Automatically opens in your default browser
   - If not, navigate to `http://localhost:8501`

3. **First run**
   - Model will download automatically (~2.4GB)
   - Subsequent runs will be faster (model is cached)

## Usage Examples

### Example 1: Community Meeting Announcement

**Scenario**: You need to announce a community meeting to neighbors who speak different languages.

1. Go to **Multi-Language Broadcast** tab
2. Enter your announcement in English
3. Select target languages (Spanish, Haitian Creole, Mandarin, Arabic)
4. Click "Broadcast Translation"
5. Download all translations to distribute

### Example 2: Worker Rights Flyer

**Scenario**: Creating a "Know Your Rights" flyer for workers.

1. Go to **Document Templates** tab
2. Select "Worker Rights Information"
3. Edit the template with your local resources
4. Translate to Spanish
5. Download and print

### Example 3: Quick Translation

**Scenario**: Need to translate a message from a community member.

1. Go to **Single Translation** tab
2. Select source language (e.g., Spanish)
3. Select target language (e.g., English)
4. Paste or type the message
5. Click "Translate"

## Use Cases

### Community Organizing
- Multilingual meeting announcements
- Flyer and poster translation
- Social media posts in multiple languages
- Community resource guides

### Mutual Aid Networks
- Resource sharing across language groups
- Emergency communications
- Volunteer coordination
- Needs assessments

### Labor Organizing
- Worker rights information
- Union materials translation
- Solidarity messages
- Strike communications

### Immigrant Support
- Know Your Rights materials
- Service navigation guides
- Legal resource information
- Community welcomes

## Technical Details

### Architecture
- **Frontend**: Streamlit (Python web framework)
- **Model**: HuggingFace Transformers + Meta NLLB-200
- **Translation Pipeline**: Sequence-to-sequence generation
- **Caching**: Model cached after first load for performance

### Performance
- **First Translation**: ~30-60 seconds (model loading)
- **Subsequent Translations**: ~2-5 seconds per translation
- **Batch Translations**: ~3-5 seconds per language
- **Model Size**: ~2.4GB

### Limitations
- Maximum input length: 512 tokens (~300-400 words)
- Translation quality varies by language pair
- Not a replacement for professional human translation
- Best for community communications, not legal/medical documents

## Troubleshooting

### Model Download Issues
```bash
# If download fails, manually download:
python -c "from transformers import AutoModelForSeq2SeqLM; AutoModelForSeq2SeqLM.from_pretrained('facebook/nllb-200-distilled-600M')"
```

### Out of Memory Errors
- Close other applications
- Reduce batch size in multi-language broadcast
- Use fewer simultaneous translations

### Slow Performance
- First run is always slower (model loading)
- Ensure model is cached (check ~/.cache/huggingface/)
- Consider using GPU if available

### Common Errors
```bash
# Module not found:
pip install --upgrade -r requirements.txt

# Streamlit not found:
python -m streamlit run app.py

# Token limit exceeded:
# Break long text into smaller chunks
```

## Best Practices

### For Accurate Translations
1. Use clear, simple language
2. Avoid idioms and slang when possible
3. Keep sentences reasonably short
4. Proofread important documents with native speakers
5. Test translations with community members

### For Community Use
1. Always have translations reviewed by native speakers when possible
2. Use templates as starting points, customize for your community
3. Include contact information in multiple languages
4. Consider cultural context, not just language
5. Build relationships with multilingual community members

## Project Structure

```
community-translator-app/
├── app.py              # Main application code
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Dependencies

- **streamlit**: Web application framework
- **transformers**: HuggingFace model library
- **torch**: PyTorch deep learning framework
- **sentencepiece**: Tokenization for NLLB model
- **protobuf**: Protocol buffers
- **sacremoses**: Text preprocessing

## Privacy & Ethics

### Data Privacy
- All translations happen locally on your machine
- No data is sent to external servers (after model download)
- No translation history is stored
- No user data is collected

### Ethical Considerations
- This tool is designed for **community empowerment**
- Not intended for commercial exploitation
- Respect language diversity and cultural context
- Support language justice principles
- Center the needs of language-marginalized communities

## Contributing

This is an educational project for community use. Feel free to:
- Customize templates for your community
- Add additional languages
- Improve the UI/UX
- Share with other organizers

## Credits

- **Model**: Meta AI's NLLB-200 (No Language Left Behind)
- **Framework**: Streamlit
- **Inspiration**: Language justice movements worldwide
- **Built for**: Community organizers, activists, and grassroots movements

## License

This project is for educational and community organizing purposes. The NLLB model is subject to Meta's licensing terms.

## Resources

### Learn More About Language Justice
- Language justice principles and practices
- Community organizing best practices
- Multilingual communication strategies

### Support
- Report issues or suggest features
- Share with other organizers
- Contribute improvements

## Future Enhancements

Potential additions:
- Voice input/output
- Image/PDF document translation
- More organizing templates
- Offline mode
- Mobile app version
- Translation memory for consistency
- Community-contributed templates
- Integration with design tools for flyers

---

**✊ Built for organizers, by organizers**

*Language justice is social justice. Solidarity forever.*

**Powered by Meta's NLLB-200 • Built with Streamlit**
# community_translator
