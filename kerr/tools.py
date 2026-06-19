import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


class LorenzSystem():
    # """The Lorenz system of ordinary differential equations.

    # The state is a 3D vector (x, y, z) that evolves according to the
    # equations

    #     dx/dt = sigma * (y - x)
    #     dy/dt = x * (rho - z) - y
    #     dz/dt = x * y - beta * z

    # Attributes
    # ----------
    # sigma : float
    #     The "Prandtl number" parameter.
    # rho : float
    #     The "Rayleigh number" parameter.
    # beta : float
    #     The "geometric factor" parameter.
    # """

    def __init__(self):
        pass

    # def __repr__(self):
    #     """Return a human-readable summary of the system's parameters."""
    #     return f"LorenzSystem(sigma={self.sigma}, rho={self.rho}, beta={self.beta})"
    
    def vx(self, x, y, z, sigma = 10, rho= 28, beta = 8/3):
        return sigma * (y - x)
    
    def vy(self, x, y, z, sigma = 10, rho= 28, beta = 8/3):
        return x * (rho - z) - y
    
    def vz(self, x, y, z, sigma = 10, rho= 28, beta = 8/3):
        return x * y - beta * z
    
    def lorenz_sim_euler(self, x0, y0, z0, tmax, dt, sigma = 10, rho= 28, beta = 8/3):
        points = []
        t = 0

        while t < tmax : 
            x = x0 + self.vx(x0,y0,z0, sigma, rho, beta)*dt
            y = y0 + self.vy(x0,y0,z0, sigma, rho, beta)*dt
            z = z0 + self.vz(x0,y0,z0, sigma, rho, beta)*dt

            x0,y0,z0 = x,y,z

            points.append((x,y,z))
            t += dt

        return points
    
    def lorenz_sim_rk(self, x0, y0, z0, tmax, dt, sigma = 10, rho= 28, beta = 8/3): 
        points = []
        t = 0
        def k_machine(vx, vy, vz):
            v = lambda x,y,z : (vx(x,y,z,sigma,rho,beta), vy(x,y,z,sigma,rho,beta), vz(x,y,z,sigma,rho,beta))
            k1x, k1y, k1z = v(x0,y0,z0)
            k2x, k2y, k2z = v(x0+(dt/2)*k1x,y0+(dt/2)*k1y,z0+(dt/2)*k1z)
            k3x, k3y, k3z = v(x0+(dt/2)*k2x,y0+(dt/2)*k2y,z0+(dt/2)*k2z)
            k4x, k4y, k4z = v(x0+(dt)*k3x,y0+(dt)*k3y,z0+(dt)*k3z)

            kx = (1/6)*(k1x + 2*k2x + 2*k3x + k4x)
            ky = (1/6)*(k1y + 2*k2y + 2*k3y + k4y)
            kz = (1/6)*(k1z + 2*k2z + 2*k3z + k4z)
            
            return (kx,ky,kz)
            
        while t < tmax :
            kx, ky, kz = k_machine(self.vx, self.vy, self.vz)
            x = x0 + dt*kx
            y = y0 + dt*ky
            z = z0 + dt*kz
            x0,y0,z0 = x,y,z

            points.append((x,y,z))
            t += dt

        return points

    def lorenz_solve_ivp(self, x0, y0, z0, tmax, res, atol, rtol, sigma = 10, rho= 28, beta = 8/3):
        def v(t, state):
            x,y,z = state
            return [self.vx(x,y,z, sigma), self.vy(x,y,z, rho), self.vz(x,y,z, beta)]
        sol = solve_ivp(v, (0,tmax), [x0,y0,z0], t_eval=np.linspace(0, tmax, res),atol=atol, rtol=rtol)
        return sol


    

    

    
