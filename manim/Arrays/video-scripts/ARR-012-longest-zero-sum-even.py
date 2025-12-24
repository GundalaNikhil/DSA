"""
Manim animation script for ARR-012-longest-zero-sum-even

This script creates an animated visualization for the problem:
ARR-012-longest-zero-sum-even

Topic: Arrays
"""

from manim import *


class Arr012LongestZeroSumEvenScene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("ARR-012-longest-zero-sum-even", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # TODO: Add animation implementation
        
        self.wait(2)
