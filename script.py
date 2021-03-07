from stack import Stack
import random
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Create new CSV file for each run instance and write header record. CSV will later be used to create Pandas module Dataframe object.
filename = "TowersOfHanoi_" + str(datetime.datetime.now()) + ".csv"
filename = filename.replace(":",".")
f = open(filename, "a")
f.write("Header " + "Start Time: " + str(datetime.datetime.now()) + "\n")

#Enter number of disks
num_disks = 3 


num_optimal_moves = (2**num_disks)-1
print("The fastest you can solve this game is in", num_optimal_moves)

        
#Play the Game
def play_game():
  #Store function start time for later use
  startTime= datetime.datetime.now()
  
  #(Re)-initilize stack setup for every play_game function call
  left_stack= Stack("Left")
  middle_stack= Stack("Middle")
  right_stack= Stack("Right")
  stacks= [left_stack,middle_stack,right_stack]
  for i in range(num_disks, 0, -1):
    left_stack.push(i)

  #Initialize number of use moves to zero
  num_user_moves = 0
  
  # Execute until num_user_moves is returned
  while True:
    
    #Prompt system for source and destination stacks
    src_stack_index= random.randint(0,2)
    dest_stack_index= random.randint(0,2)
    
    # Increments whether passes valid move condition or not
    num_user_moves += 1 
    if (stacks[dest_stack_index].peek() == None and stacks[src_stack_index].peek()!= None) or (stacks[src_stack_index].peek()!= None and stacks[dest_stack_index].peek()!= None and (stacks[dest_stack_index].peek() > stacks[src_stack_index].peek())) :
      stacks[dest_stack_index].push(stacks[src_stack_index].pop())
      for stack in stacks:
        stack.print_items()
      if stacks[2].get_size() == num_disks:
        endTime= datetime.datetime.now()
        deltaTime = str(int((endTime - startTime).total_seconds() * 1000)) #convert time delta to milliseconds
        print("We have a WINNER!, it took # moves:", num_user_moves, "in", deltaTime )
        f.write(str(num_user_moves) + ',' + deltaTime + "\n")
        return num_user_moves
    else:
      print("Invalid move, try again.")
      for stack in stacks:
        stack.print_items()

#Enter how many times to play game
num_user_moves_cumulative_sum = 0
for i in range(10):
  num_user_moves_cumulative_sum += play_game()
f.write("Trailer " + str(num_user_moves_cumulative_sum) + " total move over " + str(i+1) + " runs. " + "End time: " + str(datetime.datetime.now()))  
f.close()

#Import csv file using Pandas library and create Dataframe object (ignoring header and trailer records)
df = pd.read_csv(filename, names= ['# of moves','Time elapsed (ms)'], skiprows=1, skipfooter= 1, engine='python')

#Define linear regression using numpy library and insert into dataframe object
d = np.polyfit(df['# of moves'],df['Time elapsed (ms)'],1)
fpoly1d= np.poly1d(d)
df.insert(0,'Linear regression', fpoly1d(df['# of moves']))

#Print entire Dataframe object
print(df.to_string())

#Create scatterplot as subplot (ax), and plot linear regression 
ax = df.plot(kind = 'scatter', x = '# of moves', y='Time elapsed (ms)')
df.plot(x='# of moves', y='Linear regression',color='Red',ax=ax)

#Display diagram
plt.show()


  
  
