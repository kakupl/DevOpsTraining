import collections

print("Please wire a string")
value = input("Write something")
test = collections.Counter(value)


def countetrs_string(value_of_string):
    value_of_string = {}
    for key, value in test.items():
        if value > 1:
            value_of_string[key] = value
    print(value_of_string)


countetrs_string(test)
