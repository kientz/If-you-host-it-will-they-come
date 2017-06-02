# If-you-host-it-will-they-come
Steve Kientz 								May 21st, 2017
If You Host It, Will They Come?
Motivation
	Conferences play a large role in higher education.  They are used to keep professors and researchers abreast of the latest trends in education, industry and technology.  As such, multiple companies offer conference hosting services which try simply the process of connecting the academic community with the outside world.  This union often fosters the growth and awareness of fledgling industries, new teaching practices and in some cases can even create entire new fields of study for these universities.
	There are two basic type of conferences, web based and at location conferences.  In Web based conferences, patrons purchase access to a web cast of the topic, but do not physically travel to a different location.  The more traditional location based conferences involve travel to a destination city and attendance for potentially multiple days at the conference site.  
	Conferences can be hosted in any city that has a large enough hotel, and convenient airport access.  The goal of any business that hosts conferences is to maximize attendance. The number of attendees directly correlates to company profits.
	In this analysis, I will attempt to determine the factors that contribute to conference attendance.  Data will be analyzed and recommendations for conference locations will be presented.
Available Data
	A large data set from a conference hosting company that wishes to remain anonymous was obtained.  This includes the conference attendance figures for 400 conferences staged over a 5 year period.  The Conference location city, Lat/Long, Hotel, Date and attendance figures are provided.  For each of these conferences, the topic of the conference, the address and university affiliation of each attendee will also be provided.   Similar data will be available for WebCast conferences.   The total number of data points will be around 30,000.   Each data point represents an actual sale to either a conference or a Webcast.


Data Analysis Plan
1.  EDA – All data will be cleaned and scrubbed using Python Pandas.  Missing values will be quantified, and dealt with appropriately.   All dates will be converted to datetime objects.  Any missing Lat/Long Data from the attendees or conference locations will be collected using an appropriate python package (pyzipcode or geopy)
2. The conference topics will be grouped into higher level classes (continuing ed, technology etc (I think there will be 8 unique classifiers).
3. The company has also provided geographic region data based on groups of states (southeast, northwest, Midwest) etc.   These regions supposedly correlate to some attributes of higher education.  Southeast classification may be different academically than the Northeast – for example.
4. The Euclidian distance from each attendee to the conference will be computed from the Lat/Long data.
5. Attendees for a given conference will be grouped by some sensible minimum distance apart, and a nice visual map using folium will be created for each conference  (or for each conference type).
6. Clustering a sorting of the data will be attempted to logically group the conference attendees – this will be compared to the provided region data and if appropriate, recommendations to classify certain locations as a different region will be proposed.
7. The Web based statistics will be used as a control.  By topic, the attendance will be compared to the conference attendance of each location.  The average distance traveled will be examined and assertions will be made regarding local attendance (traveling less than 400? Miles) vs regional attendance (>400 miles).
8. If time permits attributes of the conference cities (nightlife, ease of transportation/accessibility) may be included.
9. Ultimately the question to be answered is what location for a conference topic will yield the best attendance, and is that better than the web based versions.
10. Ideally a model will be created to run on future datasets.  This can be used to determine if the recommendations actually result in greater attendance.
11. As the project progresses, specific models will be considered and documented – Initially I’m anticipating using a k-means unsupervised learning technique or perhaps some type of random-forest or decision tree network.
12.   The two main outputs will be data visualization of conferences and their patron locations and relative attendance.  Model results will also be presented to quantify attendance results.
13.   I’ve signed an NDA with the company and have received all of the data has been received in several .csv files.
