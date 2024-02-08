#  RECOMMENDATION SYSTEM

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_user_preferences(movie_names):
    print("Rate each movie on a scale of 1 to 10:")
    user_preferences = []
    for i, movie_name in enumerate(movie_names):
        while True:
            try:
                rating = int(input(f"Enter your rating for {movie_name}: "))
                if 1 <= rating <= 10:
                    break
                else:
                    print("Invalid rating. Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        user_preferences.append(rating)
    return np.array(user_preferences)

def recommend_movies(movie_names, movie_preferences, user_preferences, top_n=2):

    user_movie_matrix = np.vstack((user_preferences, movie_preferences))

    similarity_scores = cosine_similarity(user_movie_matrix)[0][1:]

    sorted_indices = np.argsort(similarity_scores)[::-1]

    top_n_recommendations = [(movie_names[idx], similarity_scores[idx]) for idx in sorted_indices[:top_n]]

    return top_n_recommendations

def main():
    movie_names = ["Inception", "Interstellar", "The Matrix", "Tenent", "Oppenheimer"]
    num_movies = len(movie_names)

    print("Welcome to the Movie Recommendation System!\n")

    user_preferences = get_user_preferences(movie_names)
    recommended_movies = recommend_movies(movie_names, np.random.randint(1, 11, size=(num_movies,)), user_preferences, top_n=2)

    print(f"\nYour movie preferences: {user_preferences}")
    print("Recommended movies:")
    for movie, similarity_score in recommended_movies:
        print(f"{movie} (Similarity Score: {similarity_score:.2f})")

if __name__ == "__main__":
    main()
