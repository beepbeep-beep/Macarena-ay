from flask import Flask, request, render_template_string, redirect
import requests
from urllib.parse import quote

app = Flask(__name__)

# Function to get DuckDuckGo search results
def get_ddg_results(query):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        response = requests.post(
            "https://html.duckduckgo.com/html/",
            data={"q": query},
            headers=headers,
            timeout=5
        )
        return response.text
    except Exception as e:
        return f"<h1>Error loading results</h1><p>{e}</p>"

@app.route("/")
def mobile_home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SamSearch Mobile</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                background-color: #121212;
                color: #fff;
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                text-align: center;
                padding: 20% 10px;
            }
            input {
                width: 80%;
                padding: 16px;
                font-size: 18px;
                border: none;
                border-radius: 10px;
                margin-bottom: 10px;
            }
            button {
                padding: 14px 30px;
                font-size: 18px;
                background-color: #4285f4;
                border: none;
                color: white;
                border-radius: 10px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>SamSearch Mobile</h1>
        <form action="/search" method="get">
            <input type="text" name="q" placeholder="Search DuckDuckGo...">
            <br>
            <button type="submit">Search</button>
        </form>
    </body>
    </html>
    """)
def get_ddg_results(query):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        response = requests.post(
            "https://html.duckduckgo.com/html/",
            data={"q": query},
            headers=headers,
            timeout=5
        )
        return response.text
    except Exception as e:
        return f"<h1>Error loading results</h1><p>{e}</p>"

@app.route("/search")
def search():
    query = request.args.get("q", "")
    results = get_ddg_results(query)
    return results

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
