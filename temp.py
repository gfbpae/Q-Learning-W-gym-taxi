import gym 
import numpy as np
import random 
import matplotlib.pyplot as plt


"Initializing Taxi taxi_map"
taxi_map = gym.make("Taxi-v3").env


"Learning Rate"
alpha_values = np.linspace(0.01, 0.9 ,10)
"after a parameter sweep we get this epsilon value"
alpha = 0.5

"Discount Rate"
gamma = 0.9

"Explore Rate"
epsilon_values = np.linspace(0.1, 0.9,9)
"after a parameter sweep we get this epsilon value"
epsilon = 0.2

"Reward List to hold obtained reward values for each episode"
reward_lists = []
"Dropout List to hold obtained dropout values for each episode"
dropouts_lists = []

for alpha in alpha_values:
    
    """
        Initializing Q_Table for whole possible state and action cases
        taxi_map.observation_space and taxi_map.action_space gives a Discrete(int)
        so we use these with .n then we get just int
    """
    q_table = np.zeros([taxi_map.observation_space.n,taxi_map.action_space.n])
    alpha_iter = 0
    "Iteration"
    
    reward_list = []
    dropouts_list = []
    episode_number = 1000
    for i in range (1,episode_number):
        
        """
            Inıtializing first state
            We want to get just state value so we use [0]
        """
        state = taxi_map.reset()[0]
        
        reward_count = 0 
        dropouts = 0
        
        while True:
            
            """
                Exploration-Exploitation Choice
                if random value is under our epsilon value then we choose the explore
                and we take a random action
                else we choose the exploit and we take a highest value action
            """
            if random.uniform(0, 1) < epsilon:
                action = taxi_map.action_space.sample()
            
            else:
                action = np.argmax(q_table[state])
            
            """
                taxi_map.step(action)=observation step,reward,terminated,truncated,info
                we do not want to use last 2 object so we use underline "_" for them
            """
            next_state, reward, done , _ , _ = taxi_map.step(action)
            
            "Saving current value for state and action"
            old_value = q_table[state,action]
            
            "Getting possible maximum value of next step in range of all action"
            next_max = np.max(q_table[next_state])
            
            "Calculating current value"
            next_value = (1-alpha)*old_value + alpha*(reward + gamma*next_max)
            
            "Saving current value"
            q_table[state,action] = next_value
            
            "Move on to the next step"
            state = next_state
            
            "Counting the wrong dropouts"
            if reward == -10:
                dropouts +=1 
            
            "Checking if it is complete"
            if done:
                break
            
            "summation of steps' reward"
            reward_count += reward
            
            
        if i%10== 0:
            dropouts_list.append(dropouts)
            reward_list.append(reward_count)
            print("Episode {} , Reward {} , Dropouts {}".format(i, reward_count, dropouts))
            
    reward_lists.append(reward_list)
    dropouts_lists.append(dropouts_list)

# col = 1
# for rewards in reward_lists:
#     plt.subplot(2,int(reward_lists.__len__()/2),col)
#     plt.plot(rewards)
#     plt.xlabel('for : {}'.format(alpha_values[col-1]))
#     plt.legend()
#     plt.show()
#     col += 1
    
plt.plot(reward_list)
plt.xlabel('Episodes')
plt.ylabel('Count')
plt.legend()
plt.show()
