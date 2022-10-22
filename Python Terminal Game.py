import random

weapon_types = {"stick":["melee", "magic"], "staff":"magic", "sword":"melee", "spear":["melee", "ranged"], "bow":"ranged", "gun":["magic", "ranged"]}

role_types = {"archer":"ranged", "warrior":"melee", "mage":"magic"}

special_qualities = ["poisonous", "superduper fast", "able to heal itself"]

adjectives = ["juicy", "hangry", "gorgeous", "gross af", "frickin stupid", "John Stamos-looking", "run-of-the-mill"]

# Warrior > Mage
# Archer > Warrior
# Mage > Archer

class Player:
  def __init__(self, name, role, weapon, level=1):
    self.name = name
    self.role = role
    self.weapon = weapon
    self.level = level
    self.health = level *10
    self.max_health = level *10
    self.exp = 0

  def __repr__(self):
    return "{}, a level {} {}, has {} health left.".format(self.name, self.level, self.role, self.health)

  def attack(self, enemy):
    attack_power = 0
    advantage = 1
    current_weapon_type = weapon_types.get(self.weapon)
    # Role v role advantage
    if self.role == "warrior" and enemy.role == "mage":
      advantage+=1
    if self.role == "archer" and enemy.role == "warrior":
      advantage+=1
    if self.role == "mage" and enemy.role == "archer":
      advantage+=1
    # Role v role disadvantage
    if self.role == "warrior" and enemy.role == "archer":
      advantage = advantage * .75
    if self.role == "archer" and enemy.role == "mage":
      advantage = advantage * .75
    if self.role == "mage" and enemy.role == "warrior":
      advantage = advantage * .75
    # Weapon v role advantage
    if current_weapon_type == "warrior" and enemy.role == "mage":
      advantage+=1
    if current_weapon_type == "archer" and enemy.role == "warrior":
      advantage+=1
    if current_weapon_type == "mage" and enemy.role == "archer":
      advantage+=1
    # Role and weapon compatibility
    if role_types.get(self.role) in current_weapon_type:
      advantage+=1
    # Attack power result
    attack_power = self.level * advantage
    return attack_power

  def loot(self, enemy):
    choice = input("Do you want to loot the loser or take it easy and rest? (Loot or rest):  ").lower()
    while choice not in ("loot", "rest"):
      choice = input("You think you're clever, with your free will. Choose loot or rest:  ")
    if choice == "rest":
      input("You calmly took a breath")
      input(("You've been fully restored to {} health").format(self.max_health))
      self.health = self.max_health
      return player
    if choice == "loot":
      input("You quickly scan the loser")
      possible_weapon =  random.choice(list(weapon_types.keys()))
      weapon_choice = input(("Looks like this {} was using a {}, though clearly not well. Do you want it?\n").format(enemy.role, possible_weapon)).lower()
      while weapon_choice not in ("y","n","yes","no"):
        weapon_choice = input("Just looking for yes or no, dude.  ").lower()
      if weapon_choice in ("y", "yes"):
        self.weapon = possible_weapon
        input(("You look bitchin with your new {}! Let's try it out.").format(self.weapon))
      if weapon_choice in ("n", "no"):
        input(("Good call, you look better with your {} anyway. Let's continue.").format(self.weapon))
        choice = "done"
      return player

  def exp_gain(self, enemy):
    nxt_lvl = self.level * 2
    self.exp += enemy.level
    input(("You gained {} exp").format(enemy.level))
    if self.exp >= nxt_lvl:
      self.level +=1
      self.exp -= nxt_lvl
      self.max_health = self.level *10
      input(("You leveled up! Not sure what that means, but you're now level {}").format(self.level))
      return player
    else:
      input(("Just {} exp until you level up").format(nxt_lvl - self.exp))
      return player

