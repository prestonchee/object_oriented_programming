class Vehicle:

    #class level attribute
    type = "ground"
    propulsion = "battery"



    def __init__(self, name, color, num_wheels, speed):
        self.name = name
        self.color = color
        self.num_wheels = num_wheels
        self.speed = speed  
        
        
    def print_details(self):
        print(self.name,'is',self.color, 'and is able to drive', self.speed, 'mph.')


    def paint_vehicle(self,new_color):
        self.color = new_color

bug_object = Vehicle("beetle","yellow",4,1) #object of vehicle class -- instance of vehicle class
turtle_object = Vehicle("turtlebot", "green",2,5)
rover_object = Vehicle("rover","purple",4,25)

bug_object.print_details()
# turtle_object.print_details()
# rover_object.print_details()

bug_object.paint_vehicle("blue")

bug_object.print_details()