# NOTES
## Pandas and Numpy
Pandas is best for handling tabular dataset, can be used in loading data.  
Numpy is best for basic numerical computation(mean, median, mode) also multi dimension arrays can be made in mp

```
import numpy as np
print np.__version__
```
```
1.13.3
```
---
- Create a list of nos from *0* to *9*
```
L = list(range(7,9))
```
```
[7, 8]
```
---
- Converting integers to string 
```
L = str(L)
# this will fail as it would convert whole array as string including ",". :-(
# so use this instead
for i in range(len(L)):
    L[i] = str(L[i])
print L
for i in L:
    print type(i)
```
```
['7', '8']
<type 'str'>
<type 'str'>
```
- Creating arrays  
```
#filling it with 0, so np.zeros, if 1 was to be filled then np.ones
x = np.zeros(10, dtype='int')
print x
```
```
[0 0 0 0 0 0 0 0 0 0]
```
---
```
#filling any array 2D araay
x = np.full((3,5),4.5, dtype=float)
print x
```
```
[[ 4.5  4.5  4.5  4.5  4.5]
 [ 4.5  4.5  4.5  4.5  4.5]
 [ 4.5  4.5  4.5  4.5  4.5]]
```


