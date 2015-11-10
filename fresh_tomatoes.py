"""This modules contains HTML template for the main videos page.
It also contains two functions: 
  -- open_videos_page(videos) that outputs the HTML file
  -- create_video_tiles_content(videos) that creates tiles for videos  
"""


import os
import re
import webbrowser


# styles for the main HTML page
main_page_style = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        .video-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .video-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }

        .modal-dialog {
            margin-top: 100px;
        }
        .modal-body {
        	margin-top: 20px;
        	height: 350px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        iframe {
         	border: none;
            height: 300px;
            width: 100%;
    	  }
    	  .description {
    		  padding: 5px 10px;
    		  width: 50%;
    		  height: 100%;
    		  text-align: justify;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
'''

# modal jQuery code that shows the description of each movie or TV serial 
video_info_modal_script = '''

        // Opens the description and trailer of the video
        $(document).on('click', '.video-tile', function(event) {
        	var title = $(this).attr('data-title');
        	var storyline = $(this).attr('data-storyline');
        	var duration = $(this).attr('data-duration');
        	var stars = $(this).attr('data-stars');
        	var genre = $(this).attr('data-genre');
        	var rating = $(this).attr('data-rating');
          var p_rating = $(this).attr('data-parental-rating');
        	var youtube_id = $(this).attr('data-trailer-youtube-id');

          var year = $(this).attr('data-year');
          var season = $(this).attr('data-season');
          var season_title = $(this).attr('data-seasontitle');
          var episode = $(this).attr('data-episode');
          var tv_station = $(this).attr('data-tvstation');
        	
        	var embedded_url = 'http://www.youtube.com/embed/' + youtube_id + '?autoplay=0&html5=1';
        	
          if (isNaN(year)) {
            $("#videoInfo h3").empty().append(season_title + '<br/>' + 'Season: <b>' + season + '</b>, Episode: <b>' + episode + '</b>');
            $("#videoInfo .tvstation").empty().append('AIRED ON <b>' + tv_station + '</b>');
          }
          else {
            $("#videoInfo h3").empty().append(title + ' (' + year + ')');
            $("#videoInfo .tvstation").empty();
          }
        	$("#videoInfo .storyline").empty().html('<b>' + storyline + '</b>');
        	$("#videoInfo .duration").empty().html('Duration: <b>' + duration + ' mins</b>');
        	$("#videoInfo .stars").empty().append('<b>Stars:</b> ' + stars);
        	$("#videoInfo .genre").empty().append('<b>' + genre + '</b>');
        	$("#videoInfo .rating").empty().append('IMDb Rating: <b>' + rating + '</b>');
        	$("#videoInfo .p-rating").empty().append('Parental Rating: <b>' + p_rating + '</b>');
          $("#videoInfo iframe").attr('src', embedded_url);

        });
'''

# Stops the video after the modal has been closed
trailer_modal_script = '''
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop', function (event) {
            // Remove the src so the source of the file gets removed and assign it again
            // so that the user can play it again
            var video = $("iframe").attr("src");
            $("iframe").attr("src", "");
            $("iframe").attr("src", video);
        });
'''

# Animate videos' tiles when the page loads
animate_tiles_script = '''
        // Animate in the videos' tiles when the page loads
        $(document).ready(function () {
          $('.video-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    
'''

# layout of the main HTML page (modal and navbar)
main_page_content = '''
  </script>
  </head>
  <body>
  <!-- Video Description Modal -->
  	<div class="modal fade" id="videoInfo">
  	  <div class="modal-dialog modal-lg">
  	    <div class="modal-content">
  	      <div class="modal-header" style="padding:20px 30px">
  	        <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <h3 class="modal-title" style="text-align:center"></h3>
  	      </div>
  	      <div class="modal-body">
  	      	<div class="row">
  	      	  <div class="description pull-right">
  	      	  <iframe src=""></iframe>
			  </div>
			  <div class="description">
			  	<p><span class="duration"></span><span class="pull-right genre"></span></p>
			  	<p><span class="rating"></span><span class="pull-right p-rating"></span></p><br />
			  	<p class="tvstation" style="text-align:center"></p>
          <p class="stars"></p>
			  	<p class="storyline"></p>
			  </div>
  	      	</div>

  	      </div>
  	    </div>
  	  </div>
  	</div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {video_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 video-tile text-center" 
            data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" 
            data-target="#videoInfo" data-backdrop="static" data-title = "{title}"
            data-storyline="{storyline}" data-duration="{duration}" data-stars="{stars}" 
            data-genre= "{genre}" data-rating = "{rating}" data-parental-rating="{p_rating}" data-year="{year}">

    <img src="{poster_url}" width="220" height="342">
    <h2>{title}</h2>
</div>
'''

# A single TV serial entry html template
tvserial_tile_content = '''
<div class="col-md-6 col-lg-4 video-tile text-center" 
            data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" 
            data-target="#videoInfo" data-backdrop="static" data-title = "{title}"
            data-storyline="{storyline}" data-duration="{duration}" data-stars="{stars}" 
            data-genre= "{genre}" data-rating = "{rating}" data-parental-rating="{p_rating}" data-seasontitle = "{season_title}" data-season="{season}" data-episode="{episode}" data-tvstation="{tv_station}">

    <img src="{poster_url}" width="220" height="342">
    <h2>{title}</h2>
</div>
'''


def create_video_tiles_content(videos):
    """Create video tiles by taking the actual values and filling those in HTML"""

    # The HTML content for this section of the page
    content = ''
    for video in videos:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', video.trailer_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', video.trailer_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the video with its content filled in
        if video.video_type() == 'movie': # video is a movie
          content += movie_tile_content.format(
            title = video.title,
            storyline = video.storyline,
            duration = video.duration,
            stars = video.stars,
            genre = video.genre,
            poster_url= video.poster_url,
            trailer_youtube_id= trailer_youtube_id,
            rating = video.rating,
            p_rating = video.RATINGS,
            year = video.year
          )
        else: # Video is a TV serial
            content += tvserial_tile_content.format(
              title = video.ep_title,
              storyline = video.storyline,
              duration = video.duration,
              stars = video.stars,
              genre = video.genre,
              poster_url= video.poster_url,
              trailer_youtube_id= trailer_youtube_id,
              rating = video.rating,
              season_title = video.title,
              p_rating = video.RATINGS,
              season = video.season,
              episode = video.episode,
              tv_station = video.tv_station
            )

    return content


def open_videos_page(videos):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')
    
    # Replace the video tiles placeholder generated content
    rendered_content = main_page_content.format(
        video_tiles=create_video_tiles_content(videos))

    # Concatenate all the portions of the head (i.e. styles and scripts)
    main_page_head = main_page_style + video_info_modal_script + \
					trailer_modal_script + animate_tiles_script

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    
    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)