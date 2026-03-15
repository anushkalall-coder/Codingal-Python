test_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 10
}

# value to check
value = 10

# count frequency
frequency = list(test_dict.values()).count(value)

print("Frequency of", value, "is:", frequency)