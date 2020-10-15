from PIL import Image, ImageDraw
import pickle
from mazegen.cell import Cell

cellWidth = 90
lineWidth = 12

class Maze():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = self.form()

    def form(self):
        maze = []
        for j in range(self.height):
            row = []
            for i in range(self.width):
                row.append(Cell(i, j))
            maze.append(row)
        return maze

    def checkNeighbours(self, current):
        neighbours = []
        if (current.j > 0):
            if not (self.cells[current.j - 1][current.i].isVisited):
                neighbours.append(self.cells[current.j - 1][current.i])

        if (current.i > 0):
            if not (self.cells[current.j][current.i - 1].isVisited):
                neighbours.append(self.cells[current.j][current.i - 1])
        
        if (self.height - current.j > 1):
            if not (self.cells[current.j + 1][current.i].isVisited):
                neighbours.append(self.cells[current.j + 1][current.i])
        
        if (self.width - current.i > 1):
            if not (self.cells[current.j][current.i + 1].isVisited):
                neighbours.append(self.cells[current.j][current.i + 1])
        return neighbours

    def joinCells(self,cell1, cell2):
        if cell1.i > cell2.i:
            cell1.left = False
            cell2.right = False
        elif cell1.i < cell2.i:
            cell1.right = False
            cell2.left = False
        elif cell1.j > cell2.j:
            cell1.top = False
            cell2.bottom = False
        elif cell1.j < cell2.j:
            cell1.bottom = False
            cell2.top = False
        else:
            print('how')

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)
        print()
        print(filename,'has been saved')

    def resetVisits(self):
        for row in self.cells:
            for cell in row:
                cell.isVisited = False

    def checkSolutionNeighbours(self, current):
        neighbours = []
        
        if (current.j > 0):
            if not (self.cells[current.j - 1][current.i].bottom or self.cells[current.j - 1][current.i].isVisited):
                neighbours.append(self.cells[current.j - 1][current.i])

        if (current.i > 0):
            if not (self.cells[current.j][current.i - 1].right or self.cells[current.j][current.i - 1].isVisited):
                neighbours.append(self.cells[current.j][current.i - 1])
        
        if (self.height - current.j > 1):
            if not (self.cells[current.j + 1][current.i].top or self.cells[current.j + 1][current.i].isVisited):
                neighbours.append(self.cells[current.j + 1][current.i])
        
        if (self.width - current.i > 1):
            if not (self.cells[current.j][current.i + 1].left or self.cells[current.j][current.i + 1].isVisited):
                neighbours.append(self.cells[current.j][current.i + 1])

        return neighbours
 
    def drawBorders(self, image):
        def drawCellBorder(cell, image):
            x = cell.i * (cellWidth + lineWidth)
            y = cell.j * (cellWidth + lineWidth)
            color = (122,204,196)

            if cell.top:
                image.rectangle(((x,y),(x+cellWidth+lineWidth*2, y+lineWidth)),color)
            if cell.left:
                image.rectangle(((x,y),(x+lineWidth, y+cellWidth+lineWidth*2)),color)
            if cell.bottom:
                image.rectangle(((x,y+cellWidth+lineWidth),(x+cellWidth+lineWidth*2,y+cellWidth+lineWidth*2)),color)
            if cell.right:
                image.rectangle(((x+cellWidth+lineWidth,y),(x+cellWidth+lineWidth*2,y+cellWidth+lineWidth*2)),color)

        for row in self.cells:
            for cell in row:
                drawCellBorder(cell, image)

        return image
        
    def drawMaze(self):
        im = Image.new('RGB',(self.width * cellWidth + (self.width+1)*lineWidth, self.height * cellWidth + (self.height+1)*lineWidth),(25, 25, 25))
        image = ImageDraw.Draw(im)
        self.drawBorders(image)

        return im

    def drawSolution(self, solution):
        def drawSquare(cell, image):
            x = cell.i * (cellWidth + lineWidth)
            y = cell.j * (cellWidth + lineWidth)
            color = (74,115,111)
            image.rectangle(((x,y),(x+cellWidth+lineWidth*2,y+cellWidth+lineWidth*2)),color)

        soln = Image.new('RGB',(self.width * cellWidth + (self.width+1)*lineWidth, self.height * cellWidth + (self.height+1)*lineWidth),(25, 25, 25))
        image = ImageDraw.Draw(soln)

        for cell in solution:
            drawSquare(cell,image)
        self.drawBorders(image)

        return soln
