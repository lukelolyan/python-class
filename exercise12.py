def calculate_distance():
    t1 = math.radians(float(input("Enter the latitude of Point 1 in degrees: ")))
    g1 = math.radians(float(input("Enter the longitude of Point 1 in degrees: ")))
    t2 = math.radians(float(input("Enter the latitude of Point 2 in degrees: ")))
    g2 = math.radians(float(input("Enter the longitude of Point 2 in degrees: ")))

    distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
    print(f"The distance between the two points on the Earth's surface is approximately {distance:.2f} kilometers.")

calculate_distance()
