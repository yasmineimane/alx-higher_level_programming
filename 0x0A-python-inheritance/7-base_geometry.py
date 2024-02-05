#!/usr/bin/python3
'''Module of BaseGeometry class.'''


class BaseGeometry:
    '''Defines BaseGeometry class.'''
    def area(self):
        '''Method to compute this area.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Method to validate value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
