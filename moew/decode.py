from .data import moew_to_normal
def decode(content) -> str:
  deco: str = ''
  for thing in content.split(' '): 
    if thing != '': deco += f'{moew_to_normal[thing]}'
  return deco.lower()
