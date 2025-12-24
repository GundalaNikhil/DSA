"""
Manim animation script for PRB-011-coupon-collector-expected

This script creates an animated visualization for the problem:
PRB-011-coupon-collector-expected

Topic: Probabilistic
"""

from manim import *


class Prb011CouponCollectorExpectedScene(Scene):
    def construct(self):
        """Main animation sequence"""
        # Title
        title = Text("PRB-011-coupon-collector-expected", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # TODO: Add animation implementation
        
        self.wait(2)
