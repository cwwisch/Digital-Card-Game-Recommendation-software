from operator import itemgetter


def get_preferences():
  def check_validity(var):
    while var > 4 or var < 1:
      var = int(input("""you have typed an invalid number, remember, input a 
number between 1 and 4, 4 being the most important\n"""))

  f2p = int(input("""How Important to you is it that the game is generous when
it comes to giving you cards?(input a number between 1 and 4, 4 being
the most important)\n"""))
  check_validity(f2p)
  pve = int(input("""how important is it to you that the game has PvE content?
  (input a number between 1 and 4, 4 being the most important)\n"""))
  check_validity(pve)
  competitive = int(input("""how important is it to you that the game has a well supported pro scene?
  (input a number between 1 and 4, 4 being the most important)\n"""))
  check_validity(competitive)
  p2w = int(input("""how important is it to you that you can pay to be competitive?
  (input a number between 1 and 4, 4 being the most important)\n"""))
  check_validity(p2w)
  while f2p == pve or f2p == competitive or f2p == p2w or pve == competitive or pve == p2w or competitive == p2w:
    while f2p == pve:
      choice = int(input("""Which is more important to you, 
      1) That the game is generous in giving you cards or,
      2) That the game has PvE content
      (input 1 or 2 depending on your choice)"""))
      if choice == 1:
        f2p += 1
      elif choice == 2:
        pve += 1
      else:
        print("You have input an ivalid number or a letter try again.")
    while f2p == competitive:
      choice = int(input("""Which is more important to you, 
      1) That the game is generous in giving you cards or,
      2) That the game has a well supported pro scene
      (input 1 or 2 depending on your choice)"""))
      if choice == 1:
        f2p += 1
      elif choice == 2:
        competitive += 1
      else:
        print("You have input an ivalid number or a letter try again.")
    while f2p == p2w:
      choice = int(input("""Which is more important to you, 
      1) That the game is generous in giving you cards or,
      2) That you can become competitive easily by spending money
      (input 1 or 2 depending on your choice)"""))
      if choice == 1:
        f2p += 1
      elif choice == 2:
        p2w += 1
      else:
        print("You have input an ivalid number or a letter try again.")
    while pve == competitive:
      choice = int(input("""Which is more important to you, 
      1) That the game has PvE content or,
      2) That the game has a well supported pro scene
      (input 1 or 2 depending on your choice)"""))
      if choice == 1:
        pve += 1
      elif choice == 2:
        competitive += 1
      else:
        print("You have input an ivalid number or a letter try again.")
    while pve == p2w:
      choice = int(input("""Which is more important to you, 
      1) That the game has PvE content or,
      2) That you can become competitive easily by spending money
      (input 1 or 2 depending on your choice)"""))
      if choice == 1:
        pve += 1
      elif choice == 2:
        p2w += 1
      else:
        print("You have input an ivalid number or a letter try again.")
    while competitive == p2w:
      choice = int(input("""Which is more important to you, 
      1) That the game has a well supported pro scene or,
      2) That you can become competitive easily by spending money
      (input 1 or 2 depending on your choice)"""))
      if choice == 1:
        competitive += 1
      elif choice == 2:
        p2w += 1
      else:
        print("You have input an ivalid number or a letter try again.")
  unsorted_dictionary = {"f2p": f2p, "pve": pve, "competitive": competitive, "p2w": p2w}
  sorted_dictionary = sorted(unsorted_dictionary.items(), key=itemgetter(1), reverse = True)
  """while unsorted_dictionary:
    sorted_dictionary = {}
    for item in dict(unsorted_dictionary.items()):
      max = {}
      if item.values() > max.values():
        max = item
      sorted_dictionary[max.keys()] = unsorted_dictionary.pop(max.keys())"""
  return sorted_dictionary