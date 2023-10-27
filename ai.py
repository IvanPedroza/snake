from snake_controller import SnakeController

# These constant assignments are redundant and
# already provide by Processing, however
# providing them here makes it possible to run
# tests in Pytest on functions using them.
UP, DOWN, LEFT, RIGHT = 38, 40, 37, 39


class AI(SnakeController):
    """
    AI Snake controller class
    """

    def __init__(self, gc):
        """
        Initialize AI
        GameController --> AI
        """
        self._gc = gc

    # Public methods
    def update(self):
        """
        Calculate next move and control the snake
        None --> None
        """
        dir = self._choose_dir()
        self.control_snake(dir)

    # Private methods
    def _choose_dir(self):
        """
        Score directions and return top scored
        direction
        None --> Direction
        """
        scores = {UP: 0, DOWN: 0, LEFT: 0, RIGHT: 0}

        for direction in scores.keys():
            coordinates = self._get_neighbor_coord(direction)
            neighb_score = self._clear_score(coordinates)
            appl_dist_score = self._apple_distance(coordinates)
            scores[direction] = neighb_score + appl_dist_score

        return max(scores, key=scores.get)

    def _get_neighbor_coord(self, neighbor_dir):
        """
        Get neighbor coordinate for direction
        Direction --> (Number, Number)
        """
        x = self._snake.body[0].x
        y = self._snake.body[0].y
        if neighbor_dir == UP:
            return (x, y-1)
        elif neighbor_dir == DOWN:
            return (x, y+1)
        elif neighbor_dir == LEFT:
            return (x-1, y)
        elif neighbor_dir == RIGHT:
            return (x+1, y)

    def _min_dist(self, p1, p2):
        """
        Find the minimum distance between two points
        (Number, Number) (Number, Number) --> Number
        """
        # To find the shortest path between two points
        # We calculate the inner path (within the game frame)
        # and the outer path (going out of the bounds of the
        # frame and wrapping in the other side) and take the
        # minimum of the two.
        p1_x, p1_y = p1
        p2_x, p2_y = p2

        inner_x = p1_x - p2_x
        inner_y = p1_y - p2_y

        outer_x = self._gc.w-(max(p1_x, p2_x)) + min(p1_x, p2_x)
        outer_y = self._gc.h-(max(p1_y, p2_y)) + min(p1_y, p2_y)

        print("Outer x", outer_x)
        print("Outer y", outer_y)

        # Pythagorean theorem
        shortest = (min(inner_x, outer_x)**2+min(inner_y, outer_y)**2)**0.5
        return shortest

    def _clear_score(self, coord):
        """
        Generate a weighting score (normalized)
        from the number of unoccupied neighbor squares
        for a coordinate
        (Number, Number) --> Number
        """
        # normalized number of clear neighbor squares
        if coord in self._gc.deadly_points:
            return -1
        else:
            score = 0
            if (coord[0]-1, coord[1]) not in self._gc.deadly_points:
                score += 1
            if (coord[0], coord[1]-1) not in self._gc.deadly_points:
                score += 1
            if (coord[0], coord[1]+1) not in self._gc.deadly_points:
                score += 1
            if (coord[0]+1, coord[1]) not in self._gc.deadly_points:
                score += 1
        NEIGHBOR_COUNT = 4.0
        score = score/NEIGHBOR_COUNT
        return score

    def _apple_distance(self, coords):
        """
        Get the distance score to the apple
        (Number, Number) --> Number
        """
        # Get the distance
        apple_min_dist = self._min_dist(self._gc.apple_location, coords)
        # Return the distance score
        return self._convert_min_to_score(apple_min_dist)

    def _convert_min_to_score(self, min_dist):
        """
        Convert a distance to a score
        Number --> Number
        """
        return ((self._gc.h * self._gc.w) - min_dist)
