import matplotlib.pyplot as plt

from car import Car

T = 0.01
t_sim = 1000

car = Car()
car.throttle = 1

for i in range(int(t_sim / T)):
    car.calculate_forces()
    car.calculate_velocity(T)
    # v.append(v[-1] + T*(Ft/m - 0.5*Cd*ro*Sx*v[-1]**2/m - g*Crv*v[-1]**2 - g*Crr*v[-1] - g*sin(theta)))

plt.figure(1)
plt.plot([t * T for t in range(int(t_sim / T) + 1)], [3.6 * x for x in car.velocities])
plt.figure(2)
plt.plot([t * T for t in range(int(t_sim / T) + 1)], car.rpms)

car = Car()
car.throttle = 1
for i in range(int(t_sim / T)):
    car.calculate_forces(ft0=0)
    car.calculate_velocity(T)
    # v.append(v[-1] + T*(Ft/m - 0.5*Cd*ro*Sx*v[-1]**2/m - g*Crv*v[-1]**2 - g*Crr*v[-1] - g*sin(theta)))

plt.figure(1)
plt.plot([t * T for t in range(int(t_sim / T) + 1)], [3.6 * x for x in car.velocities])
plt.figure(2)
plt.plot([t * T for t in range(int(t_sim / T) + 1)], car.rpms)

car = Car()
car.throttle = 0.3
for i in range(int(t_sim / T)):
    car.calculate_forces()
    car.calculate_velocity(T)
    # v.append(v[-1] + T*(Ft/m - 0.5*Cd*ro*Sx*v[-1]**2/m - g*Crv*v[-1]**2 - g*Crr*v[-1] - g*sin(theta)))

plt.figure(1)
plt.plot([t * T for t in range(int(t_sim / T) + 1)], [3.6 * x for x in car.velocities])
plt.figure(2)
plt.plot([t * T for t in range(int(t_sim / T) + 1)], car.rpms)
plt.show()
