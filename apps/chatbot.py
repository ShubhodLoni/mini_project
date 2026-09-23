from langchain_groq import ChatGroq
import os
import streamlit as st
import json
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-20b")

st.title("AI email analyzer")
st.markdown("This app uses the Groq LLM to analyze emails and provide insights.")


email_text = st.text_area("enter the mail text here",height=250)
if st.button("Analyze"):
    prompt=f"""
Analyze the following email.

    Return ONLY valid JSON.

    {{
      "risk_score": 0-100,
      "classification": "Safe/Low Risk/Medium Risk/High Risk/Critical",
      "reasons": ["reason1","reason2","reason3"]
    }}

    Email:
    {email_text}

    """
    response=llm.invoke(prompt)
    
    try:
        result = json.loads(response.content)

        st.metric("Risk Score", result["risk_score"])
        st.error(
            f"Classification: {result['classification']}"
        )

        st.write("### Reasons")
        for reason in result["reasons"]:
            st.write("•", reason)

    except Exception as e:
        st.error("Could not parse AI response")
        st.write("Raw Response:")
        st.code(response.content)
        st.write(e)

  