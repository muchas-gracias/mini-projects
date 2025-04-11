
class Circular:
    def __init__(self, items):
        self.lst = items
        self.curr_dir = 1

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
        self.set_current = False

        self.pivot_points = {}


        self.cir = Circular([0,1,2,3])
        # print(self.circle[-25])

        self.grid = grid
        self.symbols = {"blocker": "x", "go": "o", "start": ">", "end": "<"}
        self.blockers = []

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

    def check_if_not_obstacle(self, move):
        if move in self.blockers:
            return False
        return True
            
    def move(self, vert, horiz):
        
        
        movement = (self.current[0] + vert, self.current[1] + horiz)
        if self.set_current:
            self.current = movement
            
        if not self.check_if_in_bounds(movement) or not self.check_if_not_obstacle(movement):
            return False
        return True       
     
    def check_around(self, lst):
        temp = []
        
        for each in lst:
            if self.directions[each]():
                temp.append(each)
        
        return temp
            
    def change_current_point(self, direction):
             pass
                
            
        
    # def move(self, vertical, horizontal):

        # self.next = False

        # print(f" current is {self.current}")

        # # # setting  temp movement to the next projected move
        # movement = (self.current[0] + vertical, self.current[1] + horizontal)
        # print(f"after changing movement {movement}")

        # # if there isn't an  blocker
        # if movement not in self.blockers and self.check_if_in_bounds(movement):
        #     self.current = movement
        #     print(f"changing current {self.current}")

        # elif not self.check_if_in_bounds(movement):
        #     self.next = True
        #     print("out of bounds")
        #     return

        # else: # if there is an obstacle
        #     if self.current not in self.stuck: # if obstacle not visited

        #         self.stuck[self.current] = 1

        #     else:
        #         if self.stuck.get(self.current) == 3: # if obstacle visited 3x's
        #             self.blockers.append(self.current) # adding to blockers list
        #             del self.stuck[self.current]

        #         else: # if obstacle hasn't been visited 3x's increment
        #             self.stuck[self.current] += 1

        #     self.next = True # move to the next direction

        # return


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
        # for 4-11 each move evaluate 3 side and mark possibilities
        max_iter = len(self.directions)
        from_dir = 2
        next_move = 0
        prev_move = 0

        self.get_all_blockers()
        self.find_start()
        greg = 0
        nel = 0
        
        self.cir.curr_dir = 1 # starting direction east
        g = 0
        while not self.end:
            if not self.cir.lst:
                self.cir.fill_traveled()

            while self.cir.lst:
                g += 1
                self.cir.lst = self.check_around(self.cir.lst) # checking in all 4 directions
                print(f" \t\t\t\tcircle list {self.cir.lst}")
                if len(self.cir.lst) > 1:
                    next_move = self.cir.lst.pop(0)
                    self.pivot_points[self.current] = {"possible": self.cir.lst[:], "next": next_move}
                
                
                self.set_current = True
                self.directions[next_move]()
                print(f"next move {next_move}")
                self.set_current = False
                
                print(f" current is {self.current}")
                self.cir.lst.clear()
                self.cir.fill_traveled()
                
                # check arount
                
                
                
                        
                    
                
                if g == 8:
                    break
            break

        print(f"pivot points {self.pivot_points}")
        print(f"continued direction {self.cir.lst}")




def main():

    grid = [
    ['>', 'o', 'o', 'o', 'o', 'x', 'x', 'o'],
    ['o', 'x', 'o', 'x', 'o', 'o', 'o', 'o'],
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
