#!/usr/bin/python


import argparse

# args
parser = argparse.ArgumentParser()

parser.add_argument('--f', action='store', dest='input_file',
                    help='Store a simple value')

results = parser.parse_args()


# constants
blank = "."
filled = "#"

class Cell:
    def __init__(self, value, rd, dd):

        self.value = value
        # right distance
        self.rd = rd
        # down distance
        self.dd = dd

class Picture:

    def __init__(self, numrows, numcols):

        self.numrows = numrows
        self.numcols = numcols

        # the matrix
        self.picture = [ [ Cell(blank, 0, 0) for j in range(numcols)] for i in range(numrows)]


    # Calculate the distance to the next blanck in the directorion pointed by the vector
    def calculateDistance(self, row, col, vector):

        # for i in range(row, self.numrows):
        #     for j in range(cols, self.numcols):

        newrow = row
        newcol = col

        distance = 0
        
        newrow, newcol = row + vector[0], col + vector[1]
            
        while (newrow < self.numrows and newcol < self.numcols and self.picture[newrow][newcol].value == filled):
            
            distance += 1

            newrow, newcol = newrow + vector[0], newcol + vector[1]

        return distance
        
    def getlines(self, data):

        # put the data into the matrix
        for i, line in enumerate(data):
            for j, char in enumerate(line):

                self.picture[i][j].value = char



        # calculate the distances
        for i, line in enumerate(data):
            for j, char in enumerate(line):

                c = self.picture[i][j]

                # calculate the right distance
                c.rd = self.calculateDistance(i, j, [1,0])
                # calculate the down distance
                c.dd = self.calculateDistance(i, j, [0,1])
                


        
    def biggest_area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale




with open(results.input_file) as f:


    line = f.readline()
    maxrows, maxcols = line.split(" ")
    maxrows, maxcols = int(maxrows), int(maxcols)


    p = Picture(maxrows, maxcols)

    lines = f.read().splitlines() 
    # init the picture
    p.getlines(lines)


    

    # import ipdb
    # ipdb.set_trace()
    

    
   
    # for row in range(p.numrows):
    #     print
    #     for col in range(p.numcols):

    #         print p.picture[row][col].value
    

                
                


exit(0)
