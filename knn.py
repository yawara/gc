from collections import defaultdict

from sklearn.utils import shuffle
from sklearn.metrics import f1_score
from sklearn.datasets import fetch_mldata
from sklearn.cross_validation import train_test_split

from scipy.spatial.distance import cosine
import numpy as np


def cos_distance(a, b):
    return np.dot(a, b) / (np.sqrt(np.dot(a, a)) * np.sqrt(np.dot(b, b)))


class KNClassifier(object):

    def __init__(self, n=5):
        self.n = n

    def fit(self, train_X, train_y):
        self.train_X = train_X
        self.train_y = train_y

    def _predict(self, x):
        distances = np.asarray([cosine(train_X[i], x)
                                for i in range(train_X.shape[0])])
        neighbors_y = train_y[distances.argsort()][:self.n]
        return np.median(neighbors_y)

    def predict(self, test_X):
        pred_y = np.asarray([self._predict(x) for x in test_X])
        return pred_y

    def precision(self, test_X, test_y):
        pred_y = self.predict(test_X)
        assert pred_y.shape == test_y.shape
        return 1 - np.count_nonzero(pred_y - test_y) / test_y.shape[0]

mnist = fetch_mldata('MNIST original', data_home='./')
mnist_X, mnist_y = shuffle(mnist.data.astype('float32'),
                           mnist.target.astype('int32'), random_state=42)

mnist_X = mnist_X / 255.0

train_X, test_X, train_y, test_y = train_test_split(mnist_X, mnist_y,
                                                    test_size=0.2,
                                                    random_state=42)

knc = KNClassifier()
knc.fit(train_X, train_y)
