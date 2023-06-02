## research_track2_assignment_2 ##


# Description #

In the action_usr.py was working depends on to the inputs which are set by the user. User had to enter two integers to set x and y target positions and if the user had written ‘c’ then the target position had to be cancelled. For simulate the action_user.py node two slide widgets had been created to set the x and y target positions and two buttons had been created, purpose of the first button is after using the sliders to send and set the target positions. Purpose of the second button is to cancel the target goal. 

When user set a target position by using widgets and button, robot should start to move through the target. To visualize the robot movement one plot graph had been created by subscribing to the /odom topic. While robot moving user become able to see the robot movements on this graph. 

To know the nearest onbstacle to the robot, one button had been crated. While robot is moving if the user clik to the nearest obstacle button, he/she can learn where the nearest obstacle is. 

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


# How to use #

After opening the jupyter notebook, go to the terminal and command following lines in seperated terminals for running roscore and running the assignment. 

```bash
roscore
```

```bash
roslaunch assignment_2_2022 assignment_2.launch
```
And inside of the jupyter notebook, try to give a target x and y position by using widgets and the button, after that you can observe the movement of the robot on graph and also on Gazebo. If the user will clik to the nearest obstacle button, he/she can see the where the nearest obstacle is and if the user click to the plot button he/she can observe the number of the reached and cancelled targets. 

# Link to reach to the JupyterNotebook #

[http://0.0.0.0:8888/notebooks/assignment_2.ipynb](http://0.0.0.0:8888/notebooks/assignment_2.ipynb)
