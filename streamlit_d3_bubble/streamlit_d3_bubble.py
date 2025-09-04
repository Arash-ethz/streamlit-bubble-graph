import streamlit.components.v1 as components
import json
import os

def d3_bubble_chart(data):
    # Pass data to frontend as JSON
    data_json = json.dumps({"data": data})
    frontend_path = os.path.join(os.path.dirname(__file__), "frontend", "index.html")
    with open(frontend_path, "r", encoding="utf-8") as f:
        html = f.read()
    # Inject data into HTML
    html = html.replace("/*DATA_PLACEHOLDER*/", f"const chartData = {data_json};")
    # Set height to a large value and allow scrolling
    components.html(html, height=1200, scrolling=True)
