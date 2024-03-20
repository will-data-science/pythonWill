import pandas as pd


movie_data_csv = "C:/Users/kretz/OneDrive/DataSets/movie.csv"
rating_data_csv = "C:/Users/kretz/OneDrive/DataSets/rating.csv"

movie_df = pd.read_csv(movie_data_csv)
rating_df = pd.read_csv(rating_data_csv)

unique_users = rating_df["userId"].unique()
unique_movies = movie_df["movieId"].unique()

print(unique_users)
