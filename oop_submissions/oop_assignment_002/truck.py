from car import Car
class Truck(Car):
    sound="Honk Honk"
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self.max_cargo_weight=max_cargo_weight
        self._loads=0
    @property
    def loads(self):
        return self._loads
    def load(self,cargo_weight):
        if cargo_weight<0:
            raise ValueError("Invalid value for cargo_weight")
        
        if self.loads+cargo_weight<=self.max_cargo_weight:
            if self.current_speed==0:
                self._loads+=cargo_weight
            else:
                print("Cannot load cargo during motion")
        elif self.loads+cargo_weight>self.max_cargo_weight:
            if self.current_speed==0:
                print("Cannot load cargo more than max limit:",self.max_cargo_weight)
            else:
                print("Cannot load cargo during motion")
    def unload(self,cargo_weight):
        if cargo_weight<0:
            raise ValueError("Invalid value for cargo_weight")
        if cargo_weight<=self.max_cargo_weight:
            if self.current_speed==0:
                self._loads-=cargo_weight
            else:
                print("Cannot unload cargo during motion")
