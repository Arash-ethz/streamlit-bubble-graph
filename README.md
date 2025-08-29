# Domain/Subdomain Bubble Chart Web App

## Features
- Upload Excel file with columns: `domain`, `subdomain`, `publication_count`
- Interactive packed bubble chart (D3.js)
- Bubbles sized by publication count, grouped by domain

## Setup

1. Open a terminal in this folder.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   streamlit run app.py
   ```
4. Open the browser link provided by Streamlit.

## Excel Format

| domain | subdomain | publication_count |
|--------|-----------|------------------|
| Science | Physics | 120 |
| Science | Chemistry | 80 |
| Tech | AI | 150 |
| Tech | Robotics | 60 |

## Notes

- The bubble chart updates after each upload.
- All code is in Python except the D3.js chart (custom Streamlit component).
