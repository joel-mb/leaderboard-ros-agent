cmake_minimum_required(VERSION 2.8.3)
project(dummy_agent)

# Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  rospy
  carla_msgs
)

catkin_python_setup()

catkin_package()

include_directories(${catkin_INCLUDE_DIRS})

install(PROGRAMS src/dummy_agent/dummy_agent.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY launch/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch)
