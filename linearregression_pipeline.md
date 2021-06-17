
# Table of Contents

1.  [Train LinearRegression Model](#orgf8a4e8a)
2.  [Define Variables](#org7aaaf12)
    1.  [DB table column - HL<sub>PCT</sub>](#orgf97abbe)
    2.  [DB table column - PCT<sub>change</sub>](#org813962b)
    3.  [Python Variable - X](#org7ec028e)
    4.  [Python Variable - X<sub>lately</sub>](#orgb9dc761)
    5.  [Python Variable - y](#org60202f3)
    6.  [Python Variable - X<sub>train</sub>](#org9d44b5f)
    7.  [Python Variable - y<sub>train</sub>](#org97f145e)
    8.  [Python Variable - X<sub>test</sub>](#orgd1d68dc)
    9.  [Python Variable - y<sub>test</sub>](#orgf57cb27)
3.  [How LinearRegression Works](#org6f4ae89)
4.  [Save Model, using Pickle](#org4427b4e)
5.  [Create](#org0b88024)

Quandl api key - 6UfyTfL7MDo26ypfYzVd
Include pydoc
Include pip freeze output
Include try blocks


<a id="orgf8a4e8a"></a>

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


<a id="org7aaaf12"></a>

# Define Variables


<a id="orgf97abbe"></a>

## DB table column - HL<sub>PCT</sub>


<a id="org813962b"></a>

## DB table column - PCT<sub>change</sub>

-   This is the percent change of closing price verses the opening opening price

<https://latex.codecogs.com/svg.image?PCT\_change=\frac{Closing\_Price-Opening\_Price}{Opening\_Price}\times100>


<a id="org7ec028e"></a>

## Python Variable - X


<a id="orgb9dc761"></a>

## Python Variable - X<sub>lately</sub>


<a id="org60202f3"></a>

## Python Variable - y


<a id="org9d44b5f"></a>

## Python Variable - X<sub>train</sub>


<a id="org97f145e"></a>

## Python Variable - y<sub>train</sub>


<a id="orgd1d68dc"></a>

## Python Variable - X<sub>test</sub>


<a id="orgf57cb27"></a>

## Python Variable - y<sub>test</sub>


<a id="org6f4ae89"></a>

# How LinearRegression Works


<a id="org4427b4e"></a>

# Save Model, using Pickle


<a id="org0b88024"></a>

# Create

