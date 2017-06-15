<html>
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h1><a id="user-content-if-you-host-it-will-they-come" class="anchor" href="#if-you-host-it-will-they-come" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>If You Host It, Will They Come?</strong></h1>
<h2><a id="user-content-objective" class="anchor" href="#objective" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Background</h2>
<p>	Conferences play a large role in higher education.  They are used to keep professors and researchers abreast of the latest trends in education, industry and technology.  As such, multiple companies offer conference hosting services which try simply the process of connecting the academic community with the outside world.  This union often fosters the growth and awareness of fledgling industries, new teaching practices and in some cases can even create entire new fields of study for these universities.<br><br></p>
<p>There are two basic type of conferences, web based and at location conferences.  In Web based conferences, patrons purchase access to a web cast of the topic, but do not physically travel to a different location.  The more traditional location based conferences involve travel to a destination city and attendance for potentially multiple days at the conference site.</p>
<h2><a id="user-content-motivation" class="anchor" href="#motivation" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Motivation</h2>
<p>Conferences can be hosted in any city that has a large enough hotel, and convenient airport access.  The goal of any business that hosts conferences is to maximize attendance. The number of attendees directly correlates to company profits.
In this analysis, I will attempt to determine the factors that contribute to conference attendance.  Data will be analyzed and recommendations for conference locations will be presented.</p>
<h2><a id="user-content-data" class="anchor" href="#data" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Data</h2>
<p>	A large data set from a conference hosting company that wishes to remain anonymous was obtained.  This includes the conference attendance figures for 400 conferences staged over a 5 year period.  The Conference location city, Lat/Long, Hotel, Date and attendance figures are provided.  For each of these conferences, the topic of the conference, the address and university affiliation of each attendee will also be provided.   Similar data will be available for WebCast conferences.   The total number of data points will be around 30,000.   Each data point represents an actual sale to either a conference or a Webcast.</p>

<h2><a id="user-content-steps-of-the-challenge" class="anchor" href="#steps-of-the-challenge" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Data Analysis Plan</h2>
<p>To answer questions about logic games, seven steps must be performed.  Here, I describe each step, indicate its degree of difficulty, and suggest how I intend to approach it:</p>
<ol>
<li>
<p>EDA:<br>
All data will be cleaned and scrubbed using Python Pandas.  Missing values will be quantified, and dealt with appropriately.   All dates will be converted to datetime objects.  Any missing Lat/Long Data from the attendees or conference locations will be collected using an appropriate python package (pyzipcode or geopy)</p>
</li>
<li>
<p>The conference topics will be grouped into higher level classes (continuing ed, technology etc (I think there will be 8 unique classifiers).</p>
</li>
<li>
<p>The company has also provided geographic region data based on groups of states (southeast, northwest, Midwest) etc.   These regions supposedly correlate to some attributes of higher education.  Southeast classification may be different academically than the Northeast – for example.</p>
</li>
<li>
<p>The Euclidian distance from each attendee to the conference will be computed from the Lat/Long data</p>
</li>
<li>
<p>Attendees for a given conference will be grouped by some sensible minimum distance apart, and a nice visual map using folium will be created for each conference  (or for each conference type).</p>
</li>
<li>
<p>Clustering a sorting of the data will be attempted to logically group the conference attendees – this will be compared to the provided region data and if appropriate, recommendations to classify certain locations as a different region will be proposed.</p>
</li>
<li>
<p>The Web based statistics will be used as a control.  By topic, the attendance will be compared to the conference attendance of each location.  The average distance traveled will be examined and assertions will be made regarding local attendance (traveling less than 400? Miles) vs regional attendance (>400 miles).</p>
</li>
<li>
<p>If time permits attributes of the conference cities (nightlife, ease of transportation/accessibility) may be included.</p>
</li>
<li>
<p>Ultimately the question to be answered is what location for a conference topic will yield the best attendance, and is that better than the web based versions.</p>
</li>
<li>
<p>Ideally a model will be created to run on future datasets.  This can be used to determine if the recommendations actually result in greater attendance.</p>
</li>
<li>
<p>As the project progresses, specific models will be considered and documented – Initially I’m anticipating using a k-means unsupervised learning technique or perhaps some type of random-forest or decision tree network.</p>
</li>
<li>   The two main outputs will be data visualization of conferences and their patron locations and relative attendance.  Model results will also be presented to quantify attendance results.</p>













</li>
</ol>

</html>
