import pickle

def main(directory, filename, save):

    path = directory + '\\' + filename
    if path[-5:] != '.maze':
        path += '.maze'

    with open(path,'rb') as f:
        maze = pickle.load(f)

    im = maze.drawMaze()
    if save:
        im.save(filename+'.png')
    im.show()
