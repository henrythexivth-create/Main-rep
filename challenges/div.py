n1 = int(input('numerator'))
n2 = int(input('denominator'))
if n1 % n2 == 0:
    print ('these numbers,', n1,', and ',n2,' are divisible')
else: 
    print ('this is the remainder',n1 % n2)