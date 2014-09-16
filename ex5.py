name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# conversions
metric_height = height * 2.54 # centimeters
metric_weight = weight * 0.45 # kg

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d centimeters tall." % metric_height
print "He's %d pounds heavy." % weight
print "He has a mass of %d kilograms." % metric_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)