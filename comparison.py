bananacost = int (2.99)
applecost = int (3.99)
ricecost = int (10.99)
juicecost = int (6.99)
candycost = int (1.99)
print ('your parents send you to get groceries. what do you get?')
bmount = int (input('how many bananas do you get? :'))
amount = int (input('how many apples do you get? :'))
rmount = int (input('how many cups of rice do you get? :'))
jmount = int (input('how many bottles of juice do you get? :'))
cmount = int (input('how many bags of candy do you get? :'))
total_cost = int (bmount * bananacost + amount * applecost + cmount * ricecost + jmount * juicecost + cmount * candycost)
print ('here is your total. :',total_cost)
told_cost = int (input('how much do you tell your parents you spent? :'))
if told_cost > total_cost:
    print ('isnt that kind of counterintuitive?')
if told_cost < 23.94:
    if total_cost > 30:
        print ('they will definitely yell at you when they find out how much you really spent.')
    else: 
         print ('okay, pretty nice.')
if total_cost == told_cost:
    print ('telling the truth huh?')