class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY
        self.table = [None] * self.capacity

    """
    Return the length of the list you're using to hold the hash
    table data. (Not the number of items stored in the hash table,
    but the number of slots in the main list.)
    """

    def get_num_slots(self):
        return self.capacity

    # Return the load factor for this hash table.
    def get_load_factor(self):
        pass

    # FNV-1 Hash, 64-bit
    def fnv1(self, key):
        # pseudo code source -- https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
        # and to learn more about the XOR operator source
        # https://kite.com/python/answers/how-to-use-the-xor-operator-in-python
        FNV_offset_basis = 0xcbf29ce484222325
        FNV_prime = 0x100000001b3

        hash = FNV_offset_basis
        for letter_val in key.encode():
            hash *= FNV_prime
            hash ^= letter_val
        return hash

    # DJB2 hash, 32-bit
    def djb2(self, key):
        # pseudo code source -- http://www.cse.yorku.ca/~oz/hash.html
        hash = 5381

        for letter_val in key.encode():
            hash = (hash * 33) + letter_val
        return hash

    """
    Take an arbitrary key and return a valid integer index
    between within the storage capacity of the hash table.
    """

    def hash_index(self, key):
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    """
    Store the value with the given key.

    Hash collisions should be handled with Linked List Chaining.
    """

    def put(self, key, value):
        hashed_index = self.hash_index(key)
        self.table[hashed_index] = value

    """
    Remove the value stored with the given key.

    Print a warning if the key is not found.
    """

    def delete(self, key):
        hashed_index = self.hash_index(key)

        try:
            if self.table[hashed_index] is not None:
                self.table[hashed_index] = None
            return
        except ValueError:
            print('***WARNING***\nThat key does not exist in this hash table.')

    """
    Retrieve the value stored with the given key.
    Returns None if the key is not found.
    """

    def get(self, key):
        hashed_index = self.hash_index(key)

        try:
            return self.table[hashed_index]
        except:
            return None

    """
    Changes the capacity of the hash table and
    rehashes all key/value pairs.
    """

    def resize(self, new_capacity):
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
