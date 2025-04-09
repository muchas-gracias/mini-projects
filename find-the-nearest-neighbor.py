"""
Program Name: find-the-nearest-neighbor

Description:
    This program finds the nearest neighbor in a python 2D grid filled with 
    x's and 0's.  The x's are the neighbors and the o's are spread throughout
    the grid.  The program uses a distinct formula to calculate the grid coordinates
    to decipher which is the closest to the starting point.

Features:
    - Reads from a manual grid within the program

Dependencies:
    - None

Usage:
    python3 find-the-nearest-neighbor

Example:
    python3 find-the-nearest-neighbor

Author:
    Greg Nelson

Date Created:
    2025-04-08

Version:
    1.0.0

License:
    None

"""
class Grid_Search:
  def __init__(self, start_row, start_col, grid):
    self.vertical = start_row
    self.horizontal = start_col
    self.grid = grid
    
    self.cols = len(self.grid[0]) -1
    self.rows = len(self.grid) -1

    self.points = []
    self.point = "x"

  def get_all_points(self) -> bool:
    points_found = False
    
    for index, row in enumerate(self.grid):
      for each, x in enumerate(row):
        if x == self.point:
          tup = (index, each)
          self.points.append(tup)
          points_found = True
    
    return True if points_found else False
  
  def find_min_val(self, temp) -> list:
    min_val = min(temp)
    
    min_indices = [index for index, value in enumerate(temp) if value == min_val]

    return min_indices
    
  def find_closest(self) -> list:
    temp = []

    for each in self.points:
      temp.append(abs(self.vertical - each[0]) + abs(self.horizontal - each[1]))

    indices = self.find_min_val(temp)
    
    return indices

  def start(self) -> list:
    if not self.get_all_points():
      return []

    
    indices = self.find_closest()
    
    return [self.points[each] for each in indices]


def main() -> None:
  
  grid = [
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'V', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
  ]

  start_row, start_col = 6, 4
  start = Grid_Search(start_row, start_col, grid)
  print(f"Closest Points = {start.start()}")


if __name__ == "__main__":
  main()  
