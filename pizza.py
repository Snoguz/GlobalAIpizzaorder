import csv
import datetime 

# pizza üst sinifi:

class Pizza:
  def get_description(self):
    return self_class.name

  def get_cost(self):
    return self_class.cost
    
    
 # Musterilerin secebilecegi pizza alt siniflari

 class KlasikPizza(Pizza):
   cost = 45

   def _init_(self):
     self.description = "\n Klasik pizza: Sucuk,sosis,mısır,domates sosu,kasar ve zeytin"
     print(self.description)


class MargheritaPizza(Pizza):
  cost = 50

  def _init_(self):
    self.description = "\n Margherita pizza: Mozarella,domates feslegen ve zeytınyag"
    print(self.description)


class TürkPizzası(Pizza):
  cost = 65

  def _init_(self):
    self.description = "\n Türk pizzası: Kıyma,kasar,kekik ve kurutulmus domates"
    print(self.description)

class MixPizza(Pizza):
  cost = 55

  def _init_(self):
    self.description = "\n Mix pizza: Kasar,sucuk,salam,domates,biber,zeytin,mantar ve mısır"
    print(self.description)
    
    
 # Pizza sinifinin ozelliklerini tasiyan decorator sinifi:

class Decorator(Pizza):
  def _init_(self,extra_malzeme):
    super(). _init_()
    self.component = ing

  def get_cost(self):
    return self.component.get_cost() + \
    Pizza.get_cost(self)

  def get_description(self):
    return self.component.get-description() + \
    ';' + Pizza.get_description(self)
    
    
   # decorator classı icinde olan malzemelerin subclassları oluşturalım.

class Zeytin(Decorator):
  cost = 3

  def _init_(self,extra_malzeme):
    super(). _init_(extra_malzeme)


class Mantar(Decorator):
  cost = 4

  def _init_(self,extra_malzeme):
    super()._init_(extra_malzeme)

class KeciPeyniri(Decorator):
  cost = 7

  def _init_(self,extra_malzeme):
    super(). _init_(extra_malzeme)

class Et(Decorator):
  cost = 9

  def _init_(self,extra_malzeme):
    super()._init_(extra_malzeme)

class Sogan(Decorator):
  cost = 5

  def _init_(self,extra_malzeme):
    super(). _init_(extra_malzeme)

class Mısır(Decorator):
  cost = 4

  def _init_(self,extra_malzeme):
    super(). _init_(extra_malzeme)
    
    
def create_order():
    with open("Menu.txt","r",encoding="utf-8") as f:
        menu=f.read()
        print(menu)


pizza_choice = int(input("Please select a pizza  : "))
if pizza_choice == 1:
  Pizza = KlasikPizza("Klasik Pizza", 45)
  if pizza_choice == 2:
    Pizza = MargheritaPizza("Margherita Pizza", 50)
  elif pizza_choice == 3:
    Pizza = MixPizza("Mix Pizza", 55)
  elif pizza_choice == 3:
    Pizza = TurkPizzası("Turk Pizzası", 65)
  else:
    print("Gecersiz secim.")
      



extra_list = []
extra_choice = input("Please choose your extra : (q for quit )")
if extra_choice == 'q':
           break
  elif extra_choice == '11':
      extra = Zeytin("Zeytin",3)
      extra_list.append(extra)
  elif extra_choice == '12':
            extra = Mantar("Mantar",4)
            extra_list.append(extra)
  elif extra_choice == '13':
            extra = KeciPeyniri("KeciPeyniri",7)
            extra_list.append(extra)
  elif extra_choice == '14':
            extra = Et("Et",9)
            extra_list.append(extra)
  elif extra_choice == '15':
            extra = Sogan("Sogan",5)
            extra_list.append(extra)
  elif extra_choice == '16':
            extra = Misir("Misir",4)
            extra_list.append(extra)
  else:
            print("Gecersiz secim.")
            
# Musterinin bilgilerini kaydediyoruz.
print("Lutfen istenilen bilgileri giriniz.")
name = input("isminiz: ")
surname = input("Soyadınız: ")
phone_number = input("Telefon numaranız: ")
identity_number = input("T.C. kimlik numaranız: ")
cart_number = input("Kredi kartı numaranız: ")
cart_pass = input("Kredi kartı sifreniz: ")
addres = input("Adres bilgileriniz: ")
time = datetime.datetime.now()

with open('Orders_Datas.csv', 'a') as orders:
  orders = csv.writer(orders, delimiter=',')
  order.writerow([name, surname, phone_number, identity_number, cart_number, cart_pass, addres, time, order.get_description, order.get_cost])
  print("Siparisiniz onaylanmıstır.Tesekkür ederiz.")
