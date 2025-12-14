# Assignment Extendible Hashing Implementation
class Bucket:
    def __init__(self, depth, size):
        self.depth = depth
        self.size = size
        self.items = {}  # Key - value pairs

    def is_full(self):
        return len(self.items) >= self.size

    def insert(self, key, value):
        self.items[key] = value

    def delete(self, key):
        if key in self.items:
            del self.items[key]

    def search(self, key):
        return self.items.get(key, None)

class ExtendibleHashTable:
    def __init__(self, bucket_size=2):
        self.global_depth = 1
        self.bucket_size = bucket_size
        self.directory = [Bucket(self.global_depth, self.bucket_size) for _ in range(2)]

    # Hash function using lower 'global_depth' bits
    def _hash(self, key):
        # We use Python's built-in hash(key) for the initial hash value,
        # then mask it with the global depth to get the directory index.
        # This is correct for the logic of Extendible Hashing.
        return hash(key) & ((1 << self.global_depth) - 1)

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.directory[index]

        if key in bucket.items or not bucket.is_full():
            bucket.insert(key, value)
            print(f"Inserted ({key}, {value}) into bucket {index}")
            return
        
        # Bucket full → Split
        print(f"Bucket {index} is full. Splitting....")
        self._split_bucket(index)
        
        # Retry insertion
        self.insert(key, value)

    def _split_bucket(self, index):
        old_bucket = self.directory[index]
        local_depth = old_bucket.depth
        old_bucket.depth += 1  # Increment local depth of old bucket

        # If local depth exceeds global depth, double directory
        if old_bucket.depth > self.global_depth:
            self._double_directory()

        new_bucket = Bucket(old_bucket.depth, self.bucket_size)

        # Update directory entries to point to new bucket
        # (i >> local_depth) & 1 checks if the bit at position 'local_depth' is 1
        # This is the new index bit for the new bucket
        for i in range(len(self.directory)):
            # Check if this directory entry currently points to the old_bucket AND
            # if the new bit that determines the split (at local_depth position) is 1.
            # Only entries whose index now includes the new bit (1) should point to new_bucket.
            if self.directory[i] is old_bucket and ((i >> local_depth) & 1):
                self.directory[i] = new_bucket

        # Rehash items
        old_items = list(old_bucket.items.items())
        old_bucket.items.clear()
        
        for k, v in old_items:
            # Re-inserting will send to either old_bucket or new_bucket
            self.insert(k, v)
    
    def _double_directory(self):
        print("Doubling directory size.")
        self.directory += self.directory
        self.global_depth += 1

    def search(self, key):
        index = self._hash(key)
        value = self.directory[index].search(key)
        if value is not None:
            print(f"Found key {key} with value {value} in bucket {index}")
        else:
            print(f"Key {key} not found.")
        return value

    def delete(self, key):
        index = self._hash(key)
        bucket = self.directory[index]
        
        if key in bucket.items:
            bucket.delete(key)
            print(f"Key {key} deleted from bucket {index}")
        else:
            print(f"Key {key} not found for deletion.")

    def display(self):
        seen = set()
        print("\nDirectory:")
        for i, bucket in enumerate(self.directory):
            # Only display each unique bucket once
            if id(bucket) not in seen:
                seen.add(id(bucket))
                # Using bucket.depth for the local depth display
                print(f"Bucket {i} (depth={bucket.depth}): {bucket.items}")

# --- Example Usage (UNCOMMENTED) ---
ht = ExtendibleHashTable(bucket_size=2)
ht.insert(1, "One")
ht.insert(2, "Two")
ht.insert(3, "Three")
ht.insert(4, "Four")
ht.insert(5, "Five")
ht.display()
ht.search(3)
ht.delete(3)
ht.search(3)
ht.display()