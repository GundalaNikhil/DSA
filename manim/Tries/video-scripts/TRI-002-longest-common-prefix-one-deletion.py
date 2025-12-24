"""
Manim animation script for TRI-002-longest-common-prefix-one-deletion

This script creates an animated visualization for the problem:
TRI-002-longest-common-prefix-one-deletion

Topic: Tries
"""

from manim import *


class Tri002LongestCommonPrefixOneDeletionScene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("TRI-002-longest-common-prefix-one-deletion", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # TODO: Add animation implementation
        
        self.wait(2)
