#!/usr/bin/python

# Script par dictionnaire

import hashlib
from timeit import default_timer as timer

with open('shadow', 'r') as f:
   lines = f.readlines()

for line in lines:
    shadow_items = line.split(":")
    for items in shadow_items:
        if items.startswith("$1"):
            md5 = items.replace("$1$", "")
            name = shadow_items[0]

            with open('dico_mini_fr', 'r') as f:
               lines = f.readlines()

            for line in lines:
                start = timer()
                hash = line.strip()
                dico_hash = hashlib.md5(hash.encode()).hexdigest()

                if str(dico_hash) == str(md5):
                    end = timer()
                    with open('password_decrypt_dico.txt', 'a') as d:
                        temps = end-start
                        d.write("User : " + name + ", mot de passe : "+str(line.strip())+", temps : "+str(temps)+" s \n")
                        print("User : " + name + ", mot de passe : "+str(line.strip())+", temps : "+str(temps)+" s")
