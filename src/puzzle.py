# Bintang Fajarianto
# 13519138

class Puzzle:
    def __init__(self, position):
        self.size = 4
        self.position = position
        self.end_position = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

    def _swap_value(self, x1, y1, x2, y2):
        new_position = [list(row) for row in self.position]  # copy the puzzle
        new_position[x1][y1], new_position[x2][y2] = new_position[x2][y2], new_position[x1][y1]
        return new_position

    def _get_coordinate(self, value, position=None):
        if not position:
            position = self.position

        for i in range(self.size):
            for j in range(self.size):
                if position[i][j] == value:
                    return i, j

    def possible_moves(self):
        next_position = []

        # BLANK coordinate
        i, j = self._get_coordinate(0)

        # Vertical move
        if i > 0:
            next_position.append(Puzzle(self._swap_value(i, j, i-1, j)))  # DOWN
        if i < self.size - 1:
            next_position.append(Puzzle(self._swap_value(i, j, i+1, j)))  # UP

        # Horizontal move
        if j > 0:
            next_position.append(Puzzle(self._swap_value(i, j, i, j-1)))  # LEFT
        if j < self.size - 1:
            next_position.append(Puzzle(self._swap_value(i, j, i, j+1)))  # RIGHT

        return next_position

    def manhattan_dist(self):
        jarak = 0
        for i in range(self.size):
            for j in range(self.size):
                brs, kol = self._get_coordinate(self.position[i][j], self.end_position)
                jarak += abs(i - brs) + abs(j - kol)
        return jarak

    def _get_blank_row_from_bottom(self):
        # BLANK coordinate
        blank_row, _ = self._get_coordinate(0)
        return self.size - blank_row

    def _count_inversions(self):
        # Convert 2D to 1D
        puzzle = [number for row in self.position for number in row if number != 0]

        count = 0
        for i in range(self.size*self.size-1):
            for j in range(i+1, self.size*self.size-1):
                if puzzle[i] > puzzle[j]:
                    count += 1
        return count

    def _is_odd(self, num):
        return num % 2 != 0

    def _is_even(self, num):
        return num % 2 == 0

    def is_solvable(self):
        inversions_count = self._count_inversions()
        blank_position = self._get_blank_row_from_bottom()

        solvable = True if \
            (self._is_even(blank_position) and self._is_odd(inversions_count)) or \
            (self._is_odd(blank_position) and self._is_even(inversions_count)) \
                else False
                
        return solvable