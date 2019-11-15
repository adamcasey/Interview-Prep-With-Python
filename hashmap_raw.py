# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()

# Create a HashMap in Python without using the builtin Dictionary

class HashMap:
    def __init__(self):
        # Initialize with empty lists
        self.store = [[] for _ in range(16)]
        self.size = 0
        self.key_2 = None
        self.value_2 = None

    def get(self, key):
        #key_hash = self._hash(key)
        key_hash = self._hash_2(key)
        index = self._position(key_hash)
        if not self.store[index]:
            return None
        else:
            list_at_index = self.store[index]
            for i in list_at_index:
                if i.key == key:
                    return i.value
            return None

    def put(self, key, value):
        p = Node(key, value)
        #self.key_2 = key
        #self.value_2 = value
        #key_hash = self._hash(key)
        key_hash = self._hash_2(key)
        index = self._position(key_hash)
        if not self.store[index]:
            self.store[index] = [p]
            self.size += 1
        else:
            list_at_index = self.store[index]
            #print(f'p: {p]
            if p not in list_at_index:
                list_at_index.append(p)
                self.size += 1
            else:
                for i in list_at_index:
                    # Define my own equivalence check below
                    print("i: {}".format(i))
                    if i == p:
                        i.value = value
                        return
                list_at_index.append(p)
                self.size += 1

    # Get the length of hashmap
    def __len__(self):
        return self.size
    
    # Using Python's built in hash()
    def _hash_2(self, key):
        if isinstance(key, int):
            return key
        else:
            return(hash(key))

    # Doing my own hashing
    def _hash(self, key):
        if isinstance(key, int):
            return key
        result = 5381
        for char in key:
            # Get an int from a char
            result = 33 * result + ord(char)
        return result

    def _position(self, key_hash):
        return key_hash % 15


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        #print(other)
        # Compares Node objects and returns True/False
        #print("__eq__: {}".format(self.key == other.key))
        return self.key == other.key


# if __name__ == '__main__':
#     hashmap = HashMap()
#     hashmap.put(2, 12)
#     hashmap.put('asd', 13)
#     hashmap.put(2, 11)
#     print(f'Hashmap length: {len(hashmap.store)}')
#     print(hashmap.get(2))
#     print(hashmap.get('asd'))
#     print(hashmap.get('ade'))
#     for k in hashmap.store:
#         print(k)

# Creates a list containing 5 lists, each of 8 items, all set to 0
width, height = 8, 5;
Matrix = [[0 for x in range(width)] for y in range(height)] 

for row in Matrix:
    print(row)