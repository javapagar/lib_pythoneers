
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

import plotly as py

import plotly.graph_objs as go


import phik
from pylab import *

from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import re
from collections import Counter
import random
import os


# Commented out IPython magic to ensure Python compatibility.
def univariant(df,col_1,palette = ["#0879B1","#A61D39", "#92d7f6", "#d1979a"],kde = False, boxplot = False, rotation = False):
    
    """       
    Function that graphically displays one numerical or categorical variable through a histogram and a boxplot,
    a countplot or a displot depending on the kind of variable informed (i.e. numerical or categorical variable,
    respectively).
    
    Params:
    
     - df: dataframe.
     - col_1: dataframe column (i.e. series) that contains the numeric or categorical variable to be displayed by the function. 
     - boxplot = False by default. If boxplot is informed as True, the function displays a boxplot instead of a histogram. 
     Dispersion can only be used with numeric variables.
     - rotation = rotation takes None by default. If rotation is informed as True, the labels for x values are displayed with a 45 º rotation.
     - kde = Kernel Density Estimate is used to visualize the probability density of a continuous variable.It takes None by default.
     - palette: the palette by default is the following list : ["#0879B1","#A61D39", "#92d7f6", "#d1979a"]
      
    """
    
    import seaborn as sns
    import pandas as pd
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
   
#     %config InlineBackend.figure_format = 'retina'
    sns.set(style='white');      
    plt.figure(figsize=(10,8))
              
    if type(col_1[0]) == str or len(np.unique(col_1)) <= 2:  
        
        fig = sns.countplot(col_1,
                            palette = palette)   
        
    else:       
        
        if boxplot:
            fig =sns.boxplot(col_1, color = "#A61D39");
        
        else:
            fig= sns.displot(col_1, kde = kde, color = "#0879B1",height = 6, aspect = 1.5); 
           
    
    if rotation:
        plt.xticks(rotation = 45);
   
    return fig;

def categorical_columns(df):
    '''
    Create a dataframe with the categorical columns.
    This function is used in: 
                - phik_matrix_simple_categorical
                
    Params:
                - df = dataframe.
    '''

    categorical_df = []
    columns = df.columns

    for i in columns:
        var_1 = df[i]
        if np.dtype(var_1) == np.dtype(object):
            categorical_df.append(i)
        elif len(np.unique(var_1)) <= 2:
            categorical_df.append(i)

    categorical_df = pd.DataFrame(df, columns=categorical_df)
    
    return categorical_df

def phik_matrix_simple(df):
    '''
    Create a Phik Matrix
    
    Params:
            - df = dataframe.
    
    '''
    palette = ['#0879b1', '#FFFFFF', '#a61d39']
    size_matrix = (8, 8)
    cbar = True
    cbar_orientacion = 'vertical',
    annot = True
    phik_matrix = df.phik_matrix()
    
    fig, ax = plt.subplots(figsize=size_matrix)

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", palette)

    heatmap = sns.heatmap(phik_matrix,cbar = cbar,cmap = cmap,annot = annot,
                          square = True,center = 0, vmin = -1,vmax = 1,linewidths=.5)

    plt.title('Phik Matrix',pad = 20) 
            
    plt.show()

