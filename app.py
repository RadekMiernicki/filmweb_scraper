from scraper.links import Link, CollectedLinks
from scraper import filmweb
import time
from datetime import datetime


now = datetime.now

base_url = 'https://www.filmweb.pl'
url_list_movies = 'https://www.filmweb.pl/films/search'
url_list_series = 'https://www.filmweb.pl/serials/search'
url_list_persons = 'https://www.filmweb.pl/persons/search'


output_movies = 'movies_by_year.csv'
output_series = 'series_by_year.csv'

payload = {'connective':'OR', 'orderBy':'popularity', 'descending':'true'}




for year in [str(y) for y in range(1999,2000)]:



    params = {'startYear':year, 'endYear': year, 'startRate':'0', 'endRate':'10', 'page':'1'}
    params = {'startBirthDate': 1980, 'endBirthDate':1981}
    payload.update(params)

    print(payload)

    data = filmweb.GetLinks(url_list_series, payload)
    #print(data.url)
    for page in range(1,1001):
        movies = data.get_data(page).links
        if not movies:
            print(' * ' * 12)
            print(f'End of data for {year} on page {page} on {now().time()}')
            print(' * ' * 12)
            break
        time.sleep(3)
        if page % 100 == 0:
            time.sleep(30)
            print(page)
        with open (output_series, 'a+') as f:
            for movie in movies:
                row = str(movie.filmwebID)+';' + base_url + movie.linkHTML+';'
                row += str(movie.year) + ';' + '"' + movie.titleUTF8 + '"' + '\n'
                f.write(row)



