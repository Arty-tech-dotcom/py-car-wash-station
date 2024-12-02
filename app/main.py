class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:  # List of Cars and return income as float
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                washing_cost = self.calculate_washing_price(car)
                income += washing_cost
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:  # Car object and return price as float
        price = car.comfort_class * (
                    self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:  # Car object and no return value
        car.clean_mark = min(car.clean_mark + 1, self.clean_power)

    def rate_service(self, rating: float) -> None:  # Rating as float and no return value
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating * (self.count_of_ratings - 1) + rating) / self.count_of_ratings, 1)
