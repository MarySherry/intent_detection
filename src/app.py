import sys

from flask import Flask, request

sys.path.append("content/")
from predictor import Predictor

predictor = Predictor()
predictor.setup()

app = Flask(__name__)


@app.route('/process', methods=['POST'])
def process():
    content = request.json

    prediction_message = predictor.predict(content)

    return content, prediction_message


if __name__ == '__main__':
    app.run()
