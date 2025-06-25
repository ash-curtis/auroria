# main_battle_script.py

import random
from type_data import get_damage_multiplier
from user_pokemon_data import Pokemon
from moves_data import moves

user_pokemon = Pokemon(name='Charmander',
                       pokemon_type='Fairy',
                       moves=[moves['Scratch'], moves['Ember']],
                       status=None,
                       stats={
                           'hp': 39,
                           'attack': 52,
                           'defense': 43,
                           'sp_attack': 60,
                           'sp_defense': 50,
                           'speed': 65
                       })

opponent_pokemon = Pokemon(
    name='Clodsire',
    pokemon_type='Ground',
    moves=[moves['Poison Sting'], moves['Stomp'], moves['Water Spout']],
    status=None,
    stats={
        'hp': 130,
        'attack': 75,
        'defense': 60,
        'sp_attack': 45,
        'sp_defense': 100,
        'speed': 20
    })
# initialise turn counter
turn_number = 0

# --- THE MAIN BATTLE LOOP ---
while user_pokemon.stats['hp'] > 0 and opponent_pokemon.stats['hp'] > 0:
  # start the turn and show current status
  # increase turn number
  turn_number += 1
  print(f"\n--- Turn {turn_number} ---")
  print(
      f"\nYour HP: {user_pokemon.stats['hp']} | Opponent HP: {opponent_pokemon.stats['hp']}"
  )
  choice = input(f"\nWhat will {user_pokemon.name} do? (fight / run) ")

  # handle the "fight" choice
  if choice == "fight":
    # a. Show move menu
    print("\nYour moves:")
    for move in user_pokemon.moves:
      print(f"- {move['name']} (Power: {move['power']}, Type: {move['type']})")

    move_choice = input("\nWhich move will you use? ")

    # find the chosen move and its properties
    move_power = 0
    move_type = ""
    move_category = ""
    for move in user_pokemon.moves:
      if move['name'] == move_choice:
        move_power = move['power']
        move_type = move['type']
        move_category = move['category']
        break

    # if the move was valid, work out base damage using stats
    if move_power > 0 or move_category == 'Status':
      attacker_stat = 0
      defender_stat = 0
      base_damage = 0

      # check move category
      if move_category == 'Physical':
        attacker_stat = user_pokemon.stats['attack']
        defender_stat = opponent_pokemon.stats['defense']
      elif move_category == 'Special':
        attacker_stat = user_pokemon.stats['sp_attack']
        defender_stat = opponent_pokemon.stats['sp_defense']

      # only calculate damage if physical or special move
      if move_category in ['Physical', 'Special']:
        # simple formula for now: (attacker's stat / defender's stat) * move power
        # maybe scaling constant later
        if defender_stat == 0:  # as can't divide by zero
          base_damage = 0
        else:
          base_damage = (attacker_stat / defender_stat) * move_power

      # convert to int (as health is)
      damage = int(base_damage)

      # initialise messages for opponent's attack
      critical_hit_message = ""
      stab_message = ""
      effectiveness_message = ""

      # user critical hit
      is_critical_hit = False
      if random.randint(1, 2) == 1:
        damage = int(damage * 1.5)
        critical_hit_message = f"\033[1mA critical hit for {user_pokemon.name}!\033[0m"
        is_critical_hit = True

      # user STAB multiplier
      if user_pokemon.pokemon_type == move_type:
        damage = int(damage * 1.5)
        stab_message = f"\033[1m{user_pokemon.name} got a STAB bonus! \033[0m"

      # check for user's attack effectiveness
      opponent_type = opponent_pokemon.pokemon_type
      damage_modifier = get_damage_multiplier(move_type, opponent_type)
      damage = int(damage * damage_modifier)

      if (damage_modifier > 1.0):
        effectiveness_message = "\033[1mIt's super effective!\033[0m"
      elif (damage_modifier < 1.0):
        effectiveness_message = "\033[1mIt's not very effective!\033[0m"

      # apply final damage to opponent
      opponent_pokemon.take_damage(damage)
      print(
          f"\nYour {user_pokemon.name} used {move_choice} and dealt {damage} damage!"
      )

      # play all stored messages after main attack
      if effectiveness_message:
        print(effectiveness_message)
      if stab_message:
        print(stab_message)
      if critical_hit_message:
        print(critical_hit_message)

      # check if used move has an effect
      chosen_move_data = None
      for m in user_pokemon.moves:
        if m['name'] == move_choice:
          chosen_move_data = m
          break
      if chosen_move_data and 'effect' in chosen_move_data:
        effect = chosen_move_data['effect']
        if 'status' in effect and 'chance' in effect:
          if random.randint(1,100) <= effect['chance']:
            if effect['target'] == 'opponent':
              opponent_pokemon.apply_status(effect['status'])

      # check if opponent fainted
      if opponent_pokemon.stats['hp'] <= 0:
        print(f"\n--- {opponent_pokemon.name} fainted! You win! ---")
        break

      # opponent attacks back
      print(f"\n--- {opponent_pokemon.name}'s turn ---")
      opponent_move = opponent_pokemon.moves[0]

      # opponent critical hit
      opponent_critical_hit_message = ""
      opponent_stab_message = ""
      opponent_effectiveness_message = ""

      # Finding the most effective move for the opponent
      for move in opponent_pokemon.moves:
        if get_damage_multiplier(move['type'], user_pokemon.pokemon_type) > 1.0:
          opponent_move = move
          break

      opponent_move_power = opponent_move['power']
      opponent_move_type = opponent_move['type']
      opponent_move_category = opponent_move['category']

      # initialise damage and base_damage for opponent
      opponent_damage = 0
      base_opponent_damage = 0

      # determine attacker's stat (opponent) and defender's stat (user) based on move category
      opponent_attacker_stat = 0
      opponent_defender_stat = 0

      # check move category and set relevant stats (aligned here)
      if opponent_move_category == 'Physical':
        opponent_attacker_stat = opponent_pokemon.stats['attack']
        opponent_defender_stat = user_pokemon.stats['defense']
      elif opponent_move_category == 'Special':
        opponent_attacker_stat = opponent_pokemon.stats['sp_attack']
        opponent_defender_stat = user_pokemon.stats['sp_defense']

      # Only calculate base damage if it's a physical or special move
      if opponent_move_category in ['Physical', 'Special']:
        # core damage formula: (attacker's stat / defender's stat) * move power
        if opponent_defender_stat == 0:
          base_opponent_damage = 0
        else:
          base_opponent_damage = (opponent_attacker_stat /
                                  opponent_defender_stat) * opponent_move_power

        # convert to int (as hp is int)
        opponent_damage = int(base_opponent_damage)
      else:  # if it's a Status move, ensure damage is 0
        opponent_damage = 0

      # inistialise messages for opponent's attack
      opponent_critical_hit_message = ""
      opponent_stab_message = ""
      opponent_effectiveness_message = ""

      # spply critical hit, STAB, effectiveness to opponent_damage
      # only if it's a damaging move (physical or special)
      if opponent_move_category in ['Physical', 'Special']:
        # opponent critical hit
        if random.randint(1, 2) == 1:
          opponent_damage = int(opponent_damage * 1.5)
          opponent_critical_hit_message = f"\033[1mA critical hit for {opponent_pokemon.name}!\033[0m"

        # opponent STAB multiplier
        if opponent_pokemon.pokemon_type == opponent_move_type:
          opponent_damage = int(opponent_damage * 1.5)
          opponent_stab_message = f"\033[1m{opponent_pokemon.name} got a STAB bonus! \033[0m"

        # check for opponent's attack effectiveness
        damage_modifier = get_damage_multiplier(opponent_move_type, player_type)
        opponent_damage = int(opponent_damage * damage_modifier)

        if damage_modifier > 1.0:
          opponent_effectiveness_message = "\033[1mIt's super effective!\033[0m"
        elif damage_modifier < 1.0:
          opponent_effectiveness_message = "\033[1mIt's not very effective!\033[0m"

      user_pokemon.take_damage(opponent_damage)
      print(
          f"\n{opponent_pokemon.name} used {opponent_move['name']} and dealt {opponent_damage} damage!"
      )
              
      # play all stored messages after main attack
      if opponent_effectiveness_message:
        print(opponent_effectiveness_message)
      if opponent_stab_message:
        print(opponent_stab_message)
      if opponent_critical_hit_message:
        print(opponent_critical_hit_message)

      # check if opponent's move has a status effect
      chosen_opponent_move_data_for_effect = None
      for m in opponent_pokemon.moves:
        if m['name'] == opponent_move['name']:
          chosen_opponent_move_data_for_effect = m
          break
          
      if chosen_opponent_move_data_for_effect and 'effect' in chosen_opponent_move_data_for_effect:
        effect = chosen_opponent_move_data_for_effect['effect']
        if 'status' in effect and 'chance' in effect:
          if random.randint(1,100) <= effect['chance']:
            if effect['target'] == 'opponent':
              user_pokemon.apply_status(effect['status'])
      
      # check if player fainted
      if user_pokemon.stats['hp'] <= 0:
        print(f"\n--- {user_pokemon.name} fainted! You lose. ---")
        break

    else:
      print("That's not a valid move! You lose a turn.")

  # handling the "run" choice
  elif choice == "run":
    print("You got away safely!")
    break

  # handling invalid choices
  else:
    print("Invalid choice. Please type 'fight' or 'run'.")

# end of battle
print("\nThe battle is over.")


