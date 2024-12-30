#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Goto Shingo
# SPDX-License-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitution
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='talker',
        )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
        )

    return launch.LaunchDescription([talker, listener])
