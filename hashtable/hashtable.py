class Node:
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node

    def get_key(self):
        return self.get_key

    def get_value(self):
        return self.get_value

    def get_next_node(self):
        return self.get_next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return f'Key[{key}], value[{value}]'


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def add_to_head(self, key, value):
        self.length += 1
        new_node = Node(key, value)
        prev_head = self.head
        self.head = new_node
        self.head.set_next(prev_head)

    def delete(self, key):
        cur = self.head
        if cur.key == key:
            self.head = self.head.next_node
            return cur.value

        prev = cur
        cur = cur.next_node
        # search linked list
        while cur is not None:
            # if found, delete it from the linked list,
            if cur.key == key:
                prev.set_next(cur.next_node)
                # then return the deleted value
                return cur
            prev = prev.next_node
            cur = cur.next_node
        raise Exception

    def contains(self, key):
        for i in self:
            if i.key == key:
                return i.value
        return None

    def __len__(self):
        return self.length

    def get_max(self):
        if not self.head:
            return None
        if len(self) is 0:
            return None
        sorted_ll = sorted([i.value for i in self])
        return sorted_ll[-1]

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next_node


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY
        self.table = [LinkedList()] * self.capacity
        self.stored_amount = 0

    """
    Return the length of the list you're using to hold the hash
    table data. (Not the number of items stored in the hash table,
    but the number of slots in the main list.)
    """

    def get_num_slots(self):
        return self.capacity

    # Return the load factor for this hash table.
    def get_load_factor(self):
        if self.stored_amount is 0:
            return 0
        return self.stored_amount/self.capacity

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
    """

    def put(self, key, value):
        hashed_index = self.hash_index(key)
        linked_list = self.table[hashed_index]
        # search for key in linked list
        for i in linked_list:
            # if found, update it
            if i.key == key:
                i.value = value
                return
        # if not found,
        # make a new HashTableEntry and add it to the list
        # TODO
        # check if 0.2 < load factor < 0.7
        # then resize to
        # 8 if it is > 0.2, or double the current capacity if < 0.7
        linked_list.add_to_head(key, value)

    """
    Remove the value stored with the given key.

    Print a warning if the key is not found.
    """

    def delete(self, key):
        hashed_index = self.hash_index(key)
        linkedlist = self.table[hashed_index]

        try:
            linkedlist.delete(key)
        except ValueError:
            print('***WARNING***\nThat key does not exist in this hash table.')
            return None

    """
    Retrieve the value stored with the given key.
    Returns None if the key is not found.
    """

    def get(self, key):
        hashed_index = self.hash_index(key)
        return self.table[hashed_index].contains(key)

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
