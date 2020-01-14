class Vehicle(object):
    """docstring"""
 
    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
    
    def brake(self):
        """
        Машина остановилась
        """
        return "Тормозит"
    
    def drive(self):
        """
        Машина едет
        """
        return " Я еду!"