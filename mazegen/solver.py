import random
import pickle

maze = None
solution = []

def load(path):
    global maze
    with open(path, "rb") as f:
        maze = pickle.load(f)

def solve():
    global maze
    global solution
    while len(solution) > 0:
        if solution[-1] == maze.cells[-1][-1]:
            break
        neighbours = maze.checkSolutionNeighbours(solution[-1])
        if len(neighbours) > 0:
            neighbour = random.choice(neighbours)
            neighbour.isVisited = True
            solution.append(neighbour)
        else:
            solution.pop()
    else:
        print("No solution found!")
        exit()

def main(directory, filename, save):

    path = directory + '\\' + filename
    if path[-5:] != '.maze':
        path += '.maze'

    load(path)
    maze.resetVisits()
    solution.append(maze.cells[0][0])
    maze.cells[0][0].isVisited = True
    solve()
    soln = maze.drawSolution(solution)
    if save:
        soln.save(filename +"_sol"+ '.png')
    soln.show()
