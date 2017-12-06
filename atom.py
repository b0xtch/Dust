import numpy as np
import pandas as pd
from cv2 import imread
from etl import lweather
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer, MinMaxScaler, StandardScaler, MultiLabelBinarizer

class Atom:

    weather = ''
    X_train = ''
    X_test = ''
    y_train = ''
    y_test = ''
    y_predict = ''
    model = ''

    def __init__(self, weather, images):
        self.weather = lweather(weather, images)
        print('Initalized data for predictions')
        self.initialize()

    def initialize(self):
        '''
        Split into train and test
        '''
        print('Spliting data into training and testing')
        X = self.weather.loc[:, 'Date/Time'].values
        y = self.weather['Weather'].apply(self.get_mlb)

        self.X_train, X_test, self.y_train, y_test = train_test_split(X, y)

        print(self.X_train)
        #self.X_train = self.load_imgs(self.X_train)
        #print(self.X_train)
        #print(self.X_train)
        #print(imread(str(self.X_train)))
        #print(self.weather.loc[:, 'Images'].values)
        #print(self.weather.loc[:, 'Images'])
        self.pipeline()
        #model = self.model
        #print(self.weather.loc[:, 'Date/Time'])

    def pipeline(self):
        '''
        '''
        print('Training model...')
        #self.X_train, _ = self.load_imgs(self.X_train)
        self.model = make_pipeline(
            PCA(50),
            KNeighborsClassifier(n_neighbors=13)
        )
        self.model.fit(self.X_train, self.y_train)
        score = self.model.score(X_test, y_test)
        print('SVM score:', score)

    def get_mlb(self, weather):
        '''
        '''
        return MultiLabelBinarizer().fit_transform(weather)

    def get_pixels(self, path):
        '''
        '''

        return imread(path)

    def load_imgs(self, X_path):
        arr = np.array([np.array(imread(img)) for img in X_path])
        return arr
