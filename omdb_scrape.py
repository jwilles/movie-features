import requests
import os


def send_request(title):
    # Request
    apiKey = os.environ['apiKey']
    omdb_url = 'http://www.omdbapi.com'

    try:
        response = requests.get(
            url= omdb_url,
            params={
                "apikey": apiKey,
		"t": title
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    return response.content


if __name__ == '__main__':
  
  print send_request("ratatouille")
 
