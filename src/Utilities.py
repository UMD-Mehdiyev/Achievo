
def screen_dim(pref_height: int, pref_width: int, screen_height: int, screen_width: int):
    # calculate center of screen based on the given numbers
    x_coordinate = int((screen_width / 2) - (pref_width / 2))
    y_coordinate = int((screen_height / 2) - (pref_height / 2))
    return x_coordinate, y_coordinate
