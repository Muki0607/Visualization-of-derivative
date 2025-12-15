#!/usr/bin/env python3
from manim import *
import numpy as np

# ============================================
# SCENE 1: Geometric Definition of Derivative
# 时长: 50秒
# ============================================
class Scene1_GeometricDefinition(ThreeDScene):
    def construct(self):
        # Part 1: Title
        title = Tex(r"\text{Part 1: Geometric Definition of Derivative}")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)
        
        # Part 2: Setup coordinate system
        axes = Axes(
            x_range=[-1, 3, 1],
            y_range=[-1, 9, 2],
            x_length=6,
            y_length=5,
            axis_config={"color": BLUE},
        ).shift(DOWN * 0.5)
        
        x_label = MathTex("x").next_to(axes.x_axis.get_right(), RIGHT)
        y_label = MathTex("y").next_to(axes.y_axis.get_top(), UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)
        
        # Part 3: Function f(x) = x^2
        func = lambda x: x**2
        graph = axes.plot(func, x_range=[-0.5, 2.8], color=GREEN)
        graph_label = MathTex(r"f(x) = x^2", color=GREEN)
        graph_label.next_to(graph.point_from_proportion(0.7), RIGHT)
        
        self.play(Create(graph), Write(graph_label))
        self.wait(1)
        
        # Part 4: Point at x = 1
        a = 1
        point_a = axes.coords_to_point(a, func(a))
        dot_a = Dot(point_a, color=RED, radius=0.08)
        dot_label = MathTex(r"P(1,1)", color=RED)
        dot_label.next_to(dot_a, UP + RIGHT * 0.2)
        
        self.play(Create(dot_a), Write(dot_label))
        self.wait(1)
        
        # Part 5: Secant lines with different h values
        h_values = [2.0, 1.0, 0.5, 0.1]
        
        for i, h in enumerate(h_values):
            # Calculate second point
            point_b = axes.coords_to_point(a + h, func(a + h))
            dot_b = Dot(point_b, color=ORANGE, radius=0.06)
            
            # Draw secant line
            secant = Line(point_a, point_b, color=YELLOW, stroke_width=3)
            
            # Slope calculation
            slope = (func(a + h) - func(a)) / h
            slope_text = MathTex(
                r"\text{Slope} = \frac{f(1+" + f"{h:.1f}" + r")-f(1)}{" + f"{h:.1f}" + r"}",
                r"=",
                f"{slope:.2f}",
                color=YELLOW
            )
            slope_text.scale(0.7)
            slope_text.to_edge(RIGHT).shift(UP * (0.5 - i * 0.4))
            
            self.play(Create(dot_b), Create(secant), Write(slope_text))
            self.wait(0.3)
            
            if i < len(h_values) - 1:
                self.play(FadeOut(dot_b), FadeOut(secant), FadeOut(slope_text))
        
        # Part 6: Tangent line as limit
        tangent_slope = 2 * a  # f'(x) = 2x, at x=1
        tangent = axes.plot(
            lambda x: tangent_slope * (x - a) + func(a),
            x_range=[a - 1, a + 1],
            color=RED,
            stroke_width=4
        )
        
        tangent_label = MathTex(r"f'(1) = 2", color=RED)
        tangent_label.next_to(tangent.point_from_proportion(0.3), LEFT)
        
        self.play(Transform(secant, tangent), Write(tangent_label))
        self.wait(1)
        
        # Part 7: Limit definition
        limit_def = MathTex(
            r"f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}",
            color=GREEN,
            font_size=36
        )
        limit_def.to_edge(DOWN, buff=0.5)
        
        self.play(Write(limit_def))
        self.wait(2)
        
        # Clean transition
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

