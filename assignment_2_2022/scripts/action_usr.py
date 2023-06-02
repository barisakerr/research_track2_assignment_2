#! /usr/bin/env python

"""
.. module: action_usr
	:platform unix
	:synopsis: Python module for controlling the turtlesim

.. moduleauthor:: Baris Aker

ROS node to publish the position and the velocity values of the robot by creating a custom message.

This module is created for controlling a robot using a ROS node. It subscribes to the "odom" topic to gather details about the robot's position and speed, and then shares this information on the /posxy_velxy topic. Additionally, it implements an action client which called as reaching_goal to interact with the user, allowing them to input a target position or cancel the current goal. The module sends the goal to the action server and waits for a response.

Subscribes to:
	/odom

Publishes to:
	/posxy_velxy
	
Client:
	/reaching_goal


"""


import rospy
import actionlib
import actionlib.msg
import assignment_2_2022.msg
from std_srvs.srv import *
import sys
import select
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Twist
from assignment_2_2022.msg import Posxy_velxy
from colorama import Fore, Style
from colorama import init
init()
 
# callback function for the subscriber
def publisher(msg):
   
    """
        
    This function, gets the position data from msg, gets the pose data for position and twist data for the velocity from the msg, cretaing custom message, assigins position on x and y axis and velociy on x and y axis to the custom message and publishs the custom message which is posxy_velxy
       
    """
    global pub
    position = msg.pose.pose.position # getting the position data from the msg
    velocity = msg.twist.twist.linear # getting the twist data from the msg
    # create custom message
    posxy_velxy = Posxy_velxy()
    # assign the parameters of the custom message
    posxy_velxy.msg_pos_x = position.x
    posxy_velxy.msg_pos_y = position.y
    posxy_velxy.msg_vel_x = velocity.x
    posxy_velxy.msg_vel_y = velocity.y
    # publish the custom message
    pub.publish(posxy_velxy)

def action_client():
    """
    This function creates the action client and waitingfor the server to be started 
       
    """

    # create the action client
    action_client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2022.msg.PlanningAction)
    # wait for the server to be started
    action_client.wait_for_server()
    
    status_goal = False
	
    while not rospy.is_shutdown():
        print(Fore.BLACK + "Please enter the position values of the target or write c to stop the process ") #printing the command to inform the user about the purpose with Black color
        x_position_input = input(Fore.BLUE + "X position of the target: ") #printing the 'X position of target' with the Bue color to take the info from the user
        y_position_input = input(Fore.BLUE + "Y position of the target: ") #printing the 'Y position of target' with the Blue color to take the info from the user
        
        if x_position_input == "c" or y_position_input == "c": # when the user enters a 'c' input then the robot will stops and goal cancelling 
            # Cancel the goal
            action_client.cancel_goal()
            status_goal = False
        else:
           
            x_position_send = float(x_position_input) # x position number is converting from string to float 
            y_position_send = float(y_position_input) # y position number is converting from string to float 
            
            goal = assignment_2_2022.msg.PlanningGoal()
            goal.target_pose.pose.position.x = x_position_send # the converted x position is become a goal x position to send to the server 
            goal.target_pose.pose.position.y = y_position_send # the converted y position is become a goal x position to send to the server 
					
            # Send the goal to the action server
            action_client.send_goal(goal) # sending the goal to the action 
            status_goal = True


def main():
    # initialize the node
    rospy.init_node('action_usr')
    # global publisher
    global pub
    # publisher: send a message which contains two parameters (velocity and position)
    pub = rospy.Publisher("/posxy_velxy", Posxy_velxy, queue_size = 1)
    # subscriber: get from "Odom" two parameters (velocity and position)
    sub_from_Odom = rospy.Subscriber("/odom", Odometry, publisher)
    # call the function client
    action_client()

if __name__ == '__main__':
    main()

