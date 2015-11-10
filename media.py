"""This module contains Abstract Base class Video. The module also
contains two children classes that are inherited from Video class:
	-- Movie class for storing Movies
	-- TVSerial class for storing TV Serials 
"""


import webbrowser
from abc import ABCMeta, abstractmethod


class Video(object):
	"""Video class is the Abstract Base class for Movie and TVSerial classes.
	
	Class Variables:
		RATINGS -- a list containing the valid parental ratings

	Attributes:
		title -- a string representing the title of the Video
		storyline -- a string telling the synopsis of the Video
		duration -- an integer representing the duration of Video in minutes
		stars -- a string representing the names of the actors in the Video
		genre -- a string representing the genre of the Video
		poster_url -- a string representing url of the poster of the Video
		trailer_url -- a string representing youtube url of the Video trailer
		rating -- a floating-point number representing the IMDb rating of Video
	"""

	RATINGS = []

	__metaclass__ = ABCMeta

	def __init__(self, title, storyline, duration, stars, genre, poster_url,
				trailer_url, rating):
		"""Constructor that sets the attributes of the class Video object"""
		self.title = title
		self.storyline = storyline
		self.duration = duration
		self.stars = stars
		self.genre = genre
		self.poster_url = poster_url
		self.trailer_url = trailer_url
		self.rating = rating

	def watch_trailer(self):
		"""Plays the trailer of a class Video object"""
		webbrowser.open(self.trailer_url)

	@abstractmethod
	def video_type(self):
		"""Return a string representing the type of the video"""
		pass


class Movie(Video):
	"""Movie class holds the data related to movies and besides the attributes
	inherited from Video class, it has following additional ones:

	Attributes:
		year -- an integer representing the year of release of the Movie

	Class-variables:
		RATINGS -- a list of strings representing the parental rating
	"""

	# Motion Picture Association of American Film Rating System
	RATINGS = ['NR', 'G', 'PG', 'PG-13', 'R', 'NC-17']

	def __init__(self, title, storyline, duration, stars, genre, poster_url,
				trailer_url, rating, year):
		"""Constructor that sets the attributes of class Movie object"""
		Video.__init__(self, title, storyline, duration, stars, genre,
						poster_url, trailer_url, rating)
		self.year = year

	def video_type(self):
		"""Return the type of the Video i.e. movie"""
		return 'movie' 


class TVSerial(Video):
	"""TVSerial class holds the data related to TV serials and besides the
	attributes inherited from Video class, it has following additional ones:

	Attributes:
		season -- a string representing the season of the TVSerial
		episode -- an integer representing the episode number of TVSerial
		ep_title -- a string representing the title of the episode of TVSerial
		tv_station -- a string representing station on which season is aired

	Class-variables:
		RATINGS -- a list of strings representing the parental rating
	"""

	# Television Content Rating System
	RATINGS = ['TV-Y', 'TV-Y7', 'TV-G', 'TV-PG', 'TV-14', 'TV-MA']

	def __init__(self, title, storyline, duration, stars, genre, poster_url,
				trailer_url, rating, season, episode, ep_title, tv_station):
		"""Constructor that sets the attributes of class TVSerial object"""
		Video.__init__(self, title, storyline, duration, stars, genre,
						poster_url, trailer_url, rating)
		self.season = season
		self.episode = episode
		self.ep_title = ep_title
		self.tv_station = tv_station

	def video_type(self):
		"""Return the type of the Video i.e. tvserial"""
		return 'tvserial'