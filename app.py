import streamlit as st

st.set_page_config(
    page_title="Sristi | Data Analyst",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# HOME
# -----------------------------

st.title("Sristi")
st.subheader("Aspiring Data Analyst")

st.write(
    "I am building my skills in SQL, Python, Excel, "
    "Statistics, and Data Analytics."
)

st.divider()

# -----------------------------
# SKILLS
# -----------------------------

st.header("Skills")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("🐍 Python")
    st.write("Python, Pandas, Data Analysis")

with col2:
    st.subheader("🗄️ SQL")
    st.write("SQL queries, aggregation, analysis")

with col3:
    st.subheader("📊 Excel")
    st.write("Data cleaning, analysis, dashboards")

with col4:
    st.subheader("📈 Statistics")
    st.write("Descriptive & inferential statistics")

st.divider()

# -----------------------------
# PROJECTS
# -----------------------------

st.header("Projects")

st.subheader("🦠 COVID-19 Data Analysis")

st.write(
    "SQL analysis exploring reported COVID-19 cases, "
    "deaths, and trends over time."
)

st.write("**Tools:** SQL, Data Analysis")

st.divider()

st.subheader("🐍 Python Data Analysis")

st.write(
    "Coming soon — Python and Pandas based data analysis project."
)

st.write("**Tools:** Python, Pandas, Matplotlib")

st.divider()

st.subheader("📊 Excel Data Analysis")

st.write(
    "Coming soon — Excel-based data analysis project."
)

st.write("**Tools:** Excel, Data Analysis")

st.divider()

# -----------------------------
# ABOUT
# -----------------------------

st.header("About Me")

st.write(
    "I am preparing for a career as a Data Analyst. "
    "My focus is on developing practical skills in SQL, "
    "Python, Excel, Statistics, and data visualization."
)

st.divider()

# -----------------------------
# CONTACT
# -----------------------------

st.header("Contact")

st.write("📧 Email: Add your email here")
st.write("🔗 LinkedIn: Add your LinkedIn here")
st.write("💻 GitHub: Add your GitHub here")
