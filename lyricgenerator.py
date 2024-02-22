#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:53:49 2023

@author: annaclaireraymer
"""

import random 
valid = "Q"
meganlist = ["that shit's super sad.", "fuck it carpe diem", "you can keep hating, I'm popping regardless", "I'm a hot girl don't try it at home", "hands on my knees shaking ass on my thot shit", "yeah I'm in my bag, but i'm in his too...ah", "he know it's very expensive to date me", "my money thick thick ay"]
taylorlist = ["It's 2AM", " I’m fine with my spite and my tears, and my beers and my candles", "Your faithless love's the only hoax I believe in", "Slut!", "Breakups happen every day, you don't have to lose it", "That's a lie"]
myinput = input("Welcome to poet chatbot, who would you like to speak with today?\nA. Megan Thee Stallion\nB. Taylor Swift\nC. Shakespeare\n")
if myinput == "A":
    print("Gladly. Paging Megan Thee Stallion.\n")
    print(random.choice(meganlist))
    userinput = input("Enter a response here (Type Q to quit): ")
    while userinput != valid: 
        print('\n')
        print(random.choice(meganlist))
        print('\n')
        userinput = input("Enter a response here (Type Q to quit): ")
if myinput == "B": 
    print('My pleasure. Calling Taylor Swift to the front desk.\n')
    print(random.choice(taylorlist))
    