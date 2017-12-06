import numpy as np
import pandas as pd
from cv2 import imread
from etl import lweather
from sklearn.svm import SVC
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
        self.X_train, X_test, self.y_train, y_test = train_test_split(
            self.weather.loc[:, 'Images'].values,
            self.weather['Weather'].apply(self.get_mlb)
        )
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
        self.model = make_pipeline(
            StandardScaler(),
            MLPClassifier(solver='lbfgs', alpha = 2,
            random_state=5, activation = 'logistic')
        )
        self.model.fit(imread(str(self.X_train)), self.y_train)
        score = self.model.score(X_test, y_test)
        print('SVM score:', score)

    def get_mlb(self, weather):
        '''
        '''
        return MultiLabelBinarizer().fit_transform(weather)

    def get_pixels(self, path):
        '''
        '''
        print('AA& : ')
        return imread(path)
