# computes the exponential coefficients for the solution of the associated homogeneous problem for the harmonic oscillator
import cmath
from math import sqrt



# from our custom solver
from mysolver import solve

mass = 46
g = 9.8
val = sqrt(4*mass*15000)
K = {15000}
C = {1700, 104, 10000, val}

height = float(1.5)



with open("General solutions for different values of K and c.txt","w") as f:
    title = "General solutions for different values of K and c\n"
    f.write(title)
    for k in K:
        for c in C:

            val1 = (-c + cmath.sqrt(pow(c,2) - 4* mass *k))/(2*mass)
            val2 = (-c - cmath.sqrt(pow(c, 2) - 4* mass * k)) / (2*mass)
            particular = (-mass*g)/(k)

            solution = solve((val1, val2), height, particular)
            if val1.imag != 0:
                sol = f"{round(solution[0].real, 4)}*exp({round(val1.real, 4)}*t)*cos(t) + {round(solution[1].real, 4)}*exp({round(val1.real, 4)}t)*sin({round(val1.imag, 4)}*t)" + str(round(particular,4))
            else:
                if val1 != val2:
                    sol = f"{round(solution[0].real, 4)}*exp({round(val1.real, 4)}*t) + {round(solution[1].real, 4)}*exp({round(val2.real, 4)}*t)" + str(round(particular, 4))
                else:
                    sol = f"{round(solution[0], 4)}*exp({round(val1.real, 4)}*t) + {round(solution[1],4)}*t*exp({round(val2.real, 4)}*t) + {round(particular, 4)}"
                print(round(val1.real, 4), round(val2.real,4))
            line = f"{k,c, sol}\n"

            f.write(line)


