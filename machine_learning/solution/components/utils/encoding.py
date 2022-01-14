from sklearn.preprocessing import OneHotEncoder
import numpy


def one_hot_encode(train_data, test_data=None):
    """
    Does one hot encoding on given datasets (train_data, test_data).
    """
    encoder = OneHotEncoder(handle_unknown='ignore')
    # Encode train data

    train = encoder.fit_transform(train_data)
    # Encode test data
    if test_data:
        test = encoder.transform(test_data)
        return train.toarray(), test.toarray(), encoder
    else:
        return train.toarray(), encoder


def manual_encoding(data):
    return numpy.nonzero(data)[1]
