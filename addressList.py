import pickle as p

addressfile = "adress.txt"
class person:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        print("__init__ name = %s, address = %s, phone = %s, email = %s" \
         % (self.name, self.address, self.phone, self.email))

name = 'Lilei'
pOne = person(name, 'shenzhen', 12345678911, '111111@163.com')
a = {name:pOne}

for name, person in a.items():
    print("contact %s by %s " %(name, person.phone))

f = open(addressfile, "wb")
p.dump(a, f)
f.close()
