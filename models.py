class Movie:
    def __init__(self, title, genre, rating, duration):
        self.title = title
        self.genre = genre
        self.rating = float(rating)
        self.duration = int(duration)

    def __str__(self):
        return f"{self.title} ({self.genre}) - Rating: {self.rating}/10 - {self.duration} mins"