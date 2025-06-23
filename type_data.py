type_chart = {
  'Normal': {
    'super_effective': ['Ghost'],
    'not_very_effective': ['Rock', 'Steel']
  },
  'Fire': {
    'super_effective': ['Grass', 'Ice', 'Bug', 'Steel'],
    'not_very_effective': ['Rock', 'Fire','Water', 'Dragon']
  },
  'Water': {
    'super_effective': ['Fire', 'Ground', 'Rock'],
    'not_very_effective': ['Water', 'Grass', 'Dragon']
  },
  'Electric': {
    'super_effective': ['Water', 'Flying'],
    'not_very_effective': ['Electric', 'Grass', 'Dragon']
  },
  'Grass': {
    'super_effective': ['Water', 'Ground', 'Rock'],
    'not_very_effective': ['Fire', 'Grass', 'Poison', 'Flying', 'Bug', 'Dragon', 'Steel']
  },
  'Ice': {
    'super_effective': ['Grass', 'Ground', 'Flying', 'Dragon'],
    'not_very_effective': ['Fire', 'Water', 'Ice', 'Steel']
  },
  'Fighting': {
    'super_effective': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'],
    'not_very_effective': ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy']
  },
  'Poison': {
    'super_effective': ['Grass', 'Fairy'],
    'not_very_effective': ['Poison', 'Ground', 'Rock', 'Ghost']
  },
  'Ground': {
    'super_effective': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'],
    'not_very_effective': ['Grass', 'Bug']
  },
  'Flying': {
    'super_effective': ['Grass', 'Fighting', 'Bug'],
    'not_very_effective': ['Electric', 'Rock', 'Steel']
  },
  'Psychic': {
    'super_effective': ['Fighting', 'Poison'],
    'not_very_effective': ['Psychic', 'Steel']
  },
  'Bug': {
    'super_effective': ['Grass', 'Psychic', 'Dark'],
    'not_very_effective': ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost', 'Steel', 'Fairy']
  },
  'Rock': {
    'super_effective': ['Fire', 'Ice', 'Flying', 'Bug'],
    'not_very_effective': ['Fighting', 'Ground', 'Steel']
  },
  'Ghost': {
    'super_effective': ['Psychic', 'Ghost'],
    'not_very_effective': ['Dark']
  },
  'Dragon': {
    'super_effective': ['Dragon'],
    'not_very_effective': ['Steel']
  },
  'Dark': {
    'super_effective': ['Psychic', 'Ghost'],
    'not_very_effective': ['Fighting', 'Dark', 'Fairy']
  },
  'Steel': {
    'super_effective': ['Ice', 'Rock', 'Fairy'],
    'not_very_effective': ['Fire', 'Water', 'Electric', 'Steel']
  },
  'Fairy': {
    'super_effective': ['Fighting', 'Dragon' 'Dark'],
    'not_very_effective': ['Fire', 'Poison', 'Steel']
  },
}
