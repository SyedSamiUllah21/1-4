movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

def add_movies():
    try:
        num_movies_add = int(input("How many movies you want to add? "))
        for _ in range(num_movies_add):
            name = input("Enter the movie name: ")
            budget = int(input("Enter the movie budget: "))
            movies.append((name, budget))
    except ValueError:
        print("Invalid input. Please enter valid numbers for budget.")

def calculate_average_budget(movie_list):
    total_movies_Budget = sum(budget for _, budget in movie_list)
    average_movie_budget = total_movies_Budget / len(movie_list) if movie_list else 0
    return average_movie_budget

def print_high_budget_movies(movie_list, avg_budget):
    count = 0
    print(f"\nAverage movie budget: pkr{avg_budget:,.2f}")
    print("\nMovies with a budget higher than the average:")
    
    for movie, budget in movie_list:
        if budget > avg_budget:
            count += 1
            difference = budget - avg_budget
            print(f"{movie}: pkr{budget:,.2f} (Exceeds average by pkr{difference:,.2f})")
    
    print(f"\nno. movies with a budget higher than the average: {count}")

add_movies()  
average_movie_budget = calculate_average_budget(movies)
print_high_budget_movies(movies, average_movie_budget)
