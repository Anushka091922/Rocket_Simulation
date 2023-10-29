import time

print("Rocket simulation loading....")
time.sleep(2)
print("Rocket Simulation finished loading")

# This is under the thrust of the rocket
avt = int(input("What is the average thrust?"))
m = float(input("What is the mass of the rocket? (in KG)"))
t = float(input("What is the burn time of the engine?"))

# Assuming you have the sensor and altitude values
x = float(input("Enter the x-value from the sensor: "))
y = float(input("Enter the y-value from the sensor: "))
z = float(input("Enter the z-value from the sensor: "))
altitude = float(input("Enter the altitude: "))

# Assuming you have the necessary dimensions and masses of rocket components to calculate CG and CP
# Calculate the center of gravity (CG) and center of pressure (CP) based on your rocket configuration
# Assuming you have computed cg and cp here

# Calculate acceleration, altitude, and velocity during powered flight
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

# Unpowered flight
s2 = 0 - pow(v1, 2) / (2 * (-9.8))
s3 = s1 + s2

# Check stability based on CG and CP
if cp < cg:
    print("The rocket is stable.")
else:
    print("The rocket is not stable.")

time.sleep(1)
print("The apogee is", s3, "m")
time.sleep(1)
print("The simulation has ended")
