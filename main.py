import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 15
print(classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week/classes_per_week)
print(cost_per_class, type(cost_per_class))
print("Damn you are wasting", cost_per_class, "units every class!")
#technically the other variables were already there so I only have to print and type the two I made myself? 
#syntax is to create variable just type the name and set it equal to something (can be calculated based on another variable), to print it just do print(), can print variables and strings together need to have a comma in between and it automatically inserts spaces too

#Part B
locations_to_get_food_poisoning_from = ["Hinman", "Appalachian", "C4", "Marketplace"]
dining_hall = random.choice(locations_to_get_food_poisoning_from)
food_poisoning_symptoms = ["throwing up","emptying your guts"]
symptom = random.choice(food_poisoning_symptoms)
print("You are", symptom, "because you ate at", dining_hall, "!!!!!")