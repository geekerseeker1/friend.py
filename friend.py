class Friend:

    #initialize the attributes
    def __init__(self, name, address, is_alone, lives_in_hostel):
        self.__name = name
        self.__address = address
        self.__is_alone = is_alone
        self.__lives_in_hostel = lives_in_hostel

    #set the attributes
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_is_alone(self, is_alone):
        self.__is_alone = is_alone

    def set_lives_in_hostel(self, lives_in_hostel):
        self.__lives_in_hostel = lives_in_hostel

    #return the attributes
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_is_alone(self):
        return self.__is_alone

    def get_lives_in_hostel(self):
        return self.__lives_in_hostel

    #return the objects state as a string

    def __str__(self):
        return 'Name: ' + self.__name + \
               '\nAddress : ' + self.__address + \
               '\nIs_alone: ' + self.__is_alone + \
               '\nLives_in_hostel: ' + self.__lives_in_hostel