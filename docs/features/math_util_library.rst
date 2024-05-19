Math Util Library
=================

.. image:: images/Math.PNG

Get Ratio Float
---------------

**Description:**

This method calculates the ratio of two floating-point numbers. It divides the Numerator by the Denominator and returns the result.

**Input Parameters:**

* Numerator (float): The numerator value.
* Denominator (float): The denominator value.

**Return Value:**

Result (float): The ratio of the numerator to the denominator.

Get InverseRatio Float
----------------------

**Description:**

This method calculates the inverse ratio of two floating-point numbers. It subtracts the Numerator from the Denominator and divides the result by the Denominator. The inverse ratio represents the remaining portion after subtracting the numerator from the denominator, relative to the denominator.

**Input Parameters:**

* Numerator (float): The numerator value.
* Denominator (float): The denominator value.

**Return Value:**

Result (float): The inverse ratio of the numerator to the denominator.

Get Percentage Float
--------------------

**Description:**

This method calculates the percentage of a value relative to a maximum value. It divides the Value by the MaxValue, multiplies the result by 100, and returns the percentage value.

**Input Parameters:**

* Value (float): The value for which the percentage is calculated.
* MaxValue (float): The maximum value against which the percentage is calculated.

**Return Value:**

Result (float): The percentage of the value relative to the maximum value.

Get Percentage Int
------------------

**Description:**

This method calculates the percentage of an integer value relative to a maximum integer value. It multiplies the Value by 100 and divides the result by the MaxValue to get the percentage value.

**Input Parameters:**

* Value (int32): The integer value for which the percentage is calculated.
* MaxValue (int32): The maximum integer value against which the percentage is calculated.

**Return Value:**

Result (int32): The percentage of the value relative to the maximum value.

Swap Int
--------

**Description:**

This method swaps the values of two integer variables. It exchanges the values of A and B by using a temporary variable.

**Input Parameters:**

* A (int32&): Reference to the first integer variable.
* B (int32&): Reference to the second integer variable.

**Return Value:**

This method does not return a value.

Swap Floats
-----------

**Description:**

This method swaps the values of two floating-point variables. It exchanges the values of A and B by using a temporary variable.

**Input Parameters:**

* A (float&): Reference to the first floating-point variable.
* B (float&): Reference to the second floating-point variable.

**Return Value:**

This method does not return a value.

Swap Vectors
------------

**Description:**

This method swaps the values of two FVector variables. It exchanges the values of A and B by using a temporary variable.

**Input Parameters:**

* A (FVector&): Reference to the first FVector variable.
* B (FVector&): Reference to the second FVector variable.

**Return Value:**

This method does not return a value.

Swap Transforms
---------------

**Description:**

This method swaps the values of two FTransform variables. It exchanges the values of A and B by using a temporary variable.

**Input Parameters:**

* A (FTransform&): Reference to the first FTransform variable.
* B (FTransform&): Reference to the second FTransform variable.

**Return Value:**

This method does not return a value.

Swap Rotators
-------------

**Description:**

This method swaps the values of two FRotator variables. It exchanges the values of A and B by using a temporary variable.

**Input Parameters:**

* A (FRotator&): Reference to the first FRotator variable.
* B (FRotator&): Reference to the second FRotator variable.

**Return Value:**

This method does not return a value.

Get Smoothing Ratio
-------------------

**Description:**

This method calculates a smoothing ratio based on the delta time and smoothing time. It uses the FInterpTo_Constant function from UKismetMathLibrary to perform the calculation.

**Input Parameters:**

* DeltaTime (float): The time elapsed since the last update.
* SmoothingTime (float): The desired smoothing time.

**Return Value:**

SmoothingRatio (float): The calculated smoothing ratio.

Raw RInterp
-----------

**Description:**

This method performs a raw interpolation between the Current and Target values using a specified delta time and interpolation speed. It uses the FInterpTo function from UKismetMathLibrary to perform the interpolation.

**Input Parameters:**

* Current (float): The current value.
* Target (float): The target value.
* DeltaTime (float): The time elapsed since the last update.
* InterpSpeed (float): The interpolation speed.

**Return Value:**

InterpolatedValue (float): The interpolated value.

Get Smoothed Vector
-------------------

**Description:**

This method calculates a smoothed vector by interpolating between the Current and Target vectors based on the delta time and smoothing time. It uses the VInterpTo_Constant function from UKismetMathLibrary to perform the interpolation.

**Input Parameters:**

* Current (const FVector&): The current vector.
* Target (const FVector&): The target vector.
* DeltaTime (float): The time elapsed since the last update.
* SmoothingTime (float): The desired smoothing time.

**Return Value:**

SmoothedVector (FVector): The calculated smoothed vector.

Get Smoothed Rotation
---------------------

**Description:**

This method calculates a smoothed rotation by interpolating between the Current and Target rotations based on the delta time and smoothing time. It uses the RInterpTo_Constant function from UKismetMathLibrary to perform the interpolation.

**Input Parameters:**

* Current (const FRotator&): The current rotation.
* Target (const FRotator&): The target rotation.
* DeltaTime (float): The time elapsed since the last update.
* SmoothingTime (float): The desired smoothing time.

