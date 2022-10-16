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
    # Weapon v role disadvantage
    if current_weapon_type == "warrior" and enemy.role == "archer":
      advantage = advantage * .75
    if current_weapon_type == "archer" and enemy.role == "mage":
      advantage = advantage * .75
    if current_weapon_type == "mage" and enemy.role == "warrior":
      advantage = advantage * .75
    # Role and weapon compatibility
    if current_weapon_type == self.role:
      advantage+=1
    if self.role != current_weapon_type:
      advantage = advantage * .80
    # Attack power result
    attack_power = self.level * advantage
    return attack_power

  def loot(self, enemy):
    choice = input("Do you want to loot the loser or take it easy and rest? (Loot or rest):  ").lower()
    loot_or_rest = 1
    while loot_or_rest == 1:
      if choice not in ("loot", "rest"):
        choice = input("You think you're clever, with your free will. Choose loot or rest:  ")
        continue
      if choice == "rest":
        input("You calmly took a breath")
        self.health = self.max_health
        loot_or_rest = 2
      if choice == "loot":
        input("You quickly scan the loser")
        possible_weapon =  random.choice(list(weapon_types.keys()))
        weapon_choice = input(("Looks like this {} was using a {}, though clearly not well. Do you want it?\n").format(enemy.role, possible_weapon)).lower()
        while loot_or_rest == 1:
          if weapon_choice not in ("y","n","yes","no"):
            weapon_choice = input("Just looking for yes or no, dude.  ").lower()
            continue
          if weapon_choice == "y" or "yes":
            self.weapon = possible_weapon
            input(("You look bitchin with your new {}! Let's try it out.").format(self.weapon))
            loot_or_rest = 2
            break
          if weapon_choice == "n" or "no":
            input(("Good call, you look better with your {} anyway. Let's continue.").format(self.weapon))
            loot_or_rest = 2
            break
        choice = "done"
      if choice == "done":
        break
  #def run_away(self):
    #guaranteed

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

  #def gloat(self):
    
player_name = input("Enter player name, then hit Enter.\n")

player_role = input("What type of fighter are you?\nArcher, Warrior, or Mage\n").lower()

#checking to see if user follows directions
while True:
  if player_role not in ("archer", "warrior", "mage"):
    player_role = input("I don't think that's a real thing. What is it similar to:\n Archer, Warrior, or Mage?\n").lower()
    continue
  else:
    print(("Ah, {}, the mighty {} I've heard nothing about.").format(player_name, player_role))
    break

player_weapon = random.choice(list(weapon_types.keys()))

player = Player(player_name, player_role, player_weapon)

input()
print(("Hey look, a {} is just lying here. \nNow it's your weapon.").format(player.weapon))
current_weapon_type = weapon_types.get(player.weapon)
input()
fight_question = input("Ready to pick a fight?\nY/N:\n")

if fight_question.lower() == "y":
  print("Great! I see some losers over there, let's go.")
  input("Press Enter to continue")
if fight_question.lower() == "n":
  print("Too bad. Should have thought about that before running this program. Let's go.")
  input("Press Enter to continue")

battle_count = 0

def battle(player, battle_count):
  battle_count += 1
  enemy = Monster(random.choice(list((role_types.keys()))), player.level, random.choice(list((special_qualities))))

  def attack_sequence(player, enemy):
      if enemy.health <= 0:
        print("You won! I haven't added exp yet, but it'll get there!")
        return player, enemy
      elif enemy.special == "superduper fast":
        bad = round(enemy.attack(player))
        player.health -= bad
        if player.health <= 0:
          return "You lose"
        else:
          print(("It's wicked fast! You lost {} health.\nYou have {} health remaining.").format(bad, player.health))
        good = round(player.attack(enemy))
        enemy.health -= good
        print(("You damaged the {} for {} health.\nThey have {} health remaining.").format(enemy.role, good, enemy.health))
        return player, enemy
      else:
        good = round(player.attack(enemy))
        enemy.health -= good
        print(("You damaged the {} for {} health.\nThey have {} health remaining.").format(enemy.role, good, enemy.health))
        bad = round(enemy.attack(player))
        player.health -= bad
        if player.health <= 0:
          return "You lose"
        else:
          print(("It attacked! You lost {} health.\nYou have {} health remaining.").format(bad, player.health))
        return player, enemy
      return player, enemy
  input(enemy)
  enemy.health = 3
  while enemy.health > 0:
    atk_or_run = input("Attack or run?\n").lower()
    if atk_or_run not in ("attack", "run"):
      atk_or_run = input("Try again.\nAttack or run?\n")
      continue
    if atk_or_run == "attack":
      attack_sequence(player, enemy)
      continue
    if atk_or_run == "run":
      input("Good call, you suck")
      input("Just kidding, I love you\nThanks for playing this")
      break
  if enemy.health <= 0:
    input("Damn fine fightin'")
    player.loot(enemy)
    play_again = input(("You've had {} battle(s)\nDo you want to play again?").format(battle_count))
  else:
    return "Didn't get here yet"

battle(player,battle_count)