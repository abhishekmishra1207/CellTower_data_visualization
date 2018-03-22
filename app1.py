from flask import Flask
from flask import render_template
from flask import g
import csv
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import json

app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyBUVpvW_3WKsouaINM5_Jp4O1tELsbG4q8"

#GoogleMaps(app)

GoogleMaps(app, key="AIzaSyBUVpvW_3WKsouaINM5_Jp4O1tELsbG4q8")

#global data_tupes
def csv_latlon():
    global data_tupes
    global JA
    with open('/home/cloudera/Shape_Egypt/sample_out.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile,delimiter=',')
        lon=[]
        lat=[]
        #JA=[]
        JA2={}
        #with open("/home/cloudera/Shape_Egypt/output111111.csv", "wb") as f:
        for row in csvReader:
	    lons=row[6]
	    lats=row[7]
	    lon.append(lons)
	    lat.append(lats)
            data_tupes=[list(a) for a in zip(lon,lat)]
            #print data_tupes
                #writer = csv.writer(f)
               # writer.writerows([list(a) for a in zip(lon,lat)])
        
	
	JA=[]  
        for row in data_tupes:
	      JA2['lng']=row[0]
	      JA2['lat']=row[1]
	      JA.append(JA2.copy())
	json.dumps(JA)
	#print JA
	#print data_tupes
    return JA #zip(lon,lat)
    #csvDataFile.close()

@app.route("/")
def index():
    template = 'index.html'
    object_list = csv_latlon()
    return render_template(template, object_list=object_list)

@app.route("/mymap/")
def mapview():
    # creating a map in the view
    #object_list = csv_latlon()
    #sndmap={}
    #latitude = []
    #longitude = [] 
    for i in (data_tupes):
        mymap = Map(
                identifier="mymap",
		style=(
                "height:100%;"
                "width:100%;"
                "top:0;"
                "left:0;"
                "position:absolute;"
                "z-index:200;"
              ),    	
	    
                lat=31.205753,
                lng=29.924526,
                markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': i[1],
             'lng': i[0],
             'infobox': "<b>Hello World</b>"
          }]
			
            )
    
    	#print i[1]
    return render_template('example.html', mymap=mymap,JA=JA)




#tt= csv_latlon()
#print tt.data_tupes
#print tt

if( __name__ == "__main__" ):
    csv_latlon()
    app.run(debug=True, use_reloader=True)