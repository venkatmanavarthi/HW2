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

## Problem 2
Problem 2:
Create a function that checks if the current node is valid based upon the list
of obstacles, grid boundaries, and current location.

Using an obstacle list of (1,1), (4,4), (3,4), (5,0), (5,1), (0,7), (1,7), (2,7), and
(3,7); and a bounding box of 0 to 10 for both x and y, and step size of 0.5,
verify that the location (2,2) is valid. Assume the obstacles have a diameter
of 0.5 (only occupy the node at which they reside).

Pass the obstacle list, node, and map boundaries/step size, and return a
Boolean True/False depending on if the node location is valid (reachable).

```
from problem1 import calculate_distance
import matplotlib.pyplot as plt

class Obstacle:
    def __init__(self, x, y, radius=0) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    def is_inside(self, cur_x, cur_y, r_radius=0) -> bool:
        """
        Args:
          ob_x: X position of the obstacle
          ob_y: Y position of the obstacle
          cur_x: X position of the robot
          cur_y: Y potition of the robot
          r_radius: Robot radius

        Returns:
          True if point is inside the obstacle
          False if point is outside the obstacle
        """
        dis = calculate_distance(cur_x, cur_y, self.x, self.y)
        if dis > (self.radius + r_radius):
            return False
        return True


def is_valid(obs, x_min, y_min, x_max, y_max, cur_x, cur_y, r_radius=0) -> bool:
    for each_obs in obs:
        if each_obs.is_inside(cur_x, cur_y, r_radius):
            return False
        
    if x_min > cur_x:
        return False
    if x_max < cur_x:
        return False
    if y_min > cur_y:
        return False
    if y_max < cur_y:
        return False
    
    return True


if __name__ == "__main__":
    obs_pos = [(1, 1), (4, 4), (3, 4), (5, 0), (5, 1),
               (0, 7), (1, 7), (2, 7), (3, 7)]
    obs_radius = 0.25
    r_radius = 0.25
    
    cur_x, cur_y = 2, 2
    
    obs_list = [Obstacle(each_ob[0], each_ob[1], obs_radius)
                for each_ob in obs_pos]
    x_min, y_min, x_max, y_max = 0, 0, 10, 10
    if is_valid(obs_list, x_min, y_min, x_max, y_max, cur_x, cur_y, r_radius):
        print("Valid Location")
    else:
        print("Invalid Location")
    
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)    
    for obs in obs_list:
        obs_plot = plt.Circle((obs.x, obs.y), obs.radius, color='blue')
        ax.add_patch(obs_plot)
    
    agent_plot = plt.Circle((cur_x, cur_y), r_radius, color='red')
    ax.add_patch(agent_plot)
    plt.show()  
```
![Problem 2 Output](./images/problem2.png)
