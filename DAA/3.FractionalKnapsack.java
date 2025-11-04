// Assignment No-3
// To solve a fractional Knapsack problem using a greedy method.

import java.util.*;

class Item {
    int value, weight;
    double ratio;

    Item(int value, int weight) {
        this.value = value;
        this.weight = weight;
        this.ratio = (double) value / weight;
    }
}

public class FractionalKnapsack {

    public static double getMaxValue(Item[] items, int capacity) {
        Arrays.sort(items, (a, b) -> Double.compare(b.ratio, a.ratio));
        double totalValue = 0.0;
        int remainingCapacity = capacity;

        System.out.println("\nItems chosen:");
        System.out.println("--------------------------------------------------");
        System.out.println("Item\tValue\tWeight\tTaken");
        System.out.println("--------------------------------------------------");

        for (Item item : items) {
            if (remainingCapacity == 0)
                break;

            if (item.weight <= remainingCapacity) {
                totalValue += item.value;
                remainingCapacity -= item.weight;
                System.out.printf("%d\t%d\t%d\t%.2f%n",
                        Arrays.asList(items).indexOf(item) + 1,
                        item.value, item.weight, 1.0);
            } else {
                double fraction = (double) remainingCapacity / item.weight;
                totalValue += item.value * fraction;
                System.out.printf("%d\t%d\t%d\t%.2f%n",
                        Arrays.asList(items).indexOf(item) + 1,
                        item.value, item.weight, fraction);
                remainingCapacity = 0;
            }
        }

        System.out.println("--------------------------------------------------");
        System.out.println("Knapsack Capacity Used: " + (capacity - remainingCapacity) + " / " + capacity);
        System.out.printf("Maximum value in Knapsack = %.2f%n", totalValue);
        return totalValue;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        Item[] items = new Item[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Enter value of item " + (i + 1) + ": ");
            int value = sc.nextInt();
            System.out.print("Enter weight of item " + (i + 1) + ": ");
            int weight = sc.nextInt();
            items[i] = new Item(value, weight);
        }

        System.out.print("Enter knapsack capacity: ");
        int capacity = sc.nextInt();

        getMaxValue(items, capacity);
        sc.close();
    }
}

// Input-output format

/*
 * Enter number of items: 3
 * Enter value of item 1: 24
 * Enter weight of item 1: 15
 * Enter value of item 2: 15
 * Enter weight of item 2: 10
 * Enter value of item 3: 25
 * Enter weight of item 3: 18
 * Enter knapsack capacity: 20
 * 
 * Items chosen:
 * -------------------------------------------------------------
 * Item Value Weight Taken
 * 1 24 15 1.00
 * 2 15 10 0.50
 * -------------------------------------------------------------
 * Knapsack Capacity Used: 20 / 20
 * Maximum value in Knapsack = 31.50
 */
