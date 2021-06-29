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
 - [bivariant_num](#bivariant_num)
 - [bivariant_cat](#bivariant_cat)
 - [bivariant_cat_num](#bivariant_cat_num)
 - [bivariant_all](#bivariant_all)
 - [trivariant_num](#trivariant_num)
 - [phik_matrix_simple](#phik_matrix_simple)
 - [overview](#overview)
 - [categorical_columns](#categorical_columns)
 - [phik_matrix](#phik_matrix)
 - [matrix_correlacion_simple](#matrix_correlacion_simple)
 - [matrix_correlacion](#matrix_correlacion)
 - [correlacion_target_simple](#correlacion_target_simple)
 - [correlacion_target](#correlacion_target)
 - [wordcloud_forms](#wordcloud_forms)
 - [goldcloud](#goldcloud)
 - [circle_wordcloud](#circle_wordcloud)
 - [simple_wordcloud](#simple_wordcloud)
 
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
Function that graphically displays one numerical or categorical variable through a distplot/boxplot and a countplot, respectively.
#### Params:     
- df: dataframe.
- col_1: dataframe column (i.e. series) that contains the numeric or categorical variable to be displayed. 
- boxplot: False by default. If boxplot is informed as True, the function displays a boxplot instead of a histogram. It can only be used with numeric variables.
- rotation: rotation takes None by default. If rotation is informed as True, the labels for x values are displayed with a 45 º rotation.
- kde: kde refers to Kernel Density Estimate, which is used for visualizing the probability density of a continuous variable.It takes None by default.
- palette: the palette by default is the following list: ["#0879B1","#A61D39", "#92d7f6", "#d1979a"], it can be changed for any Seaborn palette.
- xlabel: False by default. It is used to define the xlabel. It must be introduced as a string.
- color: this parameter is used to change the color of the plot. The color by default is "#A61D39".
#### Examples:
- univariant(titanic_df,titanic_df["Age"],kde = True);
- univariant(titanic_df,titanic_df["Fare"],kde= True,palette = "rocket", boxplot = True,xlabel = "Tarifa");
- univariant(titanic_df,titanic_df["Survived"],palette = "viridis", xlabel = "Puerta de embarque");

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### bivariant_num
Function that graphically displays two numeric variables through a scatterplot.
#### Params:     
- df: dataframe.
- col_1: dataframe column (i.e. series) containing the numeric variable to be displayed on the x axis.
- col_2: dataframe column (i.e. series) containing the numeric variable to be displayed on the y axis.
- color: this parameter is used to change the color of the plot. The color by default is "#0879B1".
- xlabel: False by default. It is used to define the xlabel. It must be introduced as a string.
- ylabel: False by default. It is used to define the ylabel. It must be introduced as a string.
#### Examples:
- bivariant_num(titanic_df,titanic_df["Age"],titanic_df["Fare"],xlabel= "Age", ylabel = "Fare");

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### bivariant_cat
Function that graphically displays two categorical or binary variables through a catplot.  
The values of the first variable are displayed on the x-axis as bars, with a count of values on the y-axis. 
The second variable is displayed through the different colors of the bars in the catplot.
#### Params:     
- df: dataframe.
- col_1: dataframe column (i.e. series) containing the first categorical variable, to be displayed through the bars.
- col_2: dataframe column (i.e. series) containing the categorical variable, to be displayed through the color of the bars.
- rotation: rotation takes None by default. If rotation is informed as True, the labels for x values are displayed with a 45 º rotation.
- palette: this parameter is used to inform a different Seaborn´s palette. The palette by default is "rocket".
- xlabel: False by default. It is used to define the xlabel. It must be introduced as a string.
- ylabel: False by default. It is used to define the ylabel. It must be introduced as a string.
#### Examples:
- bivariant_cat(titanic_df,titanic_df["Sex"],titanic_df["Embarked"], xlabel = "Género", ylabel = "Num. personas", rotation = True);
- bivariant_cat(suic_df,suic_df["country"],suic_df["sex"],rotation = True, xlabel = "Country",palette = "viridis");

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### bivariant_cat_num
Function that graphically displays the combination of a categorical and a numeric variable through a treeplot.
#### Params: 
- df: dataframe.
- col_1: dataframe column (i.e. series) containing the categorical variable.
- col_2: dataframe column (i.e. series) containing the numerical variable.
- palette: this argument is used to change the Seaborn´s palette. The palette by default is "rocket".
#### Examples:
- bivariant_cat_num(titanic_df,titanic_df["Sex"],titanic_df["Fare"]);
- bivariant_cat_num(titanic_df,titanic_df["Fare"],titanic_df["Embarked"]);

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### bivariant_all
This function has been created to be by the overview´s function, but it can be used independently.
It shows the relation between two numeric variables through the most appropiate plot depending on the type of variables informed.
- Two numeric variables are displayed through a scatterplot.
- Two categorical variables are displayed through a catplot.
It has been created to be called       
#### Params: 
- df : dataframe.
- col_1 : dataframe column (i.e. series) containing the first variable to be plotted. 
- col_2 : dataframe column (i.e. series) containing the second variable to be plotted.
- rotation: it takes None by default. If rotation is informed as True, the labels for x values are displayed with a 45 º rotation.
- color: The color to be displayed by the scatterplot when only two numeric variables are provided. Color is red ("#A61D39") by default.
- palette: this parameter is used to inform a different Seaborn´s palette. The palette by default is "rocket".
- xlabel: False by default. It is used to define the xlabel. It must be introduced as a string.
- ylabel: False by default. It is used to define the ylabel. It must be introduced as a string.
#### Examples:
- bivariant_all(titanic_df,titanic_df["Fare"],titanic_df["Survived"],palette= "viridis", xlabel = "Fare");
- bivariant_all(autism_df,autism_df["country_of_res"],autism_df["class"],palette= "viridis", xlabel = "Country");
- bivariant_all(autism_df,autism_df["country_of_res"],autism_df["screening_score"],xlabel = "Country", ylabel = "Score");

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### trivariant_num
This function shows the relation between three variables through a scatterplot.  
It only admits two numerical variables as x and y and a third categorical or binary variable as hue.
#### Params: 
- df: dataframe.
- col_1: dataframe column (i.e. series) containing the numeric variable to be displayed on the x axis.
- col_2: dataframe column (i.e. series) containing the numeric variable to be displayed on the y axis.
- hue: dataframe column´s name (i.e. string). It refers to the variable to be displayed through the colors of the scatterplot´s points, which must be a 
 a categorical or binary variable. Hue takes None by default.
- rotation: It takes None by default. If rotation is informed as True, the labels for x values are displayed with a 45 º rotation. 
- palette: this parameter is used to inform a different Seaborn´s palette. The palette by default is "rocket".
- xlabel: False by default. It is used to define the xlabel. It must be introduced as a string.
- ylabel: False by default. It is used to define the ylabel. It must be introduced as a string.
#### Examples:
- trivariant_num(titanic_df,titanic_df['Age'],titanic_df['Fare'], hue = "Sex", palette = "viridis", xlabel = "Passenger´s age", ylabel = "Fare in euros");
- trivariant_num(titanic_df,titanic_df["Embarked"], titanic_df["Fare"],hue ='Survived');

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### phik_matrix_simple
 This function creates a Phik Matrix as from the whole dataframe.
#### Params: 
- df = Dataframe
- nuevo_cmap: False by default. This parameter is used to change the Phick matrix´s colormap. Example: nuevo_cmap = sns.diverging_palette(150, 275, s=80, l=55, n=9)
#### Examples:
- phik_matrix_simple(market_df)
- phik_matrix_simple(titanic_df,nuevo_cmap = sns.diverging_palette(220, 20, as_cmap=True))

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### overview
1. Description
Function that graphically displays up to three variables through through the most appropiate kind of plot depending on the variables provided, as well as a Phick
matrix in case that a whole dataframe is provided.
The plots displayed depend on the number and kind (numeric or categorical) of the variables provided:
- One numerical varible is displayed through a through a displot or a boxplot, if the argument boxplot is introduced.
- One categorical variable is displayed through a countplot.
- Two numeric variables are displayed through a scatterplot.
- Two categorical variables are displayed through a catplot.
- A categorical and a numeric variable are displayed through a treeplot.   
- The relation between three variables is displayed through a scatterplot. The third variable is introduced as hue and must be a categorical or binary variable.
- If a whole dataframe is provided, the function displays a Phick matrix for all variables in the dataframe.    

2. Functions used by overview´s function.
The overview function uses the following functions from this same library. Please refer to their corresponding documentation for more clarification.
- univariant
- bivariant_num
- bivariant_cat
- bivariant_cat_num
- bivariant_all
- trivariant_num
- phik_matrix_simple  
  
#### Params: 
- df: dataframe.
- col_1:  dataframe´s column (i.e. series) containing the fist variable.
- col_2: dataframe´s column (i.e. series) containing the second variable.
- hue: dataframe column´s name (i.e. string). It refers to the variable to be displayed through the colors of the scatterplot´s points, which must be a 
 a categorical or binary variable. Hue takes None by default.                 
- boxplot: False by default. If boxplot is informed as True, the function displays a boxplot instead of a histogram. It can only be used with numeric variables.
- kde = kde stands for Kernel Density Estimate, which is used for visualizing the probability density of a continuous variable.It takes None by default.
- rotation = It takes None by default. If rotation is informed as True, the labels for x values are displayed with a 45 º rotation.
- color: The color to be displayed by the scatterplot when two numeric variables are provided. Color is red ("#A61D39") by default.
- palette: the palette by default is "rocket". This parameter is used to inform a different Seaborn´s palette than the palette by default.
- nuevo_cmap: False by default. This parameter is used to change the Phick matrix´s colormap. . Example: nuevo_cmap = sns.diverging_palette(150, 275, s=80, l=55, n=9)
- xlabel: False by default. This parameter is introduce a label for the x axes and it must be introduced as a string.
- ylabel: False by default. This parameter is introduce a label for the y axes and it must be introduced as a string.
   
#### Examples:
- overview(titanic_df, nuevo_cmap = sns.diverging_palette(220, 20, as_cmap=True),xlabel = "Age", ylabel = "Fare"); 
- overview(titanic_df,titanic_df["Survived"], palette = "cubehelix");
- overview(titanic_df,titanic_df["Fare"],kde=True,boxplot = True,xlabel = "Titanic Fares");
- overview(titanic_df,titanic_df["Age"],titanic_df["Fare"],hue = "Survived",palette = "magma",xlabel = "Passenger´s age", ylabel = "Fare in euros");
- overview(titanic_df,titanic_df['Age'],titanic_df['Fare'], hue = "Sex", palette = "viridis", xlabel = "Passenger´s age", ylabel = "Fare in euros")

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
