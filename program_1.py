#Logan H's Random Dice

# 1) IMPORT the random module to let us generate random numbers
import random

# 2) DEF FUNCTION random dice roll as 2 random numbers between 1-6, then return both #'s
def randDice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

# 3) ADD the 2 #'s to total
total_sum = 0
num_rolls = 100

# 4) RERUN, until the number of times we rolled the dice is equal to number of rolls
#    (number of rolls = (num_rolls = 100))
for _ in range(num_rolls):
    total_sum += randDice()

# 5) AVERAGE by dividing the sum total of the dice rolls and the number of rolls (100)
average = total_sum / num_rolls
# 6) PRINT the average and round to 2 decimal places.
print("Average roll:", round(average, 2))
