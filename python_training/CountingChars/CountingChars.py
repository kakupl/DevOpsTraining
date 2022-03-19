import collections

print("Please wire a string")
value = input("Write something")
cahrs_of_value = collections.Counter(value)


def countetrs_string(value_of_string):
    value_of_string = {}
    for key, value in cahrs_of_value.items():
        if value > 1:
            value_of_string[key] = value
    print(value_of_string)


countetrs_string(cahrs_of_value)
