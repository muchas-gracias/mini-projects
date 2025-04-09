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
  """
  Grid Search class the sets up, iterates, parses, and finds the closest point(s)
  within the grid.
  
  Attributes:
    start_row (str): start x coordinate
    start_col (str): starting y coordinate
    grid (list): list of lists

  """
  def __init__(self, start_row, start_col, grid):
    """
    
    """
    self.vertical = start_row
    self.horizontal = start_col
    self.grid = grid
    
    self.cols = len(self.grid[0]) -1
    self.rows = len(self.grid) -1

    self.points = []
    self.point = "x"

  def get_all_points(self) -> bool:
    """
    Iterates a list of lists to find every x, and append the x,y coordinate
    
    Args:
      None
    Return:
      True if > 0 has been found, or Fase if 0 found
    """
    points_found = False
    
    for index, row in enumerate(self.grid):
      for each, x in enumerate(row):
        if x == self.point:
          tup = (index, each)
          self.points.append(tup)
          points_found = True
    
    return True if points_found else False
  
  def find_min_val(self, temp) -> list:
    """
    Iterates a list and of integers and finds the minimum number and the index
    of that number.
    
    Args:
      temp (list) : list of integers
    
    Return:
      list: n returns the list of indices
    """
    min_val = min(temp)
    
    min_indices = [index for index, value in enumerate(temp) if value == min_val]

    return min_indices
    
  def find_closest(self) -> list:
    """
    
    """
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
  
  """
  Entry point of the program. Sets up the grid, the starting point,
  as well as creates and instance of the Grid_Search class.
  
  Args:
    None
    
  Return:
    None
  """
  
  grid = [
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'V', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'x', 'o', 'o', 'o', 'o', 'o', 'o']
  ]

  start_row, start_col = 0, 1
  start = Grid_Search(start_row, start_col, grid)
  print(f"Closest Points = {start.start()}")


if __name__ == "__main__":
  main()  
