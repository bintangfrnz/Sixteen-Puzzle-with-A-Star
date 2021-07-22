# Bintang Fajarianto
# 13519138

class Puzzle:
    def __init__(self, initial_position):
        self.size = 4
        self.current_position = initial_position
        self.end_position = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

    def swap_value(self, x1, y1, x2, y2):
        new_position = [list(row) for row in self.current_position]
        new_position[x1][y1], new_position[x2][y2] = new_position[x2][y2], new_position[x1][y1]
        return new_position

    def get_coordinate(self, value, position=None):
        if not position:
            position = self.current_position

        for i in range(self.size):
            for j in range(self.size):
                if position[i][j] == value:
                    return i, j

    def possible_moves(self):
        next_position = []

        # BLANK coordinate
        i, j = self.get_coordinate(0)

        # Vertical move
        if i > 0:
            next_position.append(Puzzle(self.swap_value(i, j, i-1, j)))  # DOWN
        if i < self.size - 1:
            next_position.append(Puzzle(self.swap_value(i, j, i+1, j)))  # UP

        # Horizontal move
        if j > 0:
            next_position.append(Puzzle(self.swap_value(i, j, i, j-1)))  # LEFT
        if j < self.size - 1:
            next_position.append(Puzzle(self.swap_value(i, j, i, j+1)))  # RIGHT

        return next_position

    def manhattan_dist(self):
        jarak = 0
        for i in range(self.size):
            for j in range(self.size):
                brs, kol = self.get_coordinate(self.current_position[i][j], self.end_position)
                jarak += abs(i - brs) + abs(j - kol)
        return jarak

    def get_blank_row_from_bottom(self):
        # BLANK coordinate
        blank_row = self.get_coordinate(0)[0]
        return self.size - blank_row

    def count_inversions(self):
        # Convert 2D to 1D
        puzzle = [val for row in self.current_position for val in row if val != 0]

        count = 0
        for i in range((self.size**2)-1):
            for j in range(i+1, (self.size**2)-1):
                if puzzle[i] > puzzle[j]:
                    count += 1
        return count

    def is_odd(self, num):
        return num%2 != 0

    def is_even(self, num):
        return num%2 == 0

    def is_solvable(self):
        inversions_count = self.count_inversions()
        blank_position = self.get_blank_row_from_bottom()

        solvable = True if \
            (self.is_even(blank_position) and self.is_odd(inversions_count)) or \
            (self.is_odd(blank_position) and self.is_even(inversions_count)) \
                else False
                
        return solvable