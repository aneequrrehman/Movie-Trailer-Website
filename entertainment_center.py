"""This modules contains entries for the movies and TV serials.
The movie entries are instances of Movie class and TV serials are
instances of TVSerial class.
More entries can be added in this module.
"""


import webbrowser

import media  # contains Movie and TVSerial classes
import fresh_tomatoes  # contains functions that create an external HTML page


# 7 instances of Movie class
# RATINGS = ['NR', 'G', 'PG', 'PG-13', 'R', 'NC-17']

interstellar = \
	media.Movie("Interstellar",
			"A team of explorers travel through a wormhole in space in an"\
			" attempt to ensure humanity's survival.", 169,
			"Matthew McConaughey, Anne Hathaway, Jessica Chastain",
			"Adventure, Drama, Sci-Fi",
			"https://upload.wikimedia.org/wikipedia/en/b/bc/"\
			"Interstellar_film_poster.jpg",
			"https://www.youtube.com/watch?v=zSWdZVtXT7E", 8.7, 2014)
interstellar.RATINGS = interstellar.RATINGS[3]

inception = \
	media.Movie("Inception",
			"A thief who steals corporate secrets through the use of"\
			" dream-sharing technology is given the inverse task of planting"\
			" an idea into the mind of a CEO.", 148,
			"Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
			"Action, Mystery, Sci-Fi",
			"https://upload.wikimedia.org/wikipedia/en/7/7f/Inception"\
			"_ver3.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0",
			8.8, 2010)
inception.RATINGS = inception.RATINGS[3]

avatar = \
	media.Movie("Avatar",
			"A paraplegic marine dispatched to the moon Pandora on a"\
			" unique mission becomes torn between following his"\
			" orders and protecting the world he feels is his home.", 162,
			"Sam Worthington, Zoe Saldana, Sigourney Weaver",
			"Action, Adventure, Fantasy",
			"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-"\
			"Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY",
			7.9, 2009)
avatar.RATINGS = avatar.RATINGS[3]

the_dark_knight = \
	media.Movie("The Dark Knight",
            "When the menace known as the Joker wreaks havoc and chaos on"\
            " the people of Gotham, the caped crusader must come to terms"\
            " with one of the greatest psychological tests of his ability"\
            " to fight injustice.", 152,
            "Christian Bale, Heath Ledger, Aaron Eckhart",
            "Action, Crime, Drama",
            "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
            "https://www.youtube.com/watch?v=_PZpmTj1Q8Q", 9.0, 2008)
the_dark_knight.RATINGS = the_dark_knight.RATINGS[3]

the_hunger_games = \
	media.Movie("The Hunger Games",
			"Katniss Everdeen voluntarily takes her younger sister's"\
			" place in the Hunger Games, a televised fight to the"\
			" death in which two teenagers from each of the twelve"\
			" Districts of Panem are chosen at random to compete.", 142,
			"Jennifer Lawrence, Josh Hutcherson, Liam Hemsworth",
			"Adventure, Drama, Sci-Fi",
            "https://upload.wikimedia.org/wikipedia/en/4/42/Hunger"\
            "GamesPoster.jpg","https://www.youtube.com/watch?v=mfmrPu43DF8",
            7.3, 2012)
the_hunger_games.RATINGS = the_hunger_games.RATINGS[3]

troy = \
	media.Movie("Troy",
            "An adaptation of Homer's great epic, the film follows the"\
            " assault on Troy by the united Greek forces and chronicles"\
            " the fates of the men involved.", 163,
            "Brad Pitt, Eric Bana, Orlando Bloom", "Adventure",
            "https://upload.wikimedia.org/wikipedia/en/b/b8/Troy"\
            "2004Poster.jpg", "https://www.youtube.com/watch?v=znTLzRJimeY",
            7.2, 2004)
troy.RATINGS = troy.RATINGS[4]

fight_club = \
	media.Movie("Fight Club",
            "An insomniac office worker, looking for a way to change"\
            " his life, crosses paths with a devil-may-care soap maker,"\
            " forming an underground fight club that evolves into something"\
            " much, much more...", 139,
            "Brad Pitt, Edward Norton, Helena Bonham Carter", "Drama",
            "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_"\
            "Club_poster.jpg", "https://www.youtube.com/watch?v=SUXWAEX2jlg",
            8.9, 1999)
