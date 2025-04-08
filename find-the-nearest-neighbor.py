
class Grid_search:
  def __init__(self, start_row, start_col, grid):
    self.vertical = start_row
    self.horizontal = start_col
    self.grid = grid
    self.cols = len(self.grid[0]) -1
    self.rows = len(self.grid) -1

    self.points = []
    self.point = "x"

  def get_all_points(self):
    for index, row in enumerate(self.grid):
      for each, x in enumerate(row):
        if x == self.point:
          tup = (index, each)
          self.points.append(tup)
      
  def search_north(self, idx):

    if self.vertical - idx >= 0:
      search = (self.vertical - idx, self.horizontal)
      if search in self.points:
        return search
    return ()

   def search_south(self, idx):

    if self.vertica+ - idx <= self.rows:
      search = (self.vertical + idx, self.horizontal)
      if search in self.points:
        return search
    return ()

   def search_east(self, idx):

    if self.horizontal + idx >= self.cols:
      search = (self.vertical, self.horizontal + idx)
      if search in self.points:
        return search
    return ()

   def search_west(self, idx):

    if self.horizontal - idx >= 0:
      search = (self.vertical, self.horizontal- idx)
      if search in self.points:
        return search
    return ()

  def search_north_east(self, idx):

    if self.vertical - idx >= 0 and self.horizontal + idx <= self.cols:
      search = (self.vertical - idx, self.horizontal + idx)
      if search in self.points:
        return search
    return ()
  
  def search_north_west(self, idx):

    if self.vertical - idx >= 0 and self.horizontal - idx >= 0:
      search = (self.vertical - idx, self.horizontal - idx)
      if search in self.points:
        return search
    return ()
  
  def search_south_east(self, idx):

    if self.vertical + idx <= self.rows and self.horizontal + idx <= self.cols:
      search = (self.vertical + idx, self.horizontal + idx)
      if search in self.points:
        return search
    return ()
  
  def search_south_west(self, idx):

    if self.vertical + idx <= self.rows and self.horizontal - idx >= 0:
      search = (self.vertical + idx, self.horizontal - idx)
      if search in self.points:
        return search

  def find_closest(self):
    primary = set()
    secondary = set()
    idx = 0

    while idx <= self.rows:
      if(return_value := self.search_north(idx)):
        primary.add(return_value)
      if(return_value := self.search_south(idx)):
        primary.add(return_value)
      if(return_value := self.search_east(idx)):
        primary.add(return_value)
      if(return_value := self.search_west(idx)):
        primary.add(return_value)

      if(return_value := self.search_north_east(idx)):
        primary.add(return_value)
      if(return_value := self.search_north_west(idx)):
        primary.add(return_value)
      if(return_value := self.search_south_east(idx)):
        primary.add(return_value)
      if(return_value := self.search_south_west(idx)):
        primary.add(return_value)

    if primary or secondary:
      break
    idx += 1
  return primary, secondary

def start)self):
  self.get_all_points()
  primary, secondary = self.find_closest()
  if primary:
    print(f"primary {primary}")
  else:
    print(f"secondary {secondary}")

def main():
  grid = [
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
  ]

start_row, start_col = 6, 4
start = Grid_Search(start_row, start_col, grid)
start.start()

main()
