# 🛡️ Firmware-Guardian

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://firmware-guardian.streamlit.app/)

An advanced **AI-powered firmware and binary security analysis tool** engineered to detect hardcoded secrets, private keys, vulnerabilities, and high-entropy blocks in source files and configurations.

Developed by **[NomaanOS-Dev](https://github.com/NomaanOS-Dev)**.

---

## 🚀 Key Features

* **Regex Vulnerability Scanner:** Instantly detects hardcoded API keys, passwords, private RSA keys, AWS keys, and hardcoded IPs.
* **Shannon Entropy Calculation:** Computes binary entropy scores to identify packed, encrypted, or compressed sections.
* **AI Security Audit Engine:** Leverages OpenAI `gpt-4o-mini` to generate expert risk assessments and remediation strategies.
* **Interactive UI:** Clean Streamlit interface for seamless file uploads and instant diagnostic reports.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **AI Engine:** OpenAI `gpt-4o-mini` & LangChain Core
* **UI Framework:** Streamlit
* **Security Logic:** Custom Regex & Shannon Entropy Metrics

---

## 📦 Local Installation & Setup

1. **Clone Repository:**
   ```bash
   git clone [https://github.com/NomaanOS-Dev/Firmware-Guardian-.git](https://github.com/NomaanOS-Dev/Firmware-Guardian-.git)
   cd Firmware-Guardian-
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Application:**
   ```bash
   streamlit run app.py
   ```

---

## 🛡️ License
Open-source security research utility built for demonstration and educational purposes.
