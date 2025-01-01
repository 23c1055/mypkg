import launch
import launch.actions
import launch.substitution
import launch_ros.actions


def generate_launch_description():

    prime = launch_ros.actions.Node(
        package='mypkg',
        executable='prime',
        output='screen'
        )
        
    return launch.LaunchDescription([prime])
