import random

weapon_types = {"stick":["warrior", "mage"], "staff":["mage"], "sword":["warrior"], "spear":["warrior", "archer"], "bow":["archer"], "gun":["mage", "archer"]}

special_qualities = ["poisonous", "superduper fast", "able to heal themself"]

adjectives = ["juicy", "hangry", "gorgeous", "gross af", "frickin stupid", "John Stamos-looking", "run-of-the-mill"]

# Warrior > Mage
# Archer > Warrior
# Mage > Archer
advantage_dict = {"warrior":"mage","archer":"warrior","mage":"archer"}

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
    if advantage_dict[self.role] == enemy.role:
      advantage+=1
    # if self.role == "warrior" and enemy.role == "mage":
    #   advantage+=1
    # if self.role == "archer" and enemy.role == "warrior":
    #   advantage+=1
    # if self.role == "mage" and enemy.role == "archer":
    #   advantage+=1
    # Role v role disadvantage
    if advantage_dict[enemy.role] == self.role:
      advantage = advantage * .75
    # if self.role == "warrior" and enemy.role == "archer":
    #   advantage = advantage * .75
    # if self.role == "archer" and enemy.role == "mage":
    #   advantage = advantage * .75
    # if self.role == "mage" and enemy.role == "warrior":
    #   advantage = advantage * .75
    # Weapon v role advantage
    for type in current_weapon_type:
      if enemy.role in advantage_dict[type]:
        advantage+=1
    # if current_weapon_type == "warrior" and enemy.role == "mage":
    #   advantage+=1
    # if current_weapon_type == "archer" and enemy.role == "warrior":
    #   advantage+=1
    # if current_weapon_type == "mage" and enemy.role == "archer":
    #   advantage+=1
    # Role and weapon compatibility
    if self.role in current_weapon_type:
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
    self.exp += round((enemy.level * 1.4))
    input(("You gained {} exp").format(round((enemy.level * 1.4))))
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
    self.health = level *7
    self.max_health = level *7
    self.special = special
    
  def __repr__(self):
    return "A {} {} has appeared! Looks like they're {}.".format(random.choice(adjectives), self.role, self.special)
  
  def attack(self, player):
    attack_power = 0
    advantage = 1
    if advantage_dict[self.role] == player.role:
      advantage+=1
    if advantage_dict[player.role] == self.role:
      advantage = advantage * .75
    # Attack power result
    attack_power = self.level * advantage
    return attack_power
  
  def poison(self, player):
    player.health -= round((self.level+1)/2)
    input(("The {}'s poisoned weapon stings again.\nYou have {} health left").format(self.role, player.health))
    return player

  def heal(self):
    self.health += self.level
    input(("The {} healed itself to {} health").format(self.role,self.health))
    return self

input("I'm not a game designer, but this practice game for Codecademy is basically Dark Souls")
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
  enemy = Monster(random.choice(list((advantage_dict.keys()))), player.level, random.choice(list((special_qualities))))
  if battle_count == 1 or 2:
    enemy.role = player.role
    enemy.health = 4
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
        print(("\nYou damaged the {} for {} health.").format(enemy.role, good))
        if enemy.health <= 0:
            return player, enemy
        input(("They have {} health remaining").format(enemy.health))
        return player, enemy
      else:
        good = round(player.attack(enemy))
        enemy.health -= good
        print(("\nYou damaged the {} for {} health.").format(enemy.role, good))
        if enemy.health <= 0:
            return player, enemy
        input(("They have {} health remaining").format(enemy.health))
        bad = round(enemy.attack(player))
        player.health -= bad
        if player.health <= 0:
            return "You lose"
        
        else:
          print(("It attacked! You lost {} health.\nYou have {} health remaining.").format(bad, player.health))
          input()
        return player, enemy
      return player, enemy
  input(enemy)
  turn_count=0
  while enemy.health > 0:
    if player.health <= 0:
      input(("Bad choice, the {} has beaten the crap out of you\nYou feel as though you're leaving the battle function...").format(enemy.role))
      break
    atk_or_run = input("Attack or run?\n").lower()
    while atk_or_run not in ("attack", "run", "a", "r"):
      print("Try again.\n")
      atk_or_run = input("Attack or run?\n").lower()
    if atk_or_run in("a", "attack"):
      turn_count+=1
      attack_sequence(player, enemy)
      if enemy.health > 0:
        if enemy.special == "poisonous":
          enemy.poison(player)
        if (enemy.special =="able to heal themself") & (turn_count%2==0):
          enemy.heal()
    if atk_or_run in ("r", "run"):
      input("Good call, you suck")
      input("Just kidding, I love you\nThanks for playing this")
      break
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

while battle_count < 4:
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
  
def final_battle(player):
  enemy = Monster(role=advantage_dict[player.role], level=(player.level-1), special="superduper fast")
  enemy.health = 30
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
        print(("\nYou damaged the {} for {} health.").format(enemy.role, good))
        if enemy.health <= 0:
            return player, enemy
        input(("They have {} health remaining").format(enemy.health))
        return player, enemy
      else:
        good = round(player.attack(enemy))
        enemy.health -= good
        print(("\nYou damaged the {} for {} health.").format(enemy.role, good))
        if enemy.health <= 0:
            return player, enemy
        input(("They have {} health remaining").format(enemy.health))
        bad = round(enemy.attack(player))
        player.health -= bad
        if player.health <= 0:
            return "You lose"
        
        else:
          print(("It attacked! You lost {} health.\nYou have {} health remaining.").format(bad, player.health))
          input()
        return player, enemy
      return player, enemy
  input(("Uh oh, you pissed off someone.\nThat {} looks terrifyingly cunning.").format(enemy.role))
  turn_count=0
  while enemy.health > 0:
    if player.health <= 0:
      input(("Bad choice, the {} has beaten the crap out of you\nYou feel as though you're leaving the battle function...").format(enemy.role))
      break
    atk_or_run = input("Attack or run?\n").lower()
    while atk_or_run not in ("attack", "run", "a", "r"):
      print("Try again.\n")
      atk_or_run = input("Attack or run?\n").lower()
    if atk_or_run in("a", "attack"):
      turn_count+=1
      attack_sequence(player, enemy)
      enemy.poison(player)
    if atk_or_run in ("r", "run"):
      input("Good call, you suck")
      input("Just kidding, I love you\nThanks for playing this")
      break
  if enemy.health <= 0:
    input("Huh, you did it. I think you've beaten everyone\nGoodbye")
    return player, enemy
  else:
    play_again = "n"
    return player, play_again

final_battle(player)
input("All done already?")


#fix what happens when you suck