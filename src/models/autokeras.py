import autokeras as ak
from datasplitting import splitting
import pandas as pd


def auto_keras_action(X_train="not defined", X_test="not defined", y_train="not defined", y_test="not defined",
                              input_data="not defined"):
    """
    You may specify X_train, X_test, y_train and y_test.
    You must specify your input data in order to get an output!
    """
    if "not defined" in [X_train, X_test, y_train, y_test]:
        X_train, X_test, y_train, y_test = splitting.splitting_data()

    if input_data == "not defined":
        raise ValueError("please provide input data")

    reg = ak.StructuredDataRegressor(max_trials=400, overwrite=True)
    reg.fit(X_train, y_train, epochs=600)
    y_pred = reg.predict(X_test)
    predicted_units = reg.predict(input_data)
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
        y_pred, predicted_units = auto_keras_action(X_train, X_test, y_train, y_test, input_data)
        # not sure if scores[actual_y.name] works as well or even scores[actual_y]...
        # one need to test if input data is final
        output_dataframe[f"{actual_y.name}"] = predicted_units
        y_pred_dataframe[f"{actual_y.name}"] = y_pred
    return y_pred_dataframe, output_dataframe
