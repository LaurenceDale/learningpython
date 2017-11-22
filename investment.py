#!/usr/bin/python

import time

print "Welcome to Plannr Investment Advice v0.1!"
time.sleep(3)
print "Please input your name \n"
name = raw_input('')
print "Hello " + name + "!"
time.sleep(2)
print "Let's get started.\n Firstly, are you investing for income or capital growth?\n"
time.sleep(1)
print "Input '1' for income or '2' for capital growth\n"
time.sleep(1)
objective = raw_input("Enter '1' or '2'\n")
if objective == "1":
        print "That's great, " + name + ". " + "Let's look at investment for income\n"
        time.sleep(1)
        print "Firstly, let's start by getting to know your circumstances a little better. This will help me give you the best advice possible."
        time.sleep(1)
        print "How much capital do you have to invest?"

else:
        print "Ok, let's take a look at Capital Growth options."
