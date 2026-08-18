import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Sristi | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("Sristi")
st.subheader("Aspiring Data Analyst")

st.write(
    "Building practical skills in SQL, Python, Excel, "
    "Power BI, Statistics, Data Visualization, and DSA."
)

st.divider()

# --------------------------------------------------
# ABOUT ME
# --------------------------------------------------

st.header("👩‍💻 About Me")

st.write(
    """
    I am preparing for a career as a Data Analyst with a strong focus
    on practical data analysis and problem solving.

    I am developing my skills across SQL, Python, NumPy, Pandas,
    Matplotlib, Seaborn, Plotly, Excel, Power BI, Statistics,
    Data Visualization, Git/GitHub, and Data Structures & Algorithms.

    My goal is to build real-world projects that demonstrate my
    ability to clean data, analyze information, create visualizations,
    identify insights, and communicate findings clearly.
    """
)

st.divider()

# --------------------------------------------------
# SKILLS
# --------------------------------------------------

st.header("🛠️ Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🐍 Python")
    st.write(
        "Python, NumPy, Pandas"
    )

    st.subheader("🗄️ SQL")
    st.write(
        "Queries, Filtering, Aggregation, GROUP BY, "
        "Joins, Subqueries, Data Analysis"
    )

with col2:
    st.subheader("📊 Excel")
    st.write(
        "Data Cleaning, Functions, Pivot Tables, "
        "Charts, Dashboards"
    )

    st.subheader("📈 Power BI")
    st.write(
        "Power Query, Data Modeling, DAX, "
        "Interactive Dashboards"
    )

with col3:
    st.subheader("📐 Statistics")
    st.write(
        "Descriptive Statistics, Probability, "
        "Hypothesis Testing, Regression"
    )

    st.subheader("🧠 DSA")
    st.write(
        "Arrays, Linked Lists, Stacks, Queues, "
        "Trees, Graphs, Searching, Sorting, Recursion"
    )

st.divider()

# --------------------------------------------------
# DATA VISUALIZATION & TOOLS
# --------------------------------------------------

st.header("📊 Data Visualization & Tools")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📉 Visualization")
    st.write(
        "Matplotlib, Seaborn, Plotly"
    )

with col2:
    st.subheader("🔧 Data Analysis")
    st.write(
        "Data Cleaning, EDA, Data Transformation, "
        "Data Analysis"
    )

with col3:
    st.subheader("💻 Tools")
    st.write(
        "Git, GitHub, Google Colab"
    )

st.divider()

# --------------------------------------------------
# PROJECTS
# --------------------------------------------------

st.header("📂 Projects")

# COVID PROJECT

st.subheader("🦠 COVID-19 Data Analysis")

st.write(
    """
    SQL-based analysis exploring reported COVID-19 cases,
    deaths, death rates, and changes in reported cases and
    deaths over time.
    """
)

st.write("**Tools:** SQL | Data Analysis")

st.info("🚧 Project currently in development")

st.divider()

# POWER BI

st.subheader("📊 Power BI Dashboard")

st.write(
    """
    Interactive business dashboard project using Power BI
    to explore KPIs, trends, and business performance.
    """
)

st.write(
    "**Tools:** Power BI | Power Query | DAX"
)

st.info("🚧 Coming Soon")

st.divider()

# PYTHON

st.subheader("🐍 Python Data Analysis")

st.write(
    """
    Data analysis project using Python and Pandas to clean,
    explore, visualize, and extract insights from a dataset.
    """
)

st.write(
    "**Tools:** Python | Pandas | NumPy | Matplotlib | Seaborn"
)

st.info("🚧 Coming Soon")

st.divider()

# EXCEL

st.subheader("📈 Excel Data Analysis")

st.write(
    """
    Excel-based data analysis project involving data cleaning,
    formulas, pivot tables, charts, and dashboard creation.
    """
)

st.write(
    "**Tools:** Excel | Pivot Tables | Data Visualization"
)

st.info("🚧 Coming Soon")

st.divider()

# DSA

st.subheader("🧠 DSA Problem Solving")

st.write(
    """
    Collection of Data Structures and Algorithms problems
    solved using Python, focusing on problem-solving,
    searching, sorting, trees, graphs, and recursion.
    """
)

st.write(
    "**Tools:** Python | Data Structures | Algorithms"
)

st.info("🚧 Coming Soon")

st.divider()

# --------------------------------------------------
# LEARNING JOURNEY
# --------------------------------------------------

st.header("🎯 Learning Journey")

st.write("**Currently developing:**")

progress = {
    "SQL": "In Progress",
    "Python": "In Progress",
    "NumPy": "In Progress",
    "Pandas": "In Progress",
    "Matplotlib": "In Progress",
    "Seaborn": "Planned",
    "Plotly": "Planned",
    "Excel": "In Progress",
    "Power BI": "In Progress",
    "Statistics": "In Progress",
    "DSA": "In Progress",
    "Git/GitHub": "In Progress"
}

for skill, status in progress.items():
    st.write(f"**{skill}:** {status}")

st.divider()

# --------------------------------------------------
# CAREER GOAL
# --------------------------------------------------

st.header("🚀 Career Goal")

st.write(
    """
    My goal is to become a job-ready Data Analyst by combining
    strong analytical thinking with practical skills in SQL,
    Python, Excel, Power BI, Statistics, and data visualization.

    I aim to solve real-world business problems using data and
    communicate actionable insights clearly.
    """
)

st.divider()

# --------------------------------------------------
# CONTACT
# --------------------------------------------------

st.header("📬 Contact")

st.write("📧 Email: Add your email here")
st.write("💼 LinkedIn: Add your LinkedIn profile here")
st.write("💻 GitHub: Add your GitHub profile here")

st.divider()

st.caption("© 2026 Sristi | Data Analyst Portfolio")
