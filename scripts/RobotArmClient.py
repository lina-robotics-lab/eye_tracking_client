#! /usr/bin/env python

import roslib
roslib.load_manifest('eye_tracking_client')
import rospy
import actionlib

from eye_tracking.msg import GoToAction, GoToGoal
from eye_tracking.srv import nbOfPosition

class RobotArmController():
    
    def __init__(self, resume=0):
        self.__currentIdx = resume
        self.__nbOfPosition = 1

        rospy.init_node('GoToClient')
        self.client = actionlib.SimpleActionClient('GoTo', GoToAction)
        self.client.wait_for_server()

        

        rospy.wait_for_service('nbOfPosition')
        try:
            getNPosition = rospy.ServiceProxy('nbOfPosition', nbOfPosition)
            resp1 = getNPosition()
            self.__nbOfPosition = resp1.nbOfPosition
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)
   
    
    def goto(self,idx):       
        if idx < self.__nbOfPosition and idx >= 0:
            goal = GoToGoal(idx)
            self.client.send_goal(goal)
            success = self.client.wait_for_result(rospy.Duration.from_sec(5.0))
            print('Result received, success:{}'.format(success))
            print('Number of positions:{}'.format(self.__nbOfPosition))
            
            self.__currentIdx = idx
            print(self.__currentIdx, file=open('LastPosition', 'w'))
            return True
        else:
            return False
    
    def position(self):
        return self.__currentIdx
    
    def nbPositions(self):
        # A topic subscription.
        return self.__nbOfPosition

if __name__ == '__main__':
    rc = RobotArmController()
    rc.goto(13)

    

    
