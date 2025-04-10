
class Circular:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index % len(self.items)]


class Traverse:
    def __init__(self, grid):
        self.skip = False
        self.next = False
        self.circle = Circular([0,1,2,3])
        # print(self.circle[-25])

        self.grid = grid
        self.symbols = {"blocker": "x", "go": "o", "start": ">", "end": "<"}
        self.blockers = []
        self.stuck = {}
        self.stuck_count = 0
        self.current = (0, 0)
        self.directions = [
            lambda: self.move(0, 1),
            lambda: self.move(1, 0),
            lambda: self.move(0, -1),
            lambda: self.move(-1, 0)
            ]

    def check_if_in_bounds(self, move):

        if move[0] < 0 and move[0] >= len(self.grid):
            return False

        if move[1] < 0 and move[1] >= len(self.grid[0]):
            return False

        return True


    def move(self, vertical, horizontal):

        self.next = False
        print(f" current is {self.current}")

        # # setting  temp movement to the next projected move
        movement = (self.current[0] + vertical, self.current[1] + horizontal)
        print(f"after changing movement {movement}")

        # if there isn't an  blocker
        if movement not in self.blockers and self.check_if_in_bounds(movement):
            self.current = movement
            print(f"changing current {self.current}")

        elif not self.check_if_in_bounds(movement):
            return

        else: # if there is an obstacle
            if self.current not in self.stuck: # if obstacle not visited

                self.stuck[self.current] = 1

            else:
                if self.stuck.get(self.current) == 3: # if obstacle visited 3x's
                    self.blockers.append(self.current) # adding to blockers list
                    del self.stuck[self.current]

                else: # if obstacle hasn't been visited 3x's increment
                    self.stuck[self.current] += 1

            self.next = True # move to the next direction

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
        end = False
        max_iter = len(self.directions)

        self.get_all_blockers()
        self.find_start()

        while not end:
            idx = 0
            while idx < max_iter:

                self.directions[idx]()
                if self.next:
                    idx += 1







        print(self.stuck)

def main():

    grid = [
    ['>', 'o', 'o', 'o', 'o', 'x', 'x', 'o'],
    ['x', 'x', 'o', 'x', 'o', 'o', 'o', 'o'],
    ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'o'],
    ['o', 'o', 'x', 'o', 'o', 'o', 'x', 'o'],
    ['x', 'o', 'o', 'o', 'x', 'x', 'x', 'o'],
    ['x', 'o', 'x', 'o', 'o', 'o', 'x', 'o'],
    ['x', 'o', 'x', 'x', 'x', 'o', 'o', 'o'],
    ['<', 'o', 'o', 'x', 'o', 'x', 'x', 'x']
    ]

    return grid


if __name__ == "__main__":
  grid = main()

  start = Traverse(grid)
  start.start()
