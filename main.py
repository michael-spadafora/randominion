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
overall = PanedWindow(orient = HORIZONTAL)
cardDisplay = PanedWindow(orient = HORIZONTAL)
cardDisplay2 = PanedWindow(orient = HORIZONTAL)

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

cb1 = Checkbutton(overall, text ="Promo", variable=promo)
cb2 = Checkbutton(overall, text ="Dominion", variable=dominion)
cb3 = Checkbutton(overall, text ="Dark Ages", variable=dark_ages)
cb4 = Checkbutton(overall, text ="Hinterlands", variable=hinterlands)
cb5 = Checkbutton(overall, text ="Prosperity", variable=prosperity)
cb6 = Checkbutton(overall, text ="Cornucopia", variable=cornucopia)
cb7 = Checkbutton(overall, text ="Intrigue", variable=intrigue)
cb8 = Checkbutton(overall, text ="Seaside", variable=seaside)
cb9 = Checkbutton(overall, text ="Alchemy", variable=alchemy)

i = 0
labels = []
while i < 10:

    i+=1
    url = "http://dominion.diehrstraits.com/scans/common/copper.jpg"
    response = requests.get(url)
    im = Image.open(BytesIO(response.content))
    im = im.resize((120, 200), Image.ANTIALIAS)
    ph = ImageTk.PhotoImage(im)
    label = Label(cardDisplay, image = ph)
    label.image = ph
    labels.append(label)
    # label.pack(side = RIGHT)

checkbuttons = [cb1, cb2, cb3, cb4,cb5,cb6,cb7,cb8,cb9]

for butt in checkbuttons:
    overall.add(butt)
var = StringVar()
var.set("choose items then press generate")

def showImage(name, i):

    name = name.lower()
    name = name.replace(" ", "")
    url = "http://dominion.diehrstraits.com/scans/base/" + name + ".jpg"
    response = requests.get(url)
    im = Image.open(BytesIO(response.content))
    im = im.resize((120, 200), Image.ANTIALIAS)
    ph = ImageTk.PhotoImage(im)

    labels[i].configure(image = ph)
    labels[i].image = ph


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
        if name[0] in cardsInSets:
            continue
        cardsInSets.append(name[0])
        numChosen += 1

    print(cardsInSets)
    i = 0
    for card in cardsInSets:
        showImage(card , i)
        i+=1

# label = Message(m, textvariable=var)
# name = "Smithy"
# url = "http://dominion.diehrstraits.com/scans/base/" + name + ".jpg"
# response = requests.get(url)
# im = Image.open(BytesIO(response.content))
# ph = ImageTk.PhotoImage(im)

enter = Button(overall, text="generate", command=generateItems)
overall.add(enter)
i = 0
for label in labels:
        cardDisplay.add(label)

# overall.add(cardDisplay)
overall.pack(side = TOP)
cardDisplay.pack(side = BOTTOM)
# enter.pack(side = LEFT)
m.mainloop()