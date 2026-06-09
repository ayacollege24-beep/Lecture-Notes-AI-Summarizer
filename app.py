import streamlit as st
from PyPDF2 import PdfReader
import re
from collections import Counter

# ---------- FUNCTIONS ----------

def clean_text(text):
    return text.replace("\n", " ").lower()

def summarize_text(text, num_sentences=3):
    words = re.findall(r'\w+', text)
    word_freq = Counter(words)

    sentences = text.split(".")
    sentence_scores = {}

    for sentence in sentences:
        for word in sentence.split():
            if word in word_freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]

    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    return ". ".join(top_sentences)

def get_key_points(text):
    summary_sentences = summarize_text(text, 5).split(".")
    return [point.strip() for point in summary_sentences if point]

# 🔥 NEW: Search function
def search_text(text, query):
    sentences = text.split(".")
    results = [s.strip() for s in sentences if query.lower() in s.lower()]
    return results


# ---------- UI ----------

st.title("📚 Lecture Notes Summarizer")

st.write("Upload or paste your lecture notes and analyze them instantly.")

uploaded_file = st.file_uploader(
    "Upload your lecture notes (txt or pdf)",
    type=["txt", "pdf"]
)

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        pdf = PdfReader(uploaded_file)
        text = ""
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
    else:
        text = uploaded_file.read().decode("utf-8")
else:
    text = st.text_area(
        "Paste your lecture notes here:",
        height=200
    )

# Summary style
summary_type = st.selectbox(
    "Choose summary style:",
    ["Short Summary", "Detailed Summary", "Bullet Points"]
)

# 🔥 NEW: Search input
search_query = st.text_input("🔍 Search inside your notes (keyword):")

# ---------- PROCESSING ----------

if st.button("Analyze"):
    if text:

        text = clean_text(text)

        # Summary logic
        if summary_type == "Short Summary":
            summary = summarize_text(text, 2)

        elif summary_type == "Detailed Summary":
            summary = summarize_text(text, 5)

        elif summary_type == "Bullet Points":
            points = summarize_text(text, 5).split(".")
            summary = "\n".join([f"- {point.strip()}" for point in points if point])

        key_points = get_key_points(text)

        # ---------- OUTPUT ----------
        st.subheader("📌 Your Result")
        st.write(summary)

        st.subheader("🧠 Key Points")
        for point in key_points:
            st.write(f"- {point}")

        # 🔥 NEW: Search results
        if search_query:
            results = search_text(text, search_query)

            st.subheader(f"🔍 Results for '{search_query}'")

            if results:
                for res in results[:5]:  # limit results
                    st.write(f"- {res}")
            else:
                st.write("No matches found.")

        # ---------- DOWNLOAD ----------
        key_points_text = "\n".join(key_points)
        full_output = f"SUMMARY:\n{summary}\n\nKEY POINTS:\n{key_points_text}"

        st.success("Summary ready! Download below 👇")

        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

        st.download_button(
            label="📥 Download Key Points",
            data=key_points_text,
            file_name="key_points.txt",
            mime="text/plain"
        )

        st.download_button(
            label="📥 Download Full Notes",
            data=full_output,
            file_name="lecture_summary.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please enter some text.")


# ---------- FOOTER ----------

st.write("---")
st.caption("Built to help students quickly review and understand lecture material.")
