class Base:
    def __init__(self, _val):
        self._base = _val


    @property
    def get_val_b(self):
        return self._base


class Child1(Base):
    def __init__(self, _val):
        super().__init__(_val)
        self._val = _val *2

    @property
    def get_val_c1(self):
        return self._val


class Child2(Child1):
    def __init__(self, _val):
        super().__init__(_val)
        self._val = _val*3

    @property
    def get_val_c2(self):
        return self._val