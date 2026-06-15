import streamlit as st
import time
from main import clean_text, generate_llm_response

st.title("Cry Wolf")
st.caption("A British detective to discern false urgency.")

text_input = st.text_area("Paste your text here", height=200)
if text_input:
    time.sleep(0.8)
    with st.spinner("The detective is thinking..."):
        cleaned = clean_text(text_input)
        result = generate_llm_response(cleaned)
    
    classification = result.get("classification")
    
    if classification == "NO URGENCY":
        st.success("No Urgency")
        st.write(result["verdict"])
    
    elif classification == "FALSE URGENCY":
        st.error("False Urgency Detected")
        st.write(result["verdict"])
        st.metric("Urgency Score", result["chances"])
        st.caption(f"**Top offender:** {result['top_offender'].replace('_', ' ').title()}")
        st.caption(result["top_offender_reason"])
        
    
    elif classification == "REAL URGENCY":
        if result.get("suspicion_flag"):
            st.warning("Real Urgency — But Suspicious")
            st.write(result["verdict"])
        else:
            st.success("Real Urgency")
            st.write(result["verdict"])
        st.write(f"**Deadline:** {result['deadline']}")
        st.write(f"**Consequence:** {result['consequence']}")
        
    
    elif classification == "ERROR":
        st.error(result["verdict"])