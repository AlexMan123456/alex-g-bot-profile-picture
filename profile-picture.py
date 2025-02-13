from manim import *

# manim profile-picture.py -qm ProfilePicture
class ProfilePicture(Scene):
    def construct(self):
        robot_head = Square(4, color=GRAY, fill_color=GRAY).set_opacity(1)

        self.add(robot_head)