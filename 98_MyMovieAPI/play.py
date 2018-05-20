import requests
import collections

def search(search):
    api_key="408ba11ecd062d4001fee034de52a73c"

    page = 1
    while True:
        url = 'https://api.themoviedb.org/3/search/movie?query={}&page={}&api_key={}'.format(search,page,api_key)
        resp = requests.get(url)
        movie_data = show_response(resp.json(), page)
        print("Seite {}/ {}".format(movie_data.get("page"),movie_data.get("total_pages")))
        page += 1
        if page > resp.json().get("total_pages") or page == 1000:
            break


def show_response(movie_data,page):
    movie_list = movie_data.get("results")
    MovieResult = collections.namedtuple(
        "MovieResult",
        "vote_count,id,video,vote_average,title,popularity,poster_path,original_language,original_title,genre_ids,backdrop_path,adult,overview,release_date"
    )
    movies = []
    for md in movie_list:
        m = MovieResult(**md)
        movies.append(m)
    movies.sort(key=lambda m: m.release_date, reverse=True)
    for movie in movies:
        print("{} -- {} -- {} -- {}".format(movie.release_date, movie.title, movie.original_title, movie.overview))
    print("Filme {}/{}".format((20 * (page - 1) + len(movies)), movie_data.get("total_results")))
    return movie_data


def main():
    print_header()
    while True:
        x = input("Suchbegriff: ")
        if not x or x.strip().lower() == 'x':
            break
        search(x)

def print_header():
    print("---------------------------------")
    print("             TNDB APP")
    print("---------------------------------")
    print("This product uses the TMDb API but is not endorsed or certified by TMDb.")

if __name__ == '__main__':
    main()