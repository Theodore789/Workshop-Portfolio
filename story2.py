print("Answer the following questions:")

colour = input("Enter a colour e.g. blue, green:\n>")
colour = colour.lower()

description = input("Enter a description e.g. tall, handsome:\n>")
description = description.lower()

bodypart = input("Enter a body part e.g. hand, leg:\n>")
bodypart = bodypart.lower()

animal = input("Enter a animal e.g. lion, tiger:\n>")
animal = animal.lower()

name = input("Enter a name e.g. Jeff, Anna:\n>")
name = name.title()

thing = input("Enter an object e.g. rock, stick:\n>")
thing = thing.lower()

action = input("Enter a action e.g. running, eating:\n>")
action = action.upper()

print() 

print(f"""Long, long ago...
{name} the {description} {animal} was minding its own business,
when a {colour} {thing} suddenly appeared in front of their {bodypart}. "{action}! I thought it was enough for me to escape!" """)