import sqlite3
from pprint import pprint
from tkinter import *
from random import *


db = sqlite3.connect("cards.db")
c = db.cursor()

top = Tk()

promo = IntVar()
dominion       = IntVar()
dark_ages      = IntVar()
prosperity     = IntVar()
hinterlands    = IntVar()
cornucopia     = IntVar()
intrigue       = IntVar()
seaside        = IntVar()
alchemy        = IntVar()
checked = [promo, dominion, dark_ages, hinterlands, prosperity, cornucopia, intrigue, seaside, alchemy]

cb1 = Checkbutton(top,text = "Promo", variable=promo)
cb2 = Checkbutton(top,text = "Dominion", variable=dominion)
cb3 = Checkbutton(top,text = "Dark Ages", variable=dark_ages)
cb4 = Checkbutton(top,text = "Hinterlands", variable=hinterlands)
cb5 = Checkbutton(top,text = "Prosperity", variable=prosperity)
cb6 = Checkbutton(top,text = "Cornucopia", variable=cornucopia)
cb7 = Checkbutton(top,text = "Intrigue", variable=intrigue)
cb8 = Checkbutton(top,text = "Seaside", variable=seaside)
cb9 = Checkbutton(top,text = "Alchemy", variable=alchemy)

checkbuttons = [cb1, cb2, cb3, cb4,cb5,cb6,cb7,cb8,cb9]

for butt in checkbuttons:
    butt.pack()
var = StringVar();
var.set("choose items then press generate")
def generateItems():
    numChosen = 0
    while (numChosen < 10):
        c.execute("select count(*) from cards")
        counts = c.fetchone()
        count = counts[0]
        # print( count[0])
        id = int(random() * int(count) + 1)
        # print(id)/
        c.execute("select * from cards where id = ?", (id,) )
        rows = c.fetchall()
        print(rows)
        numChosen+=1




label = Message(top, textvariable = var)
enter = Button(top, text = "generate", command = generateItems)

enter.pack()
label.pack()
top.mainloop()