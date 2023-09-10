# Unmanned Systems HW2

## Problem 1
Problem 1:
Create a function that calculates the distance from one node to another.
Pass two nodes to the function and return the Euclidean distance. Test your
function by having it calculate the distance from (2,1) to (3,2). Make sure
the answer is correct.
```
d = √(x2 - x1)^2 + (y2 - y1)^2
```

```
import math


def calculate_distance(x1, y1, x2, y2):
    """
    Args:
      x1: X for input location 1 
      x2: Y for input location 1
      y1: X for input location 2
      y2: Y for input location 2

    Returns:
      The Euclidean distance
    """
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)


if __name__ == "__main__":
    print(calculate_distance(x1=2, y1=1, x2=3, y2=2))
```