class Monster:
  def __init__(self, role, level, special):
    self.role = role
    self.level = level
    self.health = level *9
    self.max_health = level *9
    self.special = special
    
  def __repr__(self):
    return "A {} {} has appeared! Looks like they're {}.".format(random.choice(adjectives), self.role, self.special)
  
  def attack(self, player):
    attack_power = 0
    advantage = 1
    # Role v role advantage
    if self.role == "warrior" and player.role == "mage":
      advantage+=1
    if self.role == "archer" and player.role == "warrior":
      advantage+=1
    if self.role == "mage" and player.role == "archer":
      advantage+=1
    # Role v role disadvantage
    if self.role == "warrior" and player.role == "archer":
      advantage = advantage * .75
    if self.role == "archer" and player.role == "mage":
      advantage = advantage * .75
    if self.role == "mage" and player.role == "warrior":
      advantage = advantage * .75
    # Attack power result
    attack_power = self.level * advantage
    return attack_power
  
  #def poison(self, player):

  #def heal(self):
    
player_name = input("Enter player name, then hit Enter.\n")

player_role = input("What type of fighter are you?\nArcher, Warrior, or Mage\n").lower()
#checking to see if user follows directions
while player_role not in ("archer", "warrior", "mage"):
  player_role = input("I don't think that's a real thing. What is it similar to:\n Archer, Warrior, or Mage?\n").lower()
print(("Ah, {}, the mighty {} I've heard nothing about.").format(player_name, player_role))

player_weapon = random.choice(list(weapon_types.keys()))
player = Player(player_name, player_role, player_weapon)
current_weapon_type = weapon_types.get(player.weapon)
input()

print(("Hey look, a {} is just lying here. \nNow it's your weapon.").format(player.weapon))
input()

fight_question = input("Ready to pick a fight?\nY/N:\n")
while fight_question.lower() not in ("y", "n", "yes", "no"):
  fight_question = input("Not an option\nYes or no?\n")
if fight_question.lower() in ("y", "yes"):
  print("Great! I see some losers over there, let's go.")
  input()
if fight_question.lower() in ("n", "no"):
  print("Too bad. Should have thought about that before running this program. Let's go.")
  input()

def battle(player):
  enemy = Monster(random.choice(list((role_types.keys()))), player.level, random.choice(list((special_qualities))))

  def attack_sequence(player, enemy):
      if enemy.special == "superduper fast":
        bad = round(enemy.attack(player))
        player.health -= bad
        if player.health <= 0:
          return "You lose"
        else:
          print(("\nIt's wicked fast! You lost {} health.\nYou have {} health remaining.").format(bad, player.health))
          input()
        good = round(player.attack(enemy))
        enemy.health -= good
        print(("You damaged the {} for {} health.\nThey have {} health remaining.").format(enemy.role, good, enemy.health))
        input()
        return player, enemy
      else:
        good = round(player.attack(enemy))
        enemy.health -= good
        print(("\nYou damaged the {} for {} health.\nThey have {} health remaining.").format(enemy.role, good, enemy.health))
        input()
        bad = round(enemy.attack(player))
        player.health -= bad
        if player.health <= 0:
            return "You lose"
        if enemy.health <= 0:
            return player, enemy
        else:
          print(("It attacked! You lost {} health.\nYou have {} health remaining.").format(bad, player.health))
          input()
        return player, enemy
      return player, enemy
  input(enemy)
  enemy.health = 3
  while enemy.health > 0:
    if player.health <= 0:
      input(("Bad choice, the {} has beaten the crap out of you\nYou feel as though you're leaving the battle function...").format(enemy.role))
      break
    atk_or_run = input("Attack or run?\n").lower()
    while atk_or_run not in ("attack", "run"):
      print("Try again.\n")
    if atk_or_run == "attack":
      attack_sequence(player, enemy)
    if atk_or_run == "run":
      input("Good call, you suck")
      input("Just kidding, I love you\nThanks for playing this")
  if enemy.health <= 0:
    input("Damn fine fightin'")
    player.exp_gain(enemy)
    player.loot(enemy)
    return player, enemy
  else:
    play_again = "n"
    return player, play_again

battle_count = 0
play_again = "y"

while battle_count < 3:
  battle_count += 1
  battle(player)
  if player.health <= 0:
    input()
    break
  while True:
        play_again = input(("You've had {} battle(s)\nDo you want to play again?\n").format(battle_count))
        if play_again not in ("y","n","yes","no"):
            print("What was that? I can't hear incorrect inputs\n")
            continue
        break
  if play_again in ("n","no"):
    break
  continue
  
    
input("All done already?")


#enemy specials and limit on battles/some sort of endgame needed