class animal:
    sound="Animal Sound"
    br=""
    growth_factor=0
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=self.growth_factor
        
class landinganimals:
    @classmethod
    def breathe(cls):
        print("Breathe in air")
        
class wateranimals:
    @classmethod
    def breathe(cls):
        print("Breathe oxygen from water")
        
class hunting_animals:
    else_msg="No deers to hunt"
    name="Deer"
    def hunt(self,animals_object):
        c=0
        for i in animals_object.animals_in_given_zoo:
            if self.name in i:
                (animals_object.animals_in_given_zoo).remove(i)
                (animals_object.total_animals).remove(i)
                c+=1
        if c==0:
            print(self.else_msg)
        
class Deer(animal,landinganimals):
    sound="Buck Buck"
    br="Breathe in air"
    growth_factor=2
    
class Lion(animal,landinganimals,hunting_animals):
    sound="Roar Roar"
    growth_factor=4
    name="Deer"
    
class Shark(animal,wateranimals,hunting_animals):
    sound="Shark Sound"
    growth_factor=8
    name="GoldFish"
    else_msg='No GoldFish to hunt'

class GoldFish(animal,wateranimals):
    sound="Hum Hum"
    growth_factor=0.2
    
class Snake(animal,landinganimals,hunting_animals):
    sound="Hiss Hiss"
    growth_factor=0.5
    name='Deer'

class Zoo:
    total_animals=[]
    def __init__(self,reserved_food_in_kgs=0):
        self._reserved_food_in_kgs=reserved_food_in_kgs
        self.animals_in_given_zoo=[]
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    def add_animal(self,animal):
        (self.animals_in_given_zoo).append(type(animal).__name__)
        (self.total_animals).append(type(animal).__name__)
    def count_animals(self):
        return len(self.animals_in_given_zoo)
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.total_animals)
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
    def feed(self,animal):
        if self.reserved_food_in_kgs>0:
            self._reserved_food_in_kgs-=animal.required_food_in_kgs
            animal.grow()
    @staticmethod
    def count_animals_in_given_zoos(animals):
        count=0
        for i in animals:
            count+=i.count_animals()
        return count

nehru_zoological_park = Zoo()
zoo=Zoo()
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(lion)
nehru_zoological_park.add_animal(deer)
nehru_zoological_park.add_animal(lion)
#print(nehru_zoological_park.animals_in_given_zoo)
print(Zoo.count_animals_in_given_zoos([zoo,nehru_zoological_park]))
print(Zoo.count_animals_in_all_zoos())
lion.hunt(nehru_zoological_park)
print(Zoo.count_animals_in_given_zoos([zoo,nehru_zoological_park]))
print(Zoo.count_animals_in_all_zoos())