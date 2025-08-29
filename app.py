import streamlit as st
import pandas as pd
from streamlit_d3_bubble import d3_bubble_chart

st.set_page_config(page_title="Domain Bubble Chart", layout="wide")
st.title("Domain/Subdomain Publication Bubble Chart")

st.markdown("""
**How to upload your Excel file:**
- The file must be in `.xlsx` format.
- The columns must be named: `domain`, `subdomain`, and `publication_count`.
- Example:
    | domain    | subdomain | publication_count |
    |-----------|-----------|------------------|
    | Science   | Physics   | 120              |
    | Science   | Chemistry | 80               |
    | Tech      | AI        | 150              |
    | Tech      | Robotics  | 60               |
""")

uploaded_file = st.file_uploader("Upload your Excel file here:", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    if not all(col in df.columns for col in ["domain", "subdomain", "publication_count"]):
        st.error("Excel file must contain 'domain', 'subdomain', and 'publication_count' columns.")
    else:
        st.success("File uploaded and processed!")
        data = []
        for domain in df["domain"].unique():
            children = df[df["domain"] == domain][["subdomain", "publication_count"]]
            data.append({
                "name": domain,
                "children": [
                    {"name": row["subdomain"], "value": int(row["publication_count"])}
                    for _, row in children.iterrows()
                ]
            })
        d3_bubble_chart(data)
        
        
else:
    st.info("Please upload an Excel file to begin.")
