temp = float (input ("enter today's temp in celsius:"))

if temp < 20:
    outfit = "jacket"
    print ("it is cold today") 
    print ('wear a', outfit,)
else:
    outfit = 'shirt'
    print ('it is warm today')
    print ('wear a', outfit,)

rain = input ("is it raining or not today? (yes/no)")

if rain == "yes":
    print ('bring an umbrella')
    rain = ''
else:
    print ('dont bring an umbrella')
    rain = 'dont'

pudd = input ('are there puddles on the ground? (yes/no)') 

if pudd == 'yes':
    shoes = 'boots'
    print ('the ground is wet, wear some', shoes)
else:
    shoes = 'sneakers'
    print ('the ground is wet, wear some', shoes)

print ('wear a',outfit,'wear some',shoes,'and',rain,'bring an umbrella')