# ============================================
# SCENE 2: Derivative as Rate of Change
# 时长: 45秒
# ============================================
class Scene2_RateOfChange(Scene):
    def construct(self):
        # Title
        title = Tex(r"\text{Part 2: Derivative as Instantaneous Rate of Change}")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)
        
        # Create number line for position
        time_line = NumberLine(
            x_range=[0, 10, 1],
            length=9,
            include_numbers=True,
            numbers_to_include=[0, 2, 4, 6, 8, 10],
            label_direction=DOWN,
        )
        time_line.shift(UP * 1.5)
        
        time_label = Tex(r"\text{Time (seconds)}").next_to(time_line, DOWN)
        
        self.play(Create(time_line), Write(time_label))
        self.wait(0.5)
        
        # Position function: s(t) = t^2
        pos_func = lambda t: t**2
        
        # Create position axis
        pos_line = NumberLine(
            x_range=[0, 100, 20],
            length=6,
            include_numbers=True,
            numbers_to_include=[0, 20, 40, 60, 80, 100],
            label_direction=LEFT,
            rotation=90 * DEGREES,
        )
        pos_line.next_to(time_line, LEFT, buff=1)
        pos_label = Tex(r"\text{Position (meters)}").next_to(pos_line, LEFT)
        
        self.play(Create(pos_line), Write(pos_label))
        
        # Show points at different times
        times = [2, 4, 6, 8]
        positions = [pos_func(t) for t in times]
        
        dots = VGroup()
        labels = VGroup()
        
        for i, (t, s) in enumerate(zip(times, positions)):
            # Position on time line
            t_point = time_line.number_to_point(t)
            # Position on position line  
            s_point = pos_line.number_to_point(s)
            
            # Create dot and connecting lines
            dot_t = Dot(t_point, color=BLUE, radius=0.06)
            dot_s = Dot(s_point, color=GREEN, radius=0.06)
            
            # Connecting line
            line = DashedLine(t_point, s_point, color=WHITE, stroke_width=1)
            
            # Label
            label = MathTex(f"t={t},\\, s={s}", font_size=20)
            label.next_to(dot_t, DOWN)
            
            dots.add(dot_t, dot_s, line)
            labels.add(label)
            
            if i == 0:
                self.play(Create(dot_t), Create(dot_s), Create(line), Write(label))
            else:
                self.play(Create(dot_t), Create(dot_s), Create(line), Write(label), run_time=0.5)
            
            self.wait(0.3)
        
        # Average velocity calculation
        avg_velocity_text = VGroup(
            Tex(r"\text{Average Velocity: }"),
            MathTex(r"v_{\text{avg}} = \frac{\Delta s}{\Delta t}")
        ).arrange(RIGHT)
        avg_velocity_text.to_edge(LEFT).shift(DOWN * 1)
        
        self.play(Write(avg_velocity_text))
        self.wait(0.5)
        
        # Show specific calculation
        example_calc = MathTex(
            r"v_{\text{avg}}(t=2\to4) = \frac{4^2 - 2^2}{4-2} = \frac{16-4}{2} = 6\ \text{m/s}"
        )
        example_calc.next_to(avg_velocity_text, DOWN, aligned_edge=LEFT)
        
        self.play(Write(example_calc))
        self.wait(1)
        
        # Instantaneous velocity
        instant_text = VGroup(
            Tex(r"\text{Instantaneous Velocity: }"),
            MathTex(r"v(t) = \lim_{\Delta t \to 0} \frac{\Delta s}{\Delta t} = \frac{ds}{dt}")
        ).arrange(RIGHT)
        instant_text.next_to(example_calc, DOWN, aligned_edge=LEFT)
        
        derivative_calc = MathTex(
            r"\text{For } s(t)=t^2:\quad v(t)=s'(t)=2t"
        )
        derivative_calc.next_to(instant_text, DOWN, aligned_edge=LEFT)
        
        self.play(Write(instant_text))
        self.wait(0.5)
        self.play(Write(derivative_calc))
        self.wait(2)
        
        # Clean transition
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
        
# ============================================

