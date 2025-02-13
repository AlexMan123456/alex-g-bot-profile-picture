from manim import *

# manim profile-picture.py -qm -t ProfilePicture
class ProfilePicture(Scene):
    def construct(self):
        # Create robot face
        robot_head = Square(4, color=GRAY, fill_color=GRAY).set_opacity(1)
        robot_eyes = VGroup(Square(0.5, color=BLACK, fill_color=BLACK).set_opacity(1).move_to([-1,1,0]))
        robot_eyes.add(robot_eyes[0].copy().move_to([1,1,0]))
        robot_mouth = Ellipse(width=2, height=0.5, color=BLACK, fill_color=BLACK).set_opacity(1).move_to([0,-1,0])
        robot_alarm = VGroup(Rectangle(width=0.3, height=0.6, color=RED, fill_color=RED).set_opacity(1).next_to(robot_head, UP, aligned_edge=UP, buff=0.32))
        robot_alarm.add(robot_alarm[0].copy().stretch_to_fit_height(1.1).scale(0.4).set_color(WHITE).set_fill(WHITE).shift(0.05*DOWN))
        robot_face = VGroup(robot_head, robot_eyes, robot_mouth, robot_alarm).scale(0.7).shift(1.3*UP)


        robot_body = Rectangle(width=0.5, height=2, color=GRAY, fill_color=GRAY).set_opacity(1).shift(DOWN)

        robot_left_arm = Rectangle(width=0.3, height=1.5, color=GRAY, fill_color=GRAY).set_opacity(1).rotate(-PI/4).shift(0.9*DOWN+0.4*LEFT)
        robot_right_arm = robot_left_arm.copy().rotate(PI/2).shift(0.85*RIGHT)

        robot_left_leg = Rectangle(width=0.2, height=1, color=GRAY, fill_color=GRAY).set_opacity(1).shift(2*DOWN+0.15*LEFT)
        robot_right_leg = robot_left_leg.copy().shift(0.3*RIGHT)

        robot = VGroup(robot_face, robot_body, robot_left_arm, robot_right_arm, robot_left_leg, robot_right_leg).shift(0.2*DOWN)

        self.add(robot)