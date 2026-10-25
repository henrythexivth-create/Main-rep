totalhw = 6
ohw = totalhw
print ('You have',ohw,'assignments left to do.')
ccount = 0
tasknum = 1
while tasknum <= totalhw:
    if tasknum == 1:
        nextt = 'art'
    elif tasknum == 2:
        nextt = 'social studies'
    elif tasknum == 3:
        nextt = 'english'
    elif tasknum == 4:
        nextt = 'math '    
    elif tasknum == 5:
        nextt = 'coding'
    else:
        nextt = 'science'
    ans = input(f"Have you finished your {nextt} homework? (yes/no): ")
    if ans == 'yes':
        ccount += 1
        tasknum += 1
        print ('good job')
        print (totalhw - ccount,'left')    
    elif ans == 'no':
        print ('do it')
    else:
        print ('what?')
    
print ('All homeworks done')