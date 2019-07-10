

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
        self.count = 0
        self.storage = [None] * capacity


def hash(string, max):
    tmp = 5381
    for x in string:
        tmp = ((tmp << 5)+tmp) + ord(x)
    return tmp % max


# TODO Handle collisions with LL
def hash_table_insert(hash_table, key, value):
    hashed_key = hash(key, hash_table.capacity)
    # check for existing key
    if hash_table.storage[hashed_key] == None:
        # if no key create one with this key and value
        hash_table.storage[hashed_key] = LinkedPair(key, value)
        # increment the count
        hash_table.count += 1

    # else if existing key
    else:
        tmp = hash_table.storage[hashed_key]
        if tmp.key == key:
            hash_table.storage[hashed_key].value = value
            return None

        # for handeling duplicates
        else:
            while tmp.next is not None:
                tmp = tmp.next

                if tmp.key == key:
                    tmp.value = value
                    return None

        # set the next node to new linked pair
        tmp.next = LinkedPair(key, value)
        hash_table.count += 1
    # if over 80% full resize
    if hash_table.count >= 0.8 * hash_table.capacity:
        hash_table = hash_table_resize(hash_table)


# If you try to remove a value that isn't there, print a warning.
def hash_table_remove(hash_table, key):
    hashed_key = hash(key, hash_table.capacity)

    # check if key exists
    if hash_table.storage[hashed_key] == None:
        print("Deleting a key that does not exist.")
        return None
    else:
        tmp = hash_table.storage[hashed_key]

        # check if tmp.next is none
        if tmp.next is not None:
            while tmp.next is not None:
                # check for the key in next node
                if tmp.next.key == key:
                    tmp.next = tmp.next.next
                    hash_table.count -= 1
                    # resize if needed
                    if hash_table.count >= 0.8 * hash_table.capacity:
                        hash_table = hash_table_resize(hash_table)
                        break
                tmp = tmp.next
        # check if the key matches
        else:
            if tmp.key == key:
                # set value to None
                hash_table.storage[hashed_key] = None
                # resize if needed
                if hash_table.count >= 0.8 * hash_table.capacity:
                    hash_table = hash_table_resize(hash_table)
                return None

# Should return None if the key is not found.


def hash_table_retrieve(hash_table, key):
    hashed_key = hash(key, hash_table.capacity)

    # check that the key exists
    if hash_table.storage[hashed_key] is not None:
        tmp = hash_table.storage[hashed_key]

        # handle multiple matching keys
        while tmp is not None:
            if tmp.key == key:
                return tmp.value
            tmp = tmp.next
    return None


def hash_table_resize(hash_table):
    # resize smaller if less than 20% full - create a new table
    if hash_table.count <= 0.2 * hash_table.capacity:
        new_hash_table = HashTable(hash_table.capacity/2)

    # resize larger if at least 70% full- create a new table
    if hash_table.count >= 0.7 * hash_table.capacity:
        new_hash_table = HashTable(hash_table.capacity * 2)

    # if resizing is needed copy over the data
    if hash_table.count <= 0.2 * hash_table.capacity or hash_table.count >= 0.7*hash_table.capacity:
        for i in range(hash_table.capacity):
            tmp = hash_table.storage[i]

            # do not copy over none values
            if tmp is not None:
                # insert a new node with the key and value
                while tmp is not None:
                    hash_table_insert(new_hash_table, tmp.key, tmp.value)
                    # check for duplicates
                    tmp = tmp.next
        # set the hash table to the new hash table
        hash_table = new_hash_table
    return hash_table


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
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
