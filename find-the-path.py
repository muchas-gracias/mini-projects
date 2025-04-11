
class Circular:
    def __init__(self, items):
        self.lst = items
        self.curr_idx = 1

    def __getitem__(self, idx):
        item = (self.curr_idx + idx) % len(self.lst)

        return item

    def remove_from_traveled(self, val):
        print(f"REMOVING {val} from {self.lst}")
        if val in self.lst:
            self.lst.remove(val)

        return

    def fill_traveled(self):
        self.lst.clear()
        self.lst = list(range(4))

        return

class Traverse:
    def __init__(self, grid):
        self.next = False
        self.end = False


        self.cir = Circular([0,1,2,3])
        # print(self.circle[-25])

        self.grid = grid
        self.symbols = {"blocker": "x", "go": "o", "start": ">", "end": "<"}
        self.blockers = []
        self.stuck = {}
        self.stuck_count = 0
        self.current = (0, 0)
        self.directions = [
            lambda: self.move(-1, 0), #north
            lambda: self.move(0, 1), # east
            lambda: self.move(1, 0), # south
            lambda: self.move(0, -1) # west
            ]

    def check_if_in_bounds(self, move):

        if move[0] < 0 or move[0] >= len(self.grid):
            return False

        if move[1] < 0 or move[1] >= len(self.grid[0]):
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
            self.next = True
            print("out of bounds")
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

        max_iter = len(self.directions)
        from_dir = 2

        self.get_all_blockers()
        self.find_start()
        greg = 0
        nel = 0
        self.cir.curr_idx = 1
        while not self.end:
            if not self.cir.lst:
                self.cir.fill_traveled()

            #removing coming from directions
            self.cir.remove_from_traveled(self.cir.__getitem__(from_dir))
            print("++++++++++++")

            while self.cir.lst:
                greg += 1
                self.directions[self.cir.curr_idx]() #travel in the direction

                if self.end:
                    break

                if self.next:
                    print(f"curr direction ++ {self.cir.curr_idx}")
                    print(self.cir.lst)
                    self.cir.remove_from_traveled(self.cir.curr_idx) #removing curr direction
                    print("gregory")
                    self.cir.curr_idx = self.cir.lst.pop(0) # setting next direction in the list
                    print(f"current direction {self.cir.curr_idx} and list is {self.cir.lst}")
                    print(f"\t \t \t\t\tcoordinates now are {self.current}")
                if greg == 500:
                    break
            nel += 1
            if nel == 255:
                break








        print(self.stuck)

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
