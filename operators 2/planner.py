print ('smart school day planner')
print ('Answer 3 quick questions and ill plan your day!')
day = input ('what day is it? [monday-sunday]: ').strip ().capitalize()
weather = input ('what is the weather? [sunny/rainy/cloudy]').strip ().lower()
homework = input ('Is your homework done/do you have any? [yes/no]').strip ().lower()

print ('\nyour plan for',day)
print ('-'*35)

if day in ('Saturday', 'Sunday'):
    print ('day type: its the weekend.')

elif day == 'Monday':
    print ('day type: first day of the week')

elif day == 'Friday':
    print ('day type: Last day of the week!')

elif day in ['Tuesday', 'Wednesday', 'Thursday']:
    print ('day type: normal school day. hang in there')

else:
    print ('thats not a day')

if weather == 'sunny' and homework == 'yes':
    print ('after school head to the park')
