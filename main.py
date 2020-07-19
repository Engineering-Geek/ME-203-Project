import math
import numpy as np
import pygame
import sympy

t = sympy.symbols("t")
k = sympy.symbols("k")
m = sympy.symbols("m")
x0 = sympy.symbols("x0")
v0 = sympy.symbols("v0")
# Making all variables global variables for now
# We can specify certain ones as constants later


def fig2array(fig=None):
    return np.fromstring(
        fig.canvas.tostring_rgb(),
        dtype=np.uint8, sep=''
    ).reshape(fig.canvas.get_width_height()[::-1] + (3,))


class MainEquations:
    def __init__(self):
        self.w = sympy.sqrt(k/m)
        self.phi = sympy.atan2(x0, v0)
        self.amplitude = sympy.sqrt(x0**2 + v0**2)
        
        self.frequency = self.w / (2*sympy.pi)
        self.phase_shift = self.phi / self.w
        
        #                   [x0 * cos(w*t)] + [v0 * sin(w*t)]
        self.position_equation = x0*sympy.cos(self.w*t) + v0*sympy.sin(self.w*t)
    
    def get_position_equation(self):
        return self.position_equation
    
    def get_position_alternate(self):
        """
        amplitude * sin(phi + w*t)
        :return: position (meters)
        """
        position = self.amplitude*(math.sin(self.phi + self.w*t))
        return position


def main():
    equation_set_1 = MainEquations()
    position_equation = equation_set_1.get_position_equation()
    simp_eqn = position_equation.subs(k, 1.0).subs(x0, 0.5).subs(v0, -0.25).subs(m, 1).simplify()
    
    print(position_equation)
    # Calling a member of a protected series, ignore any IDE warnings.
    # fig = sympy.plot(simp_eqn, backend="matplotlib")._backend.fig
    # fig.canvas.draw()
    # data = fig2array(fig=fig)
    # print(np.shape(data))

    eqn2 = position_equation.subs(k, 1).subs(m, 1).subs(x0, 0)
    sympy.plotting.plot3d(eqn2)


if __name__ == '__main__':
    main()


