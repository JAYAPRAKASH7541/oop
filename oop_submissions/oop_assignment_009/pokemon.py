'''class pokemon:
    sound="Pika Pika"
    running="Pikachu running..."
    inc=10
    def __init__(self,name,level=1):
        if type(name) is str and len(name)>0:
            self._name=name
        else:
            raise ValueError("name cannot be empty")
        if level<=0:
            raise ValueError("level should be > 0")
        self._level=level
        self.masters='No Master'
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    @classmethod
    def run(cls):
        print(cls.running)
    @property
    def master(self):
        if self.masters!='No Master':
            return self.masters
        else:
            print("No Master")
    def attack(self):
        print("Electric attack with {} damage".format(self.inc*self.level))
    def __str__(self):
        return '{} - Level {}'.format(self.name,self.level)
class Pikachu(pokemon):
    inc=10
    sound="Pika Pika"
    running="Pikachu running..."
class swim_animals:
    naming="Squirtle"
    @classmethod
    def swim(self):
        print('{} swimming...'.format(self.naming))
class Squirtle(pokemon,swim_animals):
    sound="Squirtle...Squirtle"
    running="Squirtle running..."
    naming='Squirtle'
    inc=9
    def attack(self):
        print("Water attack with {} damage".format(9*self.level))
class water_pokemons:
    sound="Pidgey...Pidgey"
    flying="Pidgey flying..."
    inc=5
    def __init__(self,name,level=1):
        #print(name)
        if type(name) is str and len(name)>0:
            self._name=name
        else:
            raise ValueError("name cannot be empty")
        if level<=0:
            raise ValueError("level should be > 0")
        self._level=level
        self.masters='No Master'
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    @classmethod
    def fly(cls):
        print(cls.flying)
    @property
    def master(self):
        if self.masters!='No Master':
            return self.masters
        else:
            print("No Master")
    def attack(self):
        print("Air attack with {} damage".format(self.level*self.inc))
    def __str__(self):
        return '{} - Level {}'.format(self.name,self.level)
class Pidgey(water_pokemons):
    sound="Pidgey...Pidgey"
    flying="Pidgey flying..."
    inc=5
    #name='Swanna'
class Swanna(water_pokemons,swim_animals):
    naming='Swanna'
    sound="Swanna...Swanna"
    flying="Swanna flying..."
    inc=9
    def attack(self):
        print("Water attack with {} damage".format(self.level*9))
        print("Air attack with {} damage".format(self.level*5))
        #super().attack()
class Zapdos(water_pokemons):
    sound="Zap...Zap"
    flying="Zapdos flying..."
    def attack(self):
        print("Electric attack with {} damage".format(self.level*10))
        print("Air attack with {} damage".format(self.level*5))

class Island:
    li=[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self.li.append(self)
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    @property
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    def __str__(self):
        return '{} - {} pokemon - {} food'.format(self.name,self.pokemon_left_to_catch,self.total_food_available_in_kgs)
    def add_pokemon(self,pokemon):
        
        if self.pokemon_left_to_catch<self.max_no_of_pokemon:
            self._pokemon_left_to_catch+=1
            
        else:
            print("Island at its max pokemon capacity")
    @classmethod
    def get_all_islands(cls):
        return cls.li
class Trainer:
    x=0
    def __init__(self,name,experience=100,max_food_in_bag=1,food_in_bag=0):
        self._name=name
        self._experience=experience

        self._max_food_in_bag=10*experience
        self._food_in_bag=food_in_bag
        self.catched_animals=[]
    @property
    def name(self):
        return self._name
    @property
    def experience(self):
        return self._experience
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    @property
    def food_in_bag(self):
        return self._food_in_bag
    
    def catch(self,pokemon):
        if self.experience>=pokemon.level*100:
            self._experience+=(pokemon.level*20)
            (self.catched_animals).append(pokemon)
            print("You caught Pigetto")
            pokemon.masters=self
        else:
            print("You need more experience to catch Pigetto")
        
    def move_to_island(self,island):
        self.island=island
        self.x+=1
    @property
    def current_island(self):
        if self.x!=0:
            return self.island
        else:
            print("You are not on any island")
    def collect_food(self):
        if self.x!=0:
            if self.island.total_food_available_in_kgs<self.experience:
                self._food_in_bag+=self.island._total_food_available_in_kgs
                self.island._total_food_available_in_kgs=0
            elif self.food_in_bag<self.max_food_in_bag:
                self._food_in_bag+=(self.experience)*10
                self.island._total_food_available_in_kgs-=(self.experience)*10
        else:
            print("Move to an island to collect food")
    def get_my_pokemon(self):
        return (self.catched_animals)
    def __str__(self):
        return '{}'.format(self.name)'''




        