def phik_matrix(df, title = 'Phik Matrix', xlabel = None, ylabel = None,title_cbar =  None,
                palette = ['#0879b1', '#FFFFFF', '#a61d39'], size_matrix = (8,8), cbar = False, cbar_orientation = 'vertical',
                annot = False, mask = False, xticklabels = True, xticklabels_rot = None, yticklabels = True, yticklabels_rot = None):
    '''
    Create a Phik Matrix
    
    Params:
            - df = dataframe.
            - title = title.
            - xlabel = x-axis label.
            - ylabel = y-axis label.
            - title_cbar = cbar's title.
            - palette = Insert color palette.
            - size_matrix = size of the matrix.
            - cbar = If True, create a bar plot.
            - cbar_orientation = orientation's bar plot, vertical'or 'horizontal'.
            - annot = If True, write the data value in each cell.
            - mask = If True, create a triangle correlation heatmap.
            - xticklabels = If True, plot the column names of the dataframe in x-axis. If False, don’t plot the column names.
            - xticklabels_rot = degrees of rotation of the xticklabels.
            - yticklabels = If True, plot the column names of the dataframe in y-axis. If False, don’t plot the column names. 
            - yticklabels_rot= degrees of rotation of the yticklabels.  
    '''
    df_small = df.iloc[:, :]
    phik_matrix = df.phik_matrix()

    fig, ax = plt.subplots(figsize=size_matrix)

    if mask:
        mask = np.triu(np.ones_like(phik_matrix, dtype = bool))

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", palette)

    if cbar:
        cbar_kws = {"orientation": cbar_orientation}
    else:
        cbar_kws = None

    heatmap = sns.heatmap(phik_matrix, cbar = cbar, cbar_kws = cbar_kws, cmap = cmap, annot = annot, mask = mask,
                          xticklabels = xticklabels, yticklabels = yticklabels,center = 0,vmax = 1,vmin = -1,
                          square = True,linewidths = .5)
    


    ax.figure.axes[-1].set_ylabel(title_cbar)

    if xlabel:

        plt.xlabel(xlabel)

    if ylabel:
        plt.ylabel(ylabel)

    if xticklabels:
        if xticklabels_rot != 0:
            heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation = xticklabels_rot)
        else:
            heatmap.set_xticklabels(heatmap.get_xticklabels())

    if yticklabels:
        if xticklabels_rot != 0:
            heatmap.set_yticklabels(heatmap.get_yticklabels(),rotation = yticklabels_rot)
        else:
            heatmap.set_yticklabels(heatmap.get_yticklabels())

    plt.title(title, pad = 20)

    plt.show()

def matrix_correlacion_simple(df):
    '''
    Create a correlation matrix
    
    Params:
            - df = Dataframe
    '''
    palette = ['#0879b1','#FFFFFF','#a61d39']
    size_matrix = (5,5)
    cbar = True
    cbar_orientacion = 'vertical'
    annot = True
    correlation_mat = df.corr()

    fig, ax = plt.subplots(figsize = size_matrix)

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", palette)
         
    heatmap = sns.heatmap(correlation_mat, cbar = cbar, cmap = cmap, annot = annot, square = True,
                          center = 0, vmin = -1,  vmax = 1, linewidths = .5) 
   
    plt.title('Correlation Matrix', pad = 20);
        
    plt.show()

def matrix_correlacion(df, title = 'Correlation Matrix', xlabel = None, ylabel = None, title_cbar = None,
                       palette =['#0879b1', '#FFFFFF', '#a61d39'], size_matrix = (8, 8), cbar = False,
                       cbar_orientacion = 'vertical', annot = False, mask = False, xticklabels = True,
                       xticklabels_rot = None, yticklabels = True, yticklabels_rot = None):
    '''
    Create a correlation matrix
    
    Params:
            - df = Dataframe
            - title = title
            - xlabel = x-axis label
            - ylabel = y-axis label
            - title_cbar = cbar's title
            - palette = Insert color palette
            - size_matrix = size of the matrix
            - cbar = If True, create a bar plot
            - cbar_orientation = orientation's bar plot, vertical'or 'horizontal'
            - annot = If True, write the data value in each cell.
            - mask = If True, create a triangle correlation heatmap
            - xticklabels = If True, plot the column names of the dataframe in x-axis. 
            If False, don’t plot the column names.
            - xticklabels_rot = degrees of rotation of the xticklabels
            - yticklabels = If True, plot the column names of the dataframe in y-axis. 
            If False, don’t plot the column names. 
            - yticklabels_rot = degrees of rotation of the yticklabels
    '''

    df_small = df.iloc[:, :]
    correlation_mat = df_small.corr()

    fig, ax = plt.subplots(figsize=size_matrix)

    if mask:
        mask = np.triu(np.ones_like(correlation_mat, dtype=bool))

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", palette)

    if cbar:
        cbar_kws = {"orientation": cbar_orientacion}
    else:
        cbar_kws = None

    heatmap = sns.heatmap(correlation_mat, cbar = cbar, cbar_kws = cbar_kws,  cmap = cmap, annot = annot,  mask = mask,
                          xticklabels = xticklabels, yticklabels = yticklabels, square = True, center = 0,
                          vmin = -1, vmax = 1, linewidths = .5 )

    ax.figure.axes[-1].set_ylabel(title_cbar)

    if xlabel:

        plt.xlabel(xlabel)

    if ylabel:
        plt.ylabel(ylabel)

    if xticklabels:
        if xticklabels_rot != 0:
            heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation = xticklabels_rot)
        else:
            heatmap.set_xticklabels(heatmap.get_xticklabels())

    if yticklabels:
        if xticklabels_rot != 0:
            heatmap.set_yticklabels(heatmap.get_yticklabels(), rotation = yticklabels_rot)
        else:
            heatmap.set_yticklabels(heatmap.get_yticklabels())

    plt.title(title, pad = 20)

    plt.show()

