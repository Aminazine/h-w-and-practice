# 34. Создать класс Транспортное средство и его потомков - классы Поезд и Самолет.

class Vehicle(object):

    def __init__(self, vehicle_brand, numb_of_passengers, average_speed, distance):
        self.vehicle_brand = vehicle_brand
        self.numb_of_passengers = numb_of_passengers
        self.average_speed = average_speed
        self.distance = distance

    def travel_time(self):
        return self.distance / self.average_speed


class Traine(Vehicle):

    def __init__(self, vehicle_brand, numb_of_passengers, average_speed, distance, number_of_wagons):
        Vehicle.__init__(self, vehicle_brand, numb_of_passengers, average_speed, distance)
        self.number_of_wagons = number_of_wagons

    def number_of_seats(self):
        return self.numb_of_passengers * self.number_of_wagons


class Plane(Vehicle):

    def __init__(self, vehicle_brand, numb_of_passengers, average_speed, distance, flight_type):
        Vehicle.__init__(self, vehicle_brand, numb_of_passengers, average_speed, distance)
        self.flight_type = flight_type

    def check_food(self):
        if self.flight_type is "airliner":
            return ("Food included in the price")
        if self.flight_type is "charter":
            return ("Without food")

tr = Traine("Tarpan", 36, 80, 900, 28)
print("---------------------------------------------------","\n"
      "Brand:","\t\t\t\t\t","'%s'" % tr.vehicle_brand,"\n"
      "One wagon capacity:","\t","%s" % tr.numb_of_passengers,"\n"
      "Total seats in traine:","\t","%s" % tr.number_of_seats(),"\n"
      "Average speed:","\t\t\t","%s" % tr.average_speed,"\n"
      "Distance:","\t\t\t\t","%s" % tr.distance,"\n"
      "Travel time:","\t\t\t","%.2s hours" % tr.travel_time())

pl = Plane("Boeing 737", 158, 950, 10000, "airliner")
print("---------------------------------------------------","\n"
      "Brand:","\t\t\t\t\t","'%s'" % pl.vehicle_brand,"\n"
      "Flight type:","\t\t\t","%s" % pl.flight_type,"\n"
      "Food:","\t\t\t\t\t","%s" % pl.check_food(),"\n"
      "Seats in traine:","\t\t","%s" % pl.numb_of_passengers,"\n"
      "Average speed:","\t\t\t","%s" % pl.average_speed,"\n"
      "Distance:","\t\t\t\t","%s" % pl.distance,"\n"
      "Travel time:","\t\t\t","%.2s hours" % pl.travel_time())
