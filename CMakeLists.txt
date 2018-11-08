cmake_minimum_required(VERSION 2.8.3)
project(battery_nh2054)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)


## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   Battery.msg
 )


## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )

catkin_package(
  #INCLUDE_DIRS include
#  LIBRARIES battery_nh2054
  CATKIN_DEPENDS rospy std_msgs message_runtime
#  DEPENDS system_lib
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


