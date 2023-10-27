class SnakeController:
    """
    Abstract class for controlling snake
    """

    # This class is not instantiated,
    # but is extended by fully implemented
    # snake controllers for AI and humman control,
    # which inherits this class's methods.

    # Public methods
    def set_snake(self, snake):
        """
        Set the snake that will be controlled
        by this controller
        Snake --> None
        """
        self._snake = snake

    def control_snake(self, direction):
        """
        Give the snake a direction to go
        Direction --> None
        """
        self._snake.control(direction)
