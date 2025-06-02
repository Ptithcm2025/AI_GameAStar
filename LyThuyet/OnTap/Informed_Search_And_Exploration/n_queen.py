import random

def read_data():
    try:
        n = int(input("Enter the value of n: "))
        return n
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return read_data()

def is_safe(board, row, col, n): 
    
    # Row
    for i in range(row): 
        if board[i][col] == 1:
            return False

    # Main Diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    # Secondary Diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def fitness(chromosome, n):
    # Calculate the number of non-attacking pairs of queens
    non_attacking = 0
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking += 1
    return non_attacking

def selection(population, fitnesses):
    # Select two parents using roulette wheel selection
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents

def crossover(parent1, parent2, n):
    # Perform single-point crossover
    point = random.randint(1, n - 1)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(chromosome, n, mutation_rate=0.1):
    # Perform mutation with a given mutation rate
    if random.random() < mutation_rate:
        index = random.randint(0, n - 1)
        chromosome[index] = random.randint(0, n - 1)
    return chromosome

def solve_n_queens(n, population_size=100, generations=1000, mutation_rate=0.1):
    # Initialize population
    population = [[random.randint(0, n - 1) for _ in range(n)] for _ in range(population_size)]
    
    for generation in range(generations):
        # Calculate fitness for each chromosome
        fitnesses = [fitness(chromosome, n) for chromosome in population]
        
        # Check if a solution is found
        if max(fitnesses) == n * (n - 1) // 2:
            solution = population[fitnesses.index(max(fitnesses))]
            return solution
        
        # Create the next generation
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selection(population, fitnesses)
            child1 = mutate(crossover(parent1, parent2, n), n, mutation_rate)
            child2 = mutate(crossover(parent2, parent1, n), n, mutation_rate)
            new_population.extend([child1, child2])
        
        population = new_population
    
    return None  # Return None if no solution is found

def display_board(solution, n):
    board = [["." for _ in range(n)] for _ in range(n)]
    for row, col in enumerate(solution):
        board[row][col] = "Q"
    for row in board:
        print(" ".join(row))

def n_queen(n):
    solution = solve_n_queens(n)
    if solution:
        print("Solution found:", solution)
        display_board(solution, n)
    else:
        print("No solution found.")

def main():
    n = read_data()
    n_queen(n)

if __name__ == "__main__":
    main()