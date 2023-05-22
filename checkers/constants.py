from checkers.point import Point
from checkers.enums import CheckerType, SideType

# Side for which the player is playing
PLAYER_SIDE = SideType.WHITE

# Board size
X_SIZE = Y_SIZE = 8
# Cell size (in pixels)
CELL_SIZE = 75

# Animation speed (higher = faster)
ANIMATION_SPEED = 4

# Number of moves to predict
MAX_PREDICTION_DEPTH = 3

# Border width (preferably even)
BORDER_WIDTH = 2 * 2

# Game board colors
FIELD_COLORS = ['#E7CFA9', '#927456']
# Border color when hovering over a cell with the mouse
HOVER_BORDER_COLOR = '#54b346'
# Border color when a cell is selected
SELECT_BORDER_COLOR = '#944444'
# Color of circles indicating possible moves
POSSIBLE_MOVE_CIRCLE_COLOR = '#944444'

# Possible move offsets for checkers
MOVE_OFFSETS = [
    Point(-1, -1),
    Point(1, -1),
    Point(-1, 1),
    Point(1, 1)
]

# Arrays of checker types for white and black checkers [Regular, Queen]
WHITE_CHECKERS = [CheckerType.WHITE_REGULAR, CheckerType.WHITE_QUEEN]
BLACK_CHECKERS = [CheckerType.BLACK_REGULAR, CheckerType.BLACK_QUEEN]
