
# Table of Contents

1.  [Train LinearRegression Model](#org4681ae1)
2.  [Define Variables](#org0e221b6)
    1.  [DB table column - HL<sub>PCT</sub>](#org6ae20f9)
    2.  [DB table column - PCT<sub>change</sub>](#org167c5a6)
    3.  [Python Variable - X](#org6a786e0)
    4.  [Python Variable - X<sub>lately</sub>](#org7bdf8b4)
    5.  [Python Variable - y](#org2123228)
    6.  [Python Variable - X<sub>train</sub>](#org876efbe)
    7.  [Python Variable - y<sub>train</sub>](#org510394f)
    8.  [Python Variable - X<sub>test</sub>](#orgea5ec8d)
    9.  [Python Variable - y<sub>test</sub>](#org00156f9)
3.  [How LinearRegression Works](#orga4524ff)
4.  [Save Model, using Pickle](#orgcc325b7)
5.  [Create](#org768f0ca)

Quandl api key - 6UfyTfL7MDo26ypfYzVd
Include pydoc
Include pip freeze output
Include try blocks


<a id="org4681ae1"></a>

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


<a id="org0e221b6"></a>

# Define Variables


<a id="org6ae20f9"></a>

## DB table column - HL<sub>PCT</sub>


<a id="org167c5a6"></a>

## DB table column - PCT<sub>change</sub>

-   This is the percent change of closing price verses the opening opening price

<img src="<https://latex.codecogs.com/svg.image?a+b=c>" />


<a id="org6a786e0"></a>

## Python Variable - X


<a id="org7bdf8b4"></a>

## Python Variable - X<sub>lately</sub>


<a id="org2123228"></a>

## Python Variable - y


<a id="org876efbe"></a>

## Python Variable - X<sub>train</sub>


<a id="org510394f"></a>

## Python Variable - y<sub>train</sub>


<a id="orgea5ec8d"></a>

## Python Variable - X<sub>test</sub>


<a id="org00156f9"></a>

## Python Variable - y<sub>test</sub>


<a id="orga4524ff"></a>

# How LinearRegression Works


<a id="orgcc325b7"></a>

# Save Model, using Pickle


<a id="org768f0ca"></a>

# Create

