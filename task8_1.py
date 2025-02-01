class Teacher: 
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience
    
    def get_name(self):
        return self.__name
    
    def get_education(self):
        return self.__education
    
    def get_experience(self):
        return self.__experience
    
    def set_experience(self, new_experience):
        self.__experience = new_experience
    
    def get_teacher_data(self):
        data = f'{self.__name}, образование {self.__education}, опыт работы {self.__experience} года'
        return data
    
    def add_mark(self, name_student, rate_student):
        self.name_student = name_student
        self.rate_student = rate_student
        rate = f'{self.__name} поставил оценку {rate_student} студенту {name_student}'
        return rate
    
    def remove_mark(self, name_student, rate_student):
        self.name_student = name_student
        self.rate_student = rate_student
        rate = f'{self.__name} удалил оценку {rate_student} студенту {name_student}'
        return rate
    
    def give_a_consultation(self, consultations):
        self.consultations = consultations
        consultation = f'{self.__name} провел консультацию в классе {self.consultations}'
        return consultation
    
teacher1 = Teacher('Иван Петров', 'РГУ', 4)

print(teacher1.get_name())
print(teacher1.get_education())
print(teacher1.get_experience())
teacher1.set_experience(2)

print(teacher1.get_teacher_data())
print(teacher1.add_mark('Николай Попов', 5))
print(teacher1.remove_mark('Ангелина Скрябина', 3))
print(teacher1.give_a_consultation('9Б'))

