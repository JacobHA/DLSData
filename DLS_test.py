import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


list_of_nums = [2.000000000E+000, 8.975476000E+006,
4.000000000E+000, 8.968502000E+006,
6.000000000E+000, 8.965092000E+006,
8.000000000E+000, 8.946617000E+006,
1.000000000E+001, 8.936694000E+006,
1.200000000E+001, 8.931306000E+006,
1.400000000E+001, 8.921992000E+006,
1.600000000E+001, 8.915810000E+006,
1.800000000E+001, 8.911802000E+006,
2.000000000E+001, 8.894651000E+006,
2.200000000E+001, 8.888885000E+006,
2.400000000E+001, 8.882178000E+006,
2.600000000E+001, 8.868691000E+006,
2.800000000E+001, 8.869203000E+006,
3.000000000E+001, 8.864563000E+006,
3.200000000E+001, 8.854181000E+006,
3.400000000E+001, 8.847842000E+006,
3.600000000E+001, 8.853251000E+006,
3.800000000E+001, 8.835106000E+006]

x_list = []

for i in list_of_nums:
    if 'E+000' or 'E+001' in i:
        list_of_nums.remove(i)
        x_list.append(i)

y_list = list_of_nums

def func(x, a, b):
    return a * x + b


def grapher(radii, DVS_sample, title):
    
    plt.figure(figsize=(9,6))    
    
    plt.title("Intensity vs q^2 " + title)
    
    xdata = np.linspace(1, 10E6, 10000)
    popt, pcov = curve_fit(func, DVS_sample, np.array(radii))

    plt.plot(DVS_sample, radii, 'bo', label = "Initial Sizes")

    plt.plot(xdata, func(xdata, *popt), 'r-',
         label = 'A: %.4e \nB: %.2f ' 
         % tuple(popt))

    #plt.xlim(8.8E6, 9E6)
    #plt.ylim(1, 40)
    plt.xlabel("q^2")
    plt.ylabel('Size [nm]')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()

grapher(x_list, y_list, " for 524185")