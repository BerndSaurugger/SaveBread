import sklearn.metrics as metrics


def regression_results(y_test, y_pred, metric: str = "mse"):
    """
    This function is scoring the results of the model. Please provide the test output and the prediction.
    Also select a metric.
    Supported metrics are: ["explained_variance", "mean_absolute_error", "mse", "rmse", "median_absolute_error", "r2"]
    """
    assert metric in ["explained_variance", "mean_absolute_error", "mse", "rmse", "median_absolute_error", "r2"]
    # Regression metrics
    explained_variance = metrics.explained_variance_score(y_test, y_pred)
    mean_absolute_error = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = mse**0.5
    median_absolute_error = metrics.median_absolute_error(y_test, y_pred)
    r2 = metrics.r2_score(y_test, y_pred)

    if metric == "explained_variance":
        return explained_variance
    if metric == "mean_absolute_error":
        return mean_absolute_error
    if metric == "mse":
        return mse
    if metric == "rmse":
        return rmse
    if metric == "median_absolute_error":
        return median_absolute_error
    if metric == "r2":
        return r2
