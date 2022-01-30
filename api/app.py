import flask
from flask import Flask, request
import keras_demo

app = Flask(__name__)

# Ticker data API route


@app.route("/data", methods=["POST", "GET"])
def ticker_data():
    ticker = request.args.get('ticker')
    predictions = keras_demo.perform_lstm(ticker)
    data = {'ticker': ticker.upper(), 'prediction': str(
        round(predictions[0], 2))}
    return flask.jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
