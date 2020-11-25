name = 'ajAkUba'

print(len(name))
print(name.capitalize())
print(name.upper())
print(name.lower())

print(name[0])
print(name[0:2])
print(name[-3:])
print(name[3:])

channel = "Nauka programowania"
print(channel.split(" "))

join_string = "-"
print(join_string.join(['Nauka' ,'programowania']))

print(name.startswith("j"))#jaka literą sie zaczyna
print(name.startswith("J"))
print(name.endswith("b"))#jaka literą sie konczy
print(name.endswith("B"))

print(name.lstrip("a"))
print(name.split())#usuwa spacje


first_name ="Jakub"
last_name ="Marcinkowski"

print(first_name + " " + last_name)

join_string = " "
print(join_string.join([first_name , last_name]))

james_bond = 7
print(str(james_bond).zfill(3)) #dodajemy zera
