# The Lorenz System

**Jadan Kerr**

## Motivation

Among the most common and least understood properties of dynamical systems is chaos. By studying the orbits and behavior of the remarkably simple lorenz system we can gain a greater insight into these kinds of solutions, and how these chaotic orbits arise. 

## Description
The Lorenz system is a system of three ordinary differential equations originally developed by meteorologist Edward Lorenz as a simplified model of convective flow in fluids. The equations take the form: 

$$
\begin{aligned}
\frac{dx}{dt} &= \sigma(y - x) \\
\frac{dy}{dt} &= x(\rho - z) - y \\
\frac{dz}{dt} &= xy - \beta z
\end{aligned}
$$

Setting the constants 
$ \sigma = 10 $ 
$ \rho = 28 $ 
$ \beta = \frac{8}{3} $
yields the classical Lorenz attractor

The system is deterministic-- we can be confident that the solution will fall in some known orbits. But we can't predict arbitrarily far into the future with arbitrary initial conditions. The system is just too sensitive. While originally developed for weather we later found examples of the Lorenz system in all kinds of systems, from lasers and electric circuits to some chemical reactions. 
## Plan

I will use a numerical differential equation solver to solve the equations using different initial conditions, demonstrating the system's incredible sensitivity to initial conditions. I will then plot the solutions as a trajectory in phase space using numpy.

As far as finding the solutions, I plan on implementing 2-3 of the following schemes and comparing the results: 
- Euler's method
$$x_{n+1} = x_n + \Delta t \cdot f(t_n, x_n)$$
- Runge-Kutta 3rd
- Runge-Kutta 4th
$$
\begin{aligned}
k_1 &= f(t_n, x_n) \\
k_2 &= f\left(t_n + \frac{\Delta t}{2}, x_n + \frac{\Delta t}{2}k_1\right) \\
k_3 &= f\left(t_n + \frac{\Delta t}{2}, x_n + \frac{\Delta t}{2}k_2\right) \\
k_4 &= f(t_n + \Delta t, x_n + \Delta t k_3)
\end{aligned}
$$
$$x_{n+1} = x_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$



## References

- [Runge Kutta notes MIT](https://web.mit.edu/10.001/Web/Course_Notes/Differential_Equations_Notes/node5.html)
- [Runge Kutta notes wolfram](https://mathworld.wolfram.com/Runge-KuttaMethod.html)
- [Cooperative catalysis and chemical chaos: a chemical model for the Lorenz equations](https://ui.adsabs.harvard.edu/link_gateway/1993PhyD...65...86P/doi:10.1016/0167-2789(93)90006-M)
- [Analogy between higher instabilities in fluids and lasers](https://ui.adsabs.harvard.edu/link_gateway/1975PhLA...53...77H/doi:10.1016/0375-9601(75)90353-9)
- [Chaos in the segmented disk dynamo](https://ui.adsabs.harvard.edu/link_gateway/1981PhLA...82..439K/doi:10.1016/0375-9601(81)90274-7)
- [Lorenz System general info](https://en.wikipedia.org/wiki/Lorenz_system#CITEREFCuomoOppenheim1993)

