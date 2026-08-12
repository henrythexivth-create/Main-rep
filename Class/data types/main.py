name = input('enter your name:  ')
gadget = input ('enter your ideal gadget:  ')
agnt_num = 8
agnt_speed = 9.5
mission_counts = 14
active = True

print ('_____________________________________________________')
print ('[Name:,', name,'Favored Gadget:',gadget,'             ]')
print ('[Agent Number:' ,agnt_num,'agent speed' ,agnt_speed,'                    ]')
print ('[Mission count:' ,mission_counts,'Active:', active,'                     ]')
print ('------------------------------------------------------')

agnt_num_text= str(8)
agnt_speed_text = str(9.5)
mission_counts_text = str(14)
active_text = str(True)

first_three = name[0:3]
last_letter = name[-1]
codename = first_three + last_letter
print ('your secret codename is ',codename)
reversed_gad = gadget[::-1]
print (reversed_gad)

print ('___________________________________________________')
line1 = 'AGENT' + codename.upper()
line2 = 'ID  ' + agnt_num_text + '  MISSION COUNT  ' + mission_counts_text
line3 = 'SPEED  ' + agnt_speed_text + '  STATUS  ' + active_text
line4 = 'SECRET GADGET CODE  ' + reversed_gad.upper()
print (' SECRET AGENT BADGE ')
print (line1)
print (line2)
print (line3)
print (line4)