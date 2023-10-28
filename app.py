from flask import Flask, jsonify, render_template, request
from chat import get_response

app = Flask(__name__)

@app.route("/chat", methods=['GET'])
def predict():
    text = request.args.get("message")

    response = get_response(text)

    r = {
    'response' : response
        }
    return jsonify(r)

if __name__ == "__main__":
    app.run(debug = True)
