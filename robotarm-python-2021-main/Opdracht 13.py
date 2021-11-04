from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
#robotArm.speed = 3

i = 1
scan = 'a'
# Jouw python instructies zet je vanaf hier
while scan != '':
    robotArm.grab()
    scan = robotArm.scan()
    if scan != '':
        for x in range(i):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(9):
            robotArm.moveLeft()
    i += 1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()