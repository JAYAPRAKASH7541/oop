'''class Deer:
    def __init__(self,age_in_months=1,breed="ELK",required_food_in_kgs=10):
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: 10")
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        self._type="deer"
    @property
    def type(self):
        return self._type
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    def make_sound(self):
        print("Buck Buck")
    def breathe(self):
        print("Breathe in air")
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=2
    def __str__(self):
        return '{} {} {}'.format(self.age_in_months,self.breed,self.required_food_in_kgs)
class Lion:
    def __init__(self,age_in_months=1,breed="African Lion",required_food_in_kgs=15):
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        self.type='lion'
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    def make_sound(self):
        print("Roar Roar")
    def breathe(self):
        print("Breathe in air")
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=4
    def hunt(self,list_of_animals):
        #print(len(list_of_animals.li))
        c=0
        for i in list_of_animals.li:
            if i.type=='deer':
                (list_of_animals.li).remove(i)
                c+=1
        if c==0:
            print("No deers to hunt")
    def __str__(self):
        return '{} {} {}'.format(self.age_in_months,self.breed,self.required_food_in_kgs)
class Shark:
    def __init__(self,age_in_months=1, breed="Hunter Shark", required_food_in_kgs=10):
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        self.type='shark'
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    def grow(self):
        self._required_food_in_kgs+=8
        self._age_in_months+=1
    def make_sound(self):
        print("Shark Sound")
    def breathe(self):
        print("Breathe oxygen from water")
    def hunt(self,list_of_animals):
        c=0
        for i in list_of_animals.li:
            if i.type=='goldfish':
                (list_of_animals.li).remove(i)
            if i.type=='deer':
                c+=1
        if c==0:
            print("No GoldFish to hunt")
    def __str__(self):
        return '{} {} {}'.format(self.age_in_months,self.breed,self.required_food_in_kgs)
class GoldFish:
    increase=0.2
    br="Breathe oxygen from water"
    def __init__(self,age_in_months=1, breed="Nemo", required_food_in_kgs=0.5):
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        self.type='goldfish'
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    def grow(self):
        self._required_food_in_kgs+=0.2
        self._age_in_months+=1
    def make_sound(self):
        print("Hum Hum")
    @classmethod
    def breathe(cls):
        print(cls.br)
    def __str__(self):
        return '{} {} {}'.format(self.age_in_months,self.breed,self.required_food_in_kgs)

count=0    
class Zoo:
    list=[]
    def __init__(self,reserved_food_in_kgs=0):
        self._reserved_food_in_kgs=reserved_food_in_kgs
        self.animals=''
        self.li=[]
    def add_animal(self,animal):
        self.animals+=str(animal)+'\n'
        self.li.append(animal)
        Zoo.list.append(animal)
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    def count_animals(self):
        return len(self.li)
    def feed(self,animal):
        if self.reserved_food_in_kgs>0:
            self._reserved_food_in_kgs-=animal.required_food_in_kgs
            animal.grow()
    @staticmethod
    def count_animals_in_given_zoos(lii):
        count=0
        count+=len(lii)
        return count
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.list)
class Snake:
    br='Breathe in air'
    def __init__(self,age_in_months=1, breed="Indian Cobra", required_food_in_kgs=5):
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        self.type='snake'
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    def grow(self):
        self._required_food_in_kgs+=0.5
        self._age_in_months+=1
    def make_sound(self):
        print("Hiss Hiss")
    @classmethod
    def breathe(cls):
        print(cls.br)
    def hunt(self,list_of_animals):
        c=0
        for i in list_of_animals.li:
            if i.type=='deer':
                (list_of_animals.li).remove(i)
                c+=1
        if c==0:
            print("No deers to hunt")
    def __str__(self):
        return '{} {} {}'.format(self.age_in_months,self.breed,self.required_food_in_kgs)'''
        
        
        
        
        
class Deer:
    sound='Buck Buck'
    inc=2
    br='Breathe in air'
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: 10")
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        self._type="deer"
    @property
    def type(self):
        return self._type
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
    @classmethod
    def breathe(cls):
        print(cls.br)
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=self.inc
    def __str__(self):
        return '{} {} {}'.format(self.age_in_months,self.breed,self.required_food_in_kgs)
class Lion(Deer):
    sound='Roar Roar'
    inc=4
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        self._type="lion"
    
    def hunt(self,list_of_animals):
        c=0
        for i in list_of_animals.li:
            if i.type=='deer':
                (list_of_animals.li).remove(i)
                c+=1
        if c==0:
            print("No deers to hunt")
class Shark(Deer):
    sound='Shark Sound'
    br="Breathe oxygen from water"
    inc=8
    def __init__(self,age_in_months=1,breed="ELK",required_food_in_kgs=10):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        self._type="lion"
    def hunt(self,list_of_animals):
        c=0
        for i in list_of_animals.li:
            if i.type=='goldfish':
                (list_of_animals.li).remove(i)
            if i.type=='deer':
                c+=1
        if c==0:
            print("No GoldFish to hunt")
class GoldFish(Deer):
    sound='Hum Hum'
    inc=0.2
    br="Breathe oxygen from water"
    def __init__(self,age_in_months=1,breed="ELK",required_food_in_kgs=10):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        self._type="goldfish"
class Snake(Deer):
    x=0
    sound='Hiss Hiss'
    inc=0.5
    #br="Breathe in air"
    def __init__(self,age_in_months=1,breed="ELK",required_food_in_kgs=10):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        self.type="snake"
    @classmethod
    def breathe(cls):
        print(cls.br) 
    def hunt(self,list_of_animals):
        c=0
        for i in list_of_animals.li:
            if i.type=='deer':
                (list_of_animals.li).remove(i)
                c+=1
        if c==0:
            print("No deers to hunt")
    @classmethod
    def count_animals_in_Snake(cls):
        cls.x+=1
        return len(cls.x)
class Zoo:
    list=[]
    def __init__(self,reserved_food_in_kgs=0):
        self._reserved_food_in_kgs=reserved_food_in_kgs
        self.li=[]
    def add_animal(self,animal):
        self.li.append(animal)
        Zoo.list.append(animal)
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs+=food
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    def count_animals(self):
        return len(self.li)
    def feed(self,animal):
        if self.reserved_food_in_kgs>0:
            self._reserved_food_in_kgs-=animal.required_food_in_kgs
            animal.grow()
    @staticmethod
    def count_animals_in_given_zoos(lii):
        c=0
        for i in lii:
            print(i)
            c+=i.count_animals()
        return c
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.list)
zoo=Zoo()
nehru_zoological_park = Zoo()
zoo.add_food_to_reserve(10000000)
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
nehru_zoological_park.add_animal(lion)
print(nehru_zoological_park.count_animals())
zoo.add_animal(lion)
zoo.add_animal(lion)
print(Zoo.count_animals_in_all_zoos())

print(Zoo.count_animals_in_given_zoos([zoo]))