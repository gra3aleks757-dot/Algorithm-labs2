def stop(route, name, x, y, time):
    route.append([name, x, y, time])
    print(f"добавлено: {name}")
    return route

def totaltime_circle(route):
    total = 0
    for i in range(len(route)):
        total = total + route[i][3]
    return total

def where_bus_circle(route, n):
    if len(route) == 0:
        return "нет остановок"
    index = n % len(route)
    return route[index][0]

def find_time(route, max_time):
    result = []
    current = 0
    
    print(f"\nостановки до {max_time} минут:")
    for i in range(len(route)):
        if current <= max_time:
            print(f"  {i+1}. {route[i][0]} - {current} мин")
            result.append(route[i][0])
        current = current + route[i][3]
    
    if current <= max_time:
        for i in range(len(route)):
            if current <= max_time:
                print(f"  {i+1}. {route[i][0]} - {current} мин (второй круг)")
                result.append(route[i][0])
            current = current + route[i][3]
    
    return result

def print_circleroute(route):
    print("КОЛЬЦЕВОЙ МАРШРУТ")
    print("-"*40)
    for i in range(len(route)):
        if i < len(route)-1:
            print(f"{i+1}. {route[i][0]} -> {route[i+1][0]} ({route[i][3]} мин)")
        else:
            print(f"{i+1}. {route[i][0]} -> {route[0][0]} ({route[i][3]} мин)")
    print(f"полный круг: {totaltime_circle(route)} мин")
    print("-"*40)

print("-"*40)
print("ВАРИАНТ 1 \n")

circle_route = []
circle_route = stop(circle_route, "центр", 0, 0, 5)
circle_route = stop(circle_route, "вокзал", 2, 1, 7)
circle_route = stop(circle_route, "парк", 4, 2, 4)
circle_route = stop(circle_route, "универ", 6, 1, 6)

print_circleroute(circle_route)

print("\nпроверка позиции:")
print(f"через 3 остановки: {where_bus_circle(circle_route, 3)}")
print(f"через 7 остановок: {where_bus_circle(circle_route, 7)}")
print(f"через 12 остановок: {where_bus_circle(circle_route, 12)}")
print("-"*40)

find_time(circle_route, 20)
