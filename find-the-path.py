
class Traverse:
    def __init__(self, grid):

        self.mastermoves = []

        self.pivot_points = {}
        self.visited = []
        self.moves = []

        self.grid = grid
        self.symbols = {"blocker": "x", "go": "o", "start": ">", "end": "<"}
        self.blockers = []
        self.dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # north east south west

        self.current = (0, 0)

    def fill_traveled(self, lst):
        lst.clear()

        return list(range(4))

    def check_if_in_bounds(self, move):

        if move[0] < 0 or move[0] >= len(self.grid):
            return False

        if move[1] < 0 or move[1] >= len(self.grid[0]):
            return False

        return True

    def check_if_not_obstacle(self, move):
        if move in self.blockers:
            return False
        return True

    def reset_moves_path(self):
        try:
            self.moves = self.moves[:self.moves.index(self.current) + 1]
        except ValueError as err:
            print(err)
        return


    def check_around(self, lst):
        temp = []

        for each in lst:
            movement = (self.current[0] + self.dir[each][0], \
            self.current[1] + self.dir[each][1])

            if self.check_if_in_bounds(movement) \
            and self.check_if_not_obstacle(movement):
                temp.append(each)

        return temp

    def check_if_visited(self, lst):
        temp = []

        for each in lst:
            movement = (self.current[0] + self.dir[each][0],\
            self.current[1] + self.dir[each][1])
            if movement not in self.visited:
                temp.append(each)

        return temp

    def change_current_point(self, direction):
        """
        Changes self.current point based off direction of travel

        Args:
            direction (int): direction of travel
        Return:
            None
        """
        self.current = (self.current[0] + self.dir[direction][0], \
        self.current[1] + self.dir[direction][1])

        return

    def find_start(self):
        """
        Finds the start location

        Args:
            None
        Return:
            None
        """

        for index, row in enumerate(self.grid):
            for each, x in enumerate(row):
                if x == self.symbols["start"]:
                    self.current = (index, each)

        return

    def add_to_visited(self):
        """
        Adds the current location to the self.visited list

        Args:
            None
        Return:
            None
        """
        self.visited.append(self.current)

        return

    def get_all_blockers(self):
        """
        Finds every 'x' in the grid and adds to a list

        Args:
            None
        Return:
            None
        """

        for index, row in enumerate(self.grid):
            for each, x in enumerate(row):
                if x == self.symbols["blocker"]:
                    tup = (index, each)
                    self.blockers.append(tup)

        return

    def check_if_at_end(self):
        if (item := self.grid[self.current[0]][self.current[1]]) == self.symbols["end"]:
            return True
        return False

    def start(self):
        end = False
        pivots_left = True
        pivot_direction = []
        lst = []
        self.get_all_blockers()
        self.find_start()

        while pivots_left:
            while not end: # while I have directions
                self.moves.append(self.current)
                print(f"moves {self.moves}")
                if self.check_if_at_end():
                    end = True
                    break

                self.add_to_visited() # add current loc to visited

                lst = self.fill_traveled(lst) # filling up location list

                lst = self.check_around(lst) # looking in all direction
                lst = self.check_if_visited(lst) # check is visited is on of those directions

                if lst:
                    if len(lst) > 1: # if more than one direction to go

                        next_move = lst.pop(0)
                        self.pivot_points[self.current] = lst[:]
                        self.change_current_point(next_move)

                    else: # if one direction to go

                        next_move = lst.pop(0)
                        self.change_current_point(next_move)

                else:
                    # check pivot points
                    if not self.pivot_points:
                        print("Locked in")
                        end = True

                    else:
                        key, val = self.pivot_points.popitem()

                        self.current = key
                        self.reset_moves_path()

                        self.change_current_point(val[0])




                lst = self.fill_traveled(lst)

            self.mastermoves.append(self.moves.copy())

            if self.pivot_points:

                key = next(iter(self.pivot_points))
                val = self.pivot_points.pop(key)
                self.current  = key
                self.reset_moves_path()

                end = False


                self.add_to_visited()
                self.change_current_point(val[0])
                print(f"---- {self.current} {key} {val}")

            else:
                pivots_left = False
        print()
        for each in self.mastermoves:
            print(each)
        # print(self.pivot_points)
        # print(self.moves)
        # for row in self.grid:
        #     print(' '.join(row))
        # print()

        # for idx in self.moves:
        #     self.grid[idx[0]][idx[1]] = "-"

        # for row in self.grid:
        #     print(' '.join(row))

def main():

    grid = [
    ['>', 'o', 'o', 'o', 'o', 'o', 'x', 'o'],
    ['x', 'o', 'o', '<', 'x', 'o', 'x', 'o'],
    ['x', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'x', 'o', 'x', 'o'],
    ['x', 'o', 'x', 'x', 'x', 'x', 'x', 'o'],
    ['x', 'o', 'o', 'o', 'o', 'x', 'x', 'o'],
    ['x', 'o', 'x', 'x', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'x', 'o', 'x', 'x', 'x']
    ]

    return grid


if __name__ == "__main__":
  grid = main()

  start = Traverse(grid)
  start.start()
