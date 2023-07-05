
def screen_dim(pref_height: int, pref_width: int, screen_height: int, screen_width: int):
    # calculate center of screen based on the given numbers
    x_coordinate = int((screen_width / 2) - (pref_width / 2))
    y_coordinate = int((screen_height / 2) - (pref_height / 2))
    return x_coordinate, y_coordinate


def validate(value: str, break_at: int) -> str:
    """Validate or clean the given goal text. 
    To prevent goals from being too long horizontally, this function will break apart 
    the goal's value into new lines based on the given character count. 
    Arguments:
        break_at is how many characters can be in a single line at once before broken.
    """
    chunks = []
    # traverse till the end of the value and step through by the given interval
    for i in range(0, len(value), break_at):
        # take the chunk from the value and add it to the list
        chunk = value[i:i+break_at]
        chunks.append(chunk)
    # join the chunks together with a newline in between
    return '\n'.join(chunks)