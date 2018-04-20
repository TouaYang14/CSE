class Character(object):
    def __init__(self, name, inventory, abilities, stats, health, description, dialogue, attack, money, item):
        self.name = name
        self.inventory = inventory
        self.abilities = abilities
        self.stats = stats
        self.health = health
        self.description = description
        self.dialogue = dialogue
        self.attack = attack
        self.money = money
        self.item = item

    def heal(self):
        if self.health <= 5:
            self.health += 25

    def attack(self):
        if self.attack >= JohnnyNPC.health:
            print("Johnny has died")
        else:
            JohnnyNPC.health = self.attack - JohnnyNPC.health

    def sell(self):
        item = input("What do you want to sell? ")
        if item in Snapper:
            print("You have sold the %s" % item)
            Snapper.inventory.pop(item)

    def block(self):
        if self.block >= JohnnyNPC.block:
            print("You blocked the enemy's attack")




Snapper = Character("Snapper", 'wooden_stick', 'water_spiral', 'DEF = 53', 500, "Snapper\n"
                    " is a turtle that knows martial art and is seeking to find a way to get stronger.", "Snapper\n"
                    " was born in a small village and seeks a fighting spirit. Ever since he was a small kid he\n"
                    " has been trying to get stronger. He is seeking to master the water style", 37)

JohnnyNPC = Character('Johnny', 'Wooden_Sword', 'Basic_Attack', 'ATK = 21, DEF = 17', 200, None, None, 21)

