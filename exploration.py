import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_loc = 'fma_metadata'

# low_memory=False is to have multiple data types in the same matrix
# this is not ideal. Needs better investigation of what is in tha dataset
tracks = pd.read_csv(data_loc + '/tracks.csv', low_memory=False)
genres = pd.read_csv(data_loc + '/genres.csv', low_memory=False)
features = pd.read_csv(data_loc + '/features.csv', low_memory=False)
echonest = pd.read_csv(data_loc + '/echonest.csv', low_memory=False)

print(tracks.shape)
print(tracks.columns.values)

print(genres.shape)
print(genres.columns.values)

print(features.shape)
print(features.columns.values)

print(echonest.shape)
print(echonest.columns.values)