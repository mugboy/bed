from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from backend.db import DB
from pathlib import Path

app = FastAPI()

HERE = Path(__file__).parent

def minify_html(html: str) -> str:
    import re
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    html = re.sub(r'\s+', ' ', html)
    html = re.sub(r'>\s+<', '><', html)
    html = re.sub(r'>\s+', '>', html)
    html = re.sub(r'\s+<', '<', html)
    return html.strip()

@app.get("/", response_class=HTMLResponse)
async def root():
    db = DB()

    with HERE.joinpath("../frontend/index.html").open() as f:
        html = "".join(f.readlines())
    return f"{html}{db.get_messages()}"