# 时长: 50秒
# ============================================
class Scene3_Velocity(Scene):
    def construct(self):
        # Title
        title = Tex(r"\text{Part 3: Physical Interpretation - Velocity}")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)
        
        # Create coordinate system
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 36, 5],
            x_length=7,
            y_length=5,
            axis_config={"color": BLUE},
        ).shift(DOWN * 0.5)
        
        axes_labels = axes.get_axis_labels(
            MathTex(r"t\ (\text{s})"),
            MathTex(r"s(t)\ (\text{m})")
        )
        
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)
        
        # Position function s(t) = t^2
        s_func = lambda t: t**2
        s_graph = axes.plot(s_func, x_range=[0, 6], color=GREEN)
        s_label = MathTex(r"s(t) = t^2", color=GREEN)
        s_label.next_to(s_graph.point_from_proportion(0.8), RIGHT)
        
        self.play(Create(s_graph), Write(s_label))
        self.wait(1)
        
        # Velocity function v(t) = s'(t) = 2t
        v_axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 12, 2],
            x_length=7,
            y_length=3,
            axis_config={"color": BLUE},
        ).shift(DOWN * 2.5)
        
        v_axes_labels = v_axes.get_axis_labels(
            MathTex(r"t\ (\text{s})"),
            MathTex(r"v(t)\ (\text{m/s})")
        )
        
        self.play(Create(v_axes), Write(v_axes_labels))
        
        v_func = lambda t: 2*t
        v_graph = v_axes.plot(v_func, x_range=[0, 6], color=RED)
        v_label = MathTex(r"v(t) = s'(t) = 2t", color=RED)
        v_label.next_to(v_graph.point_from_proportion(0.8), RIGHT)
        
        self.play(Create(v_graph), Write(v_label))
        self.wait(1)
        
        # Show relationship
        relation = MathTex(
            r"v(t) = \frac{ds}{dt} = \lim_{\Delta t \to 0} \frac{s(t+\Delta t) - s(t)}{\Delta t}"
        )
        relation.to_edge(DOWN, buff=0.5)
        
        self.play(Write(relation))
        self.wait(1)
        
        # Animate a moving point with tangent
        t_values = [1, 2, 3, 4]
        
        for t in t_values:
            # Point on position graph
            s_point = axes.coords_to_point(t, s_func(t))
            s_dot = Dot(s_point, color=YELLOW, radius=0.08)
            
            # Tangent line at that point
            tangent_slope = v_func(t)  # = 2t
            tangent = axes.plot(
                lambda x: tangent_slope * (x - t) + s_func(t),
                x_range=[t - 0.8, t + 0.8],
                color=YELLOW,
                stroke_width=2
            )
            
            # Corresponding point on velocity graph
            v_point = v_axes.coords_to_point(t, v_func(t))
            v_dot = Dot(v_point, color=YELLOW, radius=0.08)
            
            # Labels
            s_info = MathTex(f"t={t},\\, s={s_func(t)}", font_size=20)
            s_info.next_to(s_dot, UP)
            
            v_info = MathTex(f"t={t},\\, v={v_func(t)}", font_size=20)
            v_info.next_to(v_dot, UP)
            
            if t == 1:
                self.play(Create(s_dot), Create(tangent), Create(v_dot),
                         Write(s_info), Write(v_info))
            else:
                self.play(
                    Transform(s_dot, Dot(s_point, color=YELLOW, radius=0.08)),
                    Transform(tangent, axes.plot(
                        lambda x: v_func(t) * (x - t) + s_func(t),
                        x_range=[t - 0.8, t + 0.8],
                        color=YELLOW,
                        stroke_width=2
                    )),
                    Transform(v_dot, Dot(v_point, color=YELLOW, radius=0.08)),
                    Transform(s_info, MathTex(f"t={t},\\, s={s_func(t)}", font_size=20).next_to(s_dot, UP)),
                    Transform(v_info, MathTex(f"t={t},\\, v={v_func(t)}", font_size=20).next_to(v_dot, UP)),
                    run_time=1
                )
            
            self.wait(0.5)
        
        self.wait(1)
        
        # Summary
        summary = MathTex(
            r"\text{Position } s(t) \rightarrow \text{Velocity } v(t) = s'(t) = \frac{ds}{dt}"
        )
        summary.to_edge(DOWN, buff=0.2)
        
        self.play(Write(summary))
        self.wait(2)
        
        # Clean transition
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

