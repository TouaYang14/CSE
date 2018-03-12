class Character(object):
    def __init__(self, name, inventory, abilities, stats, health, description, dialogue, attack):
        self.name = name
        self.inventory = inventory
        self.abilities = abilities
        self.stats = stats
        self.health = health
        self.description = description
        self.dialogue = dialogue
        self.attack = attack

    def move(self):



snapper = Character('snapper', 'wooden_stick', 'water_spiral', 'ATK = 97, DEF = 53', 'HP = 500', "Snapper\n"
                    " is a turtle that knows martial art and is seeking to find a way to get stronger.", "Snapper\n"
                    " was born in a small village and seeks a fighting spirit. Ever since he was a small kid he\n"
                    " has been trying to get stronger. He is seeking to master the water style", 'ATK = 97')