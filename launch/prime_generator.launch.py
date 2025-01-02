# SPDX-FileCopyrightText: 2025 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause

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
