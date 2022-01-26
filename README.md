# Python-application-in-ordinary-differential-equations
Main file: calculations.py



The objective is to handle all possible solutions that may arise from the following equation, considering a fall from height h:
  + mu''(t) + cu'(t) + ku(t) = −mg

Which is the equation that describes the front shock-absorber based on a spring-dashpot system of a 
typical mountain bike, u(t) is the distorsion with respect to the equilibrium point of the aforementioned
spring. The value c determines the viscous damping of the spring and it is measured in N/ms, and k is measured in N/m

The calculations are performed for a rider mass of 80kg and a bike mass of twelve, in such a way that m = (80 + 12)/2 = 46 kg and g = 9.8 m/s<sup>2</sup>
The solver handles all possible cases that may result because of the different values in c and k, which in turn determine the sign of the discriminant
of the characteristic polynomial, in the process of computing the solution of the associated homogeneous problem, since the particular solution remains
the same for any value of c and k.

The three different cases that the solver handles are:
  - Double real roots, which is the case of the positive discrimant in the of the characteristic polynomial, which means that c<sup>2</sup>> 4mk, the system is overdamped.
  - Repeated real roots, which is the case of 0 discriminant, which means that the system is critically damped.
  - Conjugate imaginary roots, which is the case of negative discriminant, in which the system is underdamped.

The solutions are computed with the following initial conditions:
  - At t = 0, which is the exact moment of impact the spring must be stable and thus u(0) = 0
  - At t = 0, the velocity of impact is given by the square root of 2*g*h, which is what u'(0) should equal to.
  - 
This results in a 2 x 2 system to solve for the two coefficients to fit the general solution to the particular values given by the initial conditions. These systems can be simplified in a different manner depending on which of the three cases is considered.

From the main file, we can write into the sets of values for k and c, and it will write into an output file the solution for all the different cases that may arise. Although it only handles cases for a rider mass of 80 kg and a bike mass of 12 kg, it could easily be modified to consider different combinations of these two parameters.



