import random

def birthday_generalization_simulation(group_size, n, num_simulations):
    shared_birthday_count = 0

    for _ in range(num_simulations):
        birthdays = [random.randint(1, 365) for _ in range(group_size)]
        unique_birthdays = set(birthdays)
        for birthday in unique_birthdays:
            if birthdays.count(birthday) >= n:
                shared_birthday_count += 1
                break  # Exit the loop if n or more people share the same birthday

    probability = shared_birthday_count / num_simulations
    return probability

def main():
    num_simulations = 1000000  # Number of simulations to run
    #group_sizes = [30, 40, 50]  # Example group sizes
    group_sizes = [30]
    n = 3  # Minimum number of people sharing a birthday

    print(f"Simulation Results (at least {n} people sharing a birthday):")
    for size in group_sizes:
        probability = birthday_generalization_simulation(size, n, num_simulations)
        print(f"Group size {size}: Estimated probability = {probability:.4f}")

if __name__ == "__main__":
    main()

