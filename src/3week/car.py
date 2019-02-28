import csv
import os


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        if car_type in ("car", "truck", "spec_machine"):
            self.car_type = car_type
            self.brand = str(brand)
            self.photo_file_name = str(photo_file_name)
            self.carrying = float(carrying)
        else:
            return None

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_width = 0
        self.body_height = 0
        self.body_length = 0
        try:
            whl = str(body_whl).split("x")
            self.body_width = float(whl[0])
            self.body_height = float(whl[1])
            self.body_length = float(whl[2])
        except (IndexError, ValueError):
            pass


    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = str(extra)


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                car_type = row[0]
                if car_type == "car":
                    car = Car(row[0], row[1], row[3], row[5], row[2])
                    car_list.append(car)
                if car_type == "truck":
                    truck = Truck(row[0], row[1], row[3], row[5], row[4])
                    car_list.append(truck)
                if car_type == "spec_machine":
                    spec_machine = SpecMachine(row[0], row[1], row[3], row[5], row[6])
                    car_list.append(spec_machine)
            except IndexError:
                pass

    return car_list

csvfile="_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv"
print(get_car_list(csvfile))