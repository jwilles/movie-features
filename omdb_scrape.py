import requests
import os
import csv 
import sys

def send_request(movies):

  apiKey = os.environ['apiKey']
  omdb_url = 'http://www.omdbapi.com'

  
  for idx, movie in enumerate(movies):
    try:
        response = requests.get(
            url= omdb_url,
            params={
                "apikey": apiKey,
        	"t": movie[2]
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
#        print('Response HTTP Response Body: {content}'.format(
#            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    movies[idx].append(response.content)

  return movies


def read_movie_list(filename):
 
  movies = []
 
  f = open(filename, 'rb')
  reader = csv.reader(f)

  for row in reader:
    movies.append(row)
  f.close()
 
  return movies  


if __name__ == '__main__':

  movie_list = '../data/netflix-prize-data/movie_titles.csv'
  movies = read_movie_list(movie_list)

  print len(movies) 

  print movies[:2]

  print send_request(movies[:2])

 # for movie in movies:
#	print movie
  #print send_request("ratatouille")
 
