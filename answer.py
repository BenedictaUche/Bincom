from collections import Counter
import numpy as np
import random
import psycopg2

# Reading the data from the table
data = """
GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE
GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE
BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE
"""

# Splitting the data by line and then by comma
colors = data.strip().split("\n")
colors = [color.strip().split(",") for color in colors]
colors = [color for sublist in colors for color in sublist]

# Counting the frequency of each color
colors_freq = Counter(colors)

# Getting the mean color
mean_color = max(colors_freq, key=colors_freq.get)
print("Mean color: ", mean_color)

# Getting the most worn color
most_worn_color = max(colors_freq, key=colors_freq.get)
print("Most worn color: ", most_worn_color)

# Getting the median color
colors_sorted = sorted(colors)
median_index = len(colors_sorted) // 2
median_color = colors_sorted[median_index]
print("Median color: ", median_color)

# Bonus - Getting the variance of the colors
colors_count = np.array(list(colors_freq.values()))
variance = np.var(colors_count)
print("Variance of colors: ", variance)

# Bonus - Getting the probability of a color being red
total_colors = len(colors)
red_colors = colors_freq["RED"]
probability_red = red_colors / total_colors
print("Probability of a color being red: ", probability_red)

# Bonus - Recursive searching algorithm to search for a number entered by user in a list of numbers
def recursive_search(numbers, target):
    if not numbers:
        return False
    if numbers[0] == target:
        return True
    return recursive_search(numbers[1:], target)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = int(input("Enter a number to search for in the list: "))
print("Found number: ", recursive_search(numbers, target))

# Saving the colors and their frequencies in a PostgreSQL database
try:
    connection = psycopg2.connect(user = "user",
                                  password = "password",
                                  host = "host",
                                  port = "port",
                                  database = "database")
    cursor = connection.cursor()

    # Creating the table
    create_table_query = '''CREATE TABLE colors_freq
            (color TEXT PRIMARY KEY NOT NULL,
            frequency INT NOT NULL); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

    # Inserting the data into the table
    for color, freq in colors_freq.items():
        insert_data_query = f"INSERT INTO colors_freq (color, frequency) VALUES ('{color}', {freq});"
        cursor.execute(insert_data_query)
    connection.commit()
    print("Data inserted successfully into colors_freq table")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# Generating a random 4-digit number of 0s and 1s and converting it to base 10
random_binary = "".join([str(random.randint(0, 1)) for _ in range(4)])
base_10 = int(random_binary, 2)
print("Random 4-digit binary number: ", random_binary)
print("Converted to base 10: ", base_10)

# Summing the first 50 Fibonacci numbers
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 50
fib_sum = sum([fibonacci(i) for i in range(1, n+1)])
print("Sum of the first 50 Fibonacci numbers: ", fib_sum)


