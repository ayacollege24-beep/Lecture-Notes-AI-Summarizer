# Lecture-Notes-AI-Summarizer

An interactive Streamlit-based web application designed to help students quickly digest academic material. This tool processes both **PDF** and **TXT** files, providing automated summarization, key point extraction, and an internal keyword search engine.

## Key Features
* **Multi-Format Support:** Seamlessly handles PDF text extraction and plain text files.
* **Smart Summarization:** Offers three distinct summary styles (Short, Detailed, and Bullet Points) based on sentence-scoring algorithms.
* **Internal Search:** A built-in search function to quickly locate specific keywords or concepts within long lectures.
* **Interactive UI:** Built with Streamlit for a clean, user-friendly experience.
* **Data Export:** Users can download summaries, key points, or full reports as text files.

## Technical Implementation
* **Language:** Python
* **Web Framework:** Streamlit
* **Text Processing:** Regular Expressions (re), Collections (Counter)
* **PDF Logic:** PyPDF2 for parsing complex document layouts.

## How to Use
1. **Clone the repo:** `git clone https://github.com/YOUR_USERNAME/Lecture-Notes-AI-Summarizer.git`
2. **Install requirements:** `pip install -r requirements.txt`
3. **Launch the app:** `streamlit run your_filename.py`
