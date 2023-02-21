# Settings

The seetings are defined in a YAML file at 'resources/config.yaml' with the parameters

- background_color
- border_color
- live_color
- fps
- resolution [width, height]
- scale
- timestep (in miliseconds used to update the screen view with the next iteration)

# Controls

- ENTER: Start Conway's Game of Life algorithm (you will see a green circle at the upper-right corner)
- next ENTER: Pause Conway's Game of Life algorithm (you will see a red square at the upper-right corner)
- SPACE: Stop the game
- MOUSE LEFT CLICK BUTTON: select a cell to be alive
- MOUSE RIGHT CLICK BUTTON: select a cell to be dead (all cells start as dead)

# Next Steps

- Add a user interface to repalce the keyboard controls
- Improve code with some useful Design Patterns (e.g.: State Pattern)
- Implement a GPU version of Conway's Game of Live based on Numba package
