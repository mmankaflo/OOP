# Question 1

# --- Base Class ---
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self._storage = storage
        self._battery = battery

    def get_specs(self):
        return f"{self.brand} {self.model} - Storage: {self._storage}GB, Battery: {self._battery}mAh"

    def charge(self):
        return f"{self.model} is charging... 🔋"

    def use_app(self, app_name):
        return f"{self.model} is running {app_name} 📱"

    def get_battery(self):
        return self._battery

    def set_battery(self, new_battery):
        if new_battery > 0:
            self._battery = new_battery
        else:
            print("Invalid battery capacity.")


# --- Subclass: Gaming Smartphone ---
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def use_app(self, app_name):
        return f"{self.model} launches {app_name} in high-performance gaming mode 🎮"

    def activate_cooling(self):
        return f"{self.model}'s {self.cooling_system} is keeping it cool 🧊"


# --- Subclass: Camera Smartphone ---
class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_resolution):
        super().__init__(brand, model, storage, battery)
        self.camera_resolution = camera_resolution

    def use_app(self, app_name):
        return f"{self.model} opens {app_name} with enhanced camera features 📸"

    def take_photo(self):
        return f"{self.model} takes a photo at {self.camera_resolution}MP resolution"


# --- Testing the Classes ---
if __name__ == "__main__":
    phone1 = GamingSmartphone("ROG", "Phone 6", 256, 6000, "Vapor Chamber Cooling")
    phone2 = CameraSmartphone("Pixel", "7 Pro", 128, 5000, 50)

    print(phone1.get_specs())
    print(phone1.use_app("PUBG Mobile"))
    print(phone1.activate_cooling())

    print(phone2.get_specs())
    print(phone2.use_app("Camera"))
    print(phone2.take_photo())

    # Encapsulation test
    phone1.set_battery(6500)
    print(f"Updated battery: {phone1.get_battery()} mAh")

#Question 2

# --- Base Class ---
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement the move method.")

# --- Subclasses ---
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying through the sky ✈️"
    
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling forward 🚴‍♂️"

class Boat(Vehicle):
    def move(self):
        return "Sailing on water 🚢"

class Train(Vehicle):
    def move(self):
        return "Running on tracks 🚆"


# --- Polymorphism Demo ---
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat(), Train(), Bicycle()]

    for vehicle in vehicles:
        print(vehicle.move())
