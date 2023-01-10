# eye_tracking_client
This is the client Python repository for automatic eye tracking acquisition using a robotic arm. It works together with the eye_tracking_server package(https://github.com/lina-robotics-lab/eye_tracking_server) to allow automatic robot arm movement for the eye tracking.

To use the client, first install the eye_tracking_server package(see documentations for https://github.com/lina-robotics-lab/eye_tracking_server), and ensure the server is running by 
```bash
$ Source the ROS workspace
$ roscore
$ Bringup the robot and start the MoveIt! control interface.
$ rosrun eye_tracking_server RobotArmServer.py
```
Then, in your own code, use the client class as follows.

```python
from RobotArmClient import RobotArmController

controller = RobotArmController()

waypoint_idx = 20
controller.goto(waypoint_idx). # This sends a request to the server to move the robot arm to the 20th waypoint. 

# The goto(idx) function will want until the server has sent back a result before moving on to the next line of code.
```
