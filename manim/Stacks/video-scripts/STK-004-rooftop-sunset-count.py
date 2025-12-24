"""
Manim animation script for STK-004-rooftop-sunset-count

This script creates an animated visualization for the problem:
STK-004-rooftop-sunset-count

Topic: Stacks
"""

from manim import *


class Stk004RooftopSunsetCountScene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("STK-004-rooftop-sunset-count", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # TODO: Add animation implementation
        
        self.wait(2)
