#! python3
# movieStream.py finds the movie you would like to screen on https://soap2day.to/

import requests, sys, webbrowser, bs4


While True:

	movie = input('What would you like to watch?')
	url = movie.replace(' ', '%20')
	results = []
	movieNames = []

	print('Searching...') # display text while downloading page

	# Download the page.
	print('Downloading page %s...' % url)
	res = requests.get('https://soap2day.to/search/keyword/%' +  url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, features="html.parser")

	# Find URL of available movies
	movieElem = soup.select("div", class_="img-group") 
	if movieElem == []:
		print('Could not find movie.')
		movie = input('Please enter new movie title...')
		False
	else:
		results = soup.find_all("div.img-group > a")
		results = min(3, len(results))

		#follow href & get name of movie
		for movie in range(results):
			movie = results[0].get('href').strip("http://") #Follow href link
			movieNames = movieNames.append(soup.select('div.alert alert-info')) #Find Name of movie

		#Select Movie 
		print('Movies available are...')
		for movie in range(results):
			print(movie)
		chosenFilm = input('which title would you like to see?')
		chosenFilm = requests.get(chosenFilm)

		continue

#Open browser for film
webbrowser.open('https://soap2day.to' + results[chosenFilm]) 