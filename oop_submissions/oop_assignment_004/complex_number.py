import math
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        if type(real_part) is str and type(imaginary_part) is str:
            raise ValueError("Invalid value for real and imaginary part")
        if type(real_part) is str:
            raise ValueError("Invalid value for real part")
        if type(imaginary_part) is str:
                raise ValueError("Invalid value for imaginary part")
        else:
            self.real_part=real_part
            self.imaginary_part=imaginary_part
        
    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)
    def __str__(self):
        return '{}{:+}i'.format(self.real_part,self.imaginary_part)
    def __add__(self,other):
        obj=ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)
        return obj
    def __sub__(self,other):
        obj=ComplexNumber(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)
        return obj
    def __mul__(self,other):
        obj=ComplexNumber(self.real_part*other.real_part + self.imaginary_part*other.imaginary_part,
                       self.imaginary_part*other.real_part + self.real_part*other.imaginary_part)
        return obj
    def __truediv__(self,other):
        '''k=float(other.real_part**2+other.imaginary_part**2)
        
        obj=ComplexNumber((((self.real_part*other.real_part)+(self.imaginary_part*other.imaginary_part))/k),((self.imaginary_part*other.real_part)-(self.real_part*other.imaginary_part))/k)
        return obj'''
        k=float(other.real_part**2+other.imaginary_part**2)
        other.imaginary_part=-other.imaginary_part
        complex_division=self*other
        return ComplexNumber(complex_division.real_part/k,complex_division.imaginary_part/k)

    def __eq__(self,other):
        return self.real_part==other.real_part and self.imaginary_part==other.imaginary_part
    def __abs__(self):
        x=self.real_part**2+self.imaginary_part**2
        return round(math.sqrt(x),3)
        
print(ComplexNumber(1,2) == ComplexNumber(1,2))

print(ComplexNumber(2,1) == ComplexNumber(1,2))
one_plus_two_i = ComplexNumber(1,2)
three_plus_four_i = ComplexNumber(3,4)
minus_five_plus_ten_i = one_plus_two_i * three_plus_four_i
print(minus_five_plus_ten_i)