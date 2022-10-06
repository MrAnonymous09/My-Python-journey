import random

def get_choices():
  player_choice = input("Enter Your choice (rock, paper,scissors): ")
  options = ["rock","paper","scissors"]
  computer_choice = random.choice(options)
  
  
  choices = {"player": player_choice,"computer": computer_choice}
  return choices

def check_win(player,computer):
  print(f"Your choice: {player}, Computer choice: {computer}")
  
  if player == computer:
    return "Its Tie!"
  elif (player == "stone" and computer=="scissors") or (player=="scissors" and computer=="paper") or (player=="paper" and computer=="stone"):
    return "You Won!!!" 
  else:
    return "You Lost!!!"


choices=get_choices()
result= check_win(choices["player"],choices["computer"])
print(result)
  


