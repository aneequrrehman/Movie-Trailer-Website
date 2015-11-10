# Movie-Trailer-Website
Server-side code written in Python to store a list of my favorite movies, including box art imagery
and a movie trailer URL. This data is then served to a web page using HTML and CSS allowing visitors
to review these movies and watch the trailers.

# Movie Trailer Website for Udacity Full Stack Nano Degree program 15/10/2015


FILES INCLUDED
--------------

	- entertainment_center.py
	- fresh_tomatoes.py
	- fresh_tomatoes.html
	- media.py


REQUIREMENTS
------------

	This program is developed in Python 2.7, CSS 3, jQuery 1.10 and 
	Bootstrap 3. It has been tested on IE 7, Google Chrome, and Microsoft Edge.


SPECIFICATIONS
--------------
	
	- Shows Movies and TV Serails in an HTML page
	- Shows the description of each movie and TV serial
	- Allows users to play trailer of each movie and tv serial


HOW TO USE
----------

	- Open "fresh_tomatoes.html" (it has already been generated)
	- Click on any tile and it will open up the desired video's 
	  description in a modal, with its youtube trailer on the 
	  right side.
	- The trailer can be played in the modal or on youtube.com.
	- If you want to add your own movies, or tv serials, open 
	  "entertainment_center.py" in any text editor and add create an
	  instance of Movie or TVSerial. For exampe

	  	movie_name = media.Movie(title, storyline, duration, stars, 
	  	genre, poster_url, trailer_url, rating)

	  The detailed description of Movie or TVSerial class can be
	  seen in "media.py" module.

	  After adding the movies, run the "entertainment_center.py," it
	  will over-write the current "fresh_tomatoes.html" page.


TOOLS USED
----------

	- Official Python editor IDLE was used for the development.
	- Sublime Text Editor was extensively used for the HTML codes.
	- Python interpreter was used to run the codes.


DEVELOPER's NOTES
-----------------

	Module "media.py" contains classes where Video class is Abstract
	Class which is inherited in other two classes. "entertainment.py"
	module has all the video entries in it which are then passed on to
	the function inside module "fresh_tomatoes.py."

	The program can be refined a lot because it depends heavily on the
	client side scripting. Rather than assigning and extracting values
	using jQuery on client-side, a database can be used. This will 
	increase the efficiency and speed of the website as well.

	A framework like Flask or Django can be used as well. 

	If you want to improve, feel free to go ahead.


CREDITS
-------

	Credits are given to:

	- "Udacity" for teaching the core concepts
	- "python.org" community for the concise documentation they have provided
	- "StackOverflow.com" community for their continuous support
	- "jQuery" community



CONTACT
------

	If you have any suggestions, the contact description is given below:

	Name:		ANEEQ-UR-REHMAN
	Email:		aneeqnazir@gmail.com
	Country:	Qatar
