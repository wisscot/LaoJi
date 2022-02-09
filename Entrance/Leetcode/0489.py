# 489. Robot Room Cleaner

'''
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.
'''

Basic idea: DFS

use a robot to simulate the DFS process

Note: 
variables in search function are the status requires updating, e.g. position, facing


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
class Solution(object):       
    def cleanRoom(self, robot):
        cleaned = set()
        self.search(robot, cleaned, 0, 0, 0)
        
    # Need two status: current position and facing
    # when track back, we need these two status unchanged
    def search(self, robot, cleaned, posx, posy, facing):
        # assume current position is valid and not cleaned
        robot.clean()
        cleaned.add((posx, posy))
        
        for turn in range(4):
            new_facing = (facing+turn) % 4
            new_posx = posx + DIRECTIONS[new_facing][0]
            new_posy = posy + DIRECTIONS[new_facing][1]
            if (new_posx, new_posy) not in cleaned and robot.move():
                # treat cleaned as a virtual wall
                # for a wall, think the robot hit the wall and come back
                # equals to after search and then goback status
                self.search(robot, cleaned, new_posx, new_posy, new_facing)
                self.goback(robot)
            
            robot.turnRight()
            
    def goback(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()             
        robot.turnRight()
        robot.turnRight()
        