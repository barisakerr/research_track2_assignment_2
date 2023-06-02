## research_track2_assignment_2 ##


# Description #

In the action_usr.py was working depends on to the inputs which are set by the user. User had to enter two integers to set x and y target positions and if the user had written ‘c’ then the target position had to be cancelled. For simulate the action_user.py node two slide widgets had been created to set the x and y target positions and two buttons had been created, purpose of the first button is after using the sliders to send and set the target positions. Purpose of the second button is to cancel the target goal. 

When user set a target position by using widgets and button, robot should start to move through the target. To visualize the robot movement one plot graph had been created by subscribing to the /odom topic. While robot moving user become able to see the robot movements on this graph. 

To observe the reached and unreached goals, one another graph had been created. When the robot reaches to a target it counts and graph shows how many times robot reached to the goal. Same behavior for the cancelling goal, when user click to the cancel goal button, velocity of the robot become zero suddenly and, in the graph, canceled goal increase. The total section on the graph shows the number of the reached and the cancelled target positions as a total. 

# Installing Jupyter Notebook #

```bash
pip3 install jupyter bqplot pyyaml ipywidgets
```

```bash
jupyter nbextension enable --py widgetsnbextension
```

```bash
jupyter notebook --allow-root
```

# How to run  #

```bash
jupyter notebook --allow-root --ip 0.0.0.0
```
And click to the assignment_2.ipynb


