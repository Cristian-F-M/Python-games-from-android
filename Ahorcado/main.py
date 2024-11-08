import os
import requests
import random

def get_word():
  words = ['Lunes', 'Gato', 'Zapato', "Conejo", "Silla"]
  try:
    res = requests.get('https://clientes.api.greenborn.com.ar/public-random-word?c=aders": {
        "Content-Type": "application/json"
      }
    })
    data = res.json()
    return data[0]
  except Exception as e:
    randomIndex = random.randint(0, len(words) - 1)
    return words[randomIndex]

def get_hide_word(word):
  hide_word = []
  for l in word:
    hide_word.append("_")
  return hide_word
  
def clear_terminal():
  os.system('clear')

def validate_letter():
  error = False
  while True:
    if error:
      show_interface()
      print("Caracter no valido:")
      
    letter = input(f"Ingrese una letra {'nuevamente' if error else ''}: ")
    try:
      int(letter)
      error = True 
      continue
    except:
      pass
    
    if (isinstance(letter, str) and len(letter) == 1):
      return (True, letter)
    error = True
    continue

def show_interface():
  clear_terminal()
  print()
  print(f"💚 x{VIDAS}")
  print("\n")
  print("  ", end='')
  for i, letter in enumerate(HIDE_WORD):
    print(letter, end="")
  print("\n")
 
def get_cant_hide_letters():
  count = 0
  for letter in HIDE_WORD:
    if letter == '_':
      count += 1
  return count

WORD = get_word()
HIDE_WORD = get_hide_word(WORD)


PLAYING = True
VIDAS = 7
error = False
textError = None


while PLAYING:
  show_interface()
  if error and textError is not None:
    print(textError)
  (_, letter) = validate_letter()
  
  is_found = False
  for i, l in enumerate(WORD):
    if letter.lower() == l.lower():
      error = False
      textError = None
      
      if HIDE_WORD[i] != '_':
        error = True
        textError = "Esta letra ya está."
      
      is_found = True
      HIDE_WORD[i] = l

  if not is_found:
    VIDAS -= 1

  if VIDAS <= 0:
    show_interface()
    print(f"Fin del juego, la palabra es: {''.join(WORD)}")
    PLAYING = False
    break

  if get_cant_hide_letters() <= 0:
    show_interface()
    print("FELICIDADES, haz ganado...")
    PLAYING = False
    break



print("\n")
