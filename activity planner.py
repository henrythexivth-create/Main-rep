print ('Welcome to the holiday activity planner.')
tt = int (input ('Press 1 to choose a beach holiday and 2 to choose a mountain holiday. '))
if tt == 1:
    bt = input ('You have chosen the beach holiday. would you like to press 1 to swim, or press 2 to build a sandcastle? ')
    if bt == '1':
        print ('You have chosen to swim in the ocean. Have a nice trip!')
    elif bt == '2':
        print ('You have chosen to make sandcastles at the beach. Have a nice trip!')
    else:
        bt == input ('That is not a valid choice. Please choose 1 to swim, or 2 to build a sandcastle. ')
elif tt == 2:
    mt = input ('You have chosen the mountain holiday. Would you like to press 1 to hike, or press 2 to camp out?')
    if mt == '1':
        print ('You have chosen to hike in the mountains. Have a safe trip!')
    elif mt == '2':
        print ('You have chosen to camp out in the mountains. Have a safe trip!')
    else:
        mt == input ('That is not a valid choice. Please choose 1 to hike, or 2 to camp out. ')
else:
    tt == input ('That is not a valid choice. Please choose 1 book a beach trip, or 2 to book a mountain trip. ')