directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
class Solution(object):       
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
    
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        cleaned = set()
        self.backtrack(robot, cleaned, 0, 0, 0)
        
    def backtrack(self, robot, cleaned, i,j, d):
        cell = (i,j)
        cleaned.add(cell)
        robot.clean()
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        for i in range(4):
            new_d = (d + i) % 4
            # new_cell = (cell[0] + directions[new_d][0], \
            #             cell[1] + directions[new_d][1])
            i_ = i + directions[new_d][0]
            j_ = j + directions[new_d][1]
            if not (i_,j_) in cleaned and robot.move():
                self.backtrack(robot, cleaned, i_,j_, new_d)
                self.go_back(robot)
            # turn the robot following chosen direction : clockwise
            robot.turnRight()

    def go_back(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
        
