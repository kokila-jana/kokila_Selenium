# #import modulename
# import modules
# modules.demo()
# modules.add(12,69)
# print(modules.isVowel())

#import modulename as a
# import modules as m
# m.add(12,68)
# m.demo()
# print(m.isVowel())

#from modulename import particularfunctionname
# from modules import add,demo,isVowel
# add(45,36)
# demo()
# print(isVowel())

#from modulename import functionname as a
# from modules import add as a,demo as d,isVowel as v
# print(v())
# a(45,96)
# d()

#from modulename import *
# from modules import *
# add(12,63)
# demo()
# print(isVowel())

# import math as m
# print(m.pi)
# print(m.sqrt(16))
# print(m.cbrt(27))
# print(m.ceil(2.3))
# print(m.floor(2.3))
# print(m.factorial(5))
# print(m.pow(5,3))
# print(m.remainder(5,6))
# a=10
# b=5
# print(b-a)
# print(m.fabs(b-a))

# from scipy import constants as c
# print(c.pi)
# print(c.day)
# print(c.week)
# print(c.year)
# print(c.milli)

# import time as t
# print(t.ctime())
# # t.sleep(5)
# print("hello")
# print(t.strftime("%H:%M:%S"))

# import calendar as c
# print(c.calendar(2027))
# print(c.isleap(2024))
# print(c.month(2026,7))
# print(c.weekheader(5))

# import datetime as d
# print(d.datetime.now())

# import numpy as n
# a=n.array([2,4,8,9,5,3,])#31/6
# print(n.sqrt(a))
# print(n.min(a))
# print(n.max(a))
# print(n.mean(a))#average
# print(n.median(a))#2  3  4  5   8  9

# import pywhatkit as p
# import pyautogui as pa
# p.search("Dhoni")
# p.sendwhatmsg_instantly("+91 6379885613","Hii I am kokila" )
# pa.press("enter")

# import webbrowser as w
# w.open("https://www.youtube.com/watch?v=coO5wkBJy0o&list=RDcoO5wkBJy0o&start_radio=1")

# import socket as s
# host=s.gethostname()
# print(host)

# import sys
# print(sys.path)
# print(sys.version)
# print(sys.version_info)
# sys.stdout.write("hello python")
# sys.stderr.write("Java")

# import random as r
# print(r.random())
# print(r.randint(1000,9999))
# print(r.randrange(1000,10000,10))

# import pygame as p
# import time as t
# p.init()
# p.mixer.init()
# p.mixer.music.load("C:\\Users\\manojana\\Music\\Natpu.mp3")
# p.mixer.music.set_volume(30)
# p.mixer.music.play()
# t.sleep(20)

import numpy as n
import  matplotlib.pyplot as m
a=n.array([1,2,3,4,5])
b=n.array([6,7,12,3,10])
# m.plot(a,b)
# m.xlabel("Days")
# m.ylabel("sales")
# m.bar(a,b)
m.pie(a)
m.show()



