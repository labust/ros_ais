from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Define launch arguments
    serial_port_arg = DeclareLaunchArgument(
        'serial_port',
        default_value='/dev/ais_garmin',
        description='Target port name.'
    )

    frame_id_arg = DeclareLaunchArgument(
        'frame_id',
        default_value='ais_link',
        description='Target frame name.'
    )

    # Create the node with parameters using the declared launch arguments
    ais_node = Node(
        package='ros2_ais',
        executable='ros_daisy_node.py',  # Ensure this matches the executable in your package
        name='AIS_node',
        namespace='sensor_mount',
        output='screen',
        respawn=True,
        parameters=[
            {'serial_port': LaunchConfiguration('serial_port')},
            {'frame_id': LaunchConfiguration('frame_id')},
            {'frequency': 10},
            {'baudrate': 115200}
        ]
    )

    # Return the LaunchDescription with the declared arguments and the node
    return LaunchDescription([
        serial_port_arg,
        frame_id_arg,
        ais_node
    ])
