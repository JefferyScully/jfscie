
# Table of Contents

1.  [Train LinearRegression Model](#org7dc93c0)
2.  [Define Variables](#org1e91b26)
    1.  [DB table column - HL<sub>PCT</sub>](#orgd65b2cb)
    2.  [DB table column - PCT<sub>change</sub>](#orgb67dd10)
    3.  [Python Variable - X](#orgbc0a7ee)
    4.  [Python Variable - X<sub>lately</sub>](#orge818812)
    5.  [Python Variable - y](#orgd92e19e)
    6.  [Python Variable - X<sub>train</sub>](#orgd948fdd)
    7.  [Python Variable - y<sub>train</sub>](#org2255ac6)
    8.  [Python Variable - X<sub>test</sub>](#orgbc71bb8)
    9.  [Python Variable - y<sub>test</sub>](#orgc4fbab7)
3.  [How LinearRegression Works](#org6450a73)
4.  [Save Model, using Pickle](#orgc4be762)
5.  [Create](#orged32bab)

Quandl api key - 6UfyTfL7MDo26ypfYzVd
Include pydoc
Include pip freeze output
Include try blocks


<a id="org7dc93c0"></a>

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


<a id="org1e91b26"></a>

# Define Variables


<a id="orgd65b2cb"></a>

## DB table column - HL<sub>PCT</sub>


<a id="orgb67dd10"></a>

## DB table column - PCT<sub>change</sub>

-   This is the percent change of closing price verses the opening opening price

\(PCT\_change = \frac{Closing\_Price - Opening\_Price}{Opening\_Price} \times 100\)


<a id="orgbc0a7ee"></a>

## Python Variable - X


<a id="orge818812"></a>

## Python Variable - X<sub>lately</sub>


<a id="orgd92e19e"></a>

## Python Variable - y


<a id="orgd948fdd"></a>

## Python Variable - X<sub>train</sub>


<a id="org2255ac6"></a>

## Python Variable - y<sub>train</sub>


<a id="orgbc71bb8"></a>

## Python Variable - X<sub>test</sub>


<a id="orgc4fbab7"></a>

## Python Variable - y<sub>test</sub>


<a id="org6450a73"></a>

# How LinearRegression Works


<a id="orgc4be762"></a>

# Save Model, using Pickle


<a id="orged32bab"></a>

# Create

