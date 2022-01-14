from sklearn.decomposition import SparsePCA
from sklearn.preprocessing import StandardScaler


class DimensionalityReduction:
    """
    Applies dimensionality reduction technique(s) on the dataset and return the updated dataset.

    Currently, this module only applies PCA.
    """
    
    def pca(train_data, test_data, n_components=1):
        """
        Applies scikit-learn PCA dimensionality reduction method on the data.

        Arguments:
        data: An array of data to apply PCA on. 
        n_components: The number of components to keep. Defaults to 1 (lowest possible components).

        Returns:
        An array of arrays containing the data points with only the kept components.
        """
        # scaler = StandardScaler().fit(train_data)
        # standarized_train_features = scaler.transform(train_data)
        # standardized_test_features = scaler.transform(test_data)
        sparse_pca = SparsePCA(n_components).fit(train_data.toarray())

        return sparse_pca.transform(train_data.toarray()), sparse_pca.transform(test_data.toarray())

    