
class Rotate:
    def __init__(self):
        pass


class Traverse:
    def __init__(self, grid):
        self.skip = False
        self.next = False

        self.grid = grid
        self.symbols = {"blocker": "x", "go": "o", "start": ">", "end": "<"}
        self.blockers = []
        self.stuck = {}
        self.stuck_count = 0
        self.current = (0, 0)
        self.directions = [self.move(0, 1), self.move(1, 0), self.move(0, -1), self.move(-1, 0)]



    def move(self, vertical, horizontal):
        self.next = False

        # setting  temp movement to the next projected move
        movement = (self.current[0] + vertical, self.current[1] + horizontal)

        if movement not in self.blockers: # if there isn't an  blocker
            self.current = movement

        else: # if there is an obstacle
            if not (self.current == self.stuck): # if obstacle not visited
                self.stuck = self.current
                self.stuck_count += 1
            else:
                if self.stuck_count == 3: # if obstacle visited 3x's
                    self.blockers.append(self.stuck)
                    self.stuck = ()
                    self.stuck_count = 0
                else: # if obstacle hasn't been visited 3x's increment
                    self.stuck += 1

            self.next = True # move to the next direction


        return
        print(self.grid[movement[0]][movement[1]])


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

        self.get_all_blockers()
        self.find_start()

        while not end:

            for each in self.directions:
                print(each)
            end=True



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