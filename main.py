import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from util import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("🛠️ Cold Mail Generator & Research Tool")
    
    # ✅ URL Input
    url_input = st.text_input("Enter a URL:", value="https://careers.nike.com/analyst-finance-gc/job/R-45280")

    # ✅ Buttons with unique keys
    col1, col2 = st.columns(2)
    with col1:
        submit_button = st.button("📧 Generate Email", key="submit")
    with col2:
        insights_button = st.button("🚀 Get Job Insights", key="insights")

    # ✅ Load the webpage content once
    if submit_button or insights_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)

            if insights_button:
                st.subheader("🔍 Job Insights")
                for job in jobs:
                    st.write(f"**Role:** {job.get('role', 'Unknown')}")
                    st.write(f"**Skills:** {', '.join(job.get('skills', []))}")
                    st.write(f"**Experience:** {job.get('experience', 'Not specified')}")
                    st.write("---")

            if submit_button:
                st.subheader("📩 Generated Email")
                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links)
                    st.code(email, language='markdown')

        except Exception as e:
            st.error(f"❌ An Error Occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
