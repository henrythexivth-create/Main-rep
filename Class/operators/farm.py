field1 = 38
field2 = 99
field3 = 36
field4 = 82
field5 = 59
total = field1 + field2 + field3 + field4 + field5 
ave = total // 5 
print ('total kg across all fields is',total,'and the average is',ave)
earnings = total * 15
print ('the farmer got $',earnings)
bags = total // 25
left = total % 25
print ('they were able to make',bags,'bags and ',left,'kg was leftover')
last = 500
diff = last - total
print ('better than last year?',total > last)
print ('same as last year?',total == last)
print ('atleast as good?',total >= last)
print ('worse than last year?', total < last)

total += 30 
print ('after the bonus crops,',total,'kgs')
total -= 15 
('after seed reserve,', total,'kgs')

bags = total // 25
print ('total bags packed,',bags)