# ============================================
# SCENE 4: Second Derivative - Acceleration
# 时长: 45秒
# ============================================
class Scene4_SecondDerivative(Scene):
    def construct(self):
        # Title
        title = Tex(r"\text{Part 4: Second Derivative - Acceleration}")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)
        
        # Three graphs: Position → Velocity → Acceleration
        axes_config = {
            "x_range": [0, 6, 1],
            "x_length": 6,
            "axis_config": {"color": BLUE},
        }
        
        # Position graph
        pos_axes = Axes(
            y_range=[0, 36, 5],
            **axes_config
        ).shift(UP * 1.5)
        
        pos_label = MathTex(r"s(t) = t^3 - 6t^2 + 9t", color=GREEN)
        pos_label.next_to(pos_axes, UP)
        
        s_func = lambda t: t**3 - 6*t**2 + 9*t
        pos_graph = pos_axes.plot(s_func, x_range=[0, 4.5], color=GREEN)
        
        self.play(Create(pos_axes), Write(pos_label), Create(pos_graph))
        self.wait(0.5)
        
        # Velocity graph (first derivative)
        vel_axes = Axes(
            y_range=[-10, 10, 2],
            **axes_config
        )
        
        vel_label = MathTex(r"v(t) = s'(t) = 3t^2 - 12t + 9", color=YELLOW)
        vel_label.next_to(vel_axes, UP)
        
        v_func = lambda t: 3*t**2 - 12*t + 9  # Derivative of s(t)
        vel_graph = vel_axes.plot(v_func, x_range=[0, 4.5], color=YELLOW)
        
        self.play(Create(vel_axes), Write(vel_label), Create(vel_graph))
        self.wait(0.5)
        
        # Acceleration graph (second derivative)
        acc_axes = Axes(
            y_range=[-12, 12, 2],
            **axes_config
        ).shift(DOWN * 1.5)
        
        acc_label = MathTex(r"a(t) = v'(t) = s''(t) = 6t - 12", color=RED)
        acc_label.next_to(acc_axes, UP)
        
        a_func = lambda t: 6*t - 12  # Derivative of v(t)
        acc_graph = acc_axes.plot(a_func, x_range=[0, 4.5], color=RED)
        
        self.play(Create(acc_axes), Write(acc_label), Create(acc_graph))
        self.wait(1)
        
        # Show derivative relationships
        derivative_chain = VGroup(
            MathTex(r"s(t) \xrightarrow{\frac{d}{dt}} v(t) \xrightarrow{\frac{d}{dt}} a(t)"),
            MathTex(r"\text{Position} \rightarrow \text{Velocity} \rightarrow \text{Acceleration}")
        ).arrange(DOWN)
        
        derivative_chain.to_edge(DOWN, buff=0.5)
        
        self.play(Write(derivative_chain))
        self.wait(1)
        
        # Highlight critical points
        # Find when v(t) = 0
        t_critical = [1, 3]  # Solutions to 3t^2 - 12t + 9 = 0
        
        for t in t_critical:
            # Mark on velocity graph
            v_point = vel_axes.coords_to_point(t, 0)
            v_dot = Dot(v_point, color=WHITE, radius=0.08)
            v_label_point = MathTex(f"t={t}", font_size=18)
            v_label_point.next_to(v_dot, UP)
            
            # Corresponding point on position graph
            s_point = pos_axes.coords_to_point(t, s_func(t))
            s_dot = Dot(s_point, color=WHITE, radius=0.08)
            
            # Corresponding point on acceleration graph
            a_point = acc_axes.coords_to_point(t, a_func(t))
            a_dot = Dot(a_point, color=WHITE, radius=0.08)
            a_label = MathTex(f"a({t})={a_func(t):.1f}", font_size=18)
            a_label.next_to(a_dot, DOWN)
            
            self.play(
                Create(s_dot), Create(v_dot), Create(a_dot),
                Write(v_label_point), Write(a_label),
                run_time=0.8
            )
            self.wait(0.5)
        
        # Physical interpretation
        interpretation = VGroup(
            Tex(r"$\bullet$ Velocity $v(t)$ = rate of change of position"),
            Tex(r"$\bullet$ Acceleration $a(t)$ = rate of change of velocity"),
            Tex(r"$\bullet$ $v(t)=0$: object changes direction"),
            Tex(r"$\bullet$ $a(t)=0$: velocity is maximum/minimum")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        interpretation.scale(0.7)
        interpretation.to_edge(LEFT).shift(DOWN * 0.5)
        
        self.play(Write(interpretation))
        self.wait(2)
        
        # Clean transition
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

# ============================================
# SCENE 5: Practical Applications
# 时长: 50秒
# ============================================
class Scene5_Applications(Scene):
    def construct(self):
        # Title
        title = Tex(r"\text{Part 5: Practical Applications of Derivatives}")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)
        
        # Application 1: Optimization
        app1_title = Tex(r"\text{1. Optimization: Finding Maximum/Minimum}", color=BLUE)
        app1_title.to_edge(LEFT).shift(UP * 2)
        
        # Example: Maximize area
        example1 = VGroup(
            MathTex(r"A(x) = x(10-x) = 10x - x^2"),
            MathTex(r"A'(x) = 10 - 2x"),
            MathTex(r"A'(x)=0 \Rightarrow 10-2x=0 \Rightarrow x=5"),
            MathTex(r"A''(x) = -2 < 0 \Rightarrow \text{Maximum at } x=5")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        example1.next_to(app1_title, DOWN, aligned_edge=LEFT)
        
        # Visual rectangle
        rect = Rectangle(
            height=2, width=3,
            color=GREEN,
            stroke_width=3
        ).shift(RIGHT * 3 + UP * 1)
        
        dimensions = VGroup(
            MathTex(r"x").next_to(rect, LEFT),
            MathTex(r"10-x").next_to(rect, DOWN)
        )
        
        self.play(Write(app1_title))
        self.wait(0.5)
        self.play(Write(example1), Create(rect), Write(dimensions))
        self.wait(2)
        
        # Application 2: Related Rates
        self.play(FadeOut(example1), FadeOut(rect), FadeOut(dimensions))
        
        app2_title = Tex(r"\text{2. Related Rates: Changing Dimensions}", color=YELLOW)
        app2_title.move_to(app1_title)
        
        example2 = VGroup(
            MathTex(r"\text{Volume of sphere: } V = \frac{4}{3}\pi r^3"),
            MathTex(r"\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}"),
            MathTex(r"\text{If } \frac{dV}{dt} = 100\ \text{cm}^3/\text{s},\ r=5\ \text{cm}:"),
            MathTex(r"100 = 4\pi(5)^2 \frac{dr}{dt}"),
            MathTex(r"\Rightarrow \frac{dr}{dt} = \frac{100}{100\pi} \approx 0.318\ \text{cm/s}")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        example2.next_to(app2_title, DOWN, aligned_edge=LEFT)
        
        # Animated sphere
        sphere = Circle(radius=1.5, color=RED)
        sphere.shift(RIGHT * 3)
        radius_line = Line(sphere.get_center(), sphere.get_right(), color=YELLOW)
        radius_label = MathTex(r"r=5\ \text{cm}").next_to(radius_line, UP)
        
        self.play(Transform(app1_title, app2_title))
        self.play(Write(example2), Create(sphere), Create(radius_line), Write(radius_label))
        
        # Animate growing sphere
        self.play(
            sphere.animate.scale(1.2),
            radius_line.animate.scale(1.2),
            run_time=2,
            rate_func=there_and_back
        )
        self.wait(2)
        
        # Application 3: Linear Approximation
        self.play(FadeOut(example2), FadeOut(sphere), FadeOut(radius_line), FadeOut(radius_label))
        
        app3_title = Tex(r"\text{3. Linear Approximation}", color=GREEN)
        app3_title.move_to(app1_title)
        
        example3 = VGroup(
            MathTex(r"f(x) \approx f(a) + f'(a)(x-a)"),
            MathTex(r"\text{Example: } \sqrt{16.1}"),
            MathTex(r"f(x)=\sqrt{x},\ f'(x)=\frac{1}{2\sqrt{x}}"),
            MathTex(r"a=16,\ f(16)=4,\ f'(16)=\frac{1}{8}=0.125"),
            MathTex(r"\sqrt{16.1} \approx 4 + 0.125(0.1) = 4.0125"),
            MathTex(r"\text{Actual: } \sqrt{16.1} \approx 4.01248")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        example3.next_to(app3_title, DOWN, aligned_edge=LEFT)
        
        # Graph visualization
        approx_axes = Axes(
            x_range=[15, 17, 0.5],
            y_range=[3.9, 4.2, 0.1],
            x_length=4,
            y_length=3,
            axis_config={"color": BLUE},
        ).shift(RIGHT * 3 + DOWN * 0.5)
        
        sqrt_func = lambda x: np.sqrt(x)
        approx_graph = approx_axes.plot(sqrt_func, x_range=[15.5, 16.5], color=GREEN)
        
        # Tangent at x=16
        tangent = approx_axes.plot(
            lambda x: 4 + 0.125*(x-16),
            x_range=[15.5, 16.5],
            color=RED
        )
        
        # Point at x=16.1
        point_approx = approx_axes.coords_to_point(16.1, 4 + 0.125*0.1)
        point_actual = approx_axes.coords_to_point(16.1, np.sqrt(16.1))
        dot_approx = Dot(point_approx, color=RED)
        dot_actual = Dot(point_actual, color=GREEN)
        
        self.play(Transform(app1_title, app3_title))
        self.play(
            Write(example3),
            Create(approx_axes),
            Create(approx_graph),
            Create(tangent),
            Create(dot_approx),
            Create(dot_actual)
        )
        self.wait(2)
        
        # Final summary
        summary = VGroup(
            Tex(r"\text{Derivatives are used in:}"),
            Tex(r"$\bullet$ Physics: velocity, acceleration"),
            Tex(r"$\bullet$ Economics: marginal cost, revenue"),
            Tex(r"$\bullet$ Engineering: optimization, control systems"),
            Tex(r"$\bullet$ Machine Learning: gradient descent")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        summary.scale(0.8)
        summary.to_edge(DOWN, buff=0.5)
        
        self.play(Write(summary))
        self.wait(3)
        
        # Final equation
        final_eq = MathTex(
            r"\frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}",
            font_size=40,
            color=YELLOW
        )
        final_eq.move_to(ORIGIN)
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != title],
            Write(final_eq)
        )
        self.wait(2)

# ============================================
# SCENE 6: All in One (Complete Summary)
# 时长: 50秒
# ============================================
class Scene6_CompleteSummary(Scene):
    def construct(self):
        # Main title
        main_title = Tex(r"\text{The Derivative: A Complete Picture}", font_size=48)
        main_title.to_edge(UP, buff=0.5)
        self.play(Write(main_title))
        self.wait(1)
        
        # Three column layout
        column1 = VGroup(
            Tex(r"\textbf{Geometric:}"),
            MathTex(r"\text{Slope of tangent line}"),
            MathTex(r"f'(a) = \lim_{h\to 0} \frac{f(a+h)-f(a)}{h}"),
            Tex(r"\text{ }"),
            Tex(r"\textbf{Physical:}"),
            MathTex(r"\text{Instantaneous rate of change}"),
            MathTex(r"v(t) = \frac{ds}{dt}"),
            MathTex(r"a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2}")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        column2 = VGroup(
            Tex(r"\textbf{Notation:}"),
            MathTex(r"f'(x),\quad y',\quad \frac{dy}{dx}"),
            MathTex(r"\frac{df}{dx},\quad D_x f"),
            Tex(r"\\text{ }"),
            Tex(r"\textbf{Rules:}"),
            MathTex(r"(cf)' = cf'"),
            MathTex(r"(f+g)' = f' + g'"),
            MathTex(r"(fg)' = f'g + fg'"),
            MathTex(r"\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        column3 = VGroup(
            Tex(r"\textbf{Common Derivatives:}"),
            MathTex(r"\frac{d}{dx}(c) = 0"),
            MathTex(r"\frac{d}{dx}(x^n) = nx^{n-1}"),
            MathTex(r"\frac{d}{dx}(e^x) = e^x"),
            MathTex(r"\frac{d}{dx}(\sin x) = \cos x"),
            MathTex(r"\frac{d}{dx}(\cos x) = -\sin x"),
            MathTex(r"\frac{d}{dx}(\ln x) = \frac{1}{x}")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        # Position columns
        column1.shift(LEFT * 3.5)
        column2.shift(RIGHT * 0)
        column3.shift(RIGHT * 3.5)
        
        # Animate columns one by one
        self.play(Write(column1))
        self.wait(0.5)
        self.play(Write(column2))
        self.wait(0.5)
        self.play(Write(column3))
        self.wait(2)
        
        # Applications box
        applications = VGroup(
            Tex(r"\textbf{Key Applications:}"),
            Tex(r"$\bullet$ Optimization problems"),
            Tex(r"$\bullet$ Related rates"),
            Tex(r"$\bullet$ Curve sketching"),
            Tex(r"$\bullet$ Linear approximation"),
            Tex(r"$\bullet$ Physics: motion analysis")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        applications.scale(0.8)
        applications.to_edge(DOWN, buff=0.5)
        
        self.play(Write(applications))
        self.wait(2)
        
        # Final animation: derivative symbol
        derivative_symbol = MathTex(
            r"\frac{d}{dx}",
            font_size=72,
            color=YELLOW
        )
        derivative_symbol.move_to(ORIGIN)
        
        self.play(
            Transform(main_title, Tex(r"\text{The Power of Derivatives}", font_size=48).to_edge(UP, buff=0.5)),
            *[FadeOut(col) for col in [column1, column2, column3]],
            FadeOut(applications),
            Write(derivative_symbol)
        )
        
        # Transform derivative symbol
        self.play(
            derivative_symbol.animate.scale(1.5).set_color(RED),
            run_time=1.5
        )
        self.play(
            derivative_symbol.animate.scale(1/1.5).set_color(GREEN),
            run_time=1.5
        )
        
        # Final message
        final_message = Tex(
            r"\text{Derivatives: The mathematics of change}",
            font_size=36,
            color=BLUE
        )
        final_message.to_edge(DOWN, buff=0.5)
        
        self.play(Write(final_message))
        self.wait(3)
        
        # Final equation
        final_eq = MathTex(
            r"\frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}",
            font_size=40,
            color=YELLOW
        )
        final_eq.move_to(ORIGIN)
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != title],
            Write(final_eq)
        )
        self.wait(2)

# ============================================
# SCENE 6: All in One (Complete Summary)
# 时长: 50秒
# ============================================
class Scene6_CompleteSummary(Scene):
    def construct(self):
        # Main title
        main_title = Tex(r"\text{The Derivative: A Complete Picture}", font_size=48)
        main_title.to_edge(UP, buff=0.5)
        self.play(Write(main_title))
        self.wait(1)
        
        # Three column layout
        column1 = VGroup(
            Tex(r"\textbf{Geometric:}"),
            MathTex(r"\text{Slope of tangent line}"),
            MathTex(r"f'(a) = \lim_{h\to 0} \frac{f(a+h)-f(a)}{h}"),
            Tex(r"\\text{ }"),
            Tex(r"\textbf{Physical:}"),
            MathTex(r"\text{Instantaneous rate of change}"),
            MathTex(r"v(t) = \frac{ds}{dt}"),
            MathTex(r"a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2}")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        column2 = VGroup(
            Tex(r"\textbf{Notation:}"),
            MathTex(r"f'(x),\quad y',\quad \frac{dy}{dx}"),
            MathTex(r"\frac{df}{dx},\quad D_x f"),
            Tex(r"\\text{ }"),
            Tex(r"\textbf{Rules:}"),
            MathTex(r"(cf)' = cf'"),
            MathTex(r"(f+g)' = f' + g'"),
            MathTex(r"(fg)' = f'g + fg'"),
            MathTex(r"\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        column3 = VGroup(
            Tex(r"\textbf{Common Derivatives:}"),
            MathTex(r"\frac{d}{dx}(c) = 0"),
            MathTex(r"\frac{d}{dx}(x^n) = nx^{n-1}"),
            MathTex(r"\frac{d}{dx}(e^x) = e^x"),
            MathTex(r"\frac{d}{dx}(\sin x) = \cos x"),
            MathTex(r"\frac{d}{dx}(\cos x) = -\sin x"),
            MathTex(r"\frac{d}{dx}(\ln x) = \frac{1}{x}")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        # Position columns
        column1.shift(LEFT * 3.5)
        column2.shift(RIGHT * 0)
        column3.shift(RIGHT * 3.5)
        
        # Animate columns one by one
        self.play(Write(column1))
        self.wait(0.5)
        self.play(Write(column2))
        self.wait(0.5)
        self.play(Write(column3))
        self.wait(2)
        
        # Applications box
        applications = VGroup(
            Tex(r"\textbf{Key Applications:}"),
            Tex(r"$\bullet$ Optimization problems"),
            Tex(r"$\bullet$ Related rates"),
            Tex(r"$\bullet$ Curve sketching"),
            Tex(r"$\bullet$ Linear approximation"),
            Tex(r"$\bullet$ Physics: motion analysis")
        ).arrange(DOWN, aligned_edge=LEFT)
        
        applications.scale(0.8)
        applications.to_edge(DOWN, buff=0.5)
        
        self.play(Write(applications))
        self.wait(2)
        
        # Final animation: derivative symbol
        derivative_symbol = MathTex(
            r"\frac{d}{dx}",
            font_size=72,
            color=YELLOW
        )
        derivative_symbol.move_to(ORIGIN)
        
        self.play(
            Transform(main_title, Tex(r"\text{The Power of Derivatives}", font_size=48).to_edge(UP, buff=0.5)),
            *[FadeOut(col) for col in [column1, column2, column3]],
            FadeOut(applications),
            Write(derivative_symbol)
        )
        
        # Transform derivative symbol
        self.play(
            derivative_symbol.animate.scale(1.5).set_color(RED),
            run_time=1.5
        )
        self.play(
            derivative_symbol.animate.scale(1/1.5).set_color(GREEN),
            run_time=1.5
        )
        
        # Final message
        final_message = Tex(
            r"\text{Derivatives: The mathematics of change}",
            font_size=36,
            color=BLUE
        )
        final_message.to_edge(DOWN, buff=0.5)
        
        self.play(Write(final_message))
        self.wait(3)