print("Answer the following questions, using lower case.")

colour = input("Enter a colour e.g. red, blue:\n>")

description = input("Enter a description e.g. big, invisible:\n>")

bodypart = input("Enter a body part e.g. toe, head:\n>")

animal = input("Enter a animal e.g. bear, mouse:\n>")

name = input("Enter a name e.g. alice, bob:\n>")

name = name.title() # Instruction for variable "name" to become titled

thing = input("Enter an object e.g. tin of beans, hairdrier:\n>")

action = input("Enter a action e.g. running, eating:\n>")

print()

print(f"""Once upon a time...
{name} the {description} {animal} was {action},
when a {colour} {thing} whizzed past his {bodypart}.""")