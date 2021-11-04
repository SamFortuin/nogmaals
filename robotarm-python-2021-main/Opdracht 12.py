from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2
x = 0
for i in range(9):
    robotArm.grab()
    scanResult = robotArm.scan()
    if scanResult != 'red': #checks if block is red or not
        robotArm.drop()
    else:
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(9-x):
            robotArm.moveLeft()
    robotArm.moveRight()
    x+=1 
    
robotArm.wait()
