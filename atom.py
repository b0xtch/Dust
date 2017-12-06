import numpy as np
import pandas as pd
from etl import lweather
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer, MinMaxScaler, MultiLabelBinarizer

class Atom:

    weather = ''
    X_train = ''
    y_train = ''
    y_predict = ''
    model = ''

    def __init__(self, weather, images):
        self.weather = lweather(weather, images)
        print('Initalized data for predictions')
        #self.initialize()

    def initialize(self):
        '''
        Split into train and test
        '''
        self.X_train, X_test, self.y_train, y_test = train_test_split(
            self.weather.loc[:, 'Date/Time'],
            self.weather['Weather']
        )

        print('Spliting data into training and testing')

    def imputew(self):

        #get all the data with weather with 'NA' values then drop the column
        #self.y_predict = self.weather[self.raw_weather['Weather'].isnull()].drop(['Weather'], axis=1)
        #self.pipeline()
        #predictions = self.model.predict(y_predict)
        #predictions = pd.DataFrame({'prediction': predictions})
        #raw_weather = predictions
        #print(df[df['truth'] != df['prediction']])
        return 0

    def pipeline(self):
        '''
        '''
        self.model = make_pipeline(
            StandardScaler(),
            MLPClassifier(solver='lbfgs', alpha = 2,
            random_state=5, activation = 'logistic')
        )
        self.model.fit(self.X_train, self.y_train)
        score = self.model.score(X_test, y_test)
        print('SVM score:', score)
