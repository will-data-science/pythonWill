import pandas as pd

TITLE = 'title'


def clean_raw_movie_data(raw_df) -> pd.DataFrame:
    """
    Cleans the raw movie data and returns it as a dataframe.
    :param raw_df: Raw data of movie data
    :return: DataFrame of cleaned movied data
    """
    ret_df = raw_df.copy()
    ret_df[TITLE] = ret_df[TITLE].map(lambda x: x.strip()).map(lambda x: x.lower())
    ret_df[['clean_title', 'year']] = ret_df[TITLE].str.rsplit('(', n=1, expand=True)
    ret_df['year'] = ret_df['year'].str.replace('[^0-9]', '', regex=True)
    ret_df['clean_title'] = ret_df['clean_title'].str.replace('[^a-zA-Z0-9 ]', '', regex=True)

    return ret_df


def get_genre_df(raw_df) -> pd.DataFrame:
    """
    Transforms raw movie data into a one-hot-encoded genre tab. One row per movie.

    :param raw_df: Raw movie data with genre column of pipe-delimited strings.
    :return: Data Frame of movie IDs and one hot encoded genres.
    """
    temp_df = raw_df.copy()
    temp_df = temp_df[['movieId']].merge(
        temp_df['genres'].str.split('|', expand=True),
        left_index=True,
        right_index=True
    ).melt(id_vars=['movieId'])
    temp_df = temp_df[temp_df['value'].notnull()]
    temp_df['genre'] = temp_df['value'].map(lambda x: x.strip()).map(lambda x: x.lower())
    temp_df['genre'] = temp_df['genre'].str.replace('[^a-zA-Z0-9 ]', '', regex=True)
    temp_df['genre'] = temp_df['genre'].str.replace(' ', '_', regex=False)
    temp_df['is_genre'] = 1
    ret_df = temp_df.pivot(index='movieId', columns='genre', values='is_genre').fillna(0)

    return ret_df
