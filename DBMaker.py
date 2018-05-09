import sqlite3
import json
from pprint import pprint

js = json.load(open("cards.json"))

db = sqlite3.connect("cards.db")
c = db.cursor()

# columns = ["description", "plus_actions", "expansion", "plus_treasure", "cost_treasure", "id", "cost_potions", "is_reaction", "name", "is_attack", "trashes", "treasure","plus_cards","victory_points","plus_buys"]
columns = ["id" , "description", "expansion", "cost_treasure", "name"]
c.execute("CREATE TABLE IF NOT EXISTS cards (id, name, cost_treasure, description, expansion)")

# c.execute("select  from cards")
# for card in c.fetchall():
#     print(card)
i = 0

#
# c.execute("select id, name from cards")
# ids = c.fetchall()
#
# for id in ids:
#     print(id)

# for set in js:
#
#     # print('cb' + str(i) + ' = Checkbutton(top,text = "' + set +  '", variable=' + set.lower() + ')')
#     for element in js[set]:
#         i = i + 1
#         name = element["name"]
#         scrip = element["description"]
#         expansion = element["expansion"]
#         cost = element["cost_treasure"]
#         card = [i, name, scrip, expansion, cost]
#         statement = "INSERT INTO cards (id, name, description, expansion, cost_treasure) values (?,?,?,?,?)"
#         c.execute(statement, card)
# db.commit()


    # pprint(element["name"])
# for element in js["expansion"]:
    # pprint(element["name"])


