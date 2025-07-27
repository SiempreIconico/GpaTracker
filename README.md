# 🎓 GPA Tracker

An interactive dark-mode web app that helps students calculate and visualize their **SGPA and CGPA trends**, powered by Streamlit and Plotly.

![screenshot](./screenshot.png)

## 🚀 Features

- 🔢 **Flexible Data Input**: Enter SGPA manually or calculate it automatically using subject-wise grades and credits.
- 📊 **Stunning Graph**: Track your semester-wise academic progress with a beautiful interactive line graph showing both SGPA and CGPA.
- 🧠 **CGPA Goal Predictor**: Set a target CGPA and get suggestions on what scores you need in future semesters to reach it.
- 📈 **Academic Trend Feedback**: Instantly know whether your performance is improving or declining, with visual and textual feedback.
- 🌙 **Dark Mode Only**: Clean and focused UI with full use of screen space — not boring center-aligned designs.
- ✨ **Fully Responsive & Stylish**: Uses Plotly for smooth curves, point labels, and hover tooltips.

## 🏗️ Tech Stack

- **Python**
- **Streamlit**
- **Plotly**
- **NumPy**
- **Pandas**

## 📘 Grading System (AR23 Regulation)

| Grade  | Grade Point |
|--------|--------------|
| A+ (S) | 10           |
| A      | 9            |
| B      | 8            |
| C      | 7            |
| D      | 6            |
| E      | 5            |

---

## 💡 Future Plans

- 📄 Upload result images or PDFs and auto-extract subject grades using OCR
- 🧾 Export graph as PNG or PDF
- ☁️ Save user data securely with login system
- 📱 Mobile layout / PWA version for on-the-go access

---

## 🛠️ How to Run

```bash
pip install streamlit pandas numpy plotly
streamlit run gpaapp.py
