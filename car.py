from math import sin, cos, pi


class Car:
    mass = 1830
    delta = 1.03
    width = 1.72
    height = 1.41
    wheel_radius = 0.29
    transmission_efficiency = 0.9
    gear_ratios = [0, 3.91, 2.17, 1.37, 1, 0.81]
    differential_ratio = 2.92
    min_rpm = 1000
    max_rpm = 6000
    gears = 5
    throttle = 0.5

    def __init__(self):
        self.velocities = [0]
        self.velocity = 0
        self.rpms = [self.min_rpm]
        self.gear = 1
        self.Fn = 0
        self.Ft = 0
        self.Fp = 0
        self.Fr = 0
        self.Fg = 0
        self.Fh = 0

    def gear_up(self):
        if self.gear + 1 > self.gears:
            self.gear = self.gears
        else:
            self.gear += 1

    def gear_down(self):
        if self.gear - 1:
            self.gear -= 1

    def calculate_rpm(self):
        rpm = self.velocity / self.wheel_radius * self.differential_ratio * self.gear_ratios[self.gear] * 60 / 2 / pi
        if rpm < self.min_rpm:
            return self.min_rpm
        if rpm > self.max_rpm:
            # przy maksymalnych obrotach nie powinien przyspieszać
            self.velocity = self.max_rpm * self.wheel_radius / self.differential_ratio / self.gear_ratios[
                self.gear] / 60 * 2 * pi
            self.gear_up()
            return self.max_rpm
        return rpm

    def set_throttle(self, throttle):
        if 0 <= throttle <= 1:
            self.throttle = throttle

    def get_torque(self, rpm):
        a = -1 / 60000
        b = 2 / 15
        c = 100 / 3
        # print(a*rpm**2 + b*rpm + c)
        return self.throttle * (a * rpm ** 2 + b * rpm + c)

    def calculate_forces(self, alpha=0, ft0=0.012, A=5 * 10 ** (-5), rho=1.21, Cx=0.3, g=9.81):
        self.Ft = self.mass * g * cos(alpha) * (ft0 + 12.96 * A * ft0 * self.velocity ** 2)
        self.Fp = 0.45 * rho * self.width * self.height * Cx * self.velocity ** 2
        self.Fr = 30 * Cx * self.velocity
        self.Fg = self.mass * g * sin(alpha)
        self.Fh = 0
        rpm = self.calculate_rpm()
        self.rpms.append(rpm)
        if rpm == self.max_rpm:
            # self.Fn = self.Ft + self.Fp + self.Fg + self.Fh
            self.Fn = 0
        else:
            self.Fn = self.get_torque(rpm) * self.transmission_efficiency * self.differential_ratio * self.gear_ratios[
                self.gear] / self.wheel_radius

    def calculate_velocity(self, T):
        self.velocity += T / (self.mass * self.delta) * (self.Fn - self.Ft - self.Fp - self.Fr - self.Fg - self.Fh)
        if self.velocity < 0:
            self.velocity = 0

        self.velocities.append(self.velocity)
