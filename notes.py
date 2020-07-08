'''
A hash function takes an input (string) and changes it into an integer
'''


def naive_hashing(str, list_len):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte
    return sum % list_len


starter_colours = [("aqua", "#00FFFF"),
                   ("beige", "#F5F5DC"),
                   ("chartreuse", "#7FFF00"),
                   ("deepskyblue", "#00BFFF"),
                   ("forestgreen", "#228B22")]

colours = [None] * len(starter_colours)

for color_name, color_value in starter_colours:
    colours[naive_hashing(color_name, len(starter_colours))] = color_value


'''
The General Problem the Hash Table Solve
----------------------------------------
They search fast! O(1)
We can use it to store and retrieve the results of any slow operation.
So if we have a slow operation, we can use a hash table to optimize it.
Cache is an application of a hash table.
Rainbow table: https://en.wikipedia.org/wiki/Rainbow_table

'''

if __name__ == "__main__":
    print(colours[naive_hashing('aqua', len(colours))])
