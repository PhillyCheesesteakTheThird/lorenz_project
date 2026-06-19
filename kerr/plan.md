# The Simplest Chaos: The Lorenz System

**Jadan Kerr**


## Code Structure

Describe the class and key functions you plan to write in `tools.py`.

- **Class**: `LorenzSystem` — A wrapper class that holds various functions for the purpose of modeling the lorenz system.
  - `lorenz_sim_euler(x0, y0, z0, tmax, dt, sigma = 10, rho= 28, beta = 8/3)` — This method takes initial position values, values for the coefficients rho, beta, and sigma, as well as values for total time and dt. It then uses the euler method of numerically solving the three differential equations. It returns an array, each element a triplet of (x,y,z) points. A future implementation will include an option to specify complex values for some variables, effectively switching to the general complex form of the lorenz system. 
  - `lorenz_sim_runge_kutta(...)` — This method functions similarly to lorenz_sim_euler, but uses the runge-kutta method. This function will also include optional arguments to specify complex parameters

- **Functions** (if any): standalone functions outside the class


## Milestone 1 (due Sunday, April 26)

- **Fully simulate the Lorenz system using Euler's approach** 
Get a plot resembling the "butterfly."
Observe the error induced by Euler numerical approximation. <br>
### *COMPLETED* : 
lorenz_sim_euler() is done, Getting some pretty beautiful plots! And it even appears that there's some observable numerical instablity, as expected from an approach using euler's algorithm. The function starts with an inital position, and calculates an instantaneous velocity at those coordinates using the Lorenz system equations. The next positions are calculated by adding the calculated instantaneuous velocity(multiplied by some dt) to the old position. In this image dt = 1e-5

 ![a](lorenzsystem\images\Lorenz_euler.png)


We can see some some numerical instability in this plot, especially when compared to the plots obtained using the Runge-Kutta method below. 



<br>
<br>
- **Begin draft on runge-kutta simulation** ...
Compare error in euler to error in runge-kutta

- ### *COMPLETED* : 
 The Runge Kutta simulation went well,a plot is below. 

 ![a](lorenzsystem\images\Lorenz_rk.png)


I also plotted the difference between the two methods on a log log plot, which is below. The plot is essentially abs(x_values_euler - x_values_rk). We can see the error starts quite small, but eventually grows to order 10^1:  :

 ![a](lorenzsystem\images\e_rk_delta.png)

 
## Milestone 2 (due Sunday, May 3)

All coding should be done by this milestone.

- **Implement more general complex form of the lorenz system.** ...
The generalization of the lorenz equations to include complex values(Fowler, 1982) for x and y are : 
$$
\begin{aligned}
\frac{dx}{dt} &= \sigma(y - x) \\
\frac{dy}{dt} &= x(\rho - z) - a\,y \\
\frac{dz}{dt} &= \frac{1}{2}(x^{*}y + x\,y^{*}) - \beta z \\
\rho &= \rho_1 + i\,\rho_2 \\
a &= 1 - ie
\end{aligned}
$$
- **Plot cross-sections of this complex dynamical system** ...
### *INCOMPLETE* 
note: this was planned on before the opportunity to present early was known about, decided this was outside of the scope of milestone 2(and if no more code is written after milestone 2, outside the scope of the project)


- **Implement solve_IVP Lorenz Solution method** ...
  - ### *COMPLETE* : 
      - Function written as `solve_ivp_lorenz(...)`

- **Compare Euler's method and adaptable RK45 solutions** ...
  - ### *COMPLETE* : 
- **Complete presentation** ...
  - ### *COMPLETE* : 






## Milestone 3 (due Sunday, May 10)

Write the report and finish up the project.

- **Record data and write the report**
### *COMPLETE* : 
 