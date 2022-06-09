import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import logging
# import warnings

logger = logging.getLogger()


def get_data_with_predictions(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    logger.debug("Load data for predictions from dataframe")
    clf = get_linear_regression_model(x.drop(['date', 'weekday'], axis=1), y)
    df_y = pd.DataFrame(clf.predict(x.drop(['date', 'weekday'], axis=1)), columns=y.columns)
    df_y = df_y.applymap(__relu)
    return pd.concat([x, df_y], axis=1)


def get_linear_regression_model(x, y) -> Pipeline:
    clf = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LinearRegression(n_jobs=-1)),
    ])
    scores = cross_val_score(clf, x, y, cv=5, scoring='neg_mean_squared_error')
    logger.info('Performance for Linear Regression Model -> '
                f"{-scores.mean():0.2f} mean squared error with a standard deviation of {scores.std():0.2f}")

    clf.fit(x, y)
    return clf


def __relu(input):
    if input > 0:
        return input
    else:
        return 0
