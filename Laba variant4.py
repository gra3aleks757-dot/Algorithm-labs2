import base64
def stop(route, name, x, y, time):
    route.append([name, x, y, time])
    return route

def totaltime(route):
    total = 0
    for i in range(len(route)):
        total = total + route[i][3]
    return total

def save_report(route, filename):
    f = open(filename, 'w', encoding='utf-8')
    
    f.write("-"*40 + "\n")
    f.write("ОТЧЕТ ПО МАРШРУТУ\n")
    f.write("-"*40 + "\n\n")
    
    f.write(f"остановок: {len(route)}\n")
    f.write(f"общее время: {totaltime(route)} минут\n\n")
    
    f.write("список остановок:\n")
    f.write("-"*40 + "\n")
    f.write("N  название                 координаты    время\n")
    f.write("-"*40 + "\n")
    
    for i in range(len(route)):
        stop = route[i]
        coords = f"({stop[1]},{stop[2]})"
        f.write(f"{i+1:<3} {stop[0]:<24} {coords:<12} {stop[3]} мин\n")
    
    f.write("-"*40 + "\n")
    f.close()
    
    print(f"\nотчет сохранен в {filename}")

def save_base64(route, filename):
    f = open(filename, 'w', encoding='utf-8')
    
    for i in range(len(route)):
        stop = route[i]
        stop_str = f"{stop[0]}|{stop[1]}|{stop[2]}|{stop[3]}"
        encoded = base64.b64encode(stop_str.encode()).decode()
        f.write(encoded + "\n")
    
    f.close()
    print(f"base64 сохранен в {filename}")

def load_base64(filename):
    new_route = []
    f = open(filename, 'r', encoding='utf-8')
    
    for line in f:
        line = line.strip()
        if line:
            decoded = base64.b64decode(line).decode()
            parts = decoded.split('|')
            if len(parts) == 4:
                name = parts[0]
                x = int(parts[1])
                y = int(parts[2])
                time = int(parts[3])
                new_route.append([name, x, y, time])
    
    f.close()
    print(f"загружено из {filename}")
    return new_route
def printable(route):
    if len(route) == 0:
        print("маршрут пустой")
        return
    
    print("\n" + "-"*65)
    print("ТАБЛИЦА МАРШРУТА")
    print("-"*65)
    print(f"{'N':<4} {'Название':<25} {'Координаты':<15} {'Время':<10}")
    print("-"*65)
    
    for i in range(len(route)):
        stop = route[i]
        coords = f"({stop[1]},{stop[2]})"
        print(f"{i+1:<4} {stop[0]:<25} {coords:<15} {stop[3]:<10} мин")
    
    print("-"*65)
    print(f"ИТОГО: {totaltime(route)} минут")
    print("-"*65)

print("ВАРИАНТ 4 \n")

my_route = []

my_route = stop(my_route, "рынок", 0, 0, 5)
my_route = stop(my_route, "вокзал", 2, 1, 7)
my_route = stop(my_route, "парк", 4, 2, 4)
my_route = stop(my_route, "универ", 6, 1, 6)
my_route = stop(my_route, "тц", 8, 0, 8)

printable(my_route)

save_report(my_route, "my_report.txt")


save_base64(my_route, "my_route_base64.txt")

print("\nсодержимое base64 файла:")
f = open("my_route_base64.txt", 'r')
lines = f.readlines()
for i in range(len(lines)):
    print(f"  {i+1}. {lines[i].strip()[:40]}...")
f.close()

print("\nпробуем загрузить из base64:")
loaded_route = load_base64("my_route_base64.txt")
printable(loaded_route)
