class Restaurant: #создаем класс с помощью метода init с двумя аргументами
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self): #метод describe_restaurant выводит название ресторана и тип кухни
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self): #выводит сообщение о том, что ресторан открыт в данный момент
        print("The restaurant is open.")

newRestaurant = Restaurant(input(),input())

print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant() #отвечает за описание ресторана
newRestaurant.open_restaurant() #выводит сообщение о том, что ресторан открыт


restaurant1 = Restaurant("Хачапури и вино", "Грузинская")
restaurant2 = Restaurant("Taco", "Мексиканская")
restaurant3 = Restaurant("Вкусно и точка", "Фастфуд")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
        print(f"The rating is {self.rating}.")

    def update_rating(self, new_rating):
        self.rating = new_rating
        return self.rating

restaurant1 = Restaurant("Хачапури и вино", "Грузинская")

restaurant1.describe_restaurant()

new_rating = restaurant1.update_rating(4.8)
print(f"The new rating is {new_rating}.")