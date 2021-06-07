# PYTHONEER

![Logo3](https://raw.githubusercontent.com/javapagar/pip_install_clase/master/Logo3.PNG)

## Description

This library has been designed to optimize the first steps of a data science project. It contains functions that simplify data cleaning and data visualization. 

***

## Install

To install the full library write on your console: *pip install pythoneer*

***

### Preinstall libraries

In order to use this library you will need to make sure that the following libraries are installed on your system:

  - pandas
  - numpy
  - seaborn
  - matplotlib
  - plotly
  - scipy
  - sklearn
  
***
 
<a name="index"></a>
### Structure & documentation

Here's a folder structure with documentation about Pythoneer's functions. 
Clik on any link below to read deeper:

Data cleaning:

 - [num_columns](#num_columns)
 - [rem_col_nan](#rem_col_nan)
 - [rem_outliers](#rem_outliers)
 - [knn_missings](#knn_missings)
 - [nlp_encoder](#nlp_encoder)
 
Visualization:
 - [univariant](#univariant)
 - [categorical_columns](#categorical_columns)
 - [phik_matrix_simple](#phik_matrix_simple)
 - [phik_matrix](#phik_matrix)
 - [matrix_correlacion_simple](#matrix_correlacion_simple)
 - [matrix_correlacion](#matrix_correlacion)
 - [correlacion_target_simple](#correlacion_target_simple)
 - [correlacion_target](#correlacion_target)
 - [wordcloud_forms](#wordcloud_forms)
 - [goldcloud](#goldcloud)
 - [circle_wordcloud](#circle_wordcloud)
 - [simplewordcloud](#simplewordcloud)
 
***

### Documentation
<a href="#index"><p align="right" href="#index">Back to index</p></a>

### num_columns
This function creates a list with the names of the numeric columns of a dataframe.
It is also used on rem_outliers and knn_missings functions later.
#### Params:
 - df : dataframe

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### rem_col_nan
This function removes the columns with more than 30 % NaN, by default.
The threshold can be be changed through the second param of the function.
#### Params:
 - df = dataframe.
 - per_na = threshold of NaN above which the column will be removed, by default 0.30.
 - rem_print = prints the list with columns removed.

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### rem_outliers
The rows with a value more than 3 z-score, will be removed.
The z-score indicates if the number is an outlier.
Z-Score could be changed through the second param of the function.
#### Params:
- df = dataframe
- z_num = limit of z-score to consider an outlier, by default 3.
- shape_print: print the number of rows removed.

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### knn_missings
This function firstly calls the first function above to select the numeric columns of the dataframe and then replace the NaNs through a KNN algorithm.
The return of the function replace the values on the original dataframe.
#### Params:
- df = dataframe.
- n_ngb = number of neighbors of KNN, by default 3.

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### nlp_encoder
This function compiles the most used encoders to have them all easily at hand, uses Sklearn and Pandas tools for its operation and currently has 4 functions
which are called using their respective encoder.

1º encoder = labelencoder:
To use this encoder you must enter the column name that you want to be converted into multiple columns, it can be multiclass.

2º encoder = binary:
To use this encoder you must enter the column name that you want to be converted into 2 columns. This column must contain only 2 values, since the contained values are converted only into 0 and 1.

3º encoder = onehotencoder:
To use this encoder you must enter the column names that you want to be converted as many columns as there are variables. The function remove the original columns and add the new "variables columns" at the end.

4º encoder = dummies:
Similar to One hot encoder, you must enter the column names that you want to be converted as many columns as there are variables. The function remove the original columns and add the new "variables columns" at the end.
#### Params:
- df = dataframe.
- cols = list of columns to be transformed.
- encoder = select as a string the desired encode to tranform:
        - labelencoder
        - binary
        - onehotencoder
        - dummies

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### univariant
Function that graphically displays one numerical or categorical variable through a histogram and a boxplot, a countplot or a displot depending on the kind of variable informed (i.e. numerical or categorical variable, respectively).
#### Params:
- df: dataframe.
- col_1: dataframe column (i.e. series) that contains the numeric or categorical variable to be displayed by the function. 
- boxplot = False by default. If boxplot is informed as True, the function displays a boxplot instead of a histogram. It can only be used to dispolay numeric variables.
 - rotation = rotation takes None by default. If rotation is informed as True, the labels for x values are displayed with a 45 º rotation.
 - kde = Kernel Density Estimate is used to visualize the probability density of a continuous variable.It takes None by default.
 - palette: the palette by default is the following list : ["#0879B1","#A61D39", "#92d7f6", "#d1979a"]

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### categorical_columns
Create a new dataframe containing only the categorical variables of the original dataframe.
#### Params:
- df = dataframe.

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### phik_matrix_simple
Creates a Phik Matrix
#### Params:
- df = dataframe.

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### phik_matrix
Creates a Phik Matrix. The plot can be highly personalized through the params described below. 
#### Params:
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

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### matrix_correlacion_simple
Creates a correlation matrix.
#### Params:
- df = dataframe.

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### matrix_correlacion
This function creates a correlation matrix. The plot can be highly personalized through the params described below.  
#### Params:
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
 - xticklabels = If True, plot the column names of the dataframe in x-axis. If False, don’t plot the column names.
 - xticklabels_rot = degrees of rotation of the xticklabels
 - yticklabels = If True, plot the column names of the dataframe in y-axis. If False, don’t plot the column names. 
 - yticklabels_rot = degrees of rotation of the yticklabels

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### correlacion_target_simple
Creates a correlation matrix of the target with the rest of the variables in the dataframe.
#### Params:
- df = dataframe.
- target: name of the target column

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### correlacion_target
Create a correlation matrix of the target with the rest of the variables which can be highly personalized through the params described below.
#### Params:
- df = dataframe.
- df: Dataframe
- target: name of the target column
- size = size of the matrix
- palette = Insert color palette
- title = title
- cbar = If True, create a bar plot

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### wordcloud_forms
Show wordcloud with form and colour based on uploaded png. image
#### Params:
- image_pad: Write a string with the png directory.
- text: string text to wordcloud
- background_color: (Default: 'White')
- stopwords: (Default: None)

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### goldcloud
Show luxury wordcloud with golden letters and black background.
#### Params:
- text: string text to wordcloud
- backgrouncolor: (Default: 'Black')
- stopwords: (Default: None)

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### circle_wordcloud
Show simple wordcloud with circle form.
#### Params:
- text: string text to wordcloud
- backgrouncolor: (Default: 'white')
- stopwords: (Default: None)

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### simple_wordcloud
Show simple wordcloud with basic color.
#### Params:
- text: string text to wordcloud
- backgrouncolor: (Default: 'black')
- stopwords: (Default: None)



***

### Memory

This library has been created by Data Science students from The Bridge (Digital talent accelerator).

#### Authors:
* Alberto Lara
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/alarab/)
* Julia Martínez
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/juliamariamartineztapia/)
* Javier Melo
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/f-javier-melo-delgado-836590131/)
* Cristian España
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/cespanac/)
* Javier Aparicio
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/apariciogarciajavier/)
* Cristina Martínez
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/cristina-mart%C3%ADnez-garc%C3%ADa-438209170/)
* José Serrat
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/jos%C3%A9-serrat-torres-45625b144/)
* Ramón Ascanio
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/ram%C3%B3n-ascanio-armada-78196a176/)
* Sonia Dosio
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/sonia-dosio-revenga-17812245/)
* Arturo Guzmán
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/arturo-guzm%C3%A1n-solera-3444071b3/)
* Marta Miñana
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/marta-mi%C3%B1ana-01455a2a/)
* Mario Massaro
[![LinkedIn][logo_LinkedIn]](https://www.linkedin.com/in/mariomassaro/)



[logo_LinkedIn]: https://static.licdn.com/scds/common/u/images/logos/favicons/v1/16x16/favicon.ico "LinkedIn"
