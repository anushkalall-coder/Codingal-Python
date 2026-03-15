main_counter = {101, 102, 103, 104, 105, 106}

online_counter = {104, 105, 106, 107, 108}

unique = main_counter.union(online_counter)
print("All unique ticket holders: ", unique) 

both_counters = main_counter.intersection(online_counter)
print("Students who bought from both counters: ", both_counters)

main = main_counter.difference(online_counter)
print("Print students who bought only from the main counter: ", main)

online = online_counter.difference(main_counter)
print("Print students who bought only from the online counter: ", online)

only_one = main_counter.symmetric_difference(online_counter)
print("Students who bought from one counter: ", only_one)