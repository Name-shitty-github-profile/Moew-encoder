normal_to_moew: dict = {
  "A": "moew",
  "B": "Miaw",
  "C": "Moew",
  "D": "miaw",
  "E": "mOew",
  "F": "moEw",
  "G": "moeW",
  "H": "MOew",
  "I": "MoEw",
  "J": "MoeW",
  'K': "mOEww",
  'L': "mOeW",
  'M': "mOEw",
  "N": 'MOEw',
  'O': "mOEW",
  'P': "MOEW",
  'Q': "mIaw",
  'R': 'miAw',
  'S': "miaW",
  "T": "MIaww",
  'U': "MiAww",
  'V': "MiaWw",
  'W': "MIaw",
  'X': "MiAw",
  'Y': "MiaW",
  'Z': 'MIAw',
  ' ': 'MIAW',
  '.': "Meh",
  ',': 'MEH'
}

moew_to_normal: dict = {}
for k, v in normal_to_moew.items():
  moew_to_normal[k] = v
