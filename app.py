import os
import streamlit as st
from analyzer import FirmwareScanner
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="Firmware Guardian", page_icon="🛡️", layout="wide")

st.title("🛡️ Firmware & Binary Security Guardian")
st.caption("AI-Powered Firmware Vulnerability & Hardcoded Secret Detector | Built by NomaanOS-Dev")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.info("Upload source code files, configuration files, or logs to scan for hardcoded vulnerabilities.")

uploaded_file = st.file_uploader("Upload Target File (txt, log, conf, py, json)", type=["txt", "log", "conf", "py", "json", "env"])

if uploaded_file:
    file_bytes = uploaded_file.getvalue()
    try:
        file_content = file_bytes.decode("utf-8")
    except UnicodeDecodeError:
        file_content = file_bytes.decode("latin-1", errors="ignore")
    
    st.subheader("📄 Target File Preview")
    st.code(file_content[:1000] + ("..." if len(file_content) > 1000 else ""), language="text")
    
    # Run Scanner
    scanner = FirmwareScanner()
    findings = scanner.scan_text(file_content)
    entropy_val = scanner.calculate_entropy(file_bytes)
    
    col1, col2 = st.columns(2)
    col1.metric("Total Vulnerability Indicators", sum([f['count'] for f in findings]) if findings else 0)
    col2.metric("Binary Entropy Score", f"{entropy_val} / 8.0")
    
    st.markdown("### 🔍 Regex Finding Results:")
    if findings:
        for f in findings:
            st.warning(f"**{f['type']}** detected (Count: {f['count']})")
            with st.expander("View Samples"):
                for sample in f['samples']:
                    st.code(sample)
    else:
        st.success("No common regex security signatures or hardcoded secrets found in this block.")
        
    # AI Risk Assessment
    if openai_api_key:
        st.markdown("---")
        st.markdown("### 🤖 AI Security Risk Assessment & Remediation")
        if st.button("Generate AI Security Report"):
            with st.spinner("Analyzing firmware security risks using GPT-4o-mini..."):
                os.environ["OPENAI_API_KEY"] = openai_api_key
                
                prompt_template = (
                    "You are a senior firmware security and reverse engineering expert.\n"
                    "Analyze the following findings and file content snippet to provide a professional risk assessment.\n"
                    "Highlight critical security flaws, explain the impact of exposed secrets, and provide mitigation steps.\n\n"
                    "Findings: {findings}\n\n"
                    "File Content Snippet:\n{content}"
                )
                
                prompt = ChatPromptTemplate.from_template(prompt_template)
                llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
                chain = prompt | llm | StrOutputParser()
                
                report = chain.invoke({"findings": str(findings), "content": file_content[:2000]})
                st.write(report)
    else:
        st.info("💡 Enter your OpenAI API Key in the sidebar to generate an AI-powered security audit report.")
else:
    st.info("👈 Please upload a file to begin firmware security analysis.")
