import numpy as np
import pandas as pd

from DataManager import getTrackData, getGenreData, getFeatureData, getEchonestData

tracks = getTrackData()
genres = getGenreData()
features = getFeatureData()
echonest = getEchonestData()

print(tracks.shape)
print(tracks.columns.values)

print(genres.shape)
print(genres.columns.values)

print(features.shape)
print(features.columns.values)

print(echonest.shape)
print(echonest.columns.values)