import requests


class TMDbClient:
    def __init__(self):
        self.API_URL = "https://api.themoviedb.org/3/"
        self.API_KEY = "c413685faeb150bb07fcc78a8014a769"  # Replace 'YOUR_API_KEY' with your actual TMDb API key

    def get_popular_movies(self, language="en-US"):
        response = requests.get(
            self.API_URL + "movie/popular",
            params={"api_key": self.API_KEY, "language": language, "page": 1},
        )
        return response.json()

    def search_movies(self, query, language="en-US"):
        response = requests.get(
            self.API_URL + "search/movie",
            params={
                "api_key": self.API_KEY,
                "language": language,
                "query": query,
                "page": 1,
            },
        )
        return response.json()


client = TMDbClient()

while True:
    secim = input("1-Get popular movies\n2-Search Movies\n3-Exit\nEnter your choice: ")
    if secim == "3":
        print("Exiting the program.")
        break
    language = (
        input(
            "Enter language code (e.g., 'en-US' for English, 'tr-TR' for Turkish). Default is 'en-US': "
        )
        or "en-US"
    )
    if secim == "1":
        popular_movies = client.get_popular_movies(language=language)
        for movie in popular_movies["results"]:
            print(f"Title: {movie['title']}, Release Date: {movie['release_date']}")
    elif secim == "2":
        query = input("Enter movie name to search: ")
        search_results = client.search_movies(query=query, language=language)
        for movie in search_results["results"]:
            print(f"Title: {movie['title']}, Release Date: {movie['release_date']}")
    else:
        print("Invalid input. Please try again.")
