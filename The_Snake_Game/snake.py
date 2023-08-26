from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_STEP = 4

    def __init__(self):
        self.segment = Turtle(shape='square')
        self.segments_list = []
        self.create_snakes()
        self.head = self.segments_list[0]

    def create_snakes(self):
        """Create a new snake with 3 segments"""
        for position in self.STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Add segments to new snake"""
        segment = Turtle(shape='square')
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments_list.append(segment)

    def extend(self):
        """Extend segment to snake"""
        self.add_segment(self.segments_list[-1].position())
        self.add_segment(self.segments_list[-1].position())


    def move_forward(self):
        """Move snake forward"""
        for seg_n in range(len(self.segments_list) - 1, 0, -1):
            pos_x = self.segments_list[seg_n - 1].xcor()
            pos_y = self.segments_list[seg_n - 1].ycor()
            self.segments_list[seg_n].goto(pos_x, pos_y)
        self.head.forward(self.MOVE_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


