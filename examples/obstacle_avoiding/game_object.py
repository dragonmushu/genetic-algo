class GameObject:
    def __init__(self, x1, y1, x2, y2):
        self.current_x = x1
        self.current_y = y1
        self.width = x2 - self.current_x
        self.height = y2 - self.current_y
        self.previous_x = self.current_x
        self.previous_y = self.current_y

    def previous_location(self):
        return self.previous_x, self.previous_y, self.previous_x + self.height, self.previous_y + self.height

    def current_location(self):
        return self.current_x, self.current_y, self.current_x + self.width, self.current_y + self.height

    def delta_position(self):
        return self.current_x - self.previous_x, self.current_y - self.previous_y
