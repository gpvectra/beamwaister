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
import math
from scipy.optimize import curve_fit
from scipy import special
from measurements import setmeasurement


def beamprop(z, w0, z0,m2):
    #m2=1
    zR = 3.141519 * w0 ** 2 / (lambda_mm*m2)  #
    wz = w0 * (m2 + m2*((z - z0) / zR) ** 2) ** .5
    return (wz)


run =  '10mWCOTS'

run ='collimator 314771-05'

z_mm, w_mm, lambda_mm = setmeasurement(run)

# # old data, 10/29/?? razor blade.  Not sure laser current.
# lambda_mm=532e-6
# z_mm = np.array([2.54, 20.32, 35.56, 73.66, 292.1])
# w0_mm = np.array([0.082, 0.101, 0.116, 0.179, 0.675])

# #10mw cots DPSS / used thor beam profiler,/ 200 mA ~18 mA
# lambda_mm=532e-6
# z_mm = np.array([ 2.54,18,  23,  27,  33,  41,  57,  66,  84,  109, 132 ,154,250])
#
# #'effective 4sigma dia, first point from old data (same for 2.54 z_mm)
# wD_mm = np.array([.082,.142,.174,.19,.232,.282,.370,.426,.526,.673,.865,1.02,1.557])
#
# w_mm = wD_mm / 2


#guess
w0 = .075#0.075  # waist mm (radius)
z0 = -5  #-3.36  offset
m2=1

zR = 3.14 * w0 ** 2 / 532e-6  # rayleigh

zvec_mm = np.linspace(-25, 300, 200)
w_calc_mm = w0 * (1 + ((zvec_mm - z0) / zR) ** 2) ** .5


fitparams = curve_fit(beamprop, z_mm, w_mm)#,bounds = (lowerbounds,upperbounds))
#x = beamprop(1, 1, z_mm)
print(fitparams)
w0=fitparams[0][0]
z0=fitparams[0][1]
m2=fitparams[0][2]
theta_half=m2*lambda_mm/(3.14159*w0)

w_calc_mm = beamprop(zvec_mm, w0, z0, m2)#w0 * (1 + ((zvec_mm - z0) / zR) ** 2) ** .5

fig, ax = plt.subplots()

#print(z_mm)
ax.plot(zvec_mm, w_calc_mm, color='green')
ax.plot(zvec_mm,(zvec_mm-z0)*np.tan(theta_half))
ax.plot(z_mm, w_mm, '.', markersize=12, color ='blue')
# https://matplotlib.org/3.3.4/gallery/recipes/placing_text_boxes.html
textstr = '\n'.join((
    r'$w_0=%.0f$ $\mu$m' % (1000*w0, ),
    r'$z_0=%.2f$ mm' % (z0, ),
    r'$\theta=%.1f$ mrad (half angle)' % (1000*theta_half, ),
    r'$M^2=%.2f$' % (m2, )))

# these are matplotlib.patch.Patch properties
props = dict(boxstyle='square', facecolor='white', alpha=0.5)  #'wheat'  'round'

# place a text box in upper left in axes coords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=11,
    verticalalignment='top', bbox=props)

plt.xlabel('Prop. Distance z(mm)')
plt.ylabel('Beam Waist Radius w(mm)')
plt.grid()
plt.show()

