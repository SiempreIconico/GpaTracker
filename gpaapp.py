import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="GPA Tracker", layout="wide")

# Grade Point Map (AR23 Regulations)
grade_point_map = {
    "A+ (S)": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5
}

# Custom CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #0f0f0f;
        color: white;
    }
    div[data-baseweb="radio"] label {
        font-size: 18px !important;
        font-weight: 600;
        padding: 6px 0;
    }
    section.main > div {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Academic GPA Visualizer & Planner")
st.markdown("### Choose how you want to input your semester data and visualize your academic progress easily.")

# Input Method Selector
input_method = st.radio(
    label="Input method",
    options=("🔢 Enter SGPA manually", "🧮 Auto-calculate SGPA from subject-wise grades"),
    index=0,
    label_visibility="collapsed"
)

# Number of Semesters
num_sems = st.number_input("How many semesters do you want to enter?", min_value=1, max_value=8, step=1)

sgpas = []
sem_labels = [f"Sem {i+1}" for i in range(num_sems)]

# Manual SGPA Entry
if input_method == "🔢 Enter SGPA manually":
    st.subheader("📥 Enter your SGPA for each semester")
    cols = st.columns(min(4, num_sems))
    for i in range(num_sems):
        with cols[i % len(cols)]:
            sgpa = st.number_input(
                f"{sem_labels[i]}", 
                min_value=0.0, 
                max_value=10.0, 
                step=0.01, 
                format="%.2f", 
                key=f"sgpa_{i}", 
                placeholder="Ex: 8.5"
            )
            sgpas.append(sgpa)

# Auto-grade SGPA Calculation
else:
    st.subheader("📘 Enter your grades and credits for each subject (per semester)")
    for sem in range(num_sems):
        st.markdown(f"**{sem_labels[sem]}**")
        subjects = st.number_input(f"How many subjects in {sem_labels[sem]}?", min_value=1, max_value=12, key=f"subs_{sem}")
        total_points = 0
        total_credits = 0
        cols = st.columns([4, 3])
        for i in range(subjects):
            with cols[0]:
                grade = st.selectbox(f"Subject {i+1} Grade", list(grade_point_map.keys()), key=f"grade_{sem}_{i}")
            with cols[1]:
                credit = st.number_input("Credit", min_value=1, max_value=5, step=1, key=f"credit_{sem}_{i}")
            total_points += grade_point_map[grade] * credit
            total_credits += credit
        sgpa = round(total_points / total_credits, 2) if total_credits else 0.0
        st.success(f"Calculated SGPA for {sem_labels[sem]}: **{sgpa}**")
        sgpas.append(sgpa)

# CGPA Calculation
cgpas = []
total_points = 0
total_credits = 0
for i, sgpa in enumerate(sgpas):
    total_points += sgpa * 20
    total_credits += 20
    cgpa = round(total_points / total_credits, 2)
    cgpas.append(cgpa)

# Plotting the Graph
st.markdown("### 📈 Your Academic Progress")
fig = go.Figure()

# SGPA Line
fig.add_trace(go.Scatter(
    x=[0] + list(range(1, num_sems + 1)),
    y=[0] + sgpas,
    mode='lines+markers+text',
    name='SGPA',
    line=dict(color='cyan', width=3),
    marker=dict(size=8),
    text=[f"{v:.2f}" for v in [0] + sgpas],
    textposition="top center"
))

# CGPA Line
fig.add_trace(go.Scatter(
    x=[0] + list(range(1, num_sems + 1)),
    y=[0] + cgpas,
    mode='lines+markers+text',
    name='CGPA',
    line=dict(color='orange', width=3, dash='dash'),
    marker=dict(size=8),
    text=[f"{v:.2f}" for v in [0] + cgpas],
    textposition="top center"
))

fig.update_layout(
    xaxis_title="Semester",
    yaxis_title="GPA",
    xaxis=dict(dtick=1),
    yaxis=dict(range=[0, 10], dtick=1),
    plot_bgcolor="#111111",
    paper_bgcolor="#111111",
    font=dict(color='white'),
    legend=dict(x=0.02, y=0.98),
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# 🎯 CGPA Goal Planner
st.markdown("### 🎯 Want to reach a target CGPA?")
if st.toggle("Yes, I want to set a CGPA goal"):
    goal = st.number_input("Enter your CGPA goal (e.g., 8.0):", min_value=0.0, max_value=10.0, step=0.01)
    current_cgpa = cgpas[-1]
    remaining_sems = 8 - num_sems
    if remaining_sems == 0:
        st.warning("⚠️ No semesters left. Goal can't be achieved further.")
    else:
        needed_total = goal * 8 * 20
        current_total = current_cgpa * num_sems * 20
        required_points = needed_total - current_total
        required_sgpa = required_points / 20
        if required_sgpa <= 10:
            st.info(f"✅ You need to score **{required_sgpa:.2f} SGPA** in the next semester to reach your goal of **{goal}**.")
        else:
            st.error("❌ Goal unreachable even with perfect 10 SGPA in next semester.")

# 🧠 Final Advice
st.markdown("---")
st.markdown("### 💡 Insights")
if cgpas[-1] > cgpas[0]:
    st.success("📈 You're improving steadily. Great progress!")
elif cgpas[-1] < cgpas[0]:
    st.warning("📉 CGPA trend is slightly dipping. Time to refocus.")
else:
    st.info("➖ Stable CGPA across semesters. Keep maintaining consistency.")

# Tiered Tip Based on CGPA
if cgpas[-1] < 7:
    st.info("🔍 Tip: Aim for 7.0+ CGPA to unlock more academic options.")
elif cgpas[-1] < 8:
    st.info("🌟 You're almost there! Push to cross the 8.0 mark.")
elif cgpas[-1] >= 8:
    st.success("🏆 Excellent performance! Keep the momentum high.")
