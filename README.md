# proj3_phase1

To start, simply run the program and enter the starting and finishing coordinates. Note that the coordinates for x must be greater than 5 and below 395, and the coordinates for y must be greater than 5 and below 295. This is required to meet the robot clearance of 5 around the walls. The program will run through each parent node, store the child nodes, and then choose the next parent node based on whichever child node has the lowest cost. While running, the program will print out the current coordinates of the robot, it's cost, and the current path being taken. Once the goal coordinates are reached, the program will output an image showing the path the robot took the goal in a black line. Thes nodes explored by the robot using Djikstra are shaded in gray.
