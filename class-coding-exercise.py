class Animal:
    """Animal class"""
    def __init__(self, name, type):
        print('Initializing name and type')
        self.__name = name
        self.__type = type      

    @property
    def name(self):
        print('Getting name')
        return self.__name

    @property
    def type(self):
        print('Getting type')
        return self.__type

    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name

    @type.setter
    def type(self, new_type):
        print('Setting type')
        self.__name = new_type

    @name.deleter
    def name(self):    
        print('Deleting name')
        del self.__name

    @type.deleter
    def type(self):    
        print('Deleting type')
        del self.__type

    def move(self):
        print('Moving')

    def eat(self):
        print('Eating')

    def sleep(self):
        print('Sleeping')

class Book:
    """Book Class"""
    def __init__(self, name, author):
        print('Initializing name and author')
        self.__name = name
        self.__author = author      

    @property
    def name(self):
        print('Getting name')
        return self.__name

    @property
    def author(self):
        print('Getting author')
        return self.__author

    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name

    @author.setter
    def author(self, new_author):
        print('Setting type')
        self.__name = new_author

    @name.deleter
    def name(self):    
        print('Deleting name')
        del self.__name

    @author.deleter
    def author(self):    
        print('Deleting type')
        del self.__author

    def print(self):
        print('Printing')

    def sell(self):
        print('Selling')

class Vehicle:
    """Vehicle Class"""
    def __init__(self, name, year):
        print('Initializing Vehicle and Year')
        self.__name = name
        self.__year = year      

    @property
    def name(self):
        print('Getting name')
        return self.__name

    @property
    def year(self):
        print('Getting Year')
        return self.__year

    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name

    @year.setter
    def year(self, new_year):
        print('Setting type')
        self.__year = new_year

    @name.deleter
    def name(self):    
        print('Deleting name')
        del self.__name

    @year.deleter
    def year(self):    
        print('Deleting year')
        del self.__year

    def Move(self):
        print('Moving')

    def sell(self):
        print('Selling')
