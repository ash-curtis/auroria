import random
from type_data import type_chart
from user_pokemon_data import user_pokemon
from opponent_pokemon_data import opponent_pokemon

# initialise turn counter
turn_number = 0

# --- THE MAIN BATTLE LOOP ---
# Changed access to user_pokemon['stats']['hp'] and opponent_pokemon['stats']['hp']
while user_pokemon['stats']['hp'] > 0 and opponent_pokemon['stats']['hp'] > 0:
  # 1. Start the turn and show current status
  # increase turn number
  turn_number += 1
  print(f"\n--- Turn {turn_number} ---")
  # Changed access to user_pokemon['stats']['hp'] and opponent_pokemon['stats']['hp']
  print(
      f"\nYour HP: {user_pokemon['stats']['hp']} | Opponent HP: {opponent_pokemon['stats']['hp']}"
  )
  choice = input(f"\nWhat will {user_pokemon['name']} do? (fight / run) ")

  # 2. Handle the "fight" choice
  if choice == "fight":
    # a. Show move menu
    print("\nYour moves:")
    for move in user_pokemon['moves']:
      print(f"- {move['name']} (Power: {move['power']}, Type: {move['type']})")

    move_choice = input("\nWhich move will you use? ")

    # b. Find the chosen move and its properties
    damage = 0
    move_type = ""
    for move in user_pokemon['moves']:
      if move['name'] == move_choice:
        damage = move['power']
        move_type = move['type']

    # c. If the move was valid, begin the attack sequence
    if damage > 0:
      critical_hit_message = ""
      stab_message = ""

      # user critical hit
      is_critical_hit = False
      if random.randint(1, 2) == 1:
        damage = int(damage * 1.5)
        critical_hit_message = f"\033[1mA critical hit for {user_pokemon['name']}!\033[0m"
        is_critical_hit = True

      # user STAB multiplier
      if user_pokemon['type'] == move_type:
        damage = int(damage * 1.5)
        stab_message = f"\033[1m{user_pokemon['name']} got a STAB bonus! \033[0m"

      # check for user's attack effectiveness
      effectiveness_message = ""
      opponent_type = opponent_pokemon['type']
      if move_type in type_chart and opponent_type in type_chart[move_type][
          'super_effective']:
        damage = int(damage * 1.5)
        effectiveness_message = "\n\033[1mIt's super effective!\033[0m"
      elif move_type in type_chart and opponent_type in type_chart[move_type][
          'not_very_effective']:
        damage = int(damage * 0.5)
        effectiveness_message = "\n\033[1mIt's not very effective!\033[0m"

      # Apply final damage to opponent
      # Changed access to opponent_pokemon['stats']['hp']
      opponent_pokemon['stats'][
          'hp'] = opponent_pokemon['stats']['hp'] - damage
      print(
          f"\nYour {user_pokemon['name']} used {move_choice} and dealt {damage} damage!"
      )

      # play all stored messages after main attack
      if effectiveness_message:
        print(effectiveness_message)
      if stab_message:
        print(stab_message)
      if critical_hit_message:
        print(critical_hit_message)

        # check if opponent fainted
      # Changed access to opponent_pokemon['stats']['hp']
      if opponent_pokemon['stats']['hp'] <= 0:
        print(f"\n--- {opponent_pokemon['name']} fainted! You win! ---")
        break

      # opponent attacks back
      print(f"\n--- {opponent_pokemon['name']}'s turn ---")
      opponent_move = opponent_pokemon['moves'][0]

      # opponent critical hit
      opponent_critical_hit_message = ""
      opponent_stab_message = ""
      opponent_effectiveness_message = ""

      player_type = user_pokemon['type']
      for move in opponent_pokemon['moves']:
        move_type_for_check = move['type']
        if move_type_for_check in type_chart and player_type in type_chart[
            move_type_for_check]['super_effective']:
          opponent_move = move
          break

      opponent_damage = opponent_move['power']
      opponent_move_type = opponent_move['type']

      # opponent critical hit
      if random.randint(1, 2) == 1:
        opponent_damage = int(opponent_damage * 1.5)
        opponent_critical_hit_message = f"\033[1mA critical hit for {opponent_pokemon['name']}!\033[0m"

      # opponent STAB multiplier
      if opponent_pokemon['type'] == opponent_move_type:
        opponent_damage = int(opponent_damage * 1.5)
        opponent_stab_message = f"\033[1m{opponent_pokemon['name']} got a STAB bonus! \033[0m"

        # check for opponent's attack effectiveness
      opponent_effectiveness_message = ""
      if opponent_move_type in type_chart and player_type in type_chart[
          opponent_move_type]['super_effective']:
        opponent_damage = int(opponent_damage * 1.5)
        opponent_effectiveness_message = "\033[1mIt's super effective!\033[0m"
      elif opponent_move_type in type_chart and player_type in type_chart[
          opponent_move_type]['not_very_effective']:
        opponent_damage = int(opponent_damage * 0.5)
        opponent_effectiveness_message = "\033[1mIt's not very effective!\033[0m"

      # spply final damage to player
      # Changed access to user_pokemon['stats']['hp']
      user_pokemon['stats'][
          'hp'] = user_pokemon['stats']['hp'] - opponent_damage
      print(
          f"\n{opponent_pokemon['name']} used {opponent_move['name']} and dealt {opponent_damage} damage!"
      )

      # play all stored messages after main attack
      if opponent_effectiveness_message:
        print("\n" + opponent_effectiveness_message)
      if opponent_stab_message:
        print(opponent_stab_message)
      if opponent_critical_hit_message:
        print(opponent_critical_hit_message)

      # check if player fainted
      # Changed access to user_pokemon['stats']['hp']
      if user_pokemon['stats']['hp'] <= 0:
        print(f"\n--- {user_pokemon['name']} fainted! You lose. ---")
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
