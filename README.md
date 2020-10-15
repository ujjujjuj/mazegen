# Mazegen
Mazegen is a python command line tool to generate and solve mazes

## Installation
```
pip install mazegen
```
## Help
You can get help information by running `-h` or `--help`
```
mazegen --help
```
This will output the following documentation
```
Usage: mazegen [option] [filename] [optional]

OPTIONS:
generate        Generates .maze file
view            Views existing .maze file as an image
solve           Solves a .maze file

OPTIONAL ARGUMENTS:
-s, --save      Save generated .png file
```

## Usage
To generate a pxq maze named `first.maze`, run the following command
```
mazegen generate first.maze
```
To view the output from a .maze file
```
mazegen view first.maze
```
To solve a .maze file
```
mazegen solve first.maze
```

## Options
* `-s` or `--save` will save the generated image file

## Example
An unsolved 42x42 maze<br />
<img src="https://github.com/ujjujjuj/mazegen/raw/master/example/test.png?raw=true" alt="unsolved" width="270"/><br />
Solution<br />
<img src="https://github.com/ujjujjuj/mazegen/raw/master/example/test_sol.png?raw=true" alt="solved" width="270"/><br />

## Note
All mazes start from the top left and end at bottom right
