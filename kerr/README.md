# Lorenz Attractor: Chaos in all its simplicity

**Author:** Jadan Kerr

A numerical exploration of the Lorenz system using Euler's method, 4th-order Runge-Kutta (RK4), and `scipy.integrate.solve_ivp`. This project compares the accuracy, stability, and visual structure of the famous Lorenz butterfly under different integration schemes.

## Features

- Implementation of Euler and RK4 solvers for the Lorenz equations
- 3D visualizations of the Lorenz attractor using Matplotlib
- Comparison of trajectory divergence due to numerical error and chaos
- Sensitivity analysis with tiny perturbations in initial conditions

## Lorenz Equations

The system is defined by:

$$
\begin{aligned}
\dot{x} &= \sigma (y - x) \\
\dot{y} &= x(\rho - z) - y \\
\dot{z} &= xy - \beta z
\end{aligned}
$$

With the classic chaotic parameters: $\sigma = 10$, $\rho = 28$, $\beta = \frac{8}{3}$.

## Results Summary

- **Euler's method** captures the butterfly shape but suffers from visible trajectory drift and amplitude errors.
- **RK4** closely matches the benchmark `solve_ivp` solution, making it suitable for chaotic systems where error accumulates quickly.
- **Sensitivity to initial conditions** — a $10^{-9}$ perturbation leads to exponential divergence, confirming chaotic behavior.

## Dependencies

- Python 3.13+
- NumPy
- Matplotlib
- SciPy (for `solve_ivp`)

## Usage

```python
from tools import LorenzSystem

l = LorenzSystem()

# Run simulations
points_rk4 = l.lorenz_sim_rk(0.1, 1, 2, t_max=100, dt=1e-4)
points_euler = l.lorenz_sim_euler(0.1, 1, 2, t_max=100, dt=1e-4)
points_ivp = l.lorenz_solve_ivp(0.1, 1, 2, t_max=100, n_points=50001)
