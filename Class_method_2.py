class Color:
    colors = []
    def __init__(self, color):
        self.add_color(color)

    @classmethod
    def add_color(cls, color):
        if color not in cls.colors:
            cls.colors.append(color)
    @classmethod
    def show_colors(cls):
        return cls.colors


c1 = Color("red")
c2 = Color("blue")
c3 = Color("red")

print(Color.show_colors())