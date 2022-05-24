import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from utils.logging import get_logger
import warnings

log = get_logger(__name__)


def get_data_with_predictions_from_dummy_data(path='./src/data/bakery_sales_dataset_preprocessed.csv') -> pd.DataFrame:
    warnings.warn('This function is deprecated and will be removed in future releases.'
                  'Use get_data_with_predictions() instead', DeprecationWarning)
    log.debug(f"Load data for prediction from file -> {path}")
    x, y = __get_dummy_data(path)
    return get_data_with_predictions(x, y)


def get_data_with_predictions(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    log.debug(f"Load data for predictions from dataframe")
    clf = get_linear_regression_model(x.drop(['date'], axis=1), y)
    df_y = pd.DataFrame(clf.predict(x.drop(['date'], axis=1)), columns=y.columns)
    return pd.concat([x, df_y], axis=1)


def get_linear_regression_model(x, y) -> Pipeline:
    clf = Pipeline([
        ('column_transform', ColumnTransformer([
            ('one_hot', OneHotEncoder(drop='first', handle_unknown='ignore', sparse=False), ['weekday'])
        ], remainder='passthrough')),
        ("scaler", StandardScaler()),
        ("clf", LinearRegression(n_jobs=-1)),
    ])
    scores = cross_val_score(clf, x, y, cv=5, scoring='neg_mean_squared_error')
    log.info('Performance for Linear Regression Model\n'
             f"{-scores.mean():0.2f} mean squared error with a standard deviation of {scores.std():0.2f}")

    clf.fit(x, y)
    return clf


# TODO move this into the preprocessing function
def __get_dummy_data(path='./src/data/bakery_sales_dataset_preprocessed.csv'):
    """
    Get x and y from a csv source,
    this function will be used until we can use a get_data function from preprocessing
    """
    df = pd.read_csv(path, sep=',', index_col=0)
    x_columns = ['date', 'daytime', 'weekday', 'holiday', 'h_type', 'weather', 'temp']
    # Drop date because we only have 1 year of data.
    # Month is not considered as a feature because of this also.
    x = df[x_columns]
    y = df.drop(x_columns, axis=1)
    return x, y

