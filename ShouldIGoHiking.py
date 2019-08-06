"""This is a boolean look at whether I should go hiking or not and whether I will draw in my 
nature journal or keep a photographic record. I won't go if it's below 45F or above 80F.  I
also won't go if I don't have a ride or haven't reserved a rental car in time.  
I like to keep records of hikes. Either I take photos on my phone to print out at a drugstore
or I bring my dedicated nature journal and draw with an archival pen.  I'll rely on my phone
if it is downpouring or windy.  Wind causes too much disturbance and if the rain is too heavy
my phone will be in danger.  However, it's works okay to protect my phone from drizzle with
my sleeve and dry pockets stuffed with knitted gloves."""

#Is it below 45 degrees F?
below_45 = False
#Is it above 80 degrees F?
above_80 = False
#Is it sunny?
sunny = False
#Is it drizzling?
drizzling = True
#Is it downpouring?
downpour = False
#Is it windy?
windy = False
#Do I have a ride?
ride = False
#Have I reserved a rental car in time?
rental = True

yes_go = not(below_45 or above_80) and (ride or rental)
journal = sunny and not (windy or downpour) and yes_go
phone_photos = (sunny or drizzling) and not (downpour or journal) and yes_go
print(yes_go, journal, phone_photos)