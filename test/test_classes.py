from src.person import Person

class TestPersonIvan:
    ivan = Person("Ivan")
    ivans_data = ["data"]

    def test_ivan(self):
        print(self.ivans_data)
        assert self.ivan.is_data_scientist

class TestPersonGeorge:
    george = Person("Ivan")
    georges_data = ["private stuff"]

    def test_george(self):
        print(self.georges_data)
        assert self.george.is_data_scientist