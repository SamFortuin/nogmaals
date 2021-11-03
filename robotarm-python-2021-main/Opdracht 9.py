from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for y in range(1,5):
    for x in range(y):
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i2 in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()