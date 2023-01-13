import os

def home_screen():
  print("=========================================")
  print("---------------WELCOME!------------------")
  print("=========================================")


def screen_options():
  print("-Press [1] to register product.")
  print("-Press [2] to buy.")


def screen_register():
  print("Inform the name and value of product separated by comma:")
  name_value = input("> ")
  return name_value


def screen_buy():
  print("Inform the name and amount of product separated by comma:")
  name_amount = input("> ")
  return name_amount
  
  
def screen_itens():
  with open("data.txt", 'r') as data:
   dt = data.read()

  dt = dt.split('\n')
  dt.pop() # remove ''
  #print(dt)
  
  dt2 = []
  for d in dt:
    d = d.split(',')
    dt2.append(tuple(d))
    #print(d)

  print(dt2)
  return dt2


def screen_clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  

def register_product(product):
  with open("data.txt", 'a') as data:
   data.write(product+"\n")
  print("product registred!")
    
def buy(products, itens):
  total=0 
  for i in itens:
    for p in products:
      if (i[0].lower()==p[0].lower()):
        total+=int(i[1])*float(p[1])
        break

  return f"TOTAL: R${total}"
#----------------------------------------------#
home_screen()

while True:
  screen_options()
  option = input()
  
  if (option == '1'):
    register_product(screen_register())
    
    while True:
      more = input("\nRegister other? (s/n): ")
      if(more == 's'):
        register_product(screen_register())
      elif (more == 'n'):
        screen_clear()#insert clear
        break
  
  elif (option == '2'):
    products = screen_itens()

    itens = []
    itens.append(tuple(screen_buy().split(',')))
    while True:
      more = input("\nBuy other? (s/n): ")
      if(more == 's'):
        itens.append(tuple(screen_buy().split(',')))
      elif (more == 'n'):
        screen_clear()#insert clear
        print(itens)
        print(buy(products, itens))
        break

      
  else:
    break
