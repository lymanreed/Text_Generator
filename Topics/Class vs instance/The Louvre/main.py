class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def show_info(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the {Painting.museum}.')


def main():
    painting = Painting(input(), input(), input())
    painting.show_info()


if __name__ == "__main__":
    main()
