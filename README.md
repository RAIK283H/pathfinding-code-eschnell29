# Pathfinding Starter Code

Within pathing.py there are two functions, get_test_path() and get_random_path() that generate paths to the exit depending on different requirements. 

The get_random_path() creates a randomly generate path that will start at the starting node and will finish at the exit node, but sometime during its path it will hit the target node before hitting the exit node. The random algorithm allows the player to wander from node to node during its journey to the exit. It also allows the player to be able to return to the start node on its journey to the exit node. They can also hit the exit node before the target but the player will simply bounce off of the exit and head towards the target node. The get_random_path() does this by first letting the player wander until it hits the target node and then it lets the player wander again until they hit the exit node. 

In scoreboard.py the statistic of how many nodes the player passed through during their path was added. For the test player, it will be the same as the length of test_path and only counts each node once. for the random player, it will count every single time the player passes through any node, including duplicates.
