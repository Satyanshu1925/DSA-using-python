'''
#python class 
What - A class is a blueprint for creating objects.
Why -   Easier Maintenance => if we need to change something in the code it's can be easily done in class 
        Reusability => we can create same class to create alot of 



'''
### 
class car:

    #python constructor 
    def __init__(self, color, model, year):
        # this is python constructor 
        self.color = color
        self.model = model
        self.year = year


    def show_details(self):
        print(f"Car Details: {self.color} {self.model} ({self.year})")
    
    
    def change_color(object, new_color):  # Here, we're using 'object' instead of 'self'
        object.color = new_color
        print(f"The car color is now {object.color}")
    

    def start(self):
        print(f"The {self.color} {self.model} is starting.")
   

    def accelerate(object, speed):  # Using 'object' again
        print(f"The {object.color} {object.model} is now going at {speed} km/h.")



# object in 
my_car = Car("yellow", "Ford Mustang", 2021)

# Using methods with both 'self' and 'object'
my_car.show_details()  # Uses 'self' (works fine)
my_car.change_color("blue")  # Uses 'object' (also works fine)
my_car.start()  # Uses 'self' (works fine)
my_car.accelerate(60)  # Uses 'object' (works fine)