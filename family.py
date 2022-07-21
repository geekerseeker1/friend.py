class Hira:
    pass


class ABC:
    pass


class XYZ:
    pass


class Family:

    # initialize the attributes
    def __init__(self, total_members=4, father_name=Hira, mother_name=ABC, spouse_name=XYZ):
        self.__name = total_members
        self.__father = father_name
        self.__mother = mother_name
        self.__spouse = spouse_name
