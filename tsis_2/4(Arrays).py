cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
cars[0] = "Toyota"


x = len(cars)


for x in cars:
    print(x)
    

cars.append("Honda") # Adding


cars.pop(1) # Removing 2nd element

cars.remove("Volvo")