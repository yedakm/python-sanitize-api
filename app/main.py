from flask import Flask, request, jsonify
from pathlib import Path

app = Flask(__name__)

# Load replaced chars file
REPLACED = {}
PATH = Path(__file__).resolve().parent / "replaced_chars.txt"

if PATH.exists():
    for line in PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if "=" not in line:
            continue
        left, right = line.split("=", 1)
        left = left.strip()
        right = right.strip()
        if len(left) == 1 and len(right) >= 1:
            REPLACED[left] = right

def replace_chars(text: str, table: dict) -> str:
    result = []
    for ch in text:
        lower = ch.lower()
        if lower in table:
            result.append(table[lower])
        else:
            result.append(ch)
    return "".join(result)

@app.post("/replace")
def replace_endpoint():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    result = replace_chars(text, REPLACED)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
