# { "apple" : "red", "mango" : "yellow", "grapes" : "green", "cherry" : "red"}
# { "red" : "["apple", "cherry"]", "yellow" : "mango", "green" : "grapes"}
# asked in 3rd round in zupee

def convert_colour_fruit(input_dictionary):
    fruit_colour = {}
    for fruit, colour in input_dictionary.items():
        if colour not in fruit_colour:
            fruit_colour[colour] = []
        fruit_colour[colour].append(str(fruit))

    for colour in fruit_colour:
        if len(fruit_colour[colour]) == 1:
            fruit_colour[colour] = fruit_colour[colour][0]

    print(fruit_colour)


if __name__ == '__main__':
    input_dict = {"apple": "red", "mango": "yellow", "grapes": "green", "cherry": "red"}
    convert_colour_fruit(input_dict)
