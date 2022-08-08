from .data import normal_to_moew
def encode(content) -> str:
  co: str = ''
  for letter in content.upper(): co += f'{normal_to_moew[letter]} '
  return co
