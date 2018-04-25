import sqlite3
import json
from pprint import pprint

js = json.load(open("cards.json"))

db = sqlite3.connect("cards.db")
c = db.cursor()

# columns = ["description", "plus_actions", "expansion", "plus_treasure", "cost_treasure", "id", "cost_potions", "is_reaction", "name", "is_attack", "trashes", "treasure","plus_cards","victory_points","plus_buys"]
columns = ["description", "expansion", "cost_treasure", "name"]
c.execute("CREATE TABLE IF NOT EXISTS cards (name, cost_treasure, description, expansion)")

# c.execute("select * from cards")
# for card in c.fetchall():
#     print(card)
for set in js:
    for element in js[set]:
        name = element["name"]
        scrip = element["description"]
        expansion = element["expansion"]
        cost = element["cost_treasure"]
        card = [name, scrip, expansion, cost]
        statement = "INSERT INTO cards (name, description, expansion, cost_treasure) values (?,?,?,?)"
        c.execute(statement, card)
db.commit()


    # pprint(element["name"])
# for element in js["expansion"]:
    # pprint(element["name"])


