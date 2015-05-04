from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Template, Context, RequestContext
from Tool.models import *
import MySQLdb
from models import Value
# Create your views here.

def welcomeTool(request):
	if(request.method=='POST') :
		InputLocation = request.POST.get('location')
		print InputLocation
		print "hello world"
		context =""
		print InputLocation
		print type(InputLocation)
		obj=Value.objects.filter(location=InputLocation)
		print type(obj)
		print obj[0]
		print obj[0].ozone
		print obj[0].co
		print type(obj[0].co)
				

		MAP_GASES_CONC = { "Ozone": [(0.000, 0.064), (0.065, 0.084), (0.085, 0.104), (0.105, 0.124), (0.125, 0.374), (-1, -1), (-1, -1)],
		"ParticulateMatter2.5": [(0.0, 15.4), (15.5, 40.4), (40.5, 65.4), (65.5, 150.4), (150.5, 250.4), (250.5, 350.4), (350.5, 500.4)],
		"ParticulateMatter10": [(0.0, 54.0), (55.0, 154.0), (155.0, 254.0), (255.0, 354.0), (355.0, 424.0), (425.0, 504.0), (505.0, 604.0)],
		"CO": [(0.0, 4.4), (4.5, 9.4), (9.5, 12.4), (12.5, 15.4), (15.5, 30.4), (30.5, 40.4), (40.5, 50.4)],
		"SO2": [(0.000, 0.034), (0.035, 0.144), (0.145, 0.224), (0.225, 0.304), (0.305, 0.604), (0.605, 0.804), (0.805, 1.004)],
		"NO2": [(-1, -1), (-1, -1), (-1, -1), (-1, -1), (0.65, 1.24), (1.25, 1.64), (1.65, 2.04)]
		}
		GAS_HIGHER_AQI = [50, 100, 150, 200, 300, 400, 500]
		GAS_LOWER_AQI = [0, 51, 101, 151, 201, 301, 401]
		Gases = ["Ozone" , "ParticulateMatter2.5" , "ParticulateMatter10" , "CO", "SO2", "NO2"]

		Conc = [obj[0].ozone, obj[0].pmtwofive, obj[0].pmten, obj[0].co, obj[0].sotwo, obj[0].notwo]
		AQI = [1, 2, 3, 4, 5, 6]
		i=0
		for i in range(len(Gases)):
			if Gases[i] not in MAP_GASES_CONC.keys():
				return -1	# this is a bad input
			bp_low = -1.0
			bp_high = -1.0
			i_low = -1.0
			i_high = -1.0
			temp_array = MAP_GASES_CONC[Gases[i]]
			index = -1
			for dummy_i in range(7):	
				range_conc = temp_array[dummy_i]
				if Conc[i] > range_conc[0] and Conc[i] < range_conc[1]:
					index = dummy_i
					bp_low = range_conc[0]
					bp_high = range_conc[1]
					break
			i_low = GAS_LOWER_AQI[index]
			i_high = GAS_HIGHER_AQI[index]
			print index, bp_low, bp_high, i_low, i_high
			if(bp_high - bp_low) != 0:
				AQI[i] = i_low + ((Conc[i] - bp_low) * (i_high - i_low) / (bp_high - bp_low))
				

		finalAQI= 0
		for i in range(len(AQI)):
			finalAQI = finalAQI + AQI[i]
		print finalAQI

		LowLevel = [0, 51, 101, 151, 201, 301]
		HighLevel = [50, 100, 150, 200, 300, 1000]
		colorCode = ["Green", "Yellow", "Orange", "Red", "Purple", "Maroon"]
		color = [1, 2]
		for i in range(6):
			if finalAQI >= LowLevel[i] and finalAQI <= HighLevel[i]:
				color[0] = colorCode[i]
				color[1]= finalAQI
				colorDict = {color[0] : color[1]}

		print color[0]

		pollutant_mapping = { 0: "Ozone",
                      1: "ParticulateMatter2.5",
                      2: "ParticulateMatter10",
                      3: "CO",
                      4: "SO2",
                      5: "NO2"
                    }

		values = { "Ozone": (1.003, 1013),
           "ParticulateMatter2.5": (1.003, 1013),
           "ParticulateMatter10" : (1.003, 1013),
           "CO": (1.004, 1013),
           "SO2": (1.004, 1013),
           "NO2": (1.002, 497)
        }


		def function_to_call(conc_array, Conc, aqi_array):
		    pollu_values = []
		    for dummy_i in range (0, len(conc_array)):
		        pollu = conc_array[dummy_i]
		        pollu_rr = relative_risk_calculator(pollu, Conc[dummy_i], aqi_array[dummy_i])
		        pollu_values.append(pollu_rr)
		    return air_risk_calculation(pollu_values)
    

		def relative_risk_calculator(pollutant, conc, aqi):
		    dummy_a = (conc - aqi) / 10
		    dummy_b = (values[pollutant][0]) - 1
		    rel_risk = (dummy_a * dummy_b) + 1
		    return rel_risk
    
    
		def air_risk_calculation(pollutants_values):
		    numerator = 0
		    denomenator  = 0
		    for dummy_i in range (0, len(pollutants_values)):
		        dummy_a = values[pollutant_mapping[dummy_i]][1]
		        numerator += (pollutants_values[dummy_i] - 1) * dummy_a 
		        denomenator += pollutants_values[dummy_i] * dummy_a
		    return numerator / denomenator

		colorDict['RiskAssessment'] = function_to_call(Gases, Conc, AQI)



		'''db = MySQLdb.connect("localhost","root","1819212228","AQIvalues")
		cursor = db.cursor()
		sql="SELECT * FROM value"
	#	print sql
		#q = value(location = InputLocation)
		cursor.execute(sql)
		data = cursor.fetchall() 
	#	output = data
		output = value.objects.all()
		db.close()

		#output = Value.objects.all()
	#	output = cursor.fetchone()
		context= {'output':output}
	#	context = {'q': q} '''
	#	return render(request, 'tool.html', {'obj': obj})
		return render(request, 'tool.html', {'colorDict': colorDict})
	else:
        	context =""
        print "hello"
        return render(request, 'tool.html', context)




def AQIResult(request):
	if(request.method=='POST') :
		InputLocation = request.POST.get('location')
		print InputLocation
		print "hello world"
		'''db = MySQLdb.connect("localhost","root","1819212228","AQIvalues")
		cursor = db.cursor()
		sql="SELECT * FROM value"
	#	print sql
		#q = value(location = InputLocation)
		cursor.execute(sql)
		data = cursor.fetchall() 
	#	output = data
		output = value.objects.all()
		db.close()

		#output = Value.objects.all()
	#	output = cursor.fetchone()
		context= {'output':output}
	#	context = {'q': q} '''
	return render(request, 'tool.html', context)

