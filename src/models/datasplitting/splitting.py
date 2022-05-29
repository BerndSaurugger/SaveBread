from sklearn.model_selection import train_test_split


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