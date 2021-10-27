i = 1
while True:
    question = input('How are you doing?\n')
    print('times asked',i,'\n')
    if question != 'quit':
        i+=1
    else:
        exit()