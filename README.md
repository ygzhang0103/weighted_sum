# weighted_sum
Description
================
This is an efficient method to get the lower and upper bounds of weighted sum of a series of data.
It is often very useful to apply a weighted sum over a series of data, in order to create a single scalar feature. Here, we define the weight to be wi=c^i. So that the weighted sum S of a series x can be presented as 
![](formula1.png) 
Now we want to expand the weighted sum to all possible rotations of x. For example, a series x = [a,b,c,d]. We also consider [b,c,d,a],[c,d,a,b] and [d,a,b,c] in addition to x itself. And we will generate the lower and upper bounds of S for all rotations of a series x.
Install
================
