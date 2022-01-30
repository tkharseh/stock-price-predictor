import numpy as np
from sklearn import preprocessing
import keras.models
import keras.layers
import data_fetcher


def perform_lstm(ticker):
    requests = data_fetcher.StockDataRequest('10y', '1d')
    requests.add_tickers([ticker])

    response = data_fetcher.load_stock_data(
        "./data/stock_price_data.csv", up_to_date=True, request=requests)

    data = response.copy()[["Close"]]

    # Using log returns as input https://quantivity.wordpress.com/2011/02/21/why-log-returns/
    data.loc[:, ("norm_returns")] = np.log(1 + data.Close.pct_change())
    data.dropna(inplace=True)

    X = data[["Close", "norm_returns"]]

    scaler = preprocessing.MinMaxScaler().fit(X)
    X_trans = scaler.transform(X)
    Y = []  # Want to predict future closing prices
    for x in X_trans:
        Y.append(x[0])
    
    # We do an 85/15 split for training/testing
    split = int(len(X_trans) * 0.85)
    X_train, X_test = (X_trans[:split], X_trans[split:])
    Y_train, Y_test = (Y[:split], Y[split:])
    
    time_step = 5
    
    Xtrain_step, Xtest_step = ([], [])
    Ytrain_step, Ytest_step = ([], [])
    
    for t in range(time_step, len(X_train)):
        Xtrain_step.append(X_train[t - time_step: t, : X_train.shape[1]])
        Ytrain_step.append(Y_train[t])
    for t in range(time_step, len(X_test)):
        Xtest_step.append(X_test[t - time_step: t, : X_test.shape[1]])
        Ytest_step.append(Y_test[t])
    
    z = np.array(Ytrain_step[0])
    z = np.c_[z, np.zeros(z.shape)]
    scaler.inverse_transform(z)
    
    Xtrain_step, Ytrain_step = (np.array(Xtrain_step), np.array(Ytrain_step))
    Xtrain_step = np.reshape(
    Xtrain_step, (Xtrain_step.shape[0], Xtrain_step.shape[1], Xtrain_step.shape[2]))
    
    Xtest_step, Ytest_step = (np.array(Xtest_step), np.array(Ytest_step))
    Xtest_step = np.reshape(
    Xtest_step, (Xtest_step.shape[0], Xtest_step.shape[1], Xtest_step.shape[2]))
    
    lstm_model = keras.models.Sequential()
    lstm_model.add(keras.layers.LSTM(4, input_shape=(
    Xtrain_step.shape[1], Xtrain_step.shape[2])))
    
    lstm_model.add(keras.layers.Dense(1))
    lstm_model.compile(loss="mean_squared_error", optimizer="adam")
    lstm_model.fit(Xtrain_step, Ytrain_step, epochs=10, validation_data=(
    Xtest_step, Ytest_step), batch_size=10, verbose=1)
    
    print(lstm_model.summary())
    
    trainGuess = lstm_model.predict(Xtrain_step)
    testGuess = lstm_model.predict(Xtest_step)
    
    trainGuess = np.c_[trainGuess, np.zeros(trainGuess.shape)]
    testGuess = np.c_[testGuess, np.zeros(testGuess.shape)]
    
    # Invert the normalization
    trainGuess = scaler.inverse_transform(trainGuess)
    trainGuess = [guess[0] for guess in trainGuess]
    
    testGuess = scaler.inverse_transform(testGuess)
    testGuess = [guess[0] for guess in testGuess]

    return testGuess


if __name__ == "__main__":
    result = perform_lstm("MSFT")
    print(result)
    print(len(result))

