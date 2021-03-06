#!/usr/bin/python3

_spiral_max_size_ = 4294967295 # 2**32-1
deltas = {'U': (-1, 0), 'UR': (-1, 1), 'UL': (-1, -1), 'R':(0, 1)}

class UlamSpiralModded(object):

    def __init__(self, end, start=1):

        self.min_int = start
        self.max_int = end
        self.rows = [[start]]
        self.size = [1,1]
        self.x = 0
        self.y = 0

        while self.rows[self.size[0]-1][0] < self.max_int:
            self._add_row_()

        if max(self.size) != 1: # Don't try to orient the base case spiral ([[0]])
            self._orient_()


    def __str__(self):
        char_width = len(str(max([max(i) for i in self.rows]))) + 1
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

    def _rotate_(self):
        rn = self.size[0] # row size
        cn = self.size[1] # column size
        self.rows = [[self.rows[i][j] for i in list(range(rn))] for j in list(range(cn-1,-1,-1))]
        self.size = [self.size[1], self.size[0]]

    def _build_range_(self):
        x = self.x
        y = self.y 
        # print("set: ", y, x)
        rows = self.rows
        result = 0
        for delta in deltas:
            dy, dx = deltas[delta]
            nextPos = y+dy, x+dx
            try:
                if y+dy == -1 or x+dx == -1:
                    continue
                nextNum = rows[y+dy][x+dx]
                result = result + nextNum
            except IndexError:
                continue
        return result

    def _add_row_(self):
        start_int = self.rows[self.size[0]-1][0]
        end_int = start_int + self.size[0]
        self._rotate_()
        
        newRow = list(range(end_int, start_int, -1))
        self.y = len(self.rows)
        self.x = len(newRow) - 1
        self.rows.append(newRow)

        for i in newRow:
            n = self._build_range_()
            self.rows[self.y][self.x] = n
            self.x = self.x - 1

        self.size[0] += 1

    def _orient_(self):
        r = self.min_int
        s = self.min_int + 1
        while not any([r in i and s in i and i.index(r) < i.index(s) for i in self.rows]):
            self._rotate_()

    def show(self):
        print(str(self))

    def getRows(self):
        return self.rows
