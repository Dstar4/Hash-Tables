# Basic hash table key/value pair
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# Basic hash table
# Fill this in.  All storage values should be initialized to None
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]


# Fill this in.
# Research and implement the djb2 hash function
def hash(string):
    tmp = 5381
    byte_array = string.encode('utf-8')
    for byte in byte_array:
        tmp = ((tmp * 33) ^ byte) % 0x100000000
    return tmp


"""
def djb2(key):
    hash = 5381
    for c in key:
        hash = (hash * 33) + ord(c)
    return hash
"""

# Fill this in.


def hash_table_insert(hash_table, key, value):
    # hash the key so you can compare the hashed keys
    hashed_key = hash(key)
    index = hashed_key % hash_table.capacity
    # print('\nIndex', index)

    # Create a new node with the Pair class
    new_node = Pair(key, value)
    # Look for an existing node with the same key
    existing_node = hash_table.storage[index]

    if existing_node:
        # last_node = None

        while existing_node:
            if existing_node.key == key:
                # If you are overwriting a key with a different value, print a warning.
                print("You are overwriting an existing key's value.")
                existing_node.value == value
                return

            # last_node = existing_node
            existing_node = existing_node.next_node
        # last_node.next_node = new_node

    else:
        hash_table.storage[index] = new_node
        # Fill this in.
        # If you try to remove a value that isn't there, print a warning.


def hash_table_remove(hash_table, key):
    pass


# Fill this in.
# Should return None if the key is not found.
def hash_table_retrieve(hash_table, key):
    pass


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
