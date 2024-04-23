from flask import Flask, request

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    response = generate_response(data['prompt'])
    return response

if __name__ == "__main__":
    app.run(debug=True)
