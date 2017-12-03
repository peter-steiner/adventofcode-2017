#!/usr/bin/python3

# Set a limit on size of numbers inside the spiral
_spiral_max_size_ = 4294967295 # 2**32-1

class UlamSpiral(object):

    def __init__(self, end, start=1):

        # Verify that the spiral end number is valid
        if not isinstance(end,(int)):
            raise TypeError('Spiral size must be a positive integer; %s entered' % end)
        elif end < 0:
            raise ValueError('Spiral size must be a positive integer; %s entered' % end)
        elif end < start:
            raise ValueError('Spiral end (%s) smaller than start (%s)' % (end, start))
        elif end > _spiral_max_size_:
            raise ValueError('Spiral end (%s) exceeds cap (%s)' % (end, _spiral_max_size_))

        self.min_int = start
        self.max_int = end
        self.rows = [[start]]

        self.size = [1,1]

        while self.rows[self.size[0]-1][0] < self.max_int:
            # Add a new row if the spiral hasn't included its maximum natural number yet
            self._add_row_()

        # Orient the spiral (0 and 1 in same row with 0 on the left side of 1)
        if max(self.size) != 1: # Don't try to orient the base case spiral ([[0]])
            self._orient_()

    def __str__(self):
        char_width = len(str(max([max(i) for i in self.rows]))) + 1
        # Form a string to return
        return_str = ''
        for row in self.rows:
            row_str = ''
            for i in row:
                if i <= self.max_int:
                    row_str += str(i).rjust(char_width)
                else:
                    row_str += ''.rjust(char_width)
            return_str += row_str + '\n'

        return return_str


    def __repr__(self):
        return "UlamSpiral of size %s" % self.max_int


    def _rotate_(self):
        rn = self.size[0] # row size
        cn = self.size[1] # column size
        # rotate counter clockwise
        self.rows = [[self.rows[i][j] for i in range(rn)] for j in range(cn-1,-1,-1)]
        # save the row size and column size after rotation
        self.size = [self.size[1], self.size[0]]


    def _add_row_(self):
        start_int = self.rows[self.size[0]-1][0]
        end_int = start_int + self.size[0]
        # Rotate the spiral before appending the new row
        self._rotate_()
        # Append the new row
        self.rows.append(range(end_int, start_int, -1))
        # Add a row to the spiral size
        self.size[0] += 1


    def _orient_(self):
        r = self.min_int
        s = self.min_int + 1
        while not any([r in i and s in i and i.index(r) < i.index(s) for i in self.rows]):
            self._rotate_()

    def getRows(self):
        return self.rows
