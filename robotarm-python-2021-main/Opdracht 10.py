from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
iList = [10,10]
for i in range(5):
    robotArm.grab()
    for var in range(iList[0]-1-i):
        robotArm.moveRight()
    robotArm.drop()
    for var2 in range(iList[1]-2-i):
        robotArm.moveLeft()
robotArm.wait()