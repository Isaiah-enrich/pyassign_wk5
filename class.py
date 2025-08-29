# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def power_on(self):
        return f"{self.brand} {self.model} is now ON!"
    
    def power_off(self):
        return f"{self.brand} {self.model} is now OFF!"


# Child class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        # Call parent constructor
        super().__init__(brand, model)
        self.os = os
        self.storage = storage
    
    def take_photo(self):
        return f"{self.brand} {self.model} takes a photo 📸"
    
    def install_app(self, app_name):
        return f"{app_name} has been installed on {self.brand} {self.model}"


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", "Android", "256GB")
phone2 = Smartphone("Apple", "iPhone 15", "iOS", "512GB")

# Test methods
print(phone1.power_on())
print(phone1.take_photo())
print(phone2.install_app("WhatsApp"))
print(phone2.power_off())
