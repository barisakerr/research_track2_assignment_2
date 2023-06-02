#! /usr/bin/env python


"""
.. module: service_goal
	:platform unix
	:synopsis: Python module for controlling the turtlesim

.. moduleauthor:: Baris Aker

ROS node for print the number of reached goals and number of cancelled goals.

Subscribes to:
	/reaching_goal/result
	
Nodes:
	service_goal




"""

import rospy # Import the ROS python library
from assignment_2_2022.srv import goal_rc, goal_rcResponse # Import the service and service response messages
import actionlib   # Import the actionlib library
import actionlib.msg  # Import the actionlib message library
import assignment_2_2022.msg  # Import the package message library

class Service:
    """
    
    Service class includes __init__(self), result_callback functions and data. 
    
    
       Callback function to set the actual robot's velocity
       
    """
    def __init__(self):
        """
        
        This function initialize the counters for golas reached and cancelled
       
        """
    
        # Initialize the counters for goals reached and cancelled
        self.cancelled_goal = 0
        self.reached_goal   = 0

        # Create the service
        self.srv = rospy.Service('goal_service', goal_rc, self.data)

        # Subscribe to the result topic
        self.sub_result = rospy.Subscriber('/reaching_goal/result', assignment_2_2022.msg.PlanningActionResult, self.result_callback)

    def result_callback(self, msg):
        """
        
        This function gets the status from the message and determine the goals reached or cancelled depends on to the status
       
        """
        # Get the status of the result from the msg
        status = msg.status.status

        # Goal cancelled (status = 2)
        if status == 2:
            self.cancelled_goal += 1

        # Goal reached (status = 3)
        elif status == 3:
            self.reached_goal += 1
    
    def data(self, req):
    
    
        # Return the response containing the current values of goal_cancelled and goal_reached
        return goal_rcResponse(self.reached_goal, self.cancelled_goal)

def main():

    # Initialize the node
    rospy.init_node('service_goal')
    
    # Create an instance of the Service class
    service_goal = Service()
    
    # Wait for messages
    rospy.spin()

if __name__ == "__main__":
    main()

