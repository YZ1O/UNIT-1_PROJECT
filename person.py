class Person:
    def __init__(self,id:str,name:str,gender:str):
        pass
            
    def set_id(self,id:str)-> str:
        self.__id = id

    def get_id(self):
        return self.__id
 
    def set_name(self,name:str)-> str:
        self.__name = name

    def get_name(self):
        return self.__name
     
    def set_gender(self,gender:str)-> str:
        self.__gender = gender

    def get_gender(self):
        return self.__gender

#Class_Method
    def verify_info(self,id,name, gender):
        while len(id) != 10 or not id.isdigit:
            id = input("Enter a valid id: ")
        self.set_id(id)
        #######################################
        while len(name) < 3 :
            name = input("Enter a valid name: ")
        self.set_name(name)
        #######################################
        while len(gender) < 4 or len(gender) > 6 :
            gender = input("Enter a valid gender: ")
        print('the information has be saved!'.upper())
        self.set_gender(gender)

    def get_person_info(self):
        return f'ID : {self.get_id()} NAME : {self.get_name()} GENDER : {self.get_gender()}'
