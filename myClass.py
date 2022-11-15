import random

myL2 = [ 'Ferrari', 'Lambourgini', 'Aston MArtin', 'WRX']

class GetCarModel:
    def __init__(self, model_name):
        self._model_name = model_name

    # Getter def
    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, new_name):
        if new_name in myL2:
            self._model_name = new_name
        else:
            raise ValueError (f'{new_name} is not part of {myL2}')

    @staticmethod
    def get_random_car():
        print (f'Randomly chosen : {random.choice(myL2)}')



myL = [ 'Rick Ross', 'Future', 'Ricky Rose', 'MnM']
















class TrepArtist:
    def __init__(self, name):
        self._name = name

    ## This is the getter property
    @property
    def name(self):
        return self._name


    ## To set the name use the setter property
    ## We use the setter to ensure proper input
    @name.setter
    def name(self, name):
        if name in myL:
            self._name = name
        else:
            raise ValueError(f'name needs to be in {myL}')


    ## Now have a static method an independednt function in the class
    @staticmethod
    def randomArtist():
        return TrepArtist(random.choice(myL))











class TestClass:
    def __init__ (self, some_val):
        self._val = some_val

    def Print_val(self):
        return self._val






