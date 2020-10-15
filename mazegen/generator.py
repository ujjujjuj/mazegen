import random
from mazegen.maze import Maze

maze = None
cellStack = []
width = 25
height = 25

def form():
    global maze

    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    maze = Maze(width, height)

def generate():
    global maze
    global cellStack

    while len(cellStack) > 0:
        neighbours = maze.checkNeighbours(cellStack[-1])
        if len(neighbours) > 0:
            neighbour = random.choice(neighbours)
            neighbour.isVisited = True
            maze.joinCells(cellStack[-1], neighbour)
            cellStack.append(neighbour)
        else:
            cellStack.pop()

def main(directory, filename, save):
    global cellStack

    form()
    maze.cells[0][0].top = False
    maze.cells[-1][-1].bottom = False
    cellStack.append(maze.cells[0][0])
    maze.cells[0][0].isVisited = True
    generate()

    im = maze.drawMaze()
    maze.save(filename + ".maze" if filename[-5:] != '.maze' else filename)
    
    if save:
        im.save(filename + '.png')
    im.show()
