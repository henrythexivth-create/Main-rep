print ('welcome to the ride builder')
print ('')
vtype = int(input ('What type of vehicle do you want? 1 = bike, 2 = car'))
if vtype == 1:
    btype = int(input('step 2, pick your bike type. 1 = scooter, 2 = offroad'))
    if btype == 1:
        mess = ('scooter bike, top speed 80mph, best for city roads')
    else:
        mess = ('mountain bike, top speed, 40mph, best for offroading')
elif vtype == 2:
    ctype = int(input('Step 2, pick your car type. 1 = sedan, 2 = SUV'))
    if ctype == 1:
            mess = ('Sedan, seats 5, best for family trips')
    else:
            mess = ('SUV, seats 7, 40mph, best for offroad adventures')
else:
     print ('We dont have that kind of vehicle here.')

print (' your custommade ride is ready!  ')
print (mess)