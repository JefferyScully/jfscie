
# Table of Contents

1.  [Train LinearRegression Model](#org3e1e0bc)
2.  [Define Variables](#org6ec88be)
    1.  [DB table column - HL<sub>PCT</sub>](#orgf46e27b)
    2.  [DB table column - PCT<sub>change</sub>](#org31cbe69)
    3.  [Python Variable - X](#org94f2716)
    4.  [Python Variable - X<sub>lately</sub>](#orgb5a7f2f)
    5.  [Python Variable - y](#org5d1aecb)
    6.  [Python Variable - X<sub>train</sub>](#org09aefbf)
    7.  [Python Variable - y<sub>train</sub>](#org009388c)
    8.  [Python Variable - X<sub>test</sub>](#org8aea741)
    9.  [Python Variable - y<sub>test</sub>](#org1ac478e)
3.  [How LinearRegression Works](#orga2fe33b)
4.  [Save Model, using Pickle](#org4871617)
5.  [Create](#org704564a)

Quandl api key - 6UfyTfL7MDo26ypfYzVd
Include pydoc
Include pip freeze output
Include try blocks


<a id="org3e1e0bc"></a>

# Train LinearRegression Model

Using Quandl, an API that provides stock price data. The python libarary returns a pandas dataframe.

Getting Data for Google stock prices from DATE - DATE. Will train model using LinearRegression, and use it to predict future stock prices.

Data:
Open:
High:
Low:
Close:
Volume:
Ex-Dividend:
Split Ratio:
Adj. Open:
Adj. High:
Adj. Low:
Adj. Close:
Adj. Volume:


<a id="org6ec88be"></a>

# Define Variables


<a id="orgf46e27b"></a>

## DB table column - HL<sub>PCT</sub>


<a id="org31cbe69"></a>

## DB table column - PCT<sub>change</sub>

-   This is the percent change of closing price verses the opening opening price


<a id="org94f2716"></a>

## Python Variable - X


<a id="orgb5a7f2f"></a>

## Python Variable - X<sub>lately</sub>


<a id="org5d1aecb"></a>

## Python Variable - y


<a id="org09aefbf"></a>

## Python Variable - X<sub>train</sub>


<a id="org009388c"></a>

## Python Variable - y<sub>train</sub>


<a id="org8aea741"></a>

## Python Variable - X<sub>test</sub>


<a id="org1ac478e"></a>

## Python Variable - y<sub>test</sub>


<a id="orga2fe33b"></a>

# How LinearRegression Works


<a id="org4871617"></a>

# Save Model, using Pickle


<a id="org704564a"></a>

# Create

