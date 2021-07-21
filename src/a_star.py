# Bintang Fajarianto
# 13519138

class AStar:
    def __init__(self, puzzle):
        self.n_nodes_expanded = 0
        self.start = puzzle
        self.solution = None

    def get_solution(self):
        return [s.position for s in self.solution]

    def is_puzzle_solvable(self):
        return self.start.is_solvable()

    def _calculate_new_heuristic(self, move, end_node):
        return move.manhattan_dist() - end_node.manhattan_dist()

    def do_algorithm(self):
        queue = [[self.start.manhattan_dist(), self.start]]
        expanded = []
        n_nodes_expanded = 0
        path = None

        while queue:
            i = 0
            for j in range(1, len(queue)):
                if queue[i][0] > queue[j][0]:
                    i = j

            path = queue[i]
            queue = queue[:i] + queue[i + 1:]
            end_node = path[-1]

            if end_node.position == end_node.end_position:
                break
            if end_node.position in expanded:
                continue

            for move in end_node.possible_moves():
                if move.position in expanded:
                    continue
                new_path = [path[0] + self._calculate_new_heuristic(move, end_node)] + path[1:] + [move]
                queue.append(new_path)
                expanded.append(end_node.position)

            n_nodes_expanded += 1

        self.n_nodes_expanded = n_nodes_expanded
        self.solution = path[1:]