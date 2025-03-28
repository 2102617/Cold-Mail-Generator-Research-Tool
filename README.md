# 🛠️ Cold Mail Generator & Research Tool

## 🚀 Overview

The ** Cold Mail Generator & Research Tool** is a Streamlit-based web application that extracts job insights from a given URL and generates personalized cold emails for outreach. It leverages **LangChain**, **ChromaDB**, and **LLM (Llama3-8B)** to scrape job listings, analyze required skills, and create AI-driven cold emails.

## 🔥 Features

- **Job Extraction**: Scrapes job details like role, skills, and experience from a careers page.
- **AI-Powered Cold Email**: Generates customized cold emails tailored to the job listing.
- **Skill-Based Portfolio Matching**: Matches job skills with your portfolio stored in ChromaDB.
- **Streamlit UI**: User-friendly interface with side-by-side buttons for insights and email generation.

## 📌 Technologies Used

- **Python** (Main Backend)
- **Streamlit** (Frontend UI)
- **LangChain** (AI & NLP Processing)
- **ChromaDB** (Vector Database for Portfolio Matching)
- **Llama3-8B** (LLM for Content Generation)
- **Pandas** (Data Handling)

## 🛠️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/cold-mail-generator.git
cd cold-mail-generator
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run main.py
```

## 🎯 How It Works

1. **Enter a Job URL** in the input field.
2. Click **"Get Insights"** to fetch job details.
3. Click **"Generate Email"** to create a cold email tailored to the job.
4. AI extracts relevant information and generates an outreach email.

## 📷 Screenshots
![Screenshot 2025-03-27 222407](https://github.com/user-attachments/assets/84663915-4134-4dd4-93e6-ffe9f2a39343)
![Screenshot 2025-03-28 215530](https://github.com/user-attachments/assets/c3f8ea57-68bd-40bd-bda1-ade001a6c7bd)
![Screenshot 2025-03-28 215716](https://github.com/user-attachments/assets/4f59fefe-7e62-49ad-8191-35e496b34c72)

## 🤝 Contributions

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a PR.

## 📜 License

This project is open-source under the [MIT License](LICENSE).

