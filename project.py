class DelivSys:
    def __init__(self):
        self.driv_list = []
        self.city_dict = {}
        self.driv_id_count = 1

    def gen_driv_id(self):
        driv_id = "ID" + str(self.driv_id_count).zfill(3)
        self.driv_id_count += 1
        return driv_id

    def main_menu(self):
        print("Hello! Please enter:")
        print("1. To go to the drivers' menu")
        print("2. To go to the cities' menu")
        print("3. To exit the system")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.driv_menu()
        elif choice == '2':
            self.city_menu()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
            self.main_menu()

    def driv_menu(self):
        print("Drivers' Menu")
        print("1. To view all the drivers")
        print("2. To add a driver")
        print("3. To check similar drivers")
        print("4. To go back to the main menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.view_driv()
        elif choice == '2':
            self.add_driv()
        elif choice == '3':
            self.similar_driv()
        elif choice == '4':
            self.main_menu()
        else:
            print("Invalid choice. Please try again.")
            self.driv_menu()

    def view_driv(self):
        if not self.driv_list:
            print("No drivers available.")
        else:
            for driv in self.driv_list:
                print(driv['id'] + ", " + driv['name'] + ", " + driv['start_city'])
        self.driv_menu()

    def add_driv(self):
        name = input("Enter the driver's name: ")
        start_city = input("Enter the starting city of the driver: ")
        if start_city not in self.city_dict:
            add_city = input("The city '" + start_city + "' is not in the database. Do you want to add it? (yes/no): ")
            if add_city.lower() == 'yes':
                self.city_dict[start_city] = []
        if start_city in self.city_dict:
            new_id = self.gen_driv_id()
            self.driv_list.append({
                "id": new_id,
                "name": name,
                "start_city": start_city
            })
            print("Driver " + name + " added successfully with ID " + new_id + ".")
        else:
            print("City was not added. Driver cannot be created.")
        self.driv_menu()

    def similar_driv(self):
        city_driv = {}
        for driv in self.driv_list:
            city = driv["start_city"]
            if city not in city_driv:
                city_driv[city] = []
            city_driv[city].append(driv["name"])
        for city, driv in city_driv.items():
            print(city + ": " + ", ".join(driv))
        self.driv_menu()

    def city_menu(self):
        print("Cities' Menu")
        print("1. To show all cities")
        print("2. To search for a city")
        print("3. To print neighboring cities")
        print("4. To print drivers delivering to a city")
        print("5. To go back to the main menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.view_city()
        elif choice == '2':
            self.search_city()
        elif choice == '3':
            self.neighbor_city()
        elif choice == '4':
            self.driv_for_city()
        elif choice == '5':
            self.main_menu()
        else:
            print("Invalid choice. Please try again.")
            self.city_menu()

    def view_city(self):
        if not self.city_dict:
            print("No cities available.")
        else:
            sorted_city = sorted(self.city_dict.keys(), reverse=True)
            print("Cities: " + ", ".join(sorted_city))
        self.city_menu()

    def search_city(self):
        key = input("Enter search key for city: ")
        match_city = [city for city in self.city_dict if key.lower() in city.lower()]
        if match_city:
            print("Matching cities: " + ", ".join(match_city))
        else:
            print("No cities found with the given key.")
        self.city_menu()

    def neighbor_city(self):
        city_name = input("Enter the city name to see its neighbors: ")
        if city_name in self.city_dict:
            neighbors = self.city_dict[city_name]
            if neighbors:
                print("Neighboring cities for " + city_name + ": " + ", ".join(neighbors))
            else:
                print("There are no neighboring cities for " + city_name + ".")
        else:
            print("The city '" + city_name + "' is not in the database.")
        self.city_menu()

    def driv_for_city(self):
        target_city = input("Enter the city name to see drivers delivering there: ")
        driv_to_city = self.find_driv(target_city)
        if driv_to_city:
            print("Drivers delivering to " + target_city + ": " + ", ".join(driv_to_city))
        else:
            print("No drivers found delivering to " + target_city + ".")
        self.city_menu()

    def find_driv(self, city_name):
        visited_city = set()
        driv_to_city = []
        for driv in self.driv_list:
            if self.can_reach(driv["start_city"], city_name, visited_city):
                driv_to_city.append(driv["name"])
        return driv_to_city

    def can_reach(self, cur_city, target_city, visited_city):
        if cur_city == target_city:
            return True
        if cur_city in visited_city:
            return False
        visited_city.add(cur_city)
        for neighbor in self.city_dict.get(cur_city, []):
            if self.can_reach(neighbor, target_city, visited_city):
                return True
        return False

if __name__ == "__main__":
    system = DelivSys()
    system.main_menu()