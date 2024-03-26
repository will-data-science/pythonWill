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
    temp_df['is_genre'] = 1
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
    ret_df = clean_df.merge(
        genre_df,
        on=item_id_col,
        how='left'
    )
    return ret_df


def get_agg_feature_df(source_df: pd.DataFrame, ui_id_col: str, agg_feature_col: str) -> pd.DataFrame:
    """
    Returns dataframe of features aggregated to basic statisticsL mean, median, min, max, std

    :param source_df: Pandas DataFrame of non-aggregated data
    :param ui_id_col: String column name for a user (u), item (i), or other identifier that you want to aggregate to
                      that level
    :param agg_feature_col: String column name for the column you want to buidl features for
    """

    ret_df = source_df.groupby(ui_id_col).agg(
        agg_feature_mean=(agg_feature_col, 'mean'),
        agg_feature_median=(agg_feature_col, 'median'),
        agg_feature_std=(agg_feature_col, 'std'),
        agg_feature_min=(agg_feature_col, 'min'),
        agg_feature_max=(agg_feature_col, 'max')
    )

    col_rename_mapping = {
        'agg_feature_mean': agg_feature_col + '_mean',
        'agg_feature_median': agg_feature_col + '_median',
        'agg_feature_std': agg_feature_col + '_std',
        'agg_feature_min': agg_feature_col + '_min',
        'agg_feature_max': agg_feature_col + '_max',
    }

    ret_df = ret_df.rename(columns=col_rename_mapping)

    return ret_df


def get_ratings_targets_df(
        ratings_interaction_df: pd.DataFrame,
        user_ratings_df: pd.DataFrame,
        user_id_col: str,
        item_id_col: str
) -> pd.DataFrame:
    """
    Generate a dataframe of targets based on ratings.
    """
    # GroupBy incase user placed multiple ratings on an item
    ret_df = ratings_interaction_df.groupby([user_id_col, item_id_col]).agg(
        user_item_rating_mean=('rating', 'mean')
    ).merge(
        user_ratings_df, on=[user_id_col], how='left'
    )

    ret_df['has_interacted'] = True
    ret_df['rating_atleast_3'] = ret_df['user_item_rating_mean'] > 2
    ret_df['rating_atleast_4'] = ret_df['user_item_rating_mean'] > 3
    ret_df['rating_atleast_5'] = ret_df['user_item_rating_mean'] > 4
    ret_df['rating_atleast_user_mean'] = ret_df['user_item_rating_mean'] >= ret_df['rating_mean']
    ret_df['rating_atleast_user_median'] = ret_df['user_item_rating_mean'] >= ret_df['rating_median']

    return ret_df

def get_users(interaction_df: pd.DataFrame, user_id_col: str) -> pd.DataFrame:
    ret_df = interaction_df[[user_id_col]].drop_duplicates()
    return ret_df


def get_items(interaction_df: pd.DataFrame, item_id_col: str) -> pd.DataFrame:
    ret_df = interaction_df[[item_id_col]].drop_duplicates()
    return ret_df


def process_user_df(interaction_df: pd.DataFrame, user_id_col: str) -> pd.DataFrame:
    pass
