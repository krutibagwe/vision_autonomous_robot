from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_path = get_package_share_directory('robot_description')
    urdf_file = os.path.join(pkg_path, 'urdf', 'robot.urdf')

    gazebo = ExecuteProcess(
    cmd=[
        'gazebo',
        '--verbose',
        '-s', 'libgazebo_ros_factory.so'
    ],
    output='screen'
)

    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'vision_robot',
            '-file', urdf_file
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_robot
    ])