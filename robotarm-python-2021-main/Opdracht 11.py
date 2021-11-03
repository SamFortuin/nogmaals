from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

robotArm.speed = 2
#move right first to prevent double move, then work from right to left
for i in range(9):
    robotArm.moveRight()
for i in range(10):
    robotArm.grab()
    scanResult = robotArm.scan()
    if scanResult != 'white': #checks if block is white or not
        robotArm.drop()
    else:
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    robotArm.moveLeft() 
    
robotArm.wait()