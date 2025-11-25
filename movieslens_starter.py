import numpy as np
import pandas as pd
import sqlite3

movies_df = pd.read_csv('/kaggle/input/movielens/movies.csv')
ratings_df = pd.read_csv('/kaggle/input/movielens/ratings.csv')
tags_df = pd.read_csv('/kaggle/input/movielens/tags.csv')

conn = sqlite3.connect(':memory:')

movies_df.to_sql('movies', conn, index=False, if_exists='replace')
ratings_df.to_sql('ratings', conn, index=False, if_exists='replace')
tags_df.to_sql('tags', conn, index=False, if_exists='replace')
