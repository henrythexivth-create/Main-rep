chores = 5
ocount = chores
ccount = 0

while ccount <= chores:
    if ccount == 0:
        bed = input ('have you made your bed?')
        if bed == 'yes':
            ccount += 1
        else:
             print ('go do it')
    elif ccount == 1:
        fed = input ('have you fed the pet?')
        if fed == 'yes':
                ccount += 1
        else:
             print ('go do it')
    elif ccount == 2:
        trash = input ('have you taken out the trash?')
        if trash == 'yes':
             ccount += 1
        else:
            print ('go do it')
    elif ccount == 3:
        dish = input ('have you done the dishes?')
        if dish == 'yes':
                ccount += 1
        else:
             print ('go do it')
    elif ccount == 4:
        hw = input ('have you done your homework?')
        if hw == 'yes':
             ccount += 1
        else:
            print ('go do it')
print ('all chores done')


