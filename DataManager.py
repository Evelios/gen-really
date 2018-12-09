import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ast

data_loc = 'fma_metadata'

# low_memory=False is to have multiple data types in the same matrix
# this is not ideal. Needs better investigation of what is in tha dataset

def getTrackData(): 
  tracks = pd.read_csv(data_loc + '/tracks.csv', index_col=0, header=[0, 1])

  # COLUMNS = [('track', 'tags'), ('album', 'tags'), ('artist', 'tags'),
  #             ('track', 'genres'), ('track', 'genres_all'),
  #             ('track', 'genres_top')]
  # for column in COLUMNS:
  #     tracks[column] = tracks[column].map(ast.literal_eval)

  # COLUMNS = [('track', 'date_created'), ('track', 'date_recorded'),
  #             ('album', 'date_created'), ('album', 'date_released'),
  #             ('artist', 'date_created'), ('artist', 'active_year_begin'),
  #             ('artist', 'active_year_end')]
  # for column in COLUMNS:
  #     tracks[column] = pd.to_datetime(tracks[column])

  # SUBSETS = ('small', 'medium', 'large')
  # tracks['set', 'subset'] = tracks['set', 'subset'].astype(
  #         'category', categories=SUBSETS, ordered=True)

  # COLUMNS = [('track', 'license'), ('artist', 'bio'),
  #             ('album', 'type'), ('album', 'information')]
  # for column in COLUMNS:
  #     tracks[column] = tracks[column].astype('category')

  return tracks

def getGenreData():
  genres = pd.read_csv(data_loc + '/genres.csv', index_col=0)

  return genres

def getFeatureData():
  features = pd.read_csv(data_loc + '/features.csv', index_col=0, header=[0, 1, 2])

  return features

def getEchonestData():
  echonest = pd.read_csv(data_loc + '/echonest.csv', index_col=0, header=[0, 1, 2])

  return echonest