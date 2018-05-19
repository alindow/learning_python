import os
import csv
from data_types import MovieTitle

def main():
        print_header()
        read_file()


def print_header():
    print("----------------------------")
    print("         IMDB TSV")
    print("----------------------------")


def read_file():
    base_path = os.path.dirname(__file__)
    file = os.path.join(base_path, "data", "data-title-basics.tsv")

    with open(file, 'r', encoding='utf-8') as fin:
#        line = fin.readline()
        reader = csv.DictReader(fin, delimiter = '\t')
        print("Header: {}".format(reader.fieldnames))
        movies = []

        for row in reader:
            m = MovieTitle.create_from_dict(row)
            movies.append(m)

        print("Anzahl Zeilen: {:,}".format(len(movies)))

        titles = (
            (m.original_title, m.primary_title, m.runtime_minutes)
            for m in movies
        )

        movies.sort(key = lambda m:  m.original_title)
        if movies:
            print("von {} bis {}".format(movies[0].original_title, movies[-1].original_title))

            movies.sort(key=lambda m: m.primary_title)
            print("von {} bis {}".format(movies[0].primary_title, movies[-1].primary_title))

            movies.sort(key=lambda m: m.runtime_minutes)
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes, movies[-1].primary_title, movies[-1].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes, movies[-10].primary_title, movies[-10].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes, movies[-1000].primary_title, movies[-1000].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes, movies[-100000].primary_title, movies[-100000].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes, movies[-1000000].primary_title, movies[-1000000].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes, movies[-2000000].primary_title, movies[-2000000].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes,
                                               movies[-3000000].primary_title, movies[-3000000].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes,
                                               movies[-3500000].primary_title, movies[-3500000].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes,
                                               movies[-3499500].primary_title, movies[-3499500].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes,
                                               movies[-3499750].primary_title, movies[-3499750].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes,
                                               movies[-3470000].primary_title, movies[-3470000].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes,
                                               movies[-3400000].primary_title, movies[-3400000].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes,
                                               movies[-3469000].primary_title, movies[-3469000].runtime_minutes))
            print("von {} {} bis {} {}".format(movies[0].primary_title, movies[0].runtime_minutes,
                                               movies[-4000000].primary_title, movies[-4000000].runtime_minutes))


if __name__ == '__main__':
    main()