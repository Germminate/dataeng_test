import os
from sklearn.svm import SVC


class SVM:
    """
    Model that makes use of Scikit-Learn RandomForestClassifier method to build a model.
    """

    def __init__(self, data, model_args=None, random_state=123):
        """
        data: Dataset for modelling. Requires X and Y datasets.
        model_args: (Optional) Dictionary of arguments relevant to the model chosen.
        random_state: (Optional) Initialise the model with a fixed random state or random. Values differ if no random state is defined.
        """
        self._data = data
        self._model_args = model_args
        self._random_state = random_state

    def svc(self):
        model = SVC(gamma='auto')
        model.fit(self._data[0], self._data[1])

        return model
