"""
Manim animation script for STC-012-diff-substrings-two-strings

This script creates an animated visualization for the problem:
STC-012-diff-substrings-two-strings

Topic: StringsClassic
"""

from manim import *


class Stc012DiffSubstringsTwoStringsScene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("STC-012-diff-substrings-two-strings", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # TODO: Add animation implementation
        
        self.wait(2)
