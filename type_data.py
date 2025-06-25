type_chart = {
  'Normal': {
    'Ghost': 1.5,
    'Rock': 0.5,
    'Steel': 0.5
  },
  'Fire': {
    'Grass': 1.5,
    'Ice': 1.5,
    'Bug': 1.5,
    'Steel': 1.5,
    'Rock': 0.5,
    'Fire': 0.5,
    'Water': 0.5,
    'Dragon': 0.5
  },
  'Water': {
    'Fire': 1.5,
    'Ground': 1.5,
    'Rock': 1.5,
    'Water': 0.5,
    'Grass': 0.5,
    'Dragon': 0.5
  },
  'Electric': {
    'Water': 1.5,
    'Flying': 1.5,
    'Electric': 0.5,
    'Grass': 0.5,
    'Dragon': 0.5
  },
  'Grass': {
    'Water': 1.5,
    'Ground': 1.5,
    'Rock': 1.5,
    'Fire': 0.5,
    'Grass': 0.5,
    'Poison': 0.5,
    'Flying': 0.5,
    'Bug': 0.5,
    'Dragon': 0.5,
    'Steel': 0.5
  },
  'Ice': {
    'Grass': 1.5,
    'Ground': 1.5,
    'Flying': 1.5,
    'Dragon': 1.5,
    'Fire': 0.5,
    'Water': 0.5,
    'Ice': 0.5,
    'Steel': 0.5
  },
  'Fighting': {
    'Normal': 1.5,
    'Ice': 1.5,
    'Rock': 1.5,
    'Dark': 1.5,
    'Steel': 1.5,
    'Poison': 0.5,
    'Flying': 0.5,
    'Psychic': 0.5,
    'Bug': 0.5,
    'Fairy': 0.5
  },
  'Poison': {
    'Grass': 1.5,
    'Fairy': 1.5,
    'Poison': 0.5,
    'Ground': 0.5,
    'Rock': 0.5,
    'Ghost': 0.5
  },
  'Ground': {
    'Fire': 1.5,
    'Electric': 1.5,
    'Poison': 1.5,
    'Rock': 1.5,
    'Steel': 1.5,
    'Grass': 0.5,
    'Bug': 0.5
  },
  'Flying': {
    'Grass': 1.5,
    'Fighting': 1.5,
    'Bug': 1.5,
    'Electric': 0.5,
    'Rock': 0.5,
    'Steel': 0.5
  },
  'Psychic': {
    'Fighting': 1.5,
    'Poison': 1.5,
    'Psychic': 0.5,
    'Steel': 0.5
  },
  'Bug': {
    'Grass': 1.5,
    'Psychic': 1.5,
    'Dark': 1.5,
    'Fire': 0.5,
    'Fighting': 0.5,
    'Poison': 0.5,
    'Flying': 0.5,
    'Ghost': 0.5,
    'Steel': 0.5,
    'Fairy': 0.5
  },
  'Rock': {
    'Fire': 1.5,
    'Ice': 1.5,
    'Flying': 1.5,
    'Bug': 1.5,
    'Fighting': 0.5,
    'Ground': 0.5,
    'Steel': 0.5
  },
  'Ghost': {
    'Psychic': 1.5,
    'Ghost': 1.5,
    'Dark': 0.5
  },
  'Dragon': {
    'Dragon': 1.5,
    'Steel': 0.5
  },
  'Dark': {
    'Psychic': 1.5,
    'Ghost': 1.5,
    'Fighting': 0.5,
    'Dark': 0.5,
    'Fairy': 0.5
  },
  'Steel': {
    'Ice': 1.5,
    'Rock': 1.5,
    'Fairy': 1.5,
    'Fire': 0.5,
    'Water': 0.5,
    'Electric': 0.5,
    'Steel': 0.5
  },
  'Fairy': {
    'Fighting': 1.5,
    'DragonDark': 1.5,
    'Fire': 0.5,
    'Poison': 0.5,
    'Steel': 0.5
  },
}

def get_damage_multiplier(attacking_type, defending_type):
  return type_chart.get(attacking_type, {}).get(defending_type, 1.0)