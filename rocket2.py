import time

print("Rocket simulation loading....")
time.sleep(2)
print("Rocket Simulation finished loading")


avt = int(input("What is the average thrust?"))
t = float(input("What is the burn time of the engine?"))



weights = [10, 5, 20, 8, 15]  
distances = [3, 8, 15, 20, 25]  


W = sum(weights)

cg = sum([w * d for w, d in zip(weights, distances)]) / W


x = float(input("Enter the x-value from the sensor: "))
y = float(input("Enter the y-value from the sensor: "))
z = float(input("Enter the z-value from the sensor: "))
altitude = float(input("Enter the altitude: "))

pressure = float(input("Enter the pressure value from the sensor: "))


cp = pressure 


m = sum(weights)  # Total mass of the rocket
ac1 = avt / m - 9.8
s1 = 0.5 * (ac1 - 9.8) * t * t
v1 = (ac1 - 9.8) * t

print("The data is coming in....\n")

time.sleep(1)
print("The acceleration is ", ac1, "m/s^2")
time.sleep(0.5)
print("The altitude at the burnout is", s1, "m")
time.sleep(0.5)
print("The velocity at the burnout is", v1, "m/s")


s2 = 0 - pow(v1, 2) / (2 * (-9.8))
s3 = s1 + s2


if cp < cg:
    print("The rocket is stable.")
else:
    print("The rocket is not stable.")

time.sleep(1)
print("The apogee is", s3, "m")
time.sleep(1)
print("The simulation has ended")
