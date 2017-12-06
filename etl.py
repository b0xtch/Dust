import sys
import etl
import glob, os
import numpy as np
import pandas as pd
from cv2 import imread

def eweather(weather, images):
    '''
    Extract and concat csv files from dir given by user
    '''
    print('Reading weather')
    weather = pd.concat((pd.read_csv(f, header=14) for f in glob.glob(weather + "/*.csv")), ignore_index=True)
    weather = tweather(weather, images)

    return weather

def tweather(weather, images):
    '''
    #katkam-YYYYMMDDHH0000
    Transform the weather df to required criteria
    Predicate NA values from df with no NA values
    '''
    weather = weather[['Weather', 'Date/Time']]
    weather = weather.dropna(axis=1, how='all')
    #The unique strings you'll find are probably not exactly the choices you want to make for categories.
    attrs = weather['Weather'].values
    temp = ''
    attrs[0] = attrs[1]
    flag = weather['Weather'].isnull().values
    for i in range(1, len(attrs)):
        if not flag[i]:
            temp = attrs[i]
        else:
            attrs[i] = temp

    weather['Weather'] = pd.Series(attrs)
    weather = weather.dropna(axis=0, how='any')

    print('Merging weather with associated images...')
    weather['Images'] = pd.to_datetime(weather['Date/Time'], format='%Y-%m-%d %H:%M').apply(
    lambda dt:
        imread(
        images                 +
        '/katkam-'             +
        str(dt.year)           +
        str('%02d' % dt.month) +
        str('%02d' % dt.day)   +
        str('%02d' % dt.hour)  + '0000' + '.jpg'))
    weather = weather[pd.notnull(weather['Images'])]
    #weather[weather["Weather"] == "NA"] => check operation

    return weather

def lweather(weather, images):
    '''
    '''
    return eweather(weather, images)

def timage(date, images):
    '''
    Extract thou images that correspond to existing Date/Time or those != NAN | null
    '''
    print(date)

    #images = [cv2.imread(file) for file in glob.glob("path/to/files/*.png")]
    #return cv2.imread(images + '/katkam-' +  )
