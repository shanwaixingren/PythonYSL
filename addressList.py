
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

        diction = {}
        if os.path.exists(person.addressfile):
            with open(person.addressfile, "rb+") as f:
                try:
                    diction = p.load(f)
                    print(diction)
                except Exception as e:
                    print(Exception, e)
        diction[self.name] = self
        print(diction)
        with open(person.addressfile, "rb+") as f:
            p.dump(diction, f)


def delete(name):

    with open(person.addressfile, "rb+") as f:
        dict = p.load(f)
        print(p)
        dict.pop(name)
        p.dump(dict, f)

def show():
    with open(person.addressfile, "rb+") as f:
        try:
            data = p.load(f)
            print(data)
        except Exception as e:
            print(Exception, e)



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
        name = input("Please input name:")
        address = input("Please input address:")
        phone = input("Please input phone:")
        email = input("Please input email:")
        p = person(name, address, phone, email)
        p.dump()
    elif cmd == "delete":
        name = input("Please input name:")
        delete(name)
    elif cmd == "show":
        show()



if __name__ == "__main__":
    print("=== welcome to library ===")
    while(True):
        cmd = input(">> ")
        cmdhandle(cmd)
