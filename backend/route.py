import csv


def calculate_eta(distance_km, speed_kmh):
    if speed_kmh <= 0:
        return None

    time_hours = distance_km / speed_kmh
    time_minutes = time_hours * 60

    return round(time_minutes, 2)


routes = []

with open("data/traffic_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for road in reader:

        distance = float(road["distance_km"])
        speed = float(road["average_speed_kmh"])

        # ข้ามถนนที่ปิด
        if road["road_status"] == "CLOSED":
            continue

        # ข้ามถนนที่เกิดอุบัติเหตุ
        if road["accident"] == "YES":
            continue

        eta = calculate_eta(distance, speed)

        if eta is not None:
            routes.append({
                "road_name": road["road_name"],
                "eta": eta,
                "traffic": road["traffic_level"]
            })


best_route = min(routes, key=lambda route: route["eta"])


print("\n🚨 EMERGENCY SMART ROUTE")
print("-------------------------")
print(f"Recommended Route: {best_route['road_name']}")
print(f"Estimated Time: {best_route['eta']} minutes")
print(f"Traffic: {best_route['traffic']}")

print("\nWhy this route?")
print("- Road is open")
print("- No accident reported")
print("- Fast estimated travel time")