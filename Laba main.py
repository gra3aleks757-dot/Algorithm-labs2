def stop(route, name, x, y, time):
    stop = [name, x, y, time]
    route.append(stop)
    print(f"добавили {name}")
    return route

def total_time(route):
    total = 0
    for i in range(len(route)):
        total = total + route[i][3]
    return total

def where_bus(route, n):
    if n >= len(route):
        return route[-1][0]
    else:
        return route[n][0]

def reverse_route(route):
    new_route = []
    for i in range(len(route)-1, -1, -1):
        stop = route[i]
        if i > 0:
            time_back = route[i-1][3]
        else:
            time_back = 0
        new_route.append([stop[0], stop[1], stop[2], time_back])
    return new_route

def print_route(route, name):
    print(f"\n{name}:")
    print("-"*50)
    for i in range(len(route)):
        print(f"{i+1}. {route[i][0]} -> {route[i][3]} мин")
    print(f"всего: {total_time(route)} мин")
print("Обязательная часть\n")


my_route = []
my_route = stop(my_route, "рынок", 0, 0, 5)
my_route = stop(my_route, "вокзал", 2, 1, 7)
my_route = stop(my_route, "парк", 4, 2, 4)
my_route = stop(my_route, "универ", 6, 1, 6)
print_route(my_route, "мой маршрут")

print(f"\nобщее время: {total_time(my_route)} мин")
print(f"через 2 остановки: {where_bus(my_route, 2)}")
print(f"через 10 остановок: {where_bus(my_route, 10)}")

back = reverse_route(my_route)
print_route(back, "обратный маршрут")
