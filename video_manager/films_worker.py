import os

film_storage_path = r"D:\Python\dz 15\video_manager\film_storage"

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    directory_path = os.path.join(film_storage_path, letter)
    os.makedirs(directory_path, exist_ok=True)

import os

class Film:
    def __init__(self, title, description, director, writer, cast, running_time, country, language, imdb_rating,
                 year, budget, box_office, profitable, oscar_nominated, oscar_win, trailer_link):
        self.title = title
        self.description = description
        self.director = director
        self.writer = writer
        self.cast = cast
        self.running_time = running_time
        self.country = country
        self.language = language
        self.imdb_rating = imdb_rating
        self.year = year
        self.budget = budget
        self.box_office = box_office
        self.profitable = profitable
        self.oscar_nominated = oscar_nominated
        self.oscar_win = oscar_win
        self.trailer_link = trailer_link
        self.storage_address = self.upload_file()

    def upload_file(self):

        first_letter = self.title[0].upper()
        file_name = f"{self.title.replace(' ', '_')}.txt"
        directory_path = os.path.join("film_storage", first_letter, "D")

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        file_path = os.path.join(directory_path, file_name)

        with open(file_path, "w") as file:
            file.write(f"Title: {self.title}\n")
            file.write(f"Description: {self.description}\n")
            file.write(f"Director: {', '.join(self.director)}\n")
            file.write(f"Writer: {self.writer}\n")
            file.write(f"Cast: {', '.join(self.cast)}\n")
            file.write(f"Running time: {self.running_time} minutes\n")
            file.write(f"Country: {self.country}\n")
            file.write(f"Language: {self.language}\n")
            file.write(f"IMDb Rating: {self.imdb_rating}\n")
            file.write(f"Year: {self.year}\n")
            file.write(f"Budget: ${self.budget}\n")
            file.write(f"Box Office: ${self.box_office}\n")
            file.write(f"Profitable: {'Yes' if self.profitable else 'No'}\n")
            file.write(f"Oscar Nominated: {'Yes' if self.oscar_nominated else 'No'}\n")
            file.write(f"Oscar Win: {'Yes' if self.oscar_win else 'No'}\n")
            file.write(f"Trailer Link: {self.trailer_link}\n")

        return file_path

    def get_film_address(self):
        """
        Повертає повний шлях до фільму у директорії.
        """
        first_letter = self.title[0].upper()
        file_name = f"{self.title.replace(' ', '_')}.txt"
        return os.path.join("film_storage", first_letter, "D", file_name)

    def display_info(self):
        """
        Виводить інформацію про фільм.
        """
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Director: {', '.join(self.director)}")
        print(f"Writer: {self.writer}")
        print(f"Cast: {', '.join(self.cast)}")
        print(f"Running time: {self.running_time} minutes")
        print(f"Country: {self.country}")
        print(f"Language: {self.language}")
        print(f"IMDb Rating: {self.imdb_rating}")
        print(f"Year: {self.year}")
        print(f"Budget: ${self.budget}")
        print(f"Box Office: ${self.box_office}")
        print(f"Profitable: {'Yes' if self.profitable else 'No'}")
        print(f"Oscar Nominated: {'Yes' if self.oscar_nominated else 'No'}")
        print(f"Oscar Win: {'Yes' if self.oscar_win else 'No'}")
        print(f"Trailer Link: {self.trailer_link}")
        print(f"Storage Address: {self.storage_address}")

if __name__ == "__main__":
    death_on_the_nile_data = {
        "title": "Death on the Nile",
        "description": "Detective Hercule Poirot investigates the murder of a young heiress while on vacation on the Nile.",
        "director": ["Kenneth Branagh"],
        "writer": "Michael Green",
        "cast": ["Kenneth Branagh", "Gal Gadot", "Armie Hammer"],
        "running_time": 127,
        "country": "United States",
        "language": "English",
        "imdb_rating": 6.6,
        "year": 2022,
        "budget": 90000000,
        "box_office": 136900000,
        "profitable": True,
        "oscar_nominated": False,
        "oscar_win": False,
        "trailer_link": "https://www.imdb.com/video/vi3877612057/"
    }

    death_on_the_nile = Film(**death_on_the_nile_data)
    death_on_the_nile.display_info()

    print("Film Address:", death_on_the_nile.get_film_address())