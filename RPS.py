

import random

user_action = input('Enter a choice (rock, paper, scissor): ')
possible_actions = ['R','P','S']
computer_action = random.choice(possible_actions)
print(f"\nPlayer {user_action}: Computer ({computer_action})")

while True:
    if not user_action in possible_actions:
        print('User input is invalid')
        user_action = input('Enter a valid input (rock, paper, scissor): ')


    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie")
        user_action = input("It's a tie! Enter a choice (rock, paper, scissor): ")

    elif user_action == "R":
        if computer_action == "S":
            print('Rock smashes scissors! You win')
            
        else:
            print('Paper covers rock! You lose')
        break


    elif user_action == "P":
        if computer_action == "R":
            print('Paper covers rock! You win')
            
        else:
            print('Scissor cuts paper! You lose')
        break
    elif user_action == "S":
        if computer_action == "P":
            print('Scissor cuts paper! You win')
            
   
        else:
            print('Rock smashes scissors! You win')
            
        break


# In[5]:




# In[16]:





# In[17]:





# In[18]:





# In[19]:





# In[ ]:




