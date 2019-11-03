# weighted_sum
Description
--------------
This is an efficient method to get the lower and upper bounds of weighted sum of a series of data.
It is often very useful to apply a weighted sum over a series of data, in order to create a single scalar feature. Here, we define the weight to be wi=c^i. So that the weighted sum S of a series x can be presented as 

![](formula1.png) 

Now we want to expand the weighted sum to all possible rotations of x. For example, a series x = [a,b,c,d]. We also consider [b,c,d,a],[c,d,a,b] and [d,a,b,c] in addition to x itself. And we will generate the lower and upper bounds of S for all rotations of a series x.

Installation
---------------
Install weighted_sum package:
```
import weighted_sum
```
How it works
----------------
You need x and c as the input. Here, x is a list of integers and c is a float that satisfies 0.2 < c < 0.8.
The return will be a tuple with its first element being the lower bound and the second the upper bound.

Running the tests
----------------
We can use an example as a test:
```
from weighted_sum import sumbd.py

print(sumbd.bounds_of_rotations([2, 5, 6, 8], 0.8))
```
Return will be (13.936, 16.24). 13.936 as the lower bound and 16.24 as the upper bound.

Authors
------------------
Yuge Zhang


 
