from flask import Flask, render_template, request, jsonify
from resume_analyzer import predict_role, extract_text_from_file
from chatbot_client import ask_chatbot

app = Flask(__name__)
resume_text_global = ""


@app.route("/", methods=["GET", "POST"])
def index():
    global resume_text_global
    result = None

    if request.method == "POST" and "resume" in request.files:
        file = request.files.get("resume")
        if not file or file.filename == "":
            return render_template("index.html", result={"error": "No file uploaded"})

        ext = file.filename.rsplit('.', 1)[1].lower()

        try:
            resume_text_global = extract_text_from_file(file, ext)
            result = predict_role(resume_text_global)
        except Exception as e:
            result = {"error": f"Processing error: {str(e)}"}

    return render_template("index.html", result=result)


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = ask_chatbot(resume_text_global, user_message)
    return jsonify({"response": response})


if __name__ == "__main__":
    print("Starting Flask server at http://127.0.0.1:8000")
    app.run(debug=True, port=8000)
