from collections import defaultdict
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LinearRegression


def get_x_and_y(dataframe="not defined"):
    """
    You may specify an alternative dataframe
    """
    if dataframe == "not defined":
        dataframe = pd.df()
    y = []
    for name in dataframe.columns:
        if name in ["total", "date", "daytime"]:
            continue
        else:
            y.append(dataframe[name])
    X = dataframe.pop(["total", "date", "daytime"], axis=1)
    return X, y


def splitting_data(X="not defined", y="not defined"):
    """
    You may specify an alternative X and y
    """
    if "not defined" in [X, y]:
        X, y = get_x_and_y()
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1007486, train_size=0.8)
    return X_train, X_test, y_train, y_test


def linear_regresstion_action(X_train="not defined", X_test="not defined", y_train="not defined", y_test="not defined",
                              input_data="not defined"):
    """
    You may specify X_train, X_test, y_train and y_test.
    You must specify your input data in order to get an output!
    """
    if "not defined" in [X_train, X_test, y_train, y_test]:
        X_train, X_test, y_train, y_test = splitting_data()

    if input_data == "not defined":
        raise ValueError("please provide input data")

    linreg = LinearRegression()
    grid = {
        "normalize": ["True", "False"],
    }

    model = RandomizedSearchCV(linreg, grid, random_state=1007486)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = model.score(y_test, y_pred)
    predicted_units = model.predict(input_data)

    # assert score > 0.6, "fuck this model is too bad!!!"
    return score, predicted_units


def predict_all_features(input_data="not defined"):
    """
    Please provide the input_data in order to predict your output
    """
    X, y = get_x_and_y()
    scores = defaultdict(value="not searchable")
    output_dataframe = pd.DataFrame
    for actual_y in y:
        X_train, X_test, y_train, y_test = splitting_data(y=actual_y)
        score, predicted_units = linear_regresstion_action()
        # not sure if scores[actual_y.name] works as well or even scores[actual_y]...
        # one need to test if input data is final
        scores[actual_y.name] = score
        output_dataframe[f"{actual_y.name}"] = predicted_units
    return scores, output_dataframe
