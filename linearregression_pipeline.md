
# Table of Contents

1.  [Train LinearRegression Model](#org46ff185)
2.  [Define Variables](#orgea51cd9)
    1.  [DB table column - HL<sub>PCT</sub>](#orga18ee4f)
    2.  [DB table column - PCT<sub>change</sub>](#orgcd819a9)
    3.  [Python Variable - X](#org2d64454)
    4.  [Python Variable - X<sub>lately</sub>](#org871e774)
    5.  [Python Variable - y](#org65b49a6)
    6.  [Python Variable - X<sub>train</sub>](#orgdccc42e)
    7.  [Python Variable - y<sub>train</sub>](#orge26b450)
    8.  [Python Variable - X<sub>test</sub>](#orga0b9c1a)
    9.  [Python Variable - y<sub>test</sub>](#org327d476)
3.  [How LinearRegression Works](#orgbdd1da8)
4.  [Save Model, using Pickle](#org21623d8)
5.  [Create](#org6089a92)

Quandl api key - 6UfyTfL7MDo26ypfYzVd
Include pydoc
Include pip freeze output
Include try blocks


<a id="org46ff185"></a>

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


<a id="orgea51cd9"></a>

# Define Variables


<a id="orga18ee4f"></a>

## DB table column - HL<sub>PCT</sub>


<a id="orgcd819a9"></a>

## DB table column - PCT<sub>change</sub>

-   This is the percent change of closing price verses the opening opening price

\(PCT\_change = \frac{Closing\_Price - Opening\_Price}{Opening\_Price} \times 100 \)


<a id="org2d64454"></a>

## Python Variable - X


<a id="org871e774"></a>

## Python Variable - X<sub>lately</sub>


<a id="org65b49a6"></a>

## Python Variable - y


<a id="orgdccc42e"></a>

## Python Variable - X<sub>train</sub>


<a id="orge26b450"></a>

## Python Variable - y<sub>train</sub>


<a id="orga0b9c1a"></a>

## Python Variable - X<sub>test</sub>


<a id="org327d476"></a>

## Python Variable - y<sub>test</sub>


<a id="orgbdd1da8"></a>

# How LinearRegression Works


<a id="org21623d8"></a>

# Save Model, using Pickle


<a id="org6089a92"></a>

# Create

