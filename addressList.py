
# -*- coding: utf-8 -*-
import pickle as p
import sys
import os

class person:
    addressfile = "address.txt"
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        print("__init__ name = %s, address = %s, phone = %s, email = %s" \
         % (self.name, self.address, self.phone, self.email))


    def dump(self):
        '''注意参数的调用

        直接使用self
        '''
        f = open(person.addressfile, "wbr")
        diction = {}
        # if os.path.exists(person.addressfile):
        try:
            diction = p.load(f)
            print(diction)
        except:
            pass
        diction[self.name] = self
        print(diction)
        p.dump(diction, f)
        f.close()


def delete(name):

    with open(person.addressfile, "rwb") as f:
        dict = p.load(f)
        print(p)
        dict.pop(name)
        p.dump(dict, f)

def show():
    with open(person.addressfile, "rb") as f:
        data = p.load(f)
        print(data)


def main():
    name = 'Lilei'
    pOne = person(name, 'shenzhen', 12345678911, '111111@163.com')
    a = {name:pOne}

    for name, person in a.items():
        print("contact %s by %s " %(name, person.phone))



def cmdhandle(cmd):
    # pass
    if (cmd == "bye"):
        print("=== Bye ===")
        sys.exit()
    elif cmd == "add":
        name = raw_input("Please input name:")
        address = raw_input("Please input address:")
        phone = input("Please input phone:")
        email = raw_input("Please input email:")
        p = person(name, address, phone, email)
        p.dump()
    elif cmd == "delete":
        name = raw_input("Please input name:")
        delete(name)
    elif cmd == "show":
        show()



if __name__ == "__main__":
    print("=== welcome to library ===")
    while(True):
        cmd = raw_input(">> ")
        cmdhandle(cmd)
