import flask
from flask import Flask, request

app = Flask(__name__)

# Ticker data API route
@app.route("/data", methods=["POST", "GET"])
def ticker_data():
    ticker = request.args.get('ticker')
    data = {'ticker': ticker.upper()}
    return flask.jsonify(data)
    # data['price prediction'] = get_price_prediction(ticker)
    # return flask.jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)