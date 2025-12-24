from manim import *

class CampusShuttleExplanation(Scene):
    def construct(self):
        # Scene 1: Title and Introduction
        self.scene_1_intro()
        self.wait(3)
        self.clear()
        
        # Scene 2: Problem Statement
        self.scene_2_problem_statement()
        self.wait(3)
        self.clear()
        
        # Scene 3: Real World Scenario
        self.scene_3_real_world()
        self.wait(3)
        self.clear()
        
        # Scene 4: Visual Timeline
        self.scene_4_timeline()
        self.wait(3)
        self.clear()
        
        # Scene 5: Coverage Analysis
        self.scene_5_coverage()
        self.wait(3)
        self.clear()
        
        # Scene 6: Naive Approach
        self.scene_6_naive_approach()
        self.wait(3)
        self.clear()
        
        # Scene 7: Why DP?
        self.scene_7_why_dp()
        self.wait(3)
        self.clear()
        
        # Scene 8: DP State Design
        self.scene_8_dp_state()
        self.wait(3)
        self.clear()
        
        # Scene 9: Algorithm Steps
        self.scene_9_algorithm_steps()
        self.wait(3)
        self.clear()
        
        # Scene 10: Initialization
        self.scene_10_initialization()
        self.wait(3)
        self.clear()
        
        # Scene 11: Iteration Step 1
        self.scene_11_iteration_1()
        self.wait(3)
        self.clear()
        
        # Scene 12: Iteration Step 2
        self.scene_12_iteration_2()
        self.wait(3)
        self.clear()
        
        # Scene 13: Final Result
        self.scene_13_final_result()
        self.wait(3)
        self.clear()
        
        # Scene 14: Complexity Analysis
        self.scene_14_complexity_analysis()
        self.wait(3)
        self.clear()
        
        # Scene 15: Key Insights
        self.scene_15_key_insights()
        self.wait(3)
        self.clear()
        
        # Scene 16: Conclusion
        self.scene_16_conclusion()
        self.wait(3)

    def scene_1_intro(self):
        """Scene 1: Opening Title"""
        # Main title with gradient effect
        title = Text(
            "Campus Shuttle Driver Swaps",
            font_size=56,
            weight=BOLD,
            gradient=(BLUE, PURPLE)
        )
        title.shift(UP * 0.5)
        
        # Subtitle
        subtitle = Text(
            "A Dynamic Programming Problem",
            font_size=32,
            color=GRAY
        )
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Problem ID
        problem_id = Text(
            "GRD-001 | Difficulty: Easy | Topic: Greedy & DP",
            font_size=24,
            color=YELLOW
        )
        problem_id.next_to(subtitle, DOWN, buff=0.8)
        
        # Animate
        self.play(Write(title, run_time=2))
        self.wait(0.5)
        self.play(FadeIn(subtitle, shift=UP, run_time=1.5))
        self.wait(0.5)
        self.play(FadeIn(problem_id, run_time=1))
        self.wait(1)
        
        # Fade out
        self.play(
            FadeOut(title, shift=UP),
            FadeOut(subtitle, shift=UP),
            FadeOut(problem_id, shift=UP),
            run_time=1.5
        )

    def scene_2_problem_statement(self):
        """Scene 2: Clear Problem Statement (Sequential Layout)"""
        title = Text("Problem Statement", font_size=44, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title, run_time=1.5))
        self.wait(1)
        
        # Given Section - Centered Top
        given_title = Text("Given:", font_size=28, weight=BOLD, color=YELLOW)
        given_title.shift(UP * 1.5)
        
        given_items = VGroup(
            Text("• n shuttle trips [start, end] time", font_size=22),
            Text("• Two drivers A and B with working windows", font_size=22),
            Text("• Each trip must be covered by exactly one driver", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        given_items.next_to(given_title, DOWN, buff=0.4)
        
        self.play(Write(given_title, run_time=0.8))
        for line in given_items:
            self.play(FadeIn(line, shift=UP, run_time=0.6))
        self.wait(1.5)
        
        # Fade out Given section to make space for Goal
        self.play(FadeOut(given_title), FadeOut(given_items), run_time=1)
        
        # Goal Section - Centered
        goal_title = Text("Goal:", font_size=28, weight=BOLD, color=YELLOW)
        goal_title.shift(UP * 1.0)
        
        goal_items = VGroup(
            Text("Minimize the total number of", font_size=24, color=GREEN),
            Text("driver switches", font_size=32, color=GREEN, weight=BOLD),
            Text("between consecutive trips", font_size=24, color=GREEN)
        ).arrange(DOWN, buff=0.3)
        goal_items.next_to(goal_title, DOWN, buff=0.5)
        
        self.play(Write(goal_title, run_time=0.8))
        self.play(FadeIn(goal_items, shift=UP, run_time=1))
        
        self.wait(3)
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_3_real_world(self):
        """Scene 3: Real World Application (Sequential Layout)"""
        title = Text("Real-World Application", font_size=44, weight=BOLD, color=PURPLE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title, run_time=1.5))
        self.wait(1)
        
        # Main scenario
        main_title = Text("Logistics: 24/7 Delivery Operations", 
                         font_size=28, weight=BOLD, color=WHITE)
        main_title.shift(UP * 2.3)
        self.play(Write(main_title, run_time=1))
        
        # 1. Constraints Segment
        constraints_title = Text("1. Constraints", font_size=28, weight=BOLD, color=YELLOW)
        constraints_title.shift(UP * 1.0)
        
        constraints_list = VGroup(
            Text("• Driver A: 8AM - 4PM shift", font_size=24, color=GREEN),
            Text("• Driver B: 2PM - 10PM shift", font_size=24, color=ORANGE),
            Text("• Delivery trips cannot be interrupted", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        constraints_list.next_to(constraints_title, DOWN, buff=0.6)
        
        self.play(Write(constraints_title))
        for line in constraints_list:
            self.play(FadeIn(line, shift=UP))
        self.wait(2)
        
        # Clear segment for next
        self.play(FadeOut(constraints_title), FadeOut(constraints_list))
        
        # 2. Problem Segment
        problem_title = Text("2. The Problem", font_size=28, weight=BOLD, color=YELLOW)
        problem_title.shift(UP * 1.0)
        
        problem_list = VGroup(
            Text("Handing over the keys takes time", font_size=24),
            Text("Every switch adds delay and cost", font_size=24, color=RED),
            Text("How to assign drivers to minimize these stops?", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        problem_list.next_to(problem_title, DOWN, buff=0.6)
        
        self.play(Write(problem_title))
        for line in problem_list:
            self.play(FadeIn(line, shift=UP))
        self.wait(2)
        
        # Clear segment for next
        self.play(FadeOut(problem_title), FadeOut(problem_list))
        
        # 3. Solution Goal Segment
        solution_title = Text("3. Final Goal", font_size=28, weight=BOLD, color=YELLOW)
        solution_title.shift(UP * 1.0)
        
        solution_list = VGroup(
            Text("Find the optimal assignment that", font_size=24),
            Text("MINIMIZES total driver switches", font_size=32, color=GREEN, weight=BOLD),
            Text("while ensuring 100% trip coverage", font_size=24)
        ).arrange(DOWN, buff=0.5)
        solution_list.next_to(solution_title, DOWN, buff=0.6)
        
        self.play(Write(solution_title))
        self.play(FadeIn(solution_list, shift=UP))
        self.wait(3)
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_4_timeline(self):
        """Scene 4: Visual Timeline Setup"""
        title = Text("Visual Timeline", font_size=40, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.25)
        self.play(Write(title, run_time=1.5))
        self.wait(1)
        
        # Timeline with labels - more compact
        timeline = NumberLine(
            x_range=[0, 11, 1],
            length=10.5,
            include_numbers=True,
            font_size=22,
            include_ticks=True,
            tick_size=0.1
        )
        timeline.shift(UP * 1.4)
        
        time_label = Text("Time Units →", font_size=24, weight=BOLD)
        time_label.next_to(timeline, LEFT, buff=0.25)
        
        self.play(
            Create(timeline, run_time=2),
            Write(time_label, run_time=1)
        )
        self.wait(1)
        
        # Driver A window - better positioning
        driver_a_window = Rectangle(
            width=6.7,
            height=0.45,
            color=GREEN,
            fill_opacity=0.4,
            stroke_width=3
        )
        # Position from 1 to 8
        driver_a_window.move_to(timeline.n2p(4.5))
        driver_a_window.shift(DOWN * 0.7)
        
        driver_a_label = Text("Driver A [1 → 8]", font_size=22, color=GREEN, weight=BOLD)
        driver_a_label.next_to(driver_a_window, LEFT, buff=0.25)
        
        self.play(
            GrowFromCenter(driver_a_window, run_time=1.5),
            FadeIn(driver_a_label, run_time=1)
        )
        self.wait(1)
        
        # Driver B window - better positioning
        driver_b_window = Rectangle(
            width=6.7,
            height=0.45,
            color=ORANGE,
            fill_opacity=0.4,
            stroke_width=3
        )
        # Position from 3 to 10
        driver_b_window.move_to(timeline.n2p(6.5))
        driver_b_window.shift(DOWN * 1.5)
        
        driver_b_label = Text("Driver B [3 → 10]", font_size=22, color=ORANGE, weight=BOLD)
        driver_b_label.next_to(driver_b_window, LEFT, buff=0.25)
        
        self.play(
            GrowFromCenter(driver_b_window, run_time=1.5),
            FadeIn(driver_b_label, run_time=1)
        )
        self.wait(1)
        
        # Show overlap region - better positioned
        overlap_text = Text("Overlap Region [3 → 8]", font_size=20, color=YELLOW, weight=BOLD)
        overlap_text.shift(DOWN * 2.6)
        
        overlap_arrow_1 = Arrow(
            start=overlap_text.get_top(),
            end=timeline.n2p(5.5) + DOWN * 0.7,
            color=YELLOW,
            buff=0.1,
            stroke_width=3
        )
        
        self.play(
            Write(overlap_text, run_time=1),
            Create(overlap_arrow_1, run_time=1)
        )
        self.wait(2)
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_5_coverage(self):
        """Scene 5: Trip Coverage Analysis"""
        title = Text("Trip Coverage Analysis", font_size=40, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.25)
        self.play(Write(title, run_time=1.5))
        self.wait(1)
        
        # Timeline (compact version) - better positioned
        timeline = NumberLine(
            x_range=[0, 11, 1],
            length=10,
            include_numbers=True,
            font_size=18
        )
        timeline.shift(UP * 2.2)
        
        # Driver windows - better spacing
        driver_a_window = Rectangle(width=6.4, height=0.28, color=GREEN, fill_opacity=0.4)
        driver_a_window.move_to(timeline.n2p(4.5)).shift(DOWN * 0.45)
        
        driver_b_window = Rectangle(width=6.4, height=0.28, color=ORANGE, fill_opacity=0.4)
        driver_b_window.move_to(timeline.n2p(6.5)).shift(DOWN * 0.8)
        
        self.play(
            Create(timeline, run_time=1),
            FadeIn(driver_a_window),
            FadeIn(driver_b_window)
        )
        self.wait(0.5)
        
        # Trips data
        trips_data = [
            (1, 3, "T1", BLUE),
            (4, 6, "T2", BLUE),
            (7, 9, "T3", BLUE)
        ]
        
        # Create and animate each trip - better spacing
        for i, (start, end, label, color) in enumerate(trips_data):
            # Trip rectangle
            width = (end - start) * 0.9
            trip_rect = Rectangle(
                width=width,
                height=0.55,
                color=color,
                fill_opacity=0.7,
                stroke_width=3
            )
            mid = (start + end) / 2
            trip_rect.move_to(timeline.n2p(mid)).shift(DOWN * (1.5 + i * 0.75))
            
            trip_label = Text(f"{label} [{start}-{end}]", font_size=18, weight=BOLD)
            trip_label.move_to(trip_rect)
            
            # Animate trip appearance
            self.play(
                GrowFromCenter(trip_rect, run_time=0.7),
                FadeIn(trip_label, run_time=0.5)
            )
            self.wait(0.4)
            
            # Coverage check
            # Check Driver A
            if start >= 1 and end <= 8:
                a_check = Text("✓ A", font_size=18, color=GREEN, weight=BOLD)
            else:
                a_check = Text("✗ A", font_size=18, color=RED, weight=BOLD)
            
            # Check Driver B
            if start >= 3 and end <= 10:
                b_check = Text("✓ B", font_size=18, color=GREEN, weight=BOLD)
            else:
                b_check = Text("✗ B", font_size=18, color=RED, weight=BOLD)
            
            coverage_group = VGroup(a_check, b_check).arrange(RIGHT, buff=0.25)
            coverage_group.next_to(trip_rect, RIGHT, buff=0.4)
            
            self.play(FadeIn(coverage_group, shift=LEFT, run_time=0.7))
            
            # Special highlight for T3
            if label == "T3":
                self.play(
                    trip_rect.animate.set_color(RED),
                    Indicate(a_check, scale_factor=1.4, color=RED),
                    run_time=1
                )
                
                explanation = Text(
                    "Trip T3 ends at 9, but Driver A ends at 8!",
                    font_size=20,
                    color=RED,
                    weight=BOLD
                )
                explanation.to_edge(DOWN, buff=0.2) # Lowered to avoid overlap
                self.play(Write(explanation, run_time=1.3))
                self.wait(1.3)
            
            self.wait(0.8)
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_6_naive_approach(self):
        """Scene 6: Naive Approach (Sequential Layout)"""
        title = Text("Naive Approach: Try Everything", font_size=42, weight=BOLD, color=RED)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)
        
        # Segment 1: The Idea
        idea_title = Text("The Idea: Recursion (Backtracking)", font_size=28, weight=BOLD, color=YELLOW)
        idea_title.shift(UP * 1.0)
        
        idea_list = VGroup(
            Text("• For each trip, try Driver A", font_size=24),
            Text("• Then try Driver B", font_size=24),
            Text("• Calculate switches for every path", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(idea_title, DOWN, buff=0.6)
        
        self.play(Write(idea_title))
        for line in idea_list:
            self.play(FadeIn(line, shift=UP))
        self.wait(2)
        
        self.play(FadeOut(idea_title), FadeOut(idea_list))
        
        # Segment 2: The Problem
        problem_title = Text("The Problem: Complexity", font_size=28, weight=BOLD, color=YELLOW)
        problem_title.shift(UP * 1.0)
        
        problem_list = VGroup(
            Text("• 2 choices per trip", font_size=24),
            Text("• For n trips, total paths = 2 × 2 × ... × 2", font_size=24),
            Text("Complexity: O(2ⁿ)", font_size=36, color=RED, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(problem_title, DOWN, buff=0.6)
        
        self.play(Write(problem_title))
        for line in problem_list:
            self.play(FadeIn(line, shift=UP))
        self.wait(2)
        
        self.play(FadeOut(problem_title), FadeOut(problem_list))
        
        # Segment 3: Verdict
        verdict = Text("Too slow for large n!", font_size=36, color=RED, weight=BOLD)
        self.play(Write(verdict))
        self.play(Indicate(verdict, color=RED, scale_factor=1.3))
        self.wait(2)
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_7_why_dp(self):
        """Scene 7: Why DP? (Strict Sequential Layout)"""
        title = Text("Why Dynamic Programming?", font_size=42, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)
        
        # Segment 1: Key Observation
        obs_title = Text("Key Observation:", font_size=32, weight=BOLD, color=YELLOW)
        obs_title.shift(UP * 1.5)
        
        obs_desc = VGroup(
            Text("To decide who covers Trip i,", font_size=26),
            Text("we only need to know who covered Trip i-1.", font_size=26),
            Text("The previous path is irrelevant!", font_size=28, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.4).next_to(obs_title, DOWN, buff=0.8)
        
        self.play(Write(obs_title))
        for line in obs_desc:
            self.play(FadeIn(line, shift=UP))
        self.wait(3)
        
        self.play(FadeOut(obs_title), FadeOut(obs_desc))
        
        # Segment 2: Optimal Substructure
        struct_title = Text("Optimal Substructure:", font_size=32, weight=BOLD, color=YELLOW)
        struct_title.shift(UP * 1.5)
        
        struct_desc = VGroup(
            Text("The best way to cover n trips", font_size=26),
            Text("is built using the best ways to cover n-1 trips.", font_size=26),
            Text("→ We build the solution incrementally.", font_size=28, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.4).next_to(struct_title, DOWN, buff=0.8)
        
        self.play(Write(struct_title))
        for line in struct_desc:
            self.play(FadeIn(line, shift=UP))
        self.wait(3)
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_8_dp_state(self):
        """Scene 8: DP State Design (Sequential Layout)"""
        title = Text("Designing the DP State", font_size=42, weight=BOLD, color=GREEN)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)
        
        # Segment 1: The State
        state_title = Text("The DP State:", font_size=32, weight=BOLD, color=YELLOW)
        state_title.shift(UP * 1.0)
        
        state_def = VGroup(
            Text("DP[i][driver] =", font_size=36, color=BLUE, weight=BOLD),
            Text("Min switches for first i trips,", font_size=24),
            Text("ending with 'driver' covering trip i.", font_size=24)
        ).arrange(DOWN, buff=0.4).next_to(state_title, DOWN, buff=0.6)
        
        self.play(Write(state_title))
        self.play(FadeIn(state_def, shift=UP))
        self.wait(3)
        
        self.play(FadeOut(state_title), FadeOut(state_def))
        
        # Segment 2: Transitions
        trans_title = Text("The Transitions:", font_size=32, weight=BOLD, color=YELLOW)
        trans_title.shift(UP * 1.5)
        
        trans_logic = VGroup(
            Text("To calculate DP[i][A]:", font_size=24, color=GREEN, weight=BOLD),
            Text("1. Try staying with A: cost = DP[i-1][A]", font_size=22),
            Text("2. Try switching B -> A: cost = DP[i-1][B] + 1", font_size=22),
            Text("Take the minimum of both!", font_size=26, color=GREEN, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(trans_title, DOWN, buff=0.6)
        
        self.play(Write(trans_title))
        for line in trans_logic:
            self.play(FadeIn(line, shift=UP))
        self.wait(3.5)
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_9_algorithm_steps(self):
        """Scene 9: Complete Algorithm (Sequential Layout)"""
        title = Text("The DP Algorithm Steps", font_size=42, weight=BOLD, color=PURPLE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)
        
        # Step 1: Sorting
        step1_title = Text("Step 1: Sort Trips", font_size=28, weight=BOLD, color=YELLOW)
        step1_title.shift(UP * 1.0)
        step1_desc = Text("Sort trips by their start times.", font_size=24).next_to(step1_title, DOWN, buff=0.6)
        
        self.play(Write(step1_title))
        self.play(FadeIn(step1_desc, shift=UP))
        self.wait(2)
        self.play(FadeOut(step1_title), FadeOut(step1_desc))
        
        # Step 2: Initialization
        step2_title = Text("Step 2: Initialize", font_size=28, weight=BOLD, color=YELLOW)
        step2_title.shift(UP * 1.0)
        step2_desc = VGroup(
            Text("Set initial costs for Trip 1", font_size=24),
            Text("based on which drivers can cover it.", font_size=24)
        ).arrange(DOWN, buff=0.3).next_to(step2_title, DOWN, buff=0.6)
        
        self.play(Write(step2_title))
        self.play(FadeIn(step2_desc, shift=UP))
        self.wait(2)
        self.play(FadeOut(step2_title), FadeOut(step2_desc))
        
        # Step 3: Iteration
        step3_title = Text("Step 3: Fill DP Table", font_size=28, weight=BOLD, color=YELLOW)
        step3_title.shift(UP * 1.0)
        step3_desc = Text("Process trips one by one using transitions.", font_size=24).next_to(step3_title, DOWN, buff=0.6)
        
        self.play(Write(step3_title))
        self.play(FadeIn(step3_desc, shift=UP))
        self.wait(2)
        self.play(FadeOut(step3_title), FadeOut(step3_desc))
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_10_initialization(self):
        """Scene 10: Initialization for Trip 1 (Sequential Layout)"""
        title = Text("Initialization (Trip 1)", font_size=40, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)
        
        trip1 = Text("Trip 1: [1, 3]", font_size=28, color=WHITE).shift(UP * 2.0)
        self.play(Write(trip1))
        
        # Segment 1: Check Driver A
        seg1_title = Text("Step 1: Check Driver A", font_size=26, weight=BOLD, color=GREEN)
        seg1_title.shift(UP * 0.5)
        seg1_desc = VGroup(
            Text("Trip [1,3] fits in Window A [1,8].", font_size=22),
            Text("costA = 0 (Starting with A)", font_size=26, weight=BOLD, color=GREEN)
        ).arrange(DOWN, buff=0.3).next_to(seg1_title, DOWN, buff=0.5)
        
        self.play(Write(seg1_title))
        self.play(FadeIn(seg1_desc, shift=UP))
        self.wait(2)
        self.play(FadeOut(seg1_title), FadeOut(seg1_desc))
        
        # Segment 2: Check Driver B
        seg2_title = Text("Step 2: Check Driver B", font_size=26, weight=BOLD, color=ORANGE)
        seg2_title.shift(UP * 0.5)
        seg2_desc = VGroup(
            Text("Trip [1,3] fits in Window B [3,10].", font_size=22),
            Text("costB = 0 (Starting with B)", font_size=26, weight=BOLD, color=ORANGE)
        ).arrange(DOWN, buff=0.3).next_to(seg2_title, DOWN, buff=0.5)
        
        self.play(Write(seg2_title))
        self.play(FadeIn(seg2_desc, shift=UP))
        self.wait(2)
        self.play(FadeOut(seg2_title), FadeOut(seg2_desc))
        
        state_label = Text("Current State:", font_size=28, weight=BOLD, color=YELLOW)
        state_label.shift(DOWN * 2)
        
        state_values = VGroup(
            Text("costA = 0", font_size=32, color=GREEN, weight=BOLD),
            Text("costB = 0", font_size=32, color=ORANGE, weight=BOLD)
        ).arrange(RIGHT, buff=2)
        state_values.next_to(state_label, DOWN, buff=0.4)
        
        self.wait(0.5)
        self.play(Write(state_label, run_time=0.8))
        self.wait(0.3)
        self.play(
            FadeIn(state_values[0], shift=UP, run_time=0.8),
            FadeIn(state_values[1], shift=UP, run_time=0.8)
        )
        self.wait(2)
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_11_iteration_1(self):
        """Scene 11: First Iteration (Trip 1) - Sequential Layout"""
        title = Text("Iteration 1: Process Trip T2", font_size=40, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title, run_time=1))
        
        context = VGroup(
            Text("Previous: costA=0, costB=∞", font_size=22, color=YELLOW),
            Text("Current Trip: T2 = [4, 6]", font_size=22, color=BLUE)
        ).arrange(RIGHT, buff=1.0).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(context, shift=UP))
        self.wait(1)
        
        # Segment 1: Try Driver A
        segment_a_title = Text("Step 1: Try Driver A", font_size=28, weight=BOLD, color=GREEN)
        segment_a_title.shift(UP * 0.5)
        
        segment_a_content = VGroup(
            Text("• T2[4,6] fits in Driver A's window [1,8] ✓", font_size=22),
            Text("• newCostA = min(costA, costB + 1)", font_size=22),
            Text("• newCostA = min(0, ∞ + 1) = 0", font_size=26, color=GREEN, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(segment_a_title, DOWN, buff=0.5)
        
        self.play(Write(segment_a_title))
        for line in segment_a_content:
            self.play(FadeIn(line, shift=UP))
        self.wait(2)
        
        self.play(FadeOut(segment_a_title), FadeOut(segment_a_content))
        
        # Segment 2: Try Driver B
        segment_b_title = Text("Step 2: Try Driver B", font_size=28, weight=BOLD, color=ORANGE)
        segment_b_title.shift(UP * 0.5)
        
        segment_b_content = VGroup(
            Text("• T2[4,6] fits in Driver B's window [3,10] ✓", font_size=22),
            Text("• newCostB = min(costB, costA + 1)", font_size=22),
            Text("• newCostB = min(∞, 0 + 1) = 1", font_size=26, color=ORANGE, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(segment_b_title, DOWN, buff=0.5)
        
        self.play(Write(segment_b_title))
        for line in segment_b_content:
            self.play(FadeIn(line, shift=UP))
        self.wait(2)
        
        self.play(FadeOut(segment_b_title), FadeOut(segment_b_content))
        
        # Final Summary for this iteration
        state_title = Text("Updated State after T2:", font_size=28, weight=BOLD, color=YELLOW)
        state_title.shift(UP * 0.5)
        
        state_vals = VGroup(
            Text("costA = 0", font_size=32, color=GREEN, weight=BOLD),
            Text("costB = 1", font_size=32, color=ORANGE, weight=BOLD)
        ).arrange(RIGHT, buff=2.0).next_to(state_title, DOWN, buff=1.0)
        
        self.play(Write(state_title))
        self.play(FadeIn(state_vals, shift=UP))
        self.wait(2.5)
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_12_iteration_2(self):
        """Scene 12: Second Iteration (Trip 3) - Sequential Layout"""
        title = Text("Iteration 2: Process Trip T3", font_size=40, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title, run_time=1))
        
        context = VGroup(
            Text("Previous: costA=0, costB=1", font_size=22, color=YELLOW),
            Text("Current Trip: T3 = [7, 9]", font_size=22, color=BLUE)
        ).arrange(RIGHT, buff=1.0).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(context, shift=UP))
        self.wait(1)
        
        # Segment 1: Try Driver A
        segment_a_title = Text("Step 1: Try Driver A", font_size=28, weight=BOLD, color=GREEN)
        segment_a_title.shift(UP * 0.5)
        
        segment_a_content = VGroup(
            Text("• Trip ends at 9, but Driver A ends at 8!", font_size=22, color=RED),
            Text("• Driver A CANNOT cover this trip", font_size=22, color=RED, weight=BOLD),
            Text("• costA becomes ∞", font_size=26, color=RED, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(segment_a_title, DOWN, buff=0.5)
        
        self.play(Write(segment_a_title))
        for line in segment_a_content:
            self.play(FadeIn(line, shift=UP))
        self.wait(2)
        
        self.play(FadeOut(segment_a_title), FadeOut(segment_a_content))
        
        # Segment 2: Try Driver B
        segment_b_title = Text("Step 2: Try Driver B", font_size=28, weight=BOLD, color=ORANGE)
        segment_b_title.shift(UP * 0.5)
        
        segment_b_content = VGroup(
            Text("• T3[7,9] fits in Driver B's window [3,10] ✓", font_size=22),
            Text("• newCostB = min(costB, costA + 1)", font_size=22),
            Text("• newCostB = min(1, 0 + 1) = 1", font_size=26, color=ORANGE, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(segment_b_title, DOWN, buff=0.5)
        
        self.play(Write(segment_b_title))
        for line in segment_b_content:
            self.play(FadeIn(line, shift=UP))
        self.wait(2)
        
        self.play(FadeOut(segment_b_title), FadeOut(segment_b_content))
        
        # Final Summary for this iteration
        state_title = Text("Updated State after T3:", font_size=28, weight=BOLD, color=YELLOW)
        state_title.shift(UP * 0.5)
        
        state_vals = VGroup(
            Text("costA = ∞", font_size=32, color=RED, weight=BOLD),
            Text("costB = 1", font_size=32, color=ORANGE, weight=BOLD)
        ).arrange(RIGHT, buff=2.0).next_to(state_title, DOWN, buff=1.0)
        
        self.play(Write(state_title))
        self.play(FadeIn(state_vals, shift=UP))
        self.wait(2.5)
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_13_final_result(self):
        """Scene 13: Final Result and Assignment - Sequential Layout"""
        title = Text("Final Result", font_size=44, weight=BOLD, color=GREEN)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title, run_time=1.5))
        self.wait(0.5)
        
        # Segment 1: Final DP States
        states_title = Text("1. Final DP States", font_size=28, weight=BOLD, color=YELLOW)
        states_title.shift(UP * 1.0)
        
        states_vals = VGroup(
            Text("costA = ∞", font_size=32, color=RED, weight=BOLD),
            Text("costB = 1", font_size=32, color=ORANGE, weight=BOLD)
        ).arrange(RIGHT, buff=2.0).next_to(states_title, DOWN, buff=0.8)
        
        self.play(Write(states_title))
        self.play(FadeIn(states_vals, shift=UP))
        self.wait(1.5)
        
        self.play(FadeOut(states_title), FadeOut(states_vals))
        
        # Segment 2: Calculation
        calc_title = Text("2. Finding the Minimum", font_size=28, weight=BOLD, color=YELLOW)
        calc_title.shift(UP * 1.0)
        
        calc_logic = VGroup(
            Text("Result = min(costA, costB)", font_size=26),
            Text("Result = min(∞, 1) = 1", font_size=36, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.5).next_to(calc_title, DOWN, buff=0.8)
        
        self.play(Write(calc_title))
        self.play(FadeIn(calc_logic, shift=UP))
        self.wait(1.5)
        
        self.play(FadeOut(calc_title), FadeOut(calc_logic))
        
        # Segment 3: Optimal Assignment
        assign_title = Text("3. Optimal Assignment (Full Timeline)", font_size=28, weight=BOLD, color=YELLOW)
        assign_title.shift(UP * 1.0)
        
        assign_list = VGroup(
            Text("T1 [1,3] → Driver A", font_size=24, color=GREEN),
            Text("T2 [4,6] → Driver A", font_size=24, color=GREEN),
            Text("T3 [7,9] → Driver B", font_size=24, color=ORANGE),
            Text("Total Switches: 1", font_size=28, color=RED, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(assign_title, DOWN, buff=0.6)
        
        self.play(Write(assign_title))
        for line in assign_list:
            self.play(FadeIn(line, shift=UP))
            self.wait(0.5)
        
        self.wait(3.5)
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_14_complexity_analysis(self):
        """Scene 14: Complexity Analysis (Sequential Layout)"""
        title = Text("Complexity Analysis", font_size=42, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)
        
        # Segment 1: Time Complexity
        time_title = Text("Time Complexity:", font_size=32, weight=BOLD, color=YELLOW)
        time_title.shift(UP * 1.0)
        
        time_logic = VGroup(
            Text("• n trips, 2 drivers", font_size=24),
            Text("• For each trip i, we do constant work", font_size=24),
            Text("Time Complexity: O(n)", font_size=36, color=GREEN, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(time_title, DOWN, buff=0.6)
        
        self.play(Write(time_title))
        for line in time_logic:
            self.play(FadeIn(line, shift=UP))
        self.wait(2.5)
        
        self.play(FadeOut(time_title), FadeOut(time_logic))
        
        # Segment 2: Space Complexity
        space_title = Text("Space Complexity:", font_size=32, weight=BOLD, color=YELLOW)
        space_title.shift(UP * 1.0)
        
        space_logic = VGroup(
            Text("• We only store DP values for the current trip", font_size=24),
            Text("• Space = O(1) or O(n) depending on storage", font_size=24),
            Text("Space Complexity: O(n)", font_size=36, color=TEAL, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(space_title, DOWN, buff=0.6)
        
        self.play(Write(space_title))
        for line in space_logic:
            self.play(FadeIn(line, shift=UP))
        self.wait(2.5)
        
        self.play(FadeOut(space_title), FadeOut(space_logic))
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_15_key_insights(self):
        """Scene 15: Key Insights (Sequential Layout)"""
        title = Text("Key Insights", font_size=42, weight=BOLD, color=ORANGE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(1)
        
        insights = [
            ("The State Matters", "We only need the previous driver to make the current choice.", BLUE),
            ("Windows are Constraints", "Drivers can only cover trips within their working hours.", GREEN),
            ("Optimization", "Dynamic Programming turns exponential paths into linear time.", YELLOW)
        ]
        
        for i_title, i_desc, i_color in insights:
            seg_title = Text(i_title, font_size=32, weight=BOLD, color=i_color)
            seg_title.shift(UP * 1.0)
            seg_desc = VGroup(
                Text(i_desc, font_size=24),
            ).arrange(DOWN, buff=0.4).next_to(seg_title, DOWN, buff=0.6)
            
            self.play(Write(seg_title))
            self.play(FadeIn(seg_desc, shift=UP))
            self.wait(2.5)
            self.play(FadeOut(seg_title), FadeOut(seg_desc))
        
        # Explicit FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def scene_16_conclusion(self):
        """Scene 16: Conclusion (Strict Sequential Summary)"""
        title = Text("Summary & Conclusion", font_size=48, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)
        
        summary_points = [
            ("The Problem", "Minimize driver switches while covering all trips.", GREEN),
            ("The Strategy", "Use Dynamic Programming to avoid redundant work.", YELLOW),
            ("The Storage", "Only track costA and costB for the last trip.", BLUE),
            ("The Result", "Achieve O(n) time and O(1) space complexity.", TEAL),
            ("The Impact", "Fast enough for millions of trips!", GREEN)
        ]
        
        for p_title, p_desc, p_color in summary_points:
            pt_title = Text(p_title, font_size=36, weight=BOLD, color=p_color)
            pt_title.shift(UP * 0.5)
            pt_desc = Text(p_desc, font_size=28).next_to(pt_title, DOWN, buff=0.6)
            
            self.play(Write(pt_title))
            self.play(FadeIn(pt_desc, shift=UP))
            self.wait(2.5)
            self.play(FadeOut(pt_title), FadeOut(pt_desc))
            
        final_message = Text("Optimal Solutions through Smart DP", font_size=42, weight=BOLD, color=GOLD)
        self.play(Write(final_message))
        self.wait(1.5)
        self.play(Indicate(final_message, color=GOLD, scale_factor=1.2))
        self.wait(2)
        
        thank_you = Text("Thank You!", font_size=60, weight=BOLD, color=WHITE)
        self.play(FadeOut(final_message), FadeOut(title))
        self.play(Write(thank_you))
        self.wait(3)
        
        # Final FadeOut
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)


# Render command:
# manim -pqh campus_shuttle.py CampusShuttleExplanation