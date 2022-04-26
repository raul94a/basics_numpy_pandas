import numpy as np
a = np.array([1,2,3])
print(a)
print(a + 1)

b = np.arange(3)
br = b.reshape(3,1)
print(b,br,b.shape)
print(br + a)
print(np.ones((3,3)) + 10)

# Rules of Broadcasting
# Broadcasting in NumPy follows a strict set of rules to determine the interaction
# between the two arrays:
        # • Rule 1: If the two arrays differ in their number of dimensions, the shape of the
        # one with fewer dimensions is padded with ones on its leading (left) side.
        # • Rule 2: If the shape of the two arrays does not match in any dimension, the array
        # with shape equal to 1 in that dimension is stretched to match the other shape.
        # • Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is
        # raised.
        
# Broadcasting example 1
# Let’s look at adding a two-dimensional array to a one-dimensional array:
# In[8]: M = np.ones((2, 3))
# a = np.arange(3)
# Let’s consider an operation on these two arrays. The shapes of the arrays are:
    # M.shape = (2, 3)
    # a.shape = (3,)
# We see by rule 1 that the array a has fewer dimensions, so we pad it on the left with
# ones:
    # M.shape -> (2, 3)
    # a.shape -> (1, 3)
# By rule 2, we now see that the first dimension disagrees, so we stretch this dimension
# to match:
    # M.shape -> (2, 3)
    # a.shape -> (2, 3)
# The shapes match, and we see that the final shape will be (2, 3):
# In[9]: M + a
# Out[9]: array([[ 1., 2., 3.],
# [ 1., 2., 3.]])

# Broadcasting example 2
# Let’s take a look at an example where both arrays need to be broadcast:
    # In[10]: a = np.arange(3).reshape((3, 1))
    # b = np.arange(3)
# Again, we’ll start by writing out the shape of the arrays:
    # a.shape = (3, 1)
    # b.shape = (3,)
# Rule 1 says we must pad the shape of b with ones:
    # a.shape -> (3, 1)
    # b.shape -> (1, 3)
# And rule 2 tells us that we upgrade each of these ones to match the corresponding
# size of the other array:
    # a.shape -> (3, 3)
    # b.shape -> (3, 3)
# Because the result matches, these shapes are compatible. We can see this here:
# In[11]: a + b
# Out[11]: array([[0, 1, 2],
# [1, 2, 3],
# [2, 3, 4]])


