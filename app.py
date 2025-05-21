import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# Page settings
st.set_page_config(page_title="My Webpage", page_icon=":bar_chart:", layout="wide")

# Load Lottie Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_data = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jtbfg2nb.json")

# --- Sidebar ---
with st.sidebar:
    st.title("Quick Links")
    st.markdown("[LinkedIn](www.linkedin.com/in/mithun-sri-hari-k-5052b0268)", unsafe_allow_html=True)
    st.markdown("[GitHub](https://github.com/mithun1324)", unsafe_allow_html=True)
    st.markdown("[Email](mailto:mithunsrihari329@gmail.com)", unsafe_allow_html=True)

# --- Header Section ---
with st.container():
    st.subheader("Hi, I am Mithun sri hari k :wave:")
    st.title("A data Analyst from India")
    st.write("I am passionate about finding ways to use Power BI and SQL to be more efficient and effective in business settings.")
    

# --- What I Do ---
with st.container():
    st.write("---")
    st.header("What I do")
    st.write("##")
    st.markdown("""
    - **Collect Data**: From databases, APIs, CSVs, etc.
    - **Clean Data**: Fix errors, remove duplicates, handle missing values.
    - **Analyze Data**: Identify trends and patterns.
    - **Visualize Data**: Using Power BI, Excel, Tableau.
    - **Support Decisions**: Deliver actionable insights.
    """)

# --- Animation / Visual ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How I Work With Data")
        st.write("From collection to visualization, I deliver insights that drive value.")
    with right_column:
        st_lottie(lottie_data, height=300, key="data")

# --- Projects Section ---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

    st.subheader("📊 Superstore Sales Dashboard")
    st.write(
        """
        - Built an interactive Power BI dashboard using sales data.
        - Showcased KPIs, regional performance, and category-wise sales.
        """
    )
    st.markdown("[View Project](https://github.com/mithun1324/superstore-sales-project)", unsafe_allow_html=True)

    st.subheader("SQL CUSTOMER TO CUSTOMER")
    st.write(
        """
        - This project analyzes customer interactions such as referrals 
        - product swaps shared reviews or transactions between customers from a relational database using SQL. 
        - It helps businesses understand customer influence connectivity and engagement.
        """
    )
    st.markdown("[View Project](https://github.com/mithun1324/SQL-Customer-To-Customer-Project)", unsafe_allow_html=True)

# --- Contact Section ---
with st.container():
    st.write("---")
    st.header("Get In Touch")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/mithunsrihari329@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required><br><br>
         <input type="email" name="email" placeholder="Your email" required><br><br>
         <textarea name="message" placeholder="Your message here" required></textarea><br><br>
         <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

# --- Footer ---
with st.container():
    st.write("---")
    st.write("© 2025 Mithunsriharik | Built with Streamlit")
