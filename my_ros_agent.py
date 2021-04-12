"""
This module provides a leaderboard agent for ros_bridge's carla_ad_agent
"""

from leaderboard.autoagents.ros1_agent import ROS1Agent
from leaderboard.autoagents.autonomous_agent import Track

def get_entry_point():
    return "MyROSAgent"

class MyROSAgent(ROS1Agent):

    """
    Minimal Stack Agent
    """

    def setup(self, path_to_conf_file):
        self.track = Track.MAP

    def sensors(self):  # pylint: disable=no-self-use
        """
        Define the sensor suite required by the agent
        """
        return [
            {
                'type': 'sensor.camera.rgb', 
                'x': 0.7, 'y': -0.4, 'z': 1.60, 'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,
                'width': 300, 'height': 200, 'fov': 100,
                'id': 'main_rgb_camera'
            },
            {
                'type': 'sensor.lidar.ray_cast', 
                'x': 0.0, 'y': 0.0, 'z': 2.50, 'yaw': 0.0, 'pitch': 0.0, 'roll': 0.0,
                'id': 'lidar'
            },
            {
                'type': 'sensor.speedometer',
                'id': 'speed'
            },
            {
                'type': 'sensor.other.gnss',
                'x': 0.0, 'y': 0.0, 'z': 0.0, 
                'id': 'gnss'
            },
            {
                'type': 'sensor.opendrive_map',
                'id': 'map',
                'reading_frequency': 1
            }
        ]

    def get_ros_entrypoint(self):
        return {
            "package": "dummy_agent",
            "launch_file": "dummy_agent.launch"
        }
