#!/usr/bin/python

# Script brute force

import hashlib
from timeit import default_timer as timer

xrange = range
start = timer()

with open('shadow', 'r') as f:
   lines = f.readlines()

for line in lines:
    shadow_items = line.split(":")
    for items in shadow_items:
        if items.startswith("$1"):
            md5 = items.replace("$1$", "")
            name = shadow_items[0]

            # caractere = 'abcdefghijklmnopqrstuvwxyz;_@#ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            caractere = "brazil"
            for current in xrange(5,11):
                a = [i for i in caractere]
                for y in xrange(current):
                    a = [x+i for i in caractere for x in a]
                for data in a :
                    hash = hashlib.md5(data.encode()).hexdigest()
                    if str(hash) ==  str(md5):
                        end = timer()
                        with open('password_decrypt_brute.txt', 'a') as d:
                            temps = end-start
                            d.write("User : "+ name + ", mot de passe : "+str(data)+", temps : "+str(temps)+" s \n")
                            print("User : "+ name + ", mot de passe : " +str(data)+", temps : "+str(temps)+" s")
