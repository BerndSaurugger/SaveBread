import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LinearRegression
from datasplitting import splitting


def linear_regresstion_action(X_train="not defined", X_test="not defined", y_train="not defined", y_test="not defined",
                              input_data="not defined"):
    """
    You may specify X_train, X_test, y_train and y_test.
    You must specify your input data in order to get an output!
    """
    if "not defined" in [X_train, X_test, y_train, y_test]:
        X_train, X_test, y_train, y_test = splitting.splitting_data()

    if input_data == "not defined":
        raise ValueError("please provide input data")

    linreg = LinearRegression()
    grid = {
        "normalize": ["True", "False"],
    }

    model = RandomizedSearchCV(linreg, grid, random_state=1007486)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    predicted_units = model.predict(input_data)

    # assert score > 0.6, "fuck this model is too bad!!!"
    return y_pred, predicted_units


def predict_all_features(input_data="not defined"):
    """
    Please provide the input_data in order to predict your output
    """
    X, y = splitting.get_x_and_y()
    output_dataframe = pd.DataFrame
    y_pred_dataframe = pd.DataFrame
    for actual_y in y:
        X_train, X_test, y_train, y_test = splitting.splitting_data(y=actual_y)
        y_pred, predicted_units = linear_regresstion_action(X_train, X_test, y_train, y_test, input_data)
        # not sure if scores[actual_y.name] works as well or even scores[actual_y]...
        # one need to test if input data is final
        output_dataframe[f"{actual_y.name}"] = predicted_units
        y_pred_dataframe[f"{actual_y.name}"] = y_pred
    return y_pred_dataframe, output_dataframe
