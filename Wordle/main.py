import requests
from simple_colors import yellow, green, red
import os, random
from unidecode import unidecode

def local_compare(s1, s2):
  return unidecode(s1).lower() == unidecode(s2).lower()
  
def clear_terminal():
  os.system('clear')

def get_hidden_word(word):
  hidden_word = []
  for l in word:
    hidden_word.append("_")
  return hidden_word

def get_word():
  words = ['mediaban', 'ahínco', 'hirviente', 'íbamos', 'trescientos', 'agenciarse', 'evidentemente', 'canto', 'concluya', 'padecerá', 'gastronómica', 'facultades', 'atrevan', 'quitándole', 'desconceptuadas', 'avergüence', 'glacial', 'hendía', 'reconozco', 'atrajera', 'gran', 'teresuplicó', 'gabineteme', 'repita', 'asombraría', 'lagarto', 'lucecilla', 'llegó', 'encontrele', 'desconfianza']
  try:
    res = requests.get('https://clientes.api.greenborn.com.ar/public-random-word?c=1', {
      "headers": {
        "Content-Type": "application/json"
      }
    })
    data = res.json()
    return data[0].lower()
  except Exception as e:
    randomIndex = random.randint(0, len(words) - 1)
    return words[randomIndex].lower()

def show_interface(textError=None):
  clear_terminal()
  print('\n', end='')
  print(f"Intentos restantes: {MAX_ATTEMPS - ATTEMP}")
  print(f"  ({len(WORD)} letras...)\n")
  if textError is not None: 
      print(red(textError), "\n")
  show_word_with_colors()
  
def validate_word():
  error = False
  textError = None
  while True:
    show_interface(textError)
    text = input(f" :  ")
    try:
      int(text)
      error = True
      textError = "No valido"
      continue
    except:
      pass
    if len(text) != len(WORD):
      error = True
      textError = "Tamaño incorrecto"
      continue
    
    error = False
    
    return text.lower()

def is_finded_word():
  for i, letter in enumerate(ATTEMPS[ATTEMP]):
    if not local_compare(letter, WORD[i]):
      return False
  return True

def show_word_with_colors():
  for i, attemp in enumerate(ATTEMPS):
    print("    ", end="")
    for j, letter in enumerate(attemp):
      if local_compare(letter, WORD[j]):
        print(green(letter), end="")
        continue
      
      letterIndex = WORD.find(letter)
      is_in_correct_position = letterIndex != -1 and WORD[letterIndex] == attemp[letterIndex]
      
      if letter in WORD and not is_in_correct_position:
        print(yellow(letter), end="")
        continue
      
      print(letter, end="")
    print("")

def fill_attemp(word): 
  auxiliar_word = []
  for i, letter in enumerate(word):
    auxiliar_word.append(letter)
  auxiliar_word = "".join(auxiliar_word)
  ATTEMPS.append(auxiliar_word.lower())


PLAYING = True
WORD = get_word()
HIDDEN_WORD = get_hidden_word(WORD)
MAX_ATTEMPS = 7
ATTEMPS = []
ATTEMP = 0

while PLAYING:
  show_interface()
  word = validate_word()
  
  fill_attemp(word)
  
  
  
  show_interface()
  is_finded = is_finded_word()
  ATTEMP += 1
  
  if is_finded:
    print("\nFelicitaciones, haz ganado...\n")
    PLAYING = False
    break
  
  if ATTEMP >= MAX_ATTEMPS:
    print("\n"""Fin del juego..., Se acabaron los intentos.")
    print(f"\nLa palabra era: {WORD}")
    PLAYING = False
    break
