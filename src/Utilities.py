from typing import Tuple


def center_screen(pref_height: int, pref_width: int, screen_height: int, screen_width: int) -> Tuple[int, int]:
    """Retrieve the (x, y) coordinate that would center the screen.
    
    Given the preferred dimensions of the app screen and the actual dimensions of the screen, 
    this function will calculate the best x and y coordinates for where the screen should be 
    placed in order to be in the center of the user's viewable screen.  

    Arguments:
        pref_height is the preferred height of the application screen
        pref_width is the preferred width of the application screen
        screen_height is the height of the user's viewable screen
        screen_width is the width of the user's viewable screen

    Returns:
        two integers, the first being the x coordinate and the second being the y coordinate
    """
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