DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        cleaned = set()
        self.search(robot, cleaned, 0, 0, 0)
        
    def search(self, robot, cleaned, i, j, facing):
        # assume position i, j is valid and not cleaned
        robot.clean()
        cleaned.add((i,j))
        
        for i in range(4):
            new_facing = (facing+i) % 4
            i_ = i + DIRECTIONS[new_facing][0]
            j_ = j + DIRECTIONS[new_facing][1]
            if not (i_, j_) in cleaned and robot.move():
                # treat cleaned as a virtual wall
                # for a wall, think the robot hit the wall and come back
                # equals to after search and then goback status
                self.search(robot, cleaned, i_, j_, new_facing)
                self.goback(robot)
            
            robot.turnRight()
            
    def goback(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()             
        robot.turnRight()
        robot.turnRight()
        