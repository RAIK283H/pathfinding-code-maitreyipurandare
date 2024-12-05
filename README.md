# Pathfinding Starter Code
The random path algorithm works as follows:
The start node is set to 0 and the path is initialized to only include the start node. 
The current node is then set to the start node.
First the path is set to reach the target. It selects randomly one of the nodes from the
adjacency list of the current node and keeps changing current nodes until it hits the target.
After that, it does the same thing until the path reaches the exit node.

The feature that was added to the scoreboard is counting the number of moves made.
The way it tracks this for player 2 is by counting every iteration of the loops (for finding the target node and for finding the exit node). Each count is one move. For the test path player, it counts the number of nodes in the test path needed to reach the end. Usually we can see that the test path is much shorter than the path of player 2. 

HOMEWORK 7 EXTRA CREDIT:
I replaced the Dijkstra player with the Floyd Warshall Player in config_data - player data and in pathing.py, in set_current_graph_paths() i appended the FW function.