"""
Manim animation script for AGR-004-apsp-with-negatives

This script creates an animated visualization for the problem:
AGR-004-apsp-with-negatives

Topic: AdvancedGraphs
"""

from manim import *


class Agr004ApspWithNegativesScene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("AGR-004-apsp-with-negatives", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # TODO: Add animation implementation
        
        self.wait(2)