fight_club.RATINGS = fight_club.RATINGS[4]


# 5 instances of TVSerial class
# RATINGS = ['TV-Y', 'TV-Y7', 'TV-G', 'TV-PG', 'TV-14', 'TV-MA']

hardhome = \
	media.TVSerial("Game of Thrones", "Tyrion advises Daenerys. Sansa forces"\
			" Theon to tell her a secret. Cersei remains stubborn."\
			" Arya meets her first target. Jon and Tormund meet with the"\
			" Wildling Elders.", 61, 
			"Peter Dinklage, Lena Headey, Emilia Clarke", "Adventure, Drama,"\
			" Fantasy", "http://watchersonthewall.com/wp-content/uploads/2015"\
			"/02/GOT-S5-Poster.jpg", "https://www.youtube.com/watch?v=agWcTyXr"\
			"jfM", 9.8, 5, 8, "Hardhome", "HBO")
hardhome.RATINGS = hardhome.RATINGS[5]

how_your_mother_met_me = \
	media.TVSerial("How I Met Your Mother", "The story of The Mother, from"\
			" her traumatic 21st birthday to a number of close calls with"\
			" meeting Ted to the night before Barney and Robin's wedding.",
			23, "Josh Radnor, Jason Segel, Cobie Smulders", "Comedy, Romance",
			"http://vignette2.wikia.nocookie.net/himym/images/f/f1/How-i-met-"\
			"your-mother-season-9-dvd-cover.jpg/revision/latest?cb=2014100422"\
			"3440", "https://www.youtube.com/watch?v=RV0ay9zEG64", 9.5, 9, 16,
			"How Your Mother Met Me", "CBS")
how_your_mother_met_me.RATINGS = how_your_mother_met_me.RATINGS[4]

slap_bet = \
	media.TVSerial("How I Met Your Mother", "The gang discovers that Robin's"\
			" been hiding a huge secret, but they have no idea what it is."\
			" Marshall thinks she is married, and Barney thinks she was"\
			" a porn star.", 23, "Josh Radnor, Jason Segel, Cobie Smulders",
			"Comedy, Romance", "http://tvstock.net/sites/default/files/po"\
			"ster-how-i-met-your-mother-season-7.jpg", "https://www.youtube"\
			".com/watch?v=cZ_86XTkyz8", 9.4, 2, 9, "Slap Bet", "CBS")
slap_bet.RATINGS = slap_bet.RATINGS[4]

the_last_one_part_2 = \
	media.TVSerial("Friends", "Rachel is leaving for her job in Paris."\
			" Monica and Chandler are packing up the apartment.", 22,
			"Jennifer Aniston, Courteney Cox, Lisa Kudrow", "Comedy, Romance",
			"http://pics.filmaffinity.com/Friends_Serie_de_TV-888842701-large"\
			".jpg", "https://www.youtube.com/watch?v=Eibl9JIpcKk", 9.7, 10, 18,
			"The Last One: Part 2", "NBC")
the_last_one_part_2.RATINGS = the_last_one_part_2.RATINGS[3]

the_hounds_of_baskerville = \
	media.TVSerial("Sherlock", "Sherlock and John investigate the ghosts of a"\
			" young man who has been seeing monstrous hounds out in the woods"\
			" where his father died.", 88, 
			"Benedict Cumberbatch, Martin Freeman, Una Stubbs",
			"Crime, Drama, Mystery", "https://lh4.ggpht.com/LY5atFtolosm_TGq5"\
			"VjVxwFigtQ5J40sL_vYIdr3XRI-SyWC_mRJdyihI8HaWeoZTA=h900", 
			"https://www.youtube.com/watch?v=bm78r2innnE", 8.5, 2, 2, 
			"The Hounds of Baskerville", "BBC One")
the_hounds_of_baskerville.RATINGS = the_hounds_of_baskerville.RATINGS[4]


movies = [interstellar, inception, avatar, the_dark_knight, the_hunger_games,
		troy, fight_club]
		
tvserials = [hardhome, how_your_mother_met_me, slap_bet, the_last_one_part_2,
		the_hounds_of_baskerville]

videos = movies + tvserials
fresh_tomatoes.open_videos_page(videos)