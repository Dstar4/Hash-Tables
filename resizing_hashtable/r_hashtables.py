

# Linked List hash table key/value pair
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Resizing hash table
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = count
        self.storage = [None for i in range(capacity)]


def hash(string):
    tmp = 5381
    byte_array = string.encode('utf-8')
    for byte in byte_array:
        tmp = ((tmp * 33) ^ byte) % 0x100000000
    return tmp


# TODO Handle collisions with LL
def hash_table_insert(hash_table, key, value):
    hashed_key = hash(key)
    index = hashed_key % hash_table.capacity
    new_node = LinkedPair(key, value)
    existing_node = hash_table.storage[index]
    if existing_node:
        # Look for an existing node with the same key
        if existing_node.key == key:
            # If you are overwriting a key with a different value, print a warning.
            print("You are overwriting an existing key's value.")
            existing_node.value == value
        existing_node = existing_node.next
    else:
        hash_table.storage[index] = new_node


# Fill this in.
# If you try to remove a value that isn't there, print a warning.
def hash_table_remove(hash_table, key):
     # same setup as insert
    hashed_key = hash(key)
    index = hashed_key % hash_table.capacity

    existing_node = hash_table.storage[index]
    if existing_node:
        last_node = None
        # while the current index exists
        while existing_node:
            if existing_node.key == key:
                # if last node is not None set it to the next node
                if last_node:
                    last_node.next_node = existing_node.next_node
                # else set the key
                else:
                    hash_table.storage[index] = existing_node.next_node
            last_node = existing_node
            existing_node = existing_node.next_node
    else:
        # If you try to remove a value that isn't there, print a warning.
        print("Unable to remove item")
# Should return None if the key is not found.
        return None


# Should return None if the key is not found.
def hash_table_retrieve(hash_table, key):
    hashed_key = hash(key)
    index = hashed_key % hash_table.capacity

    existing_node = hash_table.storage[index]
    if existing_node:
        return existing_node.value


def hash_table_resize(hash_table):
    isNone = 0
    isSomething = 0
    for element in hash_table.storage:
        if hash_table.count/hash_table.capacity >= .5:
            hash_table.capacity = (hash_table.capacity * 2)


def Testing():
    ht = HashTable(2)
    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")
    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #   + " to " + str(new_capacity) + ".")


Testing()
