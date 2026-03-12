class AnyClass:
    value_in_class = None
    def __init__(self, value_in_constructor):
        self.value_in_constructor = value_in_constructor
        self.value_in_method = None
        just_value_in_method = self.value_in_class
        just_value_in_method = AnyClass.value_in_class

    def other_method(self):
        self.other_method_value = None
        pass


example_class = AnyClass(value_in_constructor=100)