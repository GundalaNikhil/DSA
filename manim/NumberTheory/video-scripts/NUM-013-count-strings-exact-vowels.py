"""
Manim animation script for NUM-013-count-strings-exact-vowels

This script creates an animated visualization for the problem:
NUM-013-count-strings-exact-vowels

Topic: NumberTheory
"""

from manim import *


class Num013CountStringsExactVowelsScene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("NUM-013-count-strings-exact-vowels", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # TODO: Add animation implementation
        
        self.wait(2)
