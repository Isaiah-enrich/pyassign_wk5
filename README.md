Assignment 1: Design Your Own Class

I created a Smartphone class that inherits from a Device parent class.

Features

Attributes: brand, model, OS, storage

Methods: power_on(), power_off(), take_photo(), install_app()

Inheritance: Smartphone extends Device

Example
phone1 = Smartphone("Samsung", "Galaxy S23", "Android", "256GB")
print(phone1.power_on())       # Samsung Galaxy S23 is now ON!
print(phone1.take_photo())     # Samsung Galaxy S23 takes a photo 📸

🎭 Activity 2: Polymorphism Challenge

I created a Vehicle base class and subclasses (Car, Plane, Boat) that all define a move() method differently.

Example
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    print(v.move())

Output
Driving 🚗
Flying ✈️
Sailing 🚤

🚀 How to Run

Save the Python code in a file, e.g., assignment.py

Run it in your terminal:

python assignment.py

📚 Concepts Demonstrated

Encapsulation: Keeping attributes & methods inside a class

Inheritance: Smartphone inherits from Device

Polymorphism: Different move() implementations for vehicles
