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

class Cell(object):
    def __init__(self, value=blank, rd=-1, dd=-1):

        self.value = value
        # right distance
        self.rd = rd
        # down distance
        self.dd = dd

        
class Square(object):

    def __init__(self, cell1, x1, y1, cell2, x2, y2):

        self.c1 = cell1
        self.x1 = x1
        self.y1 = y1
        
        
        self.c2 = cell2
        self.x2 = x2
        self.y2 = y2
        

    def getarea(self):

        return (self.x2-self.x1) * (self.y2-self.y1)

        
class Picture(object):

    def __init__(self, numrows, numcols):

        self.numrows = numrows
        self.numcols = numcols

        # the matrix
        self.picture = [ [ Cell(blank, 0, 0) for j in range(numcols)] for i in range(numrows)]


    # Calculate the distance to the next blanck in the directorion pointed by the vector
    def calculateDistance(self, row, col, vector, kind_of_cell_which_makes_me_not_to_stop=filled):

        newrow = row
        newcol = col
        distance = 0
        newrow, newcol = row + vector[0], col + vector[1]
            
        while (newrow < self.numrows and newcol < self.numcols and self.picture[newrow][newcol].value == kind_of_cell_which_makes_me_not_to_stop):
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
                

    def get_biggest_square_from_coords_following_vector(self, row, col, vector):
        newrow, newcol = row + vector[0], col + vector[1]


        # accumulators
        biggest_square_found = Square(self.picture[row][col], row, col, self.picture[newrow][newcol], newrow, newcol)
        newsquare = biggest_square_found
#        newsquare = biggest_square_found.copy()
 #       newsquare = type('newsquare', biggest_square_found.__bases__, dict(biggest_square_found.__dict__))
        
        while (newrow < self.numrows and newcol < self.numcols and
               self.picture[newrow][newcol].value == filled and
               biggest_square_found.getarea() <= newsquare.getarea() 
              
        ):

            # the new square is bigger or have the same length than the old one
            biggest_square_found = newsquare

            newrow += vector[0]
            newcol += vector[1]

            if self.coords_between_picture(newrow, newcol):
                newsquare = Square(self.picture[row][col], row, col, self.picture[newrow][newcol], newrow, newcol)
                    

        return biggest_square_found

    # TO BE DONE
    # returns the position of the opposite corner of the square for the biggest filled square
    # from here starting[row, col] going to the down-right direction.
    def get_biggest_square(self, row, col):

        cell = self.picture[row][col]

        x_distance = -1
        y_distance = -1

        max_potential_area = cell.rd * cell.dd


        # calculate the biggest real area going to the right and down
        # calculate the biggest potential area going down and to the right
       
        newrow = row
        newcol = col
        distance = 0

        # import ipdb
        # ipdb.set_trace()
        
        # down direction
        vector_movement = [0,1]
        down_square = self.get_biggest_square_from_coords_following_vector(row, col, vector_movement)
        # right direction
        vector_movement = [1,0]
        right_square = self.get_biggest_square_from_coords_following_vector(row, col, vector_movement)

        # import ipdb
        # ipdb.set_trace()

        return (right_square if right_square.getarea() > down_square.getarea() else down_square)
        

    def coords_between_picture(self, x, y):
        return (x < self.numrows and 0 <= x and
                y < self.numcols and 0 <= y)

        
    def erase_cell(self, row, col):

        # import ipdb
        # ipdb.set_trace()

        self.picture[row][col] = Cell()

        # TESTING: find the nearest non blank cell up and left and update the distance

        # up process
        # I'll look for the cells which are already filled and substract 1 from the down distance.
        vector=[0,-1]
        up_distance_to_blank_cell = calculateDistance(row, col, vector)

        for i in range(row-up_distance_to_blank_cell, row):
            self.picture[i][col].dd -= 1
            

        # down process - almost copy-paste of the above code
        # I'll look for the cells which are already filled and substract 1 from the down distance.
        vector=[-1,0]
        left_distance_to_blank_cell = calculateDistance(row, col, vector)

        for i in range(col-left_distance_to_blank_cell, col):
            self.picture[row][col].rd -= 1

            
        
    # Erase the square sq, instance of Square
    def paintSquare(self, sq):

        # import ipdb
        # ipdb.set_trace()

        for i in range(sq.x1, sq.x2):
            for j in range(sq.y1, sq.y1):
                self.erase_cell(i,j)
    





with open(results.input_file) as f:


    line = f.readline()
    maxrows, maxcols = line.split(" ")
    maxrows, maxcols = int(maxrows), int(maxcols)


    p = Picture(maxrows, maxcols)

    lines = f.read().splitlines() 
    # init the picture
    p.getlines(lines)


    

    
   
    for row in range(p.numrows):
        for col in range(p.numcols):
            square = p.get_biggest_square(row, col)
            p.paintSquare(square)
            
            

                
                


exit(0)
