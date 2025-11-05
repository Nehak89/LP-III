def fractional_knapsack(values, weights, capacity):
    n = len(values)
    items = []

    # Create list of items with value/weight ratio
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i], i + 1))

    # Sort items by ratio (value per weight), descending
    items.sort(reverse=True)

    total_value = 0.0
    total_weight = 0.0
    chosen = []

    # Pick items greedily
    for ratio, value, weight, index in items:
        if capacity == 0:
            break

        if weight <= capacity:
            # Take whole item
            taken = 1.0
            total_value += value
            total_weight += weight
            capacity -= weight
        else:
            # Take fractional part
            taken = capacity / weight
            total_value += value * taken
            total_weight += weight * taken
            capacity = 0

        chosen.append((index, value, weight, taken))

    return chosen, total_value, total_weight

values = []
weights = []

n = int(input("Enter number of items: "))
for i in range(n):
    val = float(input(f"Enter value of item {i+1}: "))
    wt = float(input(f"Enter weight of item {i+1}: "))
    values.append(val)
    weights.append(wt)

capacity = float(input("Enter knapsack capacity: "))

chosen_items, max_value, used_capacity = fractional_knapsack(values, weights, capacity)

print("\nItems chosen:\n")
print("------------------------------------------------------------")
print("Item\tValue\tWeight\tTaken")
for item in chosen_items:
    print(f"{item[0]}\t{item[1]:.0f}\t{item[2]:.0f}\t{item[3]:.2f}")
print("------------------------------------------------------------")
print(f"\nKnapsack Capacity Used: {used_capacity:.0f} / {sum(weights):.0f}")
print(f"Maximum value in Knapsack = {max_value:.2f}")


"""

INPUT-OUTPUT:-

Enter number of items:  3
Enter value of item 1:  24
Enter weight of item 1:  15
Enter value of item 2:  15
Enter weight of item 2:  10
Enter value of item 3:  25
Enter weight of item 3:  18
Enter knapsack capacity:  20

Items chosen:

------------------------------------------------------------
Item	Value	Weight	Taken
1	24	15	1.00
2	15	10	0.50
------------------------------------------------------------

Knapsack Capacity Used: 20 / 43
Maximum value in Knapsack = 31.50

"""