from problem2 import Obstacle, is_valid
from problem1 import calculate_distance
from hw1 import Node, compute_index


class Dijkstras:
    """
    Args:
      min_x: Grid Bounds
      min_y: Grid Bounds
      max_x: Grid Bounds
      max_y: Grid Bounds
      gs: Grid Space/Step
    Returns:
      None
    """

    def __init__(self, min_x, min_y, max_x, max_y, gs) -> None:
        self.start = None
        self.goal = None
        self.obs_list = None
        self.visited = {}
        self.unvisited = {}
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.gs = gs

    def run(self, start: tuple, goal: tuple, obs_list: list = [], r_radius=0) -> list:
        """
        Args:
          start(tuple): x,y representing the start location of the robot
          goal(tuple): x,y representing the goal location of the robot
          obs_list: List of obstacles
        Returns:
          List of nodes from start to goal
        """
        self.visited = {}
        self.unvisited = {}
        self.obs_list = obs_list
        self.goal = goal
        self.start = start
        self.r_radius = r_radius
        goal_index = compute_index(
            self.min_x, self.max_x, self.min_y, self.max_y, self.gs, goal[0], goal[1])
        start_index = compute_index(
            self.min_x, self.max_x, self.min_y, self.max_y, self.gs, start[0], start[1])
        cur_node = Node(x=0, y=0, cost=0, parent_index=-1)
        self.unvisited[0] = cur_node
        while (cur_node.x, cur_node.y) != goal:
            cur_node_index = min(
                self.unvisited, key=lambda x: self.unvisited[x].cost)
            cur_node = self.unvisited[cur_node_index]
            self.visited[cur_node_index] = cur_node

            del self.unvisited[cur_node_index]
            # if current node is the goal location the break our of the loop
            if (cur_node.x, cur_node.y) == goal:
                route = []
                while cur_node_index != -1:
                    route.append([self.visited[cur_node_index].x, self.visited[cur_node_index].y])
                    cur_node_index = self.visited[cur_node_index].parent_index
                return route[::-1]

            all_neighbours = self.get_neighbour_moves(
                cur_x=cur_node.x, cur_y=cur_node.y)
            all_neighbours = list(filter(lambda x: is_valid(obs=self.obs_list,
                                                            x_min=self.min_x,
                                                            x_max=self.max_x,
                                                            y_min=self.min_y,
                                                            y_max=self.max_y,
                                                            cur_x=x[0],
                                                            cur_y=x[1],
                                                            r_radius=r_radius
                                                            ), all_neighbours))
            for each_neighbour in all_neighbours:
                idx = compute_index(
                    self.min_x, self.max_x, self.min_y, self.max_y, self.gs, each_neighbour[0], each_neighbour[1])
                if self.visited.get(idx) != None:
                    continue
                new_cost = cur_node.cost + calculate_distance(cur_node.x, cur_node.y, each_neighbour[0], each_neighbour[1])
                if self.unvisited.get(idx) != None:
                    if self.unvisited.get(idx).cost > new_cost:
                        self.unvisited[idx].cost = new_cost
                        self.unvisited[idx].parent_index = cur_node_index
                    continue

                self.unvisited[idx] = Node(x=each_neighbour[0],
                                        y=each_neighbour[1],
                                        cost=new_cost,
                                        parent_index=cur_node_index
                                        )
                

    def get_neighbour_moves(self, cur_x, cur_y):
        import numpy as np
        """
        Args:
          cur_x: Current X position of agent/robot 
          cur_y: Current Y position of agent/robot
        Returns:
          All the possible moves from the current agent/robot position
        """
        neighbours = []
        for each_x in np.arange(-self.gs, self.gs + self.gs, self.gs):
            for each_y in np.arange(-self.gs, self.gs + self.gs, self.gs):
                if (cur_x == (each_x + cur_x) and cur_y == (each_y + cur_y)):
                    continue
                neighbours.append([(each_x + cur_x), (each_y + cur_y)])
        return neighbours

    def plot_route(self, route):
        """
        Args:
          route: Ordered list of nodes from start to end
        Returns:
          None
        """
        print(route)
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        print(self.obs_list) 
        for obs in self.obs_list:
            obs_plot = plt.Circle((obs.x, obs.y), obs.radius, color='black')
            ax.add_patch(obs_plot)
        obs_plot = plt.Circle((self.goal[0], self.goal[1]), self.r_radius, color='green')
        ax.add_patch(obs_plot)
        plt.plot([x[0] for x in route], [x[1] for x in route], c='red')
        plt.show()

if __name__ == "__main__":
    obs_pos = [(1, 1), (4, 4), (3, 4), (5, 0), (5, 1),
               (0, 7), (1, 7), (2, 7), (3, 7)]
    obs_radius = 0.25
    obs_list = [Obstacle(each_ob[0], each_ob[1], obs_radius)
                for each_ob in obs_pos]
    djs = Dijkstras(0, 0, 10, 10, 0.5)
    route = djs.run(start=(0, 0), goal=(8, 9), r_radius=0.25, obs_list=obs_list)
    djs.plot_route(route=route)
