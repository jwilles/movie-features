import requests
import os
import csv 
import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')

def send_request(movies):

  apiKey = os.environ['apiKey']
  omdb_url = 'http://www.omdbapi.com'

  for idx, movie in enumerate(movies):
    try:
        response = requests.get(
            url= omdb_url,
            params={
                "apikey": apiKey,
        	"t": movie
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))

        print('Response HTTP Response Body: {content}'.format(
            content=response.content))

  

        content = json.loads(response.content)
        
        details = [
		  content['Year'],
                  content['Rated'],
		  content['Genre'],
		  content['Director'],
		  content['Actors'],
		  content['imdbRating']
		]

        for feature in details:
    	  movies[idx].append(feature)

    except requests.exceptions.RequestException:
        print('HTTP Request failed')

  return movies


def read_movie_csv(filename):
 
  movies = []
 
  f = open(filename, 'rb')
  reader = csv.reader(f)

  for row in reader:
    movies.append(row)
  f.close()
 
  return movies  

def read_movie_txt(filename):

  f = open(filename, 'r').readlines()

  movie_titles = [[x[:-1]] for x in f]
    
  return movie_titles


if __name__ == '__main__':

  netflix_movie_csv = '../data/netflix-prize-data/movie_titles.csv'
  movies_2017_list = './movies_2017.txt'
  #movies = read_movie_csv(netflix_movie_list)

  movies_2017 = read_movie_txt(movies_2017_list)

  movie_features = send_request(movies_2017)


  movie_features_csv = [['Title', 'Year', 'Rated', 'Genre', 'Director', 'Actors', 'imdbRating']]

  for movie in movie_features:
    movie_features_csv.append(movie)


  with open("features.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(movie_features_csv)

