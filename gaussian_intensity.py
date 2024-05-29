#https://www.rp-photonics.com/optical_intensity.html
pi = 3.14159

w  = 50e-4 #gaissuan beam radius in cm
P  = 20e-3 #optical power in W

I_Wpercm2 = 2*P/(pi*w**2) #factor of two for gaussian profile
print('Optical Power = '+str(P*1000)+' mW')
print('Gaussian Beam Waist Radius = '+str(w*1e4)+' um')
print('Peak Intensity = '+ str(round(I_Wpercm2,1))+' W/cm^2')