**Return Value:**

SmoothedRotation (FRotator): The calculated smoothed rotation.

Ease Out
--------

**Description:**

This method applies an ease-out function to the input value using the specified exponent. It uses the FMath::Pow function to perform the exponentiation.

**Input Parameters:**

* InValue (float): The input value to apply the ease-out function.
* InExp (float): The exponent for the ease-out function.

**Return Value:**

OutValue (float): The result of the ease-out function applied to the input value.

Ease In Out
-----------

**Description:**

This method applies an ease-in-out function to the input value using the specified exponent. It uses the FMath::Pow function to perform the exponentiation.

**Input Parameters:**

* InValue (float): The input value to apply the ease-in-out function.
* InExp (float): The exponent for the ease-in-out function.

**Return Value:**

OutValue (float): The result of the ease-in-out function applied to the input value.

Get Sum
-------

**Description:**

This method calculates the sum of all values in the input array.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

Sum (float): The sum of all values in the input array.

Get Mean
--------

**Description:**

This method calculates the mean (average) value of the input array.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

Mean (float): The mean value of the input array.

Get Median
----------

**Description:**

This method calculates the median value of the input array. It first sorts the array in ascending order and then determines the median based on the number of values.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

Median (float): The median value of the input array.

Get Mode
--------

**Description:**

This method calculates the mode (most frequently occurring value) of the input array. It counts the occurrences of each value using a TMap and determines the value with the highest count.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

Mode (float): The mode value of the input array.

Get Sum Of Squares
------------------

**Description:**

This method calculates the sum of squares of all values in the input array.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

SumOfSquares (float): The sum of squares of all values in the input array.

Get Sum Squared
---------------

**Description:**

This method calculates the square of the sum of all values in the input array.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

SumSquared (float): The square of the sum of all values in the input array.

Get Variance
------------

**Description:**

This method calculates the variance of the input array. It first calculates the mean value, and then sums the squared differences between each value and the mean. The result is divided by the number of values.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

Variance (float): The variance of the input array.

Get Standard Deviation Est
--------------------------

**Description:**

This method calculates the estimated standard deviation of the input array. It first calculates the variance and then takes the square root of the variance.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

StandardDeviation (float): The estimated standard deviation of the input array.

Get Standard Deviation Pop
--------------------------

**Description:**

This method calculates the population standard deviation of the input array. It first calculates the variance and then takes the square root of the variance, adjusted for the population size.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

StandardDeviation (float): The population standard deviation of the input array.

Get Min
-------

**Description:**

This method finds the minimum value in the input array.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

MinValue (float): The minimum value in the input array.

Get Max
-------

**Description:**

This method finds the maximum value in the input array.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

MaxValue (float): The maximum value in the input array.

Get Range
---------

**Description:**

This method calculates the range of the input array, which is the difference between the maximum and minimum values.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

Range (float): The range of the input array.

Get First Quartile
------------------

**Description:**

This method calculates the first quartile (25th percentile) of the input array. It first sorts the array in ascending order and then determines the median of the lower half of the sorted values.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

FirstQuartile (float): The first quartile (25th percentile) of the input array.

Get Third Quartile
------------------

**Description:**

This method calculates the third quartile (75th percentile) of the input array. It first sorts the array in ascending order and then determines the median of the upper half of the sorted values.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

ThirdQuartile (float): The third quartile (75th percentile) of the input array.

Get InterQuartile Range
-----------------------

**Description:**

This method calculates the interquartile range (IQR) of the input array, which is the difference between the third quartile and the first quartile.

**Input Parameters:**

* Values (const TArray<float>&): The array of float values.

**Return Value:**

InterQuartileRange (float): The interquartile range (IQR) of the input array.

Factorial
---------

**Description:**

This method calculates the factorial of an integer number N and returns the result as a string. It uses a loop to iteratively calculate the factorial.

**Input Parameters:**

* N (int32): The integer number to calculate the factorial for.

**Return Value:**

Result (FString): The factorial of the input number N as a string.

Get Skewness
------------

**Description:**

This method calculates the skewness of the input array, which measures the asymmetry of the distribution. It calculates the mean, standard deviation, and uses a formula to compute the skewness.

**Input Parameters:**

* Data (const TArray<float>&): The array of float values.

**Return Value:**

Skewness (float): The skewness of the input array.

Get Kurtosis
------------

**Description:**

This method calculates the kurtosis of the input array, which measures the peakedness or flatness of the distribution. It calculates the mean, standard deviation, and uses a formula to compute the kurtosis.

**Input Parameters:**

* Data (const TArray<float>&): The array of float values.

**Return Value:**

Kurtosis (float): The kurtosis of the input array.

Get Correlation Coefficient
---------------------------

**Description:**

This method calculates the correlation coefficient between two arrays (DataA and DataB), which measures the linear relationship between the two datasets. It calculates the means, variances, and covariance, and uses a formula to compute the correlation coefficient.

**Input Parameters:**

* DataA (const TArray<float>&): The first array of float values.
* DataB (const TArray<float>&): The second array of float values.

**Return Value:**

CorrelationCoefficient (float): The correlation coefficient between DataA and DataB.
