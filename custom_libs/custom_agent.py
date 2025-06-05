# Copyright (c) # Copyright (c) 2018-2020 CVC.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.


""" This module implements an agent that roams around a track following random
waypoints and avoiding other vehicles. The agent also responds to traffic lights,
traffic signs, and has different possible configurations. """

import random
import numpy as np
import carla
from agents.navigation.behavior_agent import BehaviorAgent
from agents.navigation.local_planner import RoadOption
from agents.navigation.behavior_types import Cautious, Aggressive, Normal

from agents.tools.misc import get_speed, positive, is_within_distance, compute_distance

class CustomAgent(BehaviorAgent):
    def __init__(self, vehicle, behavior='normal', speed_limit=42):
        super().__init__(vehicle, behavior)
        self.custom_speed_limit = speed_limit  # m/s

    def _update_information(self):
        # print("CustomAgent: _update_information")
        # Update the speed limit and local planner settings to avoid relying on map data
        super()._update_information()
        self._speed_limit = self.custom_speed_limit
        self._local_planner.set_speed(self.custom_speed_limit)
        self._look_ahead_steps = int((self.custom_speed_limit) / 10)

    def done(self):
        # Check if the agent has reached its destination or if it is close to the end of the route to avoid deadlocks
        return len(self._local_planner._waypoints_queue) <= 1