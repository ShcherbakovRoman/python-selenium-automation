def hydrate(drink_string):
    counter = 0
    for char in drink_string:
        if char.isnumeric():
            counter += int(char)
    if counter > 1:
        return f'{counter} glasses of water'
    else:
        return f'{counter} glass of water'