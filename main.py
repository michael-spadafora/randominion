import sqlite3
from tkinter import *
from random import *
import PIL
from PIL import ImageTk
from PIL import Image
import requests
from io import BytesIO

db = sqlite3.connect("cards.db")
c = db.cursor()

m = Tk()
top = PanedWindow(orient = VERTICAL)

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
    top.add(butt)
var = StringVar();
var.set("choose items then press generate")

def getCheckedButtons():
    checkedarr = []
    i = 0
    while i<len(checked):
        tmp = checked[i]
        if checked[i].get() == 1:
            string = checkbuttons[i].cget("text")
            checkedarr.append(string)
        i+=1
    return checkedarr

def generateItems():
    numChosen = 0
    sets = getCheckedButtons()
    cardsInSets = []
    validIdNumbers = []
    for set in sets:
        # print(set)
        c.execute("select id from cards where expansion = ?", (set,) )
        nums = c.fetchall()
        # print(nums)
        for returnz in nums:
            validIdNumbers.append(returnz[0])

    count = len(validIdNumbers)
    # print(count)
    while (numChosen < 10):
        id = int(random() * int(count))
        num = validIdNumbers[id]
        c.execute("select name from cards where id = ?", (num,) )
        name = c.fetchone()
        cardsInSets.append(name[0])
        numChosen += 1

    print(cardsInSets)


label = Message(m, textvariable = var)
enter = Button(top, text= "generate", command = generateItems)
top.add(enter)
url = "http://dominion.diehrstraits.com/scans/base/cellar.jpg"
response = requests.get(url)
im = Image.open(BytesIO(response.content))
ph = ImageTk.PhotoImage(im)

label = Label(m, image=ph)
label.image=ph

top.pack(side = LEFT)
# enter.pack(side = LEFT)
label.pack(side = RIGHT)
m.mainloop()