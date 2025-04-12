
class Traverse:
    def __init__(self, grid):
        self.end = False

        self.pivot_points = {}
        self.visited = []
        self.traveled = []

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

    def check_around(self, lst):
        temp = []

        for each in lst:
            movement = (self.current[0] + self.dir[each][0], self.current[1] + self.dir[each][1])

            if self.check_if_in_bounds(movement) and self.check_if_not_obstacle(movement):
                temp.append(each)

        return temp

    def check_if_visited(self, lst):
        temp = []

        for each in lst:
            movement = (self.current[0] + self.dir[each][0], self.current[1] + self.dir[each][1])
            if movement not in self.visited:
                temp.append(each)

        return temp

    def change_current_point(self, direction):
        self.current = (self.current[0] + self.dir[direction][0], self.current[1] + self.dir[direction][1])

        return

    def find_start(self):

        for index, row in enumerate(self.grid):
            for each, x in enumerate(row):
                if x == self.symbols["start"]:
                    self.current = (index, each)

    def get_all_blockers(self):

        for index, row in enumerate(self.grid):
            for each, x in enumerate(row):
                if x == self.symbols["blocker"]:
                    tup = (index, each)
                    self.blockers.append(tup)

        return

    def start(self):
        pivot_direction = []
        lst = [0, 1, 2, 3]

        self.get_all_blockers()
        self.find_start()

        while not self.end:
            while lst:

                if not pivot_direction:
                    lst = self.check_around(lst) # checking in all 4 directions
                    lst = self.check_if_visited(lst)
                else:
                    lst = pivot_direction
                print(f" current is -> {self.current}")
                self.traveled.append(self.current)

                if not lst: # if no where to go
                    if not self.pivot_points:
                        print("Deadlocked")
                        return
                    else:
                        key, val = list(self.pivot_points.items())[-1]
                        self.current = key
                        pivot_direction = val
                        print(f" pivot direction {pivot_direction}")

                else:
                    if len(lst) == 1: # if only one direction to go

                        next_move = lst.pop(0) #getting the next move location
                        self.visited.append(self.current) #adding to visited

                        self.change_current_point(next_move) # changing current pos


                    else: # if more than one direction to go
                        print(f"\t\t\t\t {lst}")
                        print(f"visited list {self.visited}")
                        next_move = lst.pop(0) # getting the next move location
                        self.visited.append(self.current) #adding to visited
                        self.pivot_points[self.current] = lst[:]

                        self.change_current_point(next_move) # changing current pos

                lst = self.fill_traveled(lst)
                item = self.grid[self.current[0]][self.current[1]]
                if item == self.symbols["end"]:
                    self.end = True
                    print("ending")
                    break
        for row in self.grid:
            print(' '.join(row))


def main():

    grid = [
    ['>', 'o', 'o', 'o', 'o', 'x', 'x', 'o'],
    ['x', 'x', 'o', 'x', 'o', 'o', 'o', 'o'],
    ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'o'],
    ['o', 'o', 'x', 'o', 'o', 'o', 'x', 'o'],
    ['x', 'o', 'o', 'x', 'x', 'x', 'x', 'o'],
    ['x', 'o', 'o', 'o', 'o', 'o', 'x', 'o'],
    ['x', 'o', 'x', 'x', 'x', 'o', 'o', 'o'],
    ['<', 'o', 'o', 'x', 'o', 'x', 'x', 'x']
    ]

    return grid


if __name__ == "__main__":
  grid = main()

  start = Traverse(grid)
  start.start()
