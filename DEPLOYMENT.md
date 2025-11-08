# Deployment Guide - Community Translation Hub

## ⚠️ Memory Issue on Streamlit Cloud

The NLLB-200-distilled-600M model (~2.4GB) **exceeds Streamlit Cloud's free tier memory limit** (typically 1GB). This causes the "health check" errors you're seeing.

## 🎯 Solution Options

### Option 1: Use the Lite Version (RECOMMENDED for Cloud)

I've created `app_lite.py` which uses smaller Helsinki-NLP models (~300MB each).

**To deploy the lite version on Streamlit Cloud:**

1. In your Streamlit Cloud app settings, change the **Main file path** from:
   ```
   app.py
   ```
   to:
   ```
   app_lite.py
   ```

2. Reboot the app

**Pros:**
- ✅ Works on free tier
- ✅ Fast loading
- ✅ Lower memory usage

**Cons:**
- ❌ Fewer language pairs available
- ❌ No multi-language broadcast feature
- ❌ Less accurate for some languages

---

### Option 2: Run Full Version Locally

The full `app.py` with all features works great locally where you have more memory.

**Run locally:**
```bash
cd community-translator-app
pip install -r requirements.txt
streamlit run app.py
```

**Features you get:**
- ✅ 20+ languages
- ✅ Multi-language broadcast
- ✅ Document templates
- ✅ Higher quality translations

---

### Option 3: Upgrade Streamlit Cloud Plan

Streamlit offers paid tiers with more memory that can handle the full NLLB model.

- **Streamlit Community Cloud (Free)**: ~1GB RAM ❌
- **Streamlit Teams**: More resources ✅

---

### Option 4: Deploy on Alternative Platform

Consider platforms with more generous free tiers:

**Hugging Face Spaces:**
- Free tier: 2GB RAM
- Built for ML models
- Good fit for NLLB-200

**Google Cloud Run:**
- Free tier: 2GB RAM
- Pay-as-you-go

**Railway.app:**
- Free trial with 512MB-1GB RAM
- Simple deployment

---

## 📊 Model Comparison

| Model | Size | Languages | Memory | Quality | Cloud Free Tier |
|-------|------|-----------|---------|---------|-----------------|
| NLLB-200-distilled-600M (app.py) | 2.4GB | 200+ | ~4GB | Excellent | ❌ |
| NLLB-200-distilled-600M (optimized) | 1.2GB | 200+ | ~2GB | Excellent | ❌ |
| Helsinki-NLP OPUS-MT (app_lite.py) | 300MB | 50+ pairs | ~800MB | Good | ✅ |

---

## 🚀 Quick Start: Deploy Lite Version Now

1. **Go to Streamlit Cloud dashboard**
2. **Click on your app → ⚙️ Settings**
3. **Under "Main file path", change to:** `app_lite.py`
4. **Click "Save"**
5. **Reboot app**

Your app should now work on the free tier!

---

## 💡 Hybrid Approach

You can:
1. Deploy `app_lite.py` on Streamlit Cloud for public access
2. Keep `app.py` for local use when you need full features

Both apps work with the same `requirements.txt`.
