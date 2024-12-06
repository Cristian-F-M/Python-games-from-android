class Menu:
  def __init__(self, menu: dict):
    self.__dict__.update(menu)
    
  def get_length(self):
    return len(self.__dict__.values())
  
    
class Menu_option:
  def __init__(self, option: dict):
    self.__dict__.update(option)


class Menus:
  def __init__(self, menus: dict):
    self.__dict__.update(menus)
