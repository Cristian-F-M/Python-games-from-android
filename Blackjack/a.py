CARD_COLS = 15
CANT_DOTS = 3

def get_text_better(text, index):
  max_length_text = CARD_COLS - 2 - 6
  length_text = len(text)
  new_text = ""

  if length_text > max_length_text:
    for i, l in enumerate(text):
      if i < max_length_text:
        new_text += l
        continue
    
      if i < max_length_text + CANT_DOTS:
        new_text += "."
        continue
    
  length_text = len(new_text)
    
  text = text if new_text == "" else new_text
  new_text = ""
  for i, l in enumerate(text):
    if i == -1:
      continue
    l = "_" if i > index else l
    new_text += l
  return new_text.upper()
  
text = "Hola" 
for i, l in enumerate(text):
  print(get_text_better(text, i))