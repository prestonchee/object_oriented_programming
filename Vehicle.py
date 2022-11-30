class Vehicle:
    pass

bug_object = Vehicle() #object of vehicle class -- instance of vehicle class
turtle_object = Vehicle()
rover_object = Vehicle()

bug_object.color = "yellow"
bug_object.num_wheels = 4
bug_object.speed = 1

turtle_object.color = "green"
turtle_object.num_wheels = 2
turtle_object.speed = 5

rover_object.color = "purple"
rover_object.num_wheels = 4
rover_object.speed = 25

print(bug_object.speed)
print(turtle_object.speed)
print(rover_object.speed)