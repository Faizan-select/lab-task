#!/usr/bin/env python
# coding: utf-8

# In[7]:


class MultiReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature 
        self.previous_action  = None

    def perceive(self, current_temperature):
        return current_temperature

    def act(self, current_temperature):
        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        else:
            action = "Turn off heater"
        if action == self.previous_action:
            return f"no action needed, heater is already {self.previous_action.split()[1]}"
        
        self.previous_action = action
        return action

# simulating different rooms with different current temperatures
rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

# desired temperature for all rooms
desired_temperature = 22
agent = MultiReflexAgent(desired_temperature)

# run the agent for each room
for room, temperature in rooms.items():
    print(f"\nRoom: {room}, Current temperature: {temperature}°C")
    
    action = agent.act(temperature)
    print(f"Action: {action}")
  


# In[ ]:




