#Car object
class Car:
    #Class Attributes
    wheels = 4
    # initializer
    def  __init__(self, brand, style, make, model, year, color):
        self.brand = brand
        self.style = style
        self.make = make
        self.model = model
        self.year = year
        self.color = color
