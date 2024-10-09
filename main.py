class employee:
    def __init__(self):
        print("Employee object created")
    def __del__(self):
        print("Employee object destroyed")
def create_obj():
    print("Making an object")
    employee1=employee()
    return employee1
employee1=create_obj()