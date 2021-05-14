import pandas as pd
import numpy as np

from scipy import stats
from sklearn.preprocessing import LabelBinarizer, LabelEncoder, OneHotEncoder
from sklearn.impute import KNNImputer


def num_columns(df):
    """
    Create a list with the names of the numeric columns of a dataframe.
    This function is used on rem_outliers and knn_missings.

    Params:
        - df = dataframe.
    """

    df_num_cols = df.select_dtypes(include=np.number).columns

    list_num_cols = list(df_num_cols)

    return list_num_cols


def rem_col_nan(df, per_na=.3, rem_print=False):
    """
    If a column has more than 30 % NaN, will be removed.
    Percentage NaN could be changed on the params.

    Params:
        - df = dataframe.
        - per_na = percentage limit of Nan to remove the column, by default 0.30.
        - rem_print = print the list with removed columns.
    """

    df_rem_nan = df.copy()

    num_rows = len(df_rem_nan.index) * per_na

    li_col_rem = []

    for i in df_rem_nan:

        if df_rem_nan[i].isnull().sum() >= num_rows:
            df_rem_nan.drop(columns=i, inplace=True)
            li_col_rem.append(i)

    if rem_print:
        print('The columns removed are:', li_col_rem)

    return df_rem_nan


def rem_outliers(df, z_num=3, shape_print=False):
    """
    The rows with a value more than 3 z-score, will be removed.
    The z-score indicates if the number is an outlier.
    Z-Score could be changed on the input.

    Params:
        - df = dataframe
        - z_num = limit of z-score to consider an outlier, by default 3.
        - shape_print: print the number of rows removed.
    """

    df_rem_outliers = df.copy()

    list_num_cols = num_columns(df_rem_outliers)

    if df_rem_outliers[list_num_cols].isnull().values.any():

        return print('There are NaN on df. Please, treat them before transform outliers.')

    else:

        for i in list_num_cols:
            z = np.abs(stats.zscore(df_rem_outliers[i]))

            df_rem_outliers = df_rem_outliers[(z < z_num)]

    if shape_print:
        print('Number of rows removed: ', (df.shape[0] - df_rem_outliers.shape[0]))

    return df_rem_outliers


def knn_missings(df, n_ngb=3):
    """
    First calls the function to select the numeric columns of the dataframe
    and transform the NaN through a KNN with 3 neighbors (optional).
    The return change the values on the original dataframe.

    Params:
        df = dataframe.
        n_ngb = number of neighbors of KNN, by default 3.
    """

    df_knn_msg = df.copy()

    list_num_cols = num_columns(df_knn_msg)

    imputer = KNNImputer(n_neighbors=n_ngb)

    imputer.fit(df[list_num_cols])

    df_knn_msg[list_num_cols] = imputer.transform(df_knn_msg[list_num_cols])

    return df_knn_msg


def nlp_label_enc(df_encoder, cols, p_tf):

    if len(cols) == 1:

        df_encoder[cols] = LabelEncoder(
        ).fit_transform(df_encoder[cols])

        print(cols, p_tf)

    elif len(cols) > 1:

        for i in cols:
            df_encoder[i] = LabelEncoder().fit_transform(df_encoder[i])

            print(i, p_tf)

    return df_encoder


def nlp_binary_enc(df_encoder, cols, p_tf):

    if len(cols) == 1:

        if len(np.unique(df_encoder[cols])) > 2:

            return 'Column has more than two values, cannot be transformed.'

        else:

            df_encoder[cols] = LabelBinarizer(
            ).fit_transform(df_encoder[cols])

            print(cols, p_tf)

    elif len(cols) > 1:

        for i in cols:

            if len(df_encoder[i].unique()) > 2:

                print(i, ' has more than two values, cannot be transformed.')

            else:

                df_encoder[i] = LabelBinarizer(
                ).fit_transform(df_encoder[i])

                print(i, p_tf)

    return df_encoder


def nlp_ohe_enc(df_encoder, cols, p_tf):

    ohenc = OneHotEncoder()

    df_ohe = ohenc.fit_transform(df_encoder[cols]).toarray()

    cols_ohe = ohenc.get_feature_names()

    df_ohe = pd.DataFrame(df_ohe, columns=cols_ohe)

    df_encoder.drop(columns=cols, inplace=True)

    df_encoder = pd.merge(df_encoder, df_ohe,
                          left_index=True, right_index=True)

    print(cols, p_tf)

    return df_encoder


def nlp_dummies_enc(df_encoder, cols, p_tf):
    df_dummies = pd.get_dummies(df_encoder[cols])

    df_encoder.drop(columns=cols, inplace=True)

    df_encoder = pd.merge(df_encoder, df_dummies,
                          left_index=True, right_index=True)

    print(cols, p_tf)

    return df_encoder


def nlp_encoder(df, cols, encoder):
    """
    This function compiles the most used encoders to have them all easily at hand,
    uses Sklearn and Pandas tools for its operation and currently has 4 functions
    which are called using their respective encoder.

    1º encoder = labelencoder:
        To use this encoder you must enter the column name that you want to be converted
        into multiple columns, it can be multiclass.

    2º encoder = binary:
        To use this encoder you must enter the column name that you want to be converted
        into 2 columns.
        This column must contain only 2 values, since the contained values are converted only into 0 and 1.

    3º encoder = onehotencoder:
        To use this encoder you must enter the column names that you want to be converted
        as many columns as there are variables.
        The function remove the original columns and add the new "variables columns" at the end.


    4º encoder = dummies:
        Similar to One hot encoder, you must enter the column names that you want to be converted as many columns as there are variables.
        The function remove the original columns and add the new "variables columns" at the end.

    Params:
    - df = dataframe.
    - cols = pass a list of columns to transform:
    - encoder = select as a string the desired encode to tranform:
        - labelencoder
        - binary
        - onehotencoder
        - dummies
    """
    p_tf = ' has been transformed.'

    df_encoder = df.copy()

    encoder_list = ['labelencoder', 'binary', 'onehotencoder', 'dummies']

    result_enc = any(elem in encoder for elem in encoder_list)

    if not result_enc:
        return print('Param encoder is wrong.')

    if type(cols).__name__ == 'str':
        cols = [cols]

    list_num_cols = num_columns(df_encoder)

    list_passed = list(df_encoder[cols].columns)

    result_cols = any(elem in list_passed for elem in list_num_cols)

    if result_cols:
        return print('Columns passed are numeric please, '
                     'pass only categorical columns.')

    if encoder == "labelencoder":

        df_encoder = nlp_label_enc(df_encoder, cols, p_tf)

        return df_encoder

    elif encoder == 'binary':

        df_encoder = nlp_binary_enc(df_encoder, cols, p_tf)

        return df_encoder

    elif encoder == "onehotencoder":

        df_encoder = nlp_ohe_enc(df_encoder, cols, p_tf)

        return df_encoder

    elif encoder == "dummies":

        df_encoder = nlp_dummies_enc(df_encoder, cols, p_tf)

        return df_encoder
