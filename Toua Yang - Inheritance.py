class Item(object):
    def __init__(self, description, name):
        self.equip = False
        self.unequip = True
        self.description = description
        self.name = name

    def use(self):
        print("You used the item")
        
        
class Weapons(Item):
    def __init__(self, attack, block, name, description):
        super(Weapons, self).__init__(attack, block)
        
        
class WoodenSword(Weapons):
    def __init__(self):
        super(WoodenSword, self).__init__(57, 0, 'wooden_sword', 'a wooden sword')


class Shield(Weapons):
    def __init__(self):
        super(Shield, self).__init__(0, 50, 'wooden_shield', 'An old rusty shield')


class BattleAxe(Weapons):
    def __init__(self):
        super(BattleAxe, self).__init__(90, 30, 'Battle_Axe', 'A Battle Axe')
        

class Wings(Item):
    def __init__(self):
        super(Wings, self).__init__('Wings, that can make you fly', 'Wings')


class Clock(Item):
    def __init__(self):
        super(Clock, self).__init__('A clock that can tell you what time it is', 'Clock')


class Compass(Item):
    def __init__(self):
        super(Compass, self).__init__(' A compass that tells you where North, East, West, and South is', 'Compass')


class Equipment(Item):
    def __init__(self, name, description, value):
        super(Equipment, self).__init__('Something that you wear', 'Equipment')
        self.equip = False
        self.unequip = True
        self.name = name
        self.description = description
        self.value = value


class DarkArmor(Equipment):
    def __init__(self):
        super(DarkArmor, self).__init__('Dark Armor for the chest', 'Dark Chestplate, where\n'
                                         ' only those who have enough potential can use it', 950000000)


class DarkLeggings(Equipment):
    def __init__(self):
        super(DarkLeggings, self).__init__('Dark Armor for leggings' 'Dark Leggings', 'A dark\n'
                                            ' armor for the legs', 950000000)

class DarkHelment(Equipment):
    def __init__(self):
        super(DarkHelment, self).__init__('Dark Helment', 'A Dark helment only for those who are are strong enough',
                                           950000000)

class DarkGauntlets(Equipment):
    def __init__(self):
        super(DarkGauntlets, self).__init__('Dark Gauntlets', 'A Gauntlets to which you need to complete the dark set',
                                             950000000)

class DarkSword(Weapons):
    def __init__(self):
        super(DarkSword, self).__init__(350, 0, 'Dark Sword', 'THE DARK SWORD!!!')

class DarkShield(Weapons):
    def __init__(self):
        super(DarkShield, self).__init__(100, 600, 'Dark Shield', 'THE DARK SHIELD!')
