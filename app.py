import streamlit as st
from PIL import Image
import json
from predict import predict_image

# ---------------- CONFIG ----------------
st.set_page_config(page_title="GemInsight", layout="centered")

st.markdown("## 💎 GemInsight")
st.write("Smart Gemstone Recognition, Query & Sentiment Assistant")

# ---------------- LOAD DATA ----------------
try:
    with open("info.json") as f:
        info = json.load(f)
except:
    st.error("❌ info.json not found or invalid")
    info = {}

# ---------------- FUNCTION: DISPLAY RESULT ----------------
def show_result(label, conf, img):
    if label == "Low Confidence":
        st.warning("⚠️ Unable to confidently identify gemstone")
        st.write("Confidence:", round(conf, 2))

        st.info("""
        Suggestions:
        • Use better lighting  
        • Capture closer angle  
        • Use plain background  
        """)

        # ---------------- SENTIMENT ANALYSIS ----------------
        st.markdown("### 😊 Feedback Sentiment")
        feedback = st.text_input("Share your feedback about the result")

        if feedback:
            text = feedback.lower()

            positive_words = [
                "good", "great", "accurate", "helpful", "nice", "excellent", "perfect",
                "amazing", "awesome", "clear", "fast", "useful", "reliable", "smooth",
                "impressive", "smart", "easy", "friendly", "love", "liked", "satisfied",
                "fantastic", "wonderful", "best", "correct", "clean", "informative"
            ]

            negative_words = [
                "bad", "wrong", "poor", "confusing", "inaccurate", "useless", "worst",
                "slow", "difficult", "hard", "unclear", "bug", "issue", "problem",
                "misleading", "boring", "annoying", "frustrating", "disappointing",
                "error", "false", "lag", "messy", "complicated", "hate", "broken"
            ]

            neutral_words = [
                "okay", "ok", "average", "normal", "fine", "decent", "moderate",
                "acceptable", "fair", "simple", "basic", "standard", "ordinary",
                "not bad", "not good", "alright", "works", "usable"
            ]

            positive_score = sum(word in text for word in positive_words)
            negative_score = sum(word in text for word in negative_words)
            neutral_score = sum(word in text for word in neutral_words)

            if positive_score > negative_score and positive_score >= neutral_score:
                st.success("Sentiment: Positive 😊")
            elif negative_score > positive_score and negative_score >= neutral_score:
                st.error("Sentiment: Negative 😕")
            else:
                st.info("Sentiment: Neutral 😐")

    else:
        # normalize label
        label = str(label).strip().lower().replace(" ", "_")

        st.success(f"### 💎 {label.replace('_',' ').title()}")
        st.write("Confidence:", round(conf, 2))
        st.progress(int(conf * 100))

        details = info.get(label)

        if details:
            st.write("### 📌 Details")
            st.write("🌍 Origin:", details.get("origin", "N/A"))
            st.write("💰 Price:", details.get("price", "N/A"))
            st.write("✨ Features:", details.get("features", "N/A"))
            st.write("🔬 Type:", details.get("type", "N/A"))

            # ---------------- CHATBOT ----------------
            st.markdown("### 💬 Ask GemInsight")
            query = st.text_input("Ask about this gemstone")

            if query:
                q = query.lower()

                if "price" in q:
                    st.info(f"{label.replace('_',' ').title()} costs {details.get('price', 'N/A')}")

                elif "origin" in q or "found" in q:
                    st.info(f"{label.replace('_',' ').title()} is found in {details.get('origin', 'N/A')}")

                elif "feature" in q or "color" in q:
                    st.info(f"{label.replace('_',' ').title()} features: {details.get('features', 'N/A')}")

                elif "type" in q or "natural" in q:
                    st.info(f"{label.replace('_',' ').title()} is {details.get('type', 'N/A')}")

                else:
                    st.info("Please ask about price, origin, features, or type.")

        else:
            st.error(f"❌ No description found for: {label}")

        # ---------------- SENTIMENT ANALYSIS ----------------
        st.markdown("### 😊 Feedback Sentiment")
        feedback = st.text_input("Share your feedback about the result")

        if feedback:
            text = feedback.lower()

            positive_words = [
                "good", "great", "accurate", "helpful", "nice", "excellent", "perfect",
                "amazing", "awesome", "clear", "fast", "useful", "reliable", "smooth",
                "impressive", "smart", "easy", "friendly", "love", "liked", "satisfied",
                "fantastic", "wonderful", "best", "correct", "clean", "informative"
            ]

            negative_words = [
                "bad", "wrong", "poor", "confusing", "inaccurate", "useless", "worst",
                "slow", "difficult", "hard", "unclear", "bug", "issue", "problem",
                "misleading", "boring", "annoying", "frustrating", "disappointing",
                "error", "false", "lag", "messy", "complicated", "hate", "broken"
            ]

            neutral_words = [
                "okay", "ok", "average", "normal", "fine", "decent", "moderate",
                "acceptable", "fair", "simple", "basic", "standard", "ordinary",
                "not bad", "not good", "alright", "works", "usable"
            ]

            positive_score = sum(word in text for word in positive_words)
            negative_score = sum(word in text for word in negative_words)
            neutral_score = sum(word in text for word in neutral_words)

            if positive_score > negative_score and positive_score >= neutral_score:
                st.success("Sentiment: Positive 😊")
            elif negative_score > positive_score and negative_score >= neutral_score:
                st.error("Sentiment: Negative 😕")
            else:
                st.info("Sentiment: Neutral 😐")

# ---------------- INPUT OPTION ----------------
option = st.radio("Choose Input Method:", ["Upload Image", "Scan with Camera"])

# ---------------- UPLOAD ----------------
if option == "Upload Image":
    file = st.file_uploader("Upload Gemstone Image")

    if file:
        img = Image.open(file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_container_width=True)

        label, conf = predict_image(img)
        show_result(label, conf, img)

# ---------------- CAMERA ----------------
elif option == "Scan with Camera":
    camera = st.camera_input("Scan Gemstone")

    if camera:
        img = Image.open(camera).convert("RGB")
        st.image(img, caption="Captured Image", use_container_width=True)

        label, conf = predict_image(img)
        show_result(label, conf, img)

# ---------------- ABOUT ----------------
st.markdown("---")
st.markdown("### 📘 About Project")
st.write("""
GemInsight is an AI-powered gemstone recognition, query, and sentiment assistant.
It combines computer vision for gemstone identification, NLP for user queries,
and sentiment analysis for feedback understanding.
Supports image upload and real-time scanning with confidence-based prediction.
""")