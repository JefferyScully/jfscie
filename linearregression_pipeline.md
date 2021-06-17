
# Table of Contents

1.  [Train LinearRegression Model](#org449f876)
2.  [Define Variables](#org18bb51d)
    1.  [DB table column - HL<sub>PCT</sub>](#org83c35a0)
    2.  [DB table column - PCT<sub>change</sub>](#org3fedbeb)
    3.  [Python Variable - X](#org1385dea)
    4.  [Python Variable - X<sub>lately</sub>](#org4f4850d)
    5.  [Python Variable - y](#org48dc9a3)
    6.  [Python Variable - X<sub>train</sub>](#org0894329)
    7.  [Python Variable - y<sub>train</sub>](#orge732430)
    8.  [Python Variable - X<sub>test</sub>](#orgfac25e2)
    9.  [Python Variable - y<sub>test</sub>](#org9e23586)
3.  [How LinearRegression Works](#orgec88c09)
4.  [Save Model, using Pickle](#org08af7a2)
5.  [Create](#org6f56d55)

Quandl api key - 6UfyTfL7MDo26ypfYzVd
Include pydoc
Include pip freeze output
Include try blocks


<a id="org449f876"></a>

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


<a id="org18bb51d"></a>

# Define Variables


<a id="org83c35a0"></a>

## DB table column - HL<sub>PCT</sub>


<a id="org3fedbeb"></a>

## DB table column - PCT<sub>change</sub>

-   This is the percent change of closing price verses the opening opening price

<img src="<https://latex.codecogs.com/svg.image?PCT\_change=\frac{Closing\_Price-Opening\_Price}{Opening\_Price}\times100>" />


<a id="org1385dea"></a>

## Python Variable - X


<a id="org4f4850d"></a>

## Python Variable - X<sub>lately</sub>


<a id="org48dc9a3"></a>

## Python Variable - y


<a id="org0894329"></a>

## Python Variable - X<sub>train</sub>


<a id="orge732430"></a>

## Python Variable - y<sub>train</sub>


<a id="orgfac25e2"></a>

## Python Variable - X<sub>test</sub>


<a id="org9e23586"></a>

## Python Variable - y<sub>test</sub>


<a id="orgec88c09"></a>

# How LinearRegression Works


<a id="org08af7a2"></a>

# Save Model, using Pickle


<a id="org6f56d55"></a>

# Create

