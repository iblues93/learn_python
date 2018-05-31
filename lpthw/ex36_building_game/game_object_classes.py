from random import randrange

class Player:
  def __init__(self):
    self.health = randrange(8,12)
    self.stamina = 10
    self.attack = randrange(1,3)
    self.defence = randrange(0,3)
    self.inventory = {
      "weapon" : None,
      "armor"  : None,
      "food"   : []
    }

  def check_inventory(self):
    for item in self.inventory:
      if self.inventory[item] != None:
        self.inventory[item].print_info()
      else:
        print("    No {}".format(item))

  def print_info(self):
    print("""
    HP : {}
    Stamina : {}
    Atk : {}
    Def : {}
    Inventory : {}
    """.format(self.health,self.stamina,self.attack,self.defence,self.inventory))

  def get_weapon(self,weapon):
    self.inventory['weapon'] = weapon

class Weapon:
  def __init__(self,name,attack,durability):
    self.name = name
    self.attack = attack
    self.durability = durability
  def print_info(self):
    print("""
    Weapon name : {}
    Atk : {}
    Durability : {}
    """.format(self.name,self.attack,self.durability))

my_player = Player()

my_player.print_info()

weapon = Weapon("Iron Sword",5,10)
my_player.get_weapon(weapon)
my_player.check_inventory()
