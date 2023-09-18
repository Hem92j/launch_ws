from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    sen_pub = Node(
        package="simple_launch",
        executable= "sensor_data_pub",
    )

    robot_sub = Node(
        package="simple_launch",
        executable= "robot_listener",
        name = "my_robot_listener",
    )

    return LaunchDescription([
        sen_pub,
        robot_sub
    ])