# Snake Game in Processing

This is a classic Snake game implemented in the `Processing` programming environment. The game provides a fun and challenging experience, where you control a snake and aim to collect food to grow longer while avoiding collisions with an AI adversary and yourself.

### Gameplay Mechanics

In this Snake Game, there's a unique gameplay mechanic where the snake interacts with an opponent snake. When your snake eats an apple, the following events occur:

- **Your Snake**: When your snake successfully consumes an apple, it increases in size, allowing you to grow longer and score more points.
- **Opponent Snake**: Simultaneously, the opponent snake experiences a decrease in size. This mechanic adds a competitive element to the game, as you can strategically consume apples to outgrow your opponent.

This unique gameplay feature adds an extra layer of challenge and strategy to the traditional Snake Game. You can use this mechanic to your advantage to gain an edge over your opponent.

Feel free to customize the game code in the `snake.py` file to adjust the rate at which your snake grows and your opponent's snake shrinks when an apple is consumed.

## Getting Started

Follow these steps to install and play the game on your machine:

### Prerequisites

1. **Processing**: Ensure that you have Processing installed on your machine. If not, you can download it from [https://processing.org/download/](https://processing.org/download/).

### Installation

1. Clone or download this repository to your local machine using the following command:

    `git clone https://github.com/yourusername/snake-game-processing.git`

3. Open Processing.

4. Open the `snake_game.pyde` file in Processing.

5. Click the "Run" button (a triangular play button) to start the game.

### How to Play

- Use the arrow keys (Up, Down, Left, Right) to control the direction of the snake.
- The snake will automatically move in the last direction until you change it.
- Collect the food (represented as apples) to increase the length of the snake.
- Avoid running into walls or colliding with either snake's body.

### How to Win

To emerge victorious in this Snake Game, you should aim to achieve the following objectives:

- **Outlast Your Opponent**: The game features a competitive element where your opponent snake decreases in size when you eat apples. Strive to outlast and eventually eliminate your opponent by causing their snake to become too small to continue.

- **Survive as Long as Possible**: While increasing your score is crucial, your ultimate goal is to survive as long as you can. Avoid collisions with walls and the opponent snake while navigating the game board.

- **Master Strategy**: Develop and employ strategies to maximize your chances of success. Pay attention to the movement patterns of the opponent snake and plan your moves accordingly.


Remember, the game doesn't have a predefined endpoint, so your success is measured by the length of time you survive and the score you achieve. Feel free to add a score tally and end goal.


### Game Features

- Score Display: The game displays your current score on the screen.
- Game Over: When you collide with a wall or yourself, the game will end, and your final score will be displayed.
- Replay: You can restart the game by clicking the "Run" button in Processing.

### Customize the Game

You can modify the game by editing the `snake_game.pyde` file. The code is well-documented and organized, making it easy to understand and make changes.

### Dependencies

This game relies on the Processing library and PyTest for the test suite. No additional libraries are required.

### Test Suite with PyTest

The test suite uses PyTest to ensure the reliability and correctness of the Snake Game's functionality. This suite covers various aspects of the game code, including critical game mechanics, logic, and interactions.

#### Running Tests

To run the test suite, follow these steps:

1. **Prerequisites**: Ensure you have PyTest installed. If not, you can install it using `pip` using the following command:
   
    `pip install pytest`

2. **Navigate to the Tests Folder**: Open a terminal and navigate to the `tests` directory in your game repository.

3. **Execute Tests**: Run the tests using the following command:

    `pytest`

#### Test Coverage

The test suite is designed to cover the following aspects:

- **Game Mechanics**: Ensures that game mechanics, such as snake movement, collision detection, and apple spawning, work as expected.

- **Scoring and Rules**: Validates the game's scoring system and adherence to the rules, including when the game should end or continue.

- **Opponent Snake Interaction**: Tests the interaction between your snake and the opponent snake when consuming apples and colliding.

- **Edge Cases**: Includes tests for edge cases and boundary conditions to maintain the game's robustness.

#### Adding New Tests

If you make modifications to the game code or introduce new features, it's advisable to add corresponding tests. To create new tests, follow these steps:

1. **Create a Test File**: In the `tests` directory, create a new Python file that begins with `test_`, such as `test_my_feature.py`.

2. **Write Test Functions**: Write test functions within the test file using PyTest's syntax. You can refer to existing tests as examples.

3. **Run Tests**: Execute the entire test suite using `pytest` to ensure your new tests pass and do not break existing functionality.

By maintaining a comprehensive test suite, you can ensure that your Snake Game remains stable and that new features or modifications do not introduce unexpected issues.



## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. All improvements are welcome as are new features!

## License

This Snake Game in Processing is open-source and available under the [MIT License](LICENSE). You can use, modify, and distribute it freely.

## Acknowledgments

This game was developed with the help of Processing (https://processing.org/), which makes it easy to create interactive and visual applications and inspired by Nokia's game suite.

Have fun playing the Snake Game!
