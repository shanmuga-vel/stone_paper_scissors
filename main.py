from random import randint
import sps
best_of = int(input("Best of: "))
your_score = 0
AI_score = 0
In_valide = 0
for i in range(best_of):
  your_choice = int(input("Whats do you choose? Typer: 0 for Stone🗿, 1 for Paper📄 or 2 for Scissors✂️ \n"))
  print("Your choice:")
  AI_choice = randint(0, 2)
  result = (your_choice, AI_choice)
  if your_choice == 0:
    print(sps.stone)
    print("AI choice:")
  elif your_choice == 1:
    print(sps.paper)
    print("AI chose:")
  elif your_choice == 2:
    print(sps.scissor)
    print("AI chose:")

  if your_choice <= 2:
    if AI_choice == 0:
      print(sps.stone)
    elif AI_choice == 1:
      print(sps.paper)
    else:
      print(sps.scissor)
    if result == (0, 1) or result == (1, 2) or result == (2, 0):
      print("You lose :-( this match")
      AI_score += 1
    elif result == (1, 0) or result == (2, 1) or result == (0, 2):
      print("You win! this match")
      your_score += 1
    else:
      print("It's a draw match")
  else:
    print(f"Wrong input. you have left {best_of - (i+1)} chance's: ")
    In_valide += 1

if your_score > AI_score:
  print(f"You won the tournement. Your score:{your_score} and AI score:{AI_score}")
elif your_score < AI_score:
  print(f"You have lost the tournement. AI score:{AI_score} and Your score:{your_score}")
elif In_valide == best_of:
  print(f"you have entered a wrong input for all the {best_of} match's. Game Over.")
else:
  print("It's a draw")
