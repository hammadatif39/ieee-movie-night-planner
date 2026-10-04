import os
from models import Movie

def load_movies(filepath):
    movies = []
    try:
        with open(filepath, 'r') as file:
            next(file) # Skip header
            for line in file:
                try:
                    title, genre, rating, duration = line.strip().split(',')
                    movies.append(Movie(title, genre, rating, duration))
                except ValueError:
                    print(f"Skipping corrupted line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
    finally:
        print("Data loading process completed.\n")
    return movies

def main():
    movies_db = load_movies("data/movies.csv")
    watchlist = set() # Set to prevent duplicate movies

    while True:
        print("\n--- Movie Night Planner ---")
        print("1. View All Movies")
        print("2. Search by Genre")
        print("3. Add to Watchlist")
        print("4. View Watchlist Analytics")
        print("5. Exit")
        
        choice = input("Select an option: ").strip()

        if choice == '1':
            for m in movies_db:
                print(m)

        elif choice == '2':
            genre = input("Enter genre to search: ").strip()
            # List Comprehension for filtering
            results = [m for m in movies_db if m.genre.lower() == genre.lower()]
            if results:
                for r in results:
                    print(r)
            else:
                print("No movies found in that genre.")

        elif choice == '3':
            title = input("Enter movie title to add: ").strip()
            found = next((m for m in movies_db if m.title.lower() == title.lower()), None)
            if found:
                if found.title in watchlist:
                    print("Movie is already in your watchlist!")
                else:
                    watchlist.add(found.title)
                    print(f"Added '{found.title}' to watchlist.")
            else:
                print("Movie not found in database.")

        elif choice == '4':
            if not watchlist:
                print("Watchlist is empty.")
                continue
            
            # Retrieve movie objects from the set of titles
            watchlist_movies = [m for m in movies_db if m.title in watchlist]
            
            total_duration = sum(m.duration for m in watchlist_movies)
            avg_rating = sum(m.rating for m in watchlist_movies) / len(watchlist_movies)
            
            print("\n--- Watchlist Analytics ---")
            print(f"Movies saved: {', '.join(watchlist)}")
            print(f"Total Duration: {total_duration} minutes")
            print(f"Average Rating: {avg_rating:.1f}/10")

        elif choice == '5':
            print("Enjoy your movie night!")
            break
        else:
            print("Invalid choice, please select 1-5.")

if __name__ == "__main__":
    main()