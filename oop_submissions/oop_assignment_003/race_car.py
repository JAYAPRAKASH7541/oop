import math
from car import Car
class RaceCar(Car):
    Car.sound="Peep Peep\nBeep Beep"
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._nitro=0
    @property
    def nitro(self):
        return self._nitro
    def apply_brakes(self):
        if self.current_speed>(self.max_speed//2):
            self._nitro+=10
        super().apply_brakes()
    def accelerate(self):
        super().accelerate()
        if self.nitro>0 and self.is_engine_started==True:
            percentage=math.ceil(self.acceleration*0.3)
            self._current_speed+=percentage
            self._nitro-=10
        if self.current_speed>self.max_speed:
            self._current_speed=self.max_speed
    