def correlacion_target_simple(df,target):
                              
    '''
    Create a correlation matrix of the target with the rest of the variables.
    
    Params:
            - df: Dataframe
            - target: name of the target column
    '''
    size = (2, 5)
    palette = ['#0879b1', '#FFFFFF', '#a61d39']
    title = None
    cbar = True
    pad = 20

    plt.figure(figsize=size)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", palette)
    heatmap = sns.heatmap(df.corr()[[target]].sort_values(by = target, ascending = False),
    vmin = -1, vmax = 1, annot = True, cmap = cmap, cbar = cbar,square = True, center = 0,
    linewidths = .5)
    plt.title('Correlation with target', pad=pad)

def correlacion_target(df, target, size = (2, 5), palette = ['#0879b1', '#FFFFFF', '#a61d39'],
                       title = 'Correlation with target', cbar = True):
    
    '''
    Create a correlation matrix of the target with the rest of the variables.
    
    Params:
            - df: Dataframe
            - target: name of the target column
            - size = size of the matrix
            - palette = Insert color palette
            - title = title
            - cbar = If True, create a bar plot
    '''
    pad = 20

    plt.figure(figsize = size)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", palette)
    heatmap = sns.heatmap(df.corr()[[target]].sort_values(by = target, ascending = False), vmin = -1,vmax = 1,
                          annot = True, cmap = cmap, cbar = cbar, square = True, center = 0, linewidths = .5)
    heatmap.set_title(title, pad = pad)
    
    def wordcloud_forms(image_pad, text, background_color="white", stopwords=None):
    
    """ 
    Show wordcloud with form and colour based on uploaded png. image.
    
    Params:
        image_pad: Write a string with the png directory.
        text: string text to wordcloud
        background_color: (Default: 'White')
        stopwords: (Default: None)
    """
    
    custom_mask = np.array(Image.open(image_pad))
    wc = WordCloud(width=1000, height=1000, background_color = background_color , mask=custom_mask, stopwords = stopwords)
    wc.generate(text)
    image_colors = ImageColorGenerator(custom_mask)
    wc.recolor(color_func=image_colors)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure(figsize=(10,8))
    plt.show();
    
    def goldcloud(text, background_color = 'black', stopwords=None):
    
        
    """ 
    Show luxury wordcloud with golden letters and black background.
    
    Params:
        text: string text to wordcloud
        background_color: (Default: 'Black')
        stopwords: (Default: None)
    """
    

    wc = WordCloud(background_color = background_color,
                width = 1200,
                height = 1000,
                color_func = gold_color_func,
                stopwords = stopwords).generate(text)

    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    
    def circle_wordcloud(text, background_color = 'white', stopwords=None):
    
    """ 
    Show simple wordcloud with circle form.
    
    Params:
        text: string text to wordcloud
        background_color: (Default: 'white')
        stopwords: (Default: None)
    """

    x, y = np.ogrid[:300, :300]

    mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)


    wc = WordCloud(background_color = background_color, repeat=True, mask=mask, stopwords = stopwords)
    wc.generate(text)

    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    plt.show()
    
    def simplewordcloud(text, background_color = 'black', stopwords=None):
    
    """ 
    Show simple wordcloud with basic color.
    
    Params:
        text: string text to wordcloud
        background_color: (Default: 'black')
        stopwords: (Default: None)
    """

    wc = WordCloud(background_color = background_color,
                width = 1200,
                height = 1000,
                color_func = team_color_func,
                stopwords = stopwords).generate(text)

    plt.imshow(wc)
    plt.axis('off')
    plt.show()
