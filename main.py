# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import numpy as np
import matplotlib.pyplot as plt


z_mm=np.array([2.54,20.32,35.56,73.66,292.1])
w0_mm=np.array([0.082,0.101,0.116,0.179,0.675])

w0=0.075 #waist mm
z0=-5 #offset
zR=3.14*w0**2/532e-6#rayleigh

zvec_mm=np.linspace(0, 300, 20)
w0calc_mm=w0*(1+((zvec_mm-z0)/zR)**2)**.5

print(z_mm)
plt.plot(z_mm,w0_mm,'.')
plt.plot(zvec_mm,w0calc_mm)
plt.show()