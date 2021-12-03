#dict to loop through and to set while loop target
weekDict = {'ma':1,'di':2,'wo':3,'do':4,'vr':5,'za':6,'zo':7}
#set default value of i
i = 0
#input shorted to the first 2 characters
target = input('Welke dag van de week\n')[:2]
while i < weekDict[target]:
    print(list(weekDict.keys())[i])
    i+=1