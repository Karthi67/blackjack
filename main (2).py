from art import logo
import random
print(logo)
n=0
m=0
def player():
  a=["A","J","K",2,3,4,5,6,7,8,9]
  b=random.randint(0,2)
  c=random.randint(2,10)
  print(f"YOU ={a[b]} {c}")
  if a[b]=="A":
    return 11+c
  elif a[b]=="J" or  a[b]=="k" :
    return 10+c
  
def computer():
  a=["A","J","K",2,3,4,5,6,7,8,9]
  b=random.randint(0,2)
  c=random.randint(2,10)
  print(f"compuert choice={a[b]} {str(c).replace(str(c), 'X')}")
  e=input("do You want to take a card?")
  if a[b]=="A" and e=="yes":
    return 11+c
  elif (a[b]=="J" or a[b]=="K") and e=="yes":
    return 10+c
  elif e=="no":
    return 0+c
def game():
  global n,m
  player_result = player()
  computer_result = computer()
  n+=player_result
  m+=computer_result
  print(f"your score is {n} and computer score is {m}")
  if n > m or computer_result>=21:
    print("WIN")
  elif n < m or player_result>=21:
    print("Loss")
  else:
    print("Draw")
  cont=input("DO u wnt to Continue")
  while cont=="yes":
    game()
  else:
    print("thankyou")
    return()
game()