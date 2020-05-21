class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        if type(self.real_part) is str:
            raise ValueError("Invalid value for real part")
        if type(self.imaginary_part) is str:
            raise ValueError("Invalid value for imaginar part")
    def conjugate(self):
        return self.real_part,-self.imaginary_part
    def __str__(self):
        return "self.real_part,self.imaginary_part"
one_plus_two_i = ComplexNumber(1,2)
one_minus_two_i = one_plus_two_i.conjugate()
print(one_plus_two_i)

print(one_minus_two_i)

