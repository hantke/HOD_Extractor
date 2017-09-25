import numpy as np
import sys

NDen      = ['0p0316','0p01','0p00316','0p001','0p000316','0p0001']
NDen2     = ['0.0316','0.01','0.00316','0.001','0.000316','0.0001']
Snap      = ['61','46','38','34','30','27','25']
z         = ['0','0.5','1','1.5','2','2.5', '3']
Gprop     = ['Stell','SFR']
Hprop     = ['Age','C']
Hprop2    = ['formation time','concentration']
Index_Name= ['All Haloes ',
			 '10% of the haloes with the lowest ','10-20% of the haloes with the lowest ','20-30% of the haloes with the lowest ','30-40% of the haloes with the lowest ','40-50% of the haloes with the lowest ',
			 '40-50% of the haloes with the highest ','30-40% of the haloes with the highest ','20-30% of the haloes with the highest ','10-20% of the haloes with the highest ','% of the haloes with the highest ',]
Save      = False

def Read_File(sn_id,nd_id,hp_id):
	adr = 'Data_Bin/'
	return np.load(adr+'Fit_SN'+Snap[sn_id]+'_'+NDen[nd_id]+'_Stell_'+Hprop[hp_id]+'.npy')

def Fail_Exit1():
	print 'Wrong number of parameters.'
	print 'Please insert 4 parameters (eg. python Fit_Extractor.py 0 0 0 0)'
	sys.exit()
	
def Fail_Exit2():
	print 'Wrong range of parameters.'
	print 'The first parameter must be between 0 and 6 [z=0,0.5,1,1.5,2,2.5 & 3]'
	print 'The second parameter must be between 0 and 5 [n=0.0316,0.01,0.00316,0.001,0.000316,0.0001]'
	print 'The third parameter must be between 0 and 1 [Haloes selected by their Age or their Conc.]'
	print 'The fourth parameter must be between 0 and 10 [0 for the full HOD, 1-10 for the binning of the age or concentration]'
	print '1-> low formation redshift/concentration; 10 high formation redshift/concentration'
	sys.exit()
	
try:	sn_id,nd_id,hp_id,index = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
except:	Fail_Exit1()

if min(sn_id,nd_id,hp_id,index) < 0 or sn_id > 6 or nd_id > 5 or hp_id > 1 or index > 10: Fail_Exit2()
	
Data = Read_File(sn_id,nd_id,hp_id)

if Save: W = open('Out/Fit_SN'+Snap[sn_id]+'_'+NDen[nd_id]+'_'+Hprop[hp_id]+'_'+str(index)+'.txt','w')

if index: print '#z='+z[sn_id],'n = '+NDen2[nd_id]+' h^3 Mpc^-3','galaxies selected by their stellar mass,','with '+Index_Name[index],Hprop2[hp_id]
else: print '#z='+z[sn_id],'n = '+NDen2[nd_id]+' h^3 Mpc^-3','galaxies selected by their stellar mass,','with '+Index_Name[index]

if Save:	 print >>W,'#Mmin	sigmaLogM	Mcut	M1	alpha	Err_Mmin	Err_sigmaLogM	Err_Mcut	Err_M1	Err_alpha'
else:	print '#Mmin	sigmaLogM	Mcut	M1	alpha	Err_Mmin	Err_sigmaLogM	Err_Mcut	Err_M1	Err_alpha'

if Save:	print >>W, Data[index][0][0], Data[index][1][0], Data[index][2][0], Data[index][3][0], Data[index][4][0], Data[index][0][1], Data[index][1][1], Data[index][2][1], Data[index][3][1], Data[index][4][1]
else:		print      Data[index][0][0], Data[index][1][0], Data[index][2][0], Data[index][3][0], Data[index][4][0], Data[index][0][1], Data[index][1][1], Data[index][2][1], Data[index][3][1], Data[index][4][1]

if Save: print 'Done!\n Out/Fit_SN'+Snap[sn_id]+'_'+NDen[nd_id]+'_'+Hprop[hp_id]+'_'+str(index)+'.txt'
