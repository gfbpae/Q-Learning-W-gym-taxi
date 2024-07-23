# Q-Learning-W-gym-taxi

The Gym Taxi environment, provided by OpenAI Gym, is a simulation that takes place on a 5x5 grid. This grid includes the following elements:

Taxi: The taxi starts at a specific location and moves around to pick up and drop off passengers.
Passenger: The passenger is located at a random position on the grid and needs to be transported to a different, random location.
Stops: These are represented by the letters R, G, Y, and B on the grid:
R (Red): pickup and drop-off points.
G (Green): pickup and drop-off point.
Y (Yellow): pickup and drop-off point.
B (Blue): pickup and drop-off point.

```
+---------+
|R: | : :G|
| : | : : |
| : : : : |
| | : | : |
|Y| : |B: |
+---------+
```

# Objective
The objective of the Gym Taxi application is to move the taxi to the passenger's location, pick up the passenger, and then drop them off at the specified destination point, which is one of the stops (R, G, Y, or B). The goal is to complete this task in the shortest possible time and with the fewest errors.

# Parameter Sweep for Epsilon 
![epsilon](https://github.com/user-attachments/assets/5730c9b6-176a-4ed6-bde1-4830ebe7d47a)
We take our epsilon value as 0.2 because when we look at the graphic result, 0.2 is the value that provides the fastest learning and works stably.

# Parameter Sweep for Alpha
![alpha](https://github.com/user-attachments/assets/4cb3a063-e43f-41bd-bc29-e1a4851b7146)
While our epsilon value is 0.2, when we apply a parameter sweep to our alpha value, we decide that the most appropriate alpha value is 0.5.

# Result 
![sonuc](https://github.com/user-attachments/assets/f22541d8-3eb9-43e6-90a1-547b955ca2ea)
While our epsilon value is 0.2 and alpha value is 0.5, we can observe that our system works stably and learn fast in our experiments.




