def setmeasurement(run):
    import numpy as np


    if run == 'collimator 314771-05':
        # optimized for coupling cots dpss at ~ 70 mm
        lambda_mm = 532e-6
        z_mm = np.array([12,18.6,22.5,26.7,29.75,33.5,37.8,43.5,48.9,53.3,57.6,62.5,65.1,68.15,69.9,73.4,78.6,84.6,91.4,104.7,121,171])
        #mean ellipse diameter (13.5%)
        dia_um = np.array([226,208,198,195,192,185,178,166,148,135,123,118,121,129,135,149,173,208,241,310,378,648])
        # #effective beam diameter (13.5%)
        # dia_um = np.array([224,201,191,188,185,178,170,159,140.8,128,115,110,115,122,128,142,166,201,234,307,373,650])
        # #1/e2 gaussian X
        # dia_um = np.array([216,191,180,175,170,165,157,148.5,135,118,107,100,102,109,114,129,146,183,215,269,358,597])
        # #1/e2 gaussian Y
        # dia_um = np.array([208,185,173,165,165,162,155,144,126,115,103,99,106.5,111,116,129,153,185,220,296,333,594])
        w_mm = dia_um / 1000 / 2
        # z_mm = z_mm[5:]
        # w_mm = w_mm[5:]

    if run == '10mWCOTS':


        # #10mw cots DPSS / used thor beam profiler,/ 200 mA ~18 mA
        lambda_mm=532e-6
        z_mm = np.array([ 2.54,18,  23,  27,  33,  41,  57,  66,  84,  109, 132 ,154,250])

        # #'effective 4sigma dia, first point from old data (same for 2.54 z_mm)
        wD_mm = np.array([.082,.142,.174,.19,.232,.282,.370,.426,.526,.673,.865,1.02,1.557])

        w_mm=wD_mm/2

    return(z_mm,w_mm,lambda_mm) #w is radius