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

print('This vehicle is',bug_object.color, 'and is able to drive', bug_object.speed, 'mph.')
print('This vehicle is',turtle_object.color, 'and is able to drive', turtle_object.speed, 'mph.')
print('This vehicle is',rover_object.color, 'and is able to drive', rover_object.speed, 'mph.')