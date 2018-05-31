from random import randrange

class Player:
  def __init__(self,name):
    self.name = name
    self.health = randrange(8,12)
    self.stamina = 10
    self.attack = randrange(1,3)
    self.defence = randrange(0,3)
    self.inventory = {
      "weapon" : None,
      "armor"  : None,
      "food"   : Consumable_list()
    }

  def get_item(self,item):
    item_type = item.category
    if "Weapon" in item_type:
      self.get_weapon(item)
    else:
      self.get_consumable(item)

  def check_inventory(self):
    for item in self.inventory:
      if self.inventory[item] != None:
        self.inventory[item].print_info()
      else:
        print("    No {}\n".format(item))

  def print_info(self):
    print(r"""
    Player_name : {}
    HP : {}
    Stamina : {}
    Atk : {}
    Def : {}
    """.format(self.name,self.health,self.stamina,self.attack,self.defence))

  def get_weapon(self,weapon):
    self.inventory['weapon'] = weapon

  def get_consumable(self,consumable):
    self.inventory['food'].add_consumable(consumable)

class Weapon:
  def __init__(self,name,attack,durability):
    self.name = name
    self.attack = attack
    self.durability = durability
    self.category = "weapon"
  def print_info(self):
    print(r"""
    Weapon name : {}
    Atk : {}
    Durability : {}
    """.format(self.name,self.attack,self.durability))

class Consumable_list:
  def __init__(self):
    self.consumable_list = []

  def print_info(self):
    if len(self.consumable_list) == 0:
      print("    No consumable items.")
    else:
      for consumable in self.consumable_list:
        consumable.print_info()
  
  def add_consumable(self,consumable):
    self.consumable_list.append(consumable)

class Food:
  def __init__(self,name,description):
    self.name = name
    self.description = description
    self.category = "consumable"
  def print_info(self):
    print(r"""
    Name : {}
    Description : {}
    """.format(self.name,self.description))

name = "iBlues"
my_player = Player(name)
my_player.print_info()

weapon = Weapon("Iron Sword",5,10)
my_player.get_item(weapon)
my_player.get_item(Food("Apple","Recovers 3 HP and 2 stamina"))
my_player.check_inventory()
#my_player.get_item(weapon)
