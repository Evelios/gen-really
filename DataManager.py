import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_loc = 'fma_metadata'

# low_memory=False is to have multiple data types in the same matrix
# this is not ideal. Needs better investigation of what is in tha dataset

def getTrackData(): 
  tracks = pd.read_csv(data_loc + '/tracks.csv', low_memory=False)

  return tracks

def getGenreData():
  genres = pd.read_csv(data_loc + '/genres.csv', low_memory=False)

  return genres

def getFeatureData():
  features = pd.read_csv(data_loc + '/features.csv', low_memory=False)

  return features

def getEchonestData():
  echonest = pd.read_csv(data_loc + '/echonest.csv', low_memory=False)

  return echonest