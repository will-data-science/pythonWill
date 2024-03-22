import pandas as pd

TITLE = 'title'
GENRES = 'genres'
YEAR = 'year'


def clean_item_data(item_df) -> pd.DataFrame:
    """
    Cleans the raw item data and returns it as a dataframe.
    :param item_df: Raw data of movie data
    :return: DataFrame of cleaned item data
    """
    ret_df = item_df.copy()
    ret_df[TITLE] = ret_df[TITLE].map(lambda x: x.strip()).map(lambda x: x.lower())
    ret_df[['clean_title', YEAR]] = ret_df[TITLE].str.rsplit('(', n=1, expand=True)
    ret_df[YEAR] = ret_df[YEAR].str.replace('[^0-9]', '', regex=True)
    ret_df['clean_title'] = ret_df['clean_title'].str.replace('[^a-zA-Z0-9 ]', '', regex=True)

    return ret_df


def get_genre_df(item_df, item_id_col) -> pd.DataFrame:
    """
    Transforms raw movie data into a one-hot-encoded genre tab. One row per movie.

    :param item_df: Raw movie data with genre column of pipe-delimited strings.
    :param item_id_col: String column name of item id
    :return: Data Frame of movie IDs and one hot encoded genres.
    """
    temp_genre = 'genre'
    temp_df = item_df.copy()
    temp_df = temp_df[[item_id_col]].merge(
        temp_df[GENRES].str.split('|', expand=True),
        left_index=True,
        right_index=True
    ).melt(id_vars=[item_id_col])
    temp_df = temp_df[temp_df['value'].notnull()]
    temp_df[temp_genre] = temp_df['value'].map(lambda x: x.strip()).map(lambda x: x.lower())
    temp_df[temp_genre] = temp_df[temp_genre].str.replace('[^a-zA-Z0-9 ]', '', regex=True)
    temp_df[temp_genre] = temp_df[temp_genre].str.replace(' ', '_', regex=False)
    temp_df[temp_genre] = 1
    ret_df = temp_df.pivot(index=item_id_col, columns=temp_genre, values='is_genre').fillna(0)

    return ret_df


def process_item_df(item_df, item_id_col) -> pd.DataFrame:
    """
    Cleans and processes raw item data into a new dataframe that can be used for model building and inference.

    :param item_df: Raw item data with column for genre and title
    :param item_id_col: String column name of item id
    """

    clean_df = clean_item_data(item_df=item_df)
    genre_df = get_genre_df(item_df=clean_df, item_id_col=item_id_col)
    # TODO: Prob less efficient to merge against the interaction df but good for now
    # TODO: In future construct an item df with only the item information
    ret_df = clean_df.merge(
        genre_df,
        on=item_id_col,
        how='left'
    )
    return ret_df
