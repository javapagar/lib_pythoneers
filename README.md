# PYTHONEER

![Logo3](https://raw.githubusercontent.com/javapagar/pip_install_clase/master/Logo3.PNG)

## Description

This library has been designed to optimize the first steps of a data science project. It contains functions that simplify data cleaning and data visualization. Mainly, Pythoneer will help you to choose the best machine learning model for your data.

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

 - [1.Function 1](#1-Function-1)
 - [2.Function 2](#2-Function-2)
 - [3.Function 3](#3-Function-3)
 
Visualization:

 - [degrade_color](#degrade_color)
 - [color_palette](#color_palette)
 - [pythoneer_palette](#pythoneer_palette)
 - [categorical_columns](#categorical_columns)
 - [phik_matrix_simple](#phik_matrix_simple)
 - [univariant](#univariant)

Machine learning:

 - [7.Function 7](#7-Function-7)
 - [8.Function 8](#8-Function-8)
 - [9.Function 9](#9-Function-9)
 
***

### Documentation
<a href="#index"><p align="right" href="#index">Back to index</p></a>
### 1. Function 1
This function blablabla
#### Params:
 - Param1: blublublu
 - Param2: bliblibli
#### Code Example:
'a=1'

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### 2. Function 2
This function blablabla
#### Params:
 - Param1: blublublu
 - Param2: bliblibli
#### Code Example:
'a=1'

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### 3. Function 3
This function blablabla
#### Params:
 - Param1: blublublu
 - Param2: bliblibli
#### Code Example:
'a=1'

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### degrade_color
Create a variable that contains a color map segmented into 255 parts (color degradation).
#### Params:
- list_color = hexadecimal color list.
#### Code Example:
deg_color = degrade_color(['#0879b1','#FFFFFF','#a61d39'])

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### color_palette
Create a custom color palette and use the names entered as variables in your code. The minimum value of the palette must be three color. 
 Return:
- palette_2 = list of the first two colors.
- palette_3 = list of the first three colors.
- degrade_palette = variable with the gradient of the first two colors passing through white between the first color and the second.
#### Params:
- names = color name list
- colors = hexadecimal colors list
- BW = True value if you want to incorporate the color '#F08080' as 'white' and '#000000' as 'black'    
#### Code Example:
palette_2, palette_3, degrade_palette = color_palette (['blue','pink','red'],['#0879b1','#c41bab','#a61d39'], BW = True)

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### pythoneer_palette
Color palette predefined by the color blue ('#0879b1') and the color red ('#a61d39').
#### Params:

#### Code Example:
'pythoneer, pythoneer_degrade = pythoneer_palette()

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### categorical_columns
Create a dataframe with the categorical columns.
#### Params:
- df = dataframe.
#### Code Example:
categorical_df = categorical_columns(df)

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### phik_matrix_simple
Create a Phik Matrix
#### Params:
- df = dataframe.
#### Code Example:
phik_matrix_simple(df)

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### univariant


<a href="#index"><p align="right" href="#index">Back to index</p></a>
### 7. Function 7
This function blablabla
#### Params:
 - Param1: blublublu
 - Param2: bliblibli
#### Code Example:
'a=1'

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### 8. Function 8
This function blablabla
#### Params:
 - Param1: blublublu
 - Param2: bliblibli
#### Code Example:
'a=1'

<a href="#index"><p align="right" href="#index">Back to index</p></a>
### 9. Function 9
This function blablabla
#### Params:
 - Param1: blublublu
 - Param2: bliblibli
#### Code Example:
'a=1'

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
