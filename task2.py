# AI-Based Recommendation System (Content-Based)

# Movie database with genres
movies = {
    "Action": ["Avengers", "Batman", "Iron Man"],
    "Comedy": ["Mr Bean", "The Mask", "Home Alone"],
    "Drama": ["Titanic", "Notebook", "Forrest Gump"]
}

# User preference input
user_choice = input("Enter your favorite genre (Action/Comedy/Drama): ")

# AI Recommendation Logic
if user_choice in movies:
    print("\nRecommended movies for you:")
    for movie in movies[user_choice]:
        print("-", movie)
else:
    print("Sorry! Genre not found.")