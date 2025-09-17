import unroll as ur
# Sample python code for github
#print("Hello!, Good Morning!")

person=ur.Person()

person2 = ur.Person("Clayton Lin")
person3 = ur.Person("Erika Rosero")

person.addFriend(person2)
person.addFriend(person3)
print(person.friends)