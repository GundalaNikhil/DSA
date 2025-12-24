"""
Manim animation script for HEP-015-median-two-heaps-merge

This script creates an animated visualization for the problem:
HEP-015-median-two-heaps-merge

Topic: Heaps
"""

from manim import *


class Hep015MedianTwoHeapsMergeScene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("HEP-015-median-two-heaps-merge", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # TODO: Add animation implementation
        
        self.wait(2)
