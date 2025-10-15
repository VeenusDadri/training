import time
timestamp= time.strftime ('%H:%M:%S')
print ( timestamp)
hours=int(time.strftime ('%H'))
mins=int(time.strftime ('%M'))
secs=int(time.strftime ('%S'))
if hours< 12:
    print(" Hi Veenus, Very Very Good morning to you!!")
elif hours==12:
    if mins==00:
        if secs==00:
            print(" Hi Veenus, Very Very Good noon to you!!")   
elif hours>=12 and hours<16:
    print(" Hi Veenus, Very Very Good afternoon to you!!")
elif hours>=16 and hours < 22:
    print(" Hi Veenus, Very Very Good evening to you!!")
else:
    print(" Hi Veenus, 10 is already crosses. So It's time to sleep.Good night!!")

