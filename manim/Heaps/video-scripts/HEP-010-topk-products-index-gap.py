"""
Manim animation script for HEP-010-topk-products-index-gap

This script creates an animated visualization for the problem:
HEP-010-topk-products-index-gap

Topic: Heaps
"""

from manim import *


class Hep010TopkProductsIndexGapScene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("HEP-010-topk-products-index-gap", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # TODO: Add animation implementation
        
        self.wait(2)