class pokemon:
    sound="Pika Pika"
    inc=10
    type_of_attack='Electric'
    def __init__(self,name,level=1):
        if len(name)>0:
            self._name=name
        else:
            raise ValueError("name cannot be empty")
        if level<=0:
            raise ValueError("level should be > 0")
        self._level=level
        self.masters='No Master'
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
    @classmethod
    def make_sound(cls):
        print(cls.sound) 
    @property
    def master(self):
        if self.masters!='No Master':
            return self.masters
        else:
            print("No Master")
    def attack(self):
        print("{} attack with {} damage".format(self.type_of_attack,self.inc*self.level))
    def __str__(self):
        return '{} - Level {}'.format(self.name,self.level)
class running_pokemons:
    running='Pikachu running...'
    @classmethod
    def run(cls):
        print(cls.running)

class swim_animals:
    naming="Squirtle"
    @classmethod
    def swim(self):
        print('{} swimming...'.format(self.naming))
class flying_pokemons:
    flying="Pidgey flying..."
    @classmethod
    def fly(cls):
        print(cls.flying)
class Pikachu(pokemon,running_pokemons):
    inc=10
    sound="Pika Pika"
    running="Pikachu running..."
class Squirtle(pokemon,swim_animals,running_pokemons):
    sound="Squirtle...Squirtle"
    running="Squirtle running..."
    naming='Squirtle'
    inc=9
    type_of_attack='Water'
class Pidgey(pokemon,flying_pokemons):
    sound="Pidgey...Pidgey"
    flying="Pidgey flying..."
    inc=5
    type_of_attack='Air'
class Swanna(pokemon,flying_pokemons,swim_animals):
    naming='Swanna'
    sound="Swanna...Swanna"
    flying="Swanna flying..."
    inc=5
    type_of_attack='Air'
    def attack(self):
        print("Water attack with {} damage".format(self.level*9))
        super().attack()
class Zapdos(pokemon,flying_pokemons):
    sound="Zap...Zap"
    flying="Zapdos flying..."
    inc=5
    type_of_attack='Air'
    def attack(self):
        print("Electric attack with {} damage".format(self.level*10))
        super().attack()
class Island:
    li=[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self.li.append(self)
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    @property
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    def __str__(self):
        return '{} - {} pokemon - {} food'.format(self.name,self.pokemon_left_to_catch,self.total_food_available_in_kgs)
    def add_pokemon(self,pokemon):
        if self.pokemon_left_to_catch<self.max_no_of_pokemon:
            self._pokemon_left_to_catch+=1
        else:
            print("Island at its max pokemon capacity")
    @classmethod
    def get_all_islands(cls):
        return cls.li
class Trainer:
    x=0
    def __init__(self,name,experience=100,max_food_in_bag=1,food_in_bag=0):
        self._name=name
        self._experience=experience

        self._max_food_in_bag=10*experience
        self._food_in_bag=food_in_bag
        self.catched_animals=[]
    @property
    def name(self):
        return self._name
    @property
    def experience(self):
        return self._experience
    @property
    def max_food_in_bag(self):
        #return self._max_food_in_bag
        return self.experience*10
    @property
    def food_in_bag(self):
        return self._food_in_bag
    
    def catch(self,pokemon):
        if self.experience>=pokemon.level*100:
            self._experience+=(pokemon.level*20)
            (self.catched_animals).append(pokemon)
            print("You caught {}".format(pokemon.name))
            pokemon.masters=self
        else:
            print("You need more experience to catch {}".format(pokemon.name))
        
    def move_to_island(self,island):
        self.island=island
        self.x+=1
    @property
    def current_island(self):
        if self.x!=0:
            return self.island
        else:
            print("You are not on any island")
    def collect_food(self):
        if self.x!=0:
            if self.island.total_food_available_in_kgs<self.max_food_in_bag:
                self._food_in_bag+=self.island._total_food_available_in_kgs
                self.island._total_food_available_in_kgs=0
            elif self.food_in_bag<self.max_food_in_bag:
                self._food_in_bag+=(self.experience)*10
                self.island._total_food_available_in_kgs-=(self.experience)*10
        else:
            print("Move to an island to collect food")
    def get_my_pokemon(self):
        return (self.catched_animals)
    def __str__(self):
        return '{}'.format(self.name)

my_pikachu = Swanna(name="Ryan", level=1)
print(my_pikachu.name)
#Ryan
print(my_pikachu.level)
#1
print(my_pikachu)
#Ryan - Level 1

my_pikachu.make_sound()  # Print
#Pika Pika
#my_pikachu.run()  # Print
#Pikachu running...
my_pikachu.attack()  # Print