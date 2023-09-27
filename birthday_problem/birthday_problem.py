import random

def birthday_simulation(group_size, num_simulations):
    shared_birthday_count = 0

    for _ in range(num_simulations):
        birthdays = [random.randint(1, 365) for _ in range(group_size)]
        if len(birthdays) != len(set(birthdays)):
            shared_birthday_count += 1

    probability = shared_birthday_count / num_simulations
    return probability

def main():
    num_simulations = 10000  # Number of simulations to run
    group_sizes = [5, 10, 15, 20, 23, 25, 30, 35, 40, 45, 50]

    print("Simulation Results:")
    for size in group_sizes:
        probability = birthday_simulation(size, num_simulations)
        print(f"Group size {size}: Estimated probability = {probability:.4f}")

if __name__ == "__main__":
    main()

