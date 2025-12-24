"""
Manim animation script for STC-010-lcp-two-suffixes

This script creates an animated visualization for the problem:
STC-010-lcp-two-suffixes

Topic: StringsClassic
"""

from manim import *


class Stc010LcpTwoSuffixesScene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("STC-010-lcp-two-suffixes", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # TODO: Add animation implementation
        
        self.wait(2)
