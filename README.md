# CellTower_data_visualization
## GoogleMap API, Python, Flask PYSPARK 

#	Basic Challenge-
## Approach-
1-	I downloaded the “cell_towers.csv” file from the url provided, and unzipped it. The total data was around 4.* GB.
2-	I have used apache spark to process and store the data for Egypt. Usually the Mobile Country Code (mcc) for a country is unique. So I looked for mcc=602 for Egypt and used Spark SQL and processed the data for that code. 
3-	After getting the filtered data for mcc=602, I further filtered my file (data) for just latitude and longitude to get my coordinates.
4-	Finally the output (just the coordinates) was saved in as csv file and further used python and flask + html, javascript along with Googlemap API to show them over the web.

## Code and module explanation for compiling and running them -
#1-	The file “data_processing.py” is the pyspark file. To run this file we need to have “spark-csv_2.10:1.3.0.jar” in the classpath for spark. Please have it set up. If not then we can down load the jar from web and then place it at a location and run the following command-“pyspark --packages com.databricks:spark-csv_2.10:1.3.0” to start in spark-shell mode and the execute the rest of the lines one by one on spark shell to get the final out put file. If the jar is set then we can simply run the file using –“pyspark data_processing.py” this will generate the “cell_tower_output_cordinates.csv” CSV file for us which we will be using in the python code and further sending it to web.

#2 -	The zip file “code.zip” contains a file “app1.py” which is our main python file and also we have a template folder inside which we have “example.html” which is our html file to run.

#3 -	I have also zipped in a sample output of csv (sample_out.csv) file inside the code folder (after unzip) which will plot the coordinates. Sample file is some thousands(5k) of coordinates. The csv columns are converted to json object i.e kind of a list of dictionary and then sent as values to the markers variable which I have given to GoogleMap instance.

#4 -	 We need to have libraries like ‘flask_googlemaps’ , ‘flask’,’csv’,’json’,’ GoogleMaps’ already installed in python. If not available we can install using pip.

#5 -	After we have all the dependencies installed, we have to run the app1.py using “python app1.py”

#6 -	Since the sample data (which I have placed in the code folder is some 5k coordinates) it will take some 5-7 seconds to run, once you see the “debugger pin code “  line we can go to a browser and enter this url- http://localhost:5000/mymap/ This will populate the coordinates from the sample output file. I am attaching a screenshot of the output which comes up below:
![Alt text](D:\motionlogic\snap_output.png?raw=true "Optional Title")
 

## Advance Challenge- 

Since I had very little time so could not work on this challenge, but I would like to share some approach here, We can use the KNN Algorithm to find out the nearest location covered. From the input data we will take up the coordinates and check for the signal strength column. Once a coordinate is given as input, it will calculate the nearest points to the tower and hence check for avg signals. This is a high level idea, for implementation.

