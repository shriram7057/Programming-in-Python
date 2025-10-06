# Numeric Types
integer_value = 10  # Integer (int)
float_value = 10.5  # Floating point (float)
complex_value = 3 + 4j  # Complex number

# Sequence Types
string_value = "Hello, Python!"  # String (str)
list_value = [1, 2, 3, 4, 5]     # List (mutable sequence)
tuple_value = (10, 20, 30)       # Tuple (immutable sequence)

# Set Types
set_value = {1, 2, 3, 4}        # Set (unordered, unique elements)
frozen_set_value = frozenset({5, 6, 7})  # Frozenset (immutable set)

# Mapping Type
dictionary_value = {"name": "Alice", "age": 25}  # Dictionary (key-value pairs)

# Boolean Type
bool_value = True  # Boolean (True or False)

# Binary Types
byte_value = b"Hello"  # Bytes (immutable)
byte_array_value = bytearray([65, 66, 67])  # Bytearray (mutable)
memory_view_value = memoryview(byte_value)  # Memoryview (view of bytes)

# None Type
none_value = None  # NoneType (represents "nothing")

# Printing all values
output = {
    "Integer": integer_value,
    "Float": float_value,
    "Complex": complex_value,
    "String": string_value,
    "List": list_value,
    "Tuple": tuple_value,
    "Set": set_value,
    "Frozen Set": frozen_set_value,
    "Dictionary": dictionary_value,
    "Boolean": bool_value,
    "Bytes": byte_value,
    "Byte Array": list(byte_array_value),  # Converting to list for better readability
    "Memory View": list(memory_view_value),  # Converting to list for better readability
    "None Type": none_value
}

'''Integer: 10
Float: 10.5
Complex: (3+4j)
String: Hello, Python!
List: [1, 2, 3, 4, 5]
Tuple: (10, 20, 30)
Set: {1, 2, 3, 4}
Frozen Set: frozenset({5, 6, 7})
Dictionary: {'name': 'Alice', 'age': 25}
Boolean: True
Bytes: b'Hello'
Byte Array: [65, 66, 67]
Memory View: [72, 101, 108, 108, 111]
None Type: None'''
