#Class - logical representation of things 
class Student:
    a=10
    def showA(self):   #instance function
        print("Im in showA")
    def showB(a):
        print("Im in showA")

if __name__ == '__main__':
    obj=Student()
    obj.showA(11,22)
    Student.showB(22)