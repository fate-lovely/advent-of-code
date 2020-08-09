from math import sqrt
from collections import namedtuple
import numpy as np

input = """
../.. => .##/#../..#
#./.. => .##/#../###
##/.. => ..#/#.#/#..
.#/#. => #../#../.#.
##/#. => .#./#../#..
##/## => .##/.../.##
.../.../... => #.#./###./####/#..#
#../.../... => .###/####/##../#.##
.#./.../... => ###./.###/#..#/#.##
##./.../... => ..../..../.#../##..
#.#/.../... => ...#/.##./..../##..
###/.../... => ##../##../##.#/..##
.#./#../... => .#../###./##../####
##./#../... => ####/##.#/..../..##
..#/#../... => ..#./####/...#/#.##
#.#/#../... => #.#./##../##../.##.
.##/#../... => ##../####/..#./...#
###/#../... => #..#/#.#./##.#/#.#.
.../.#./... => .#.#/..#./#.../....
#../.#./... => ##../..##/..##/.#..
.#./.#./... => ..../##../##../#.##
##./.#./... => ...#/##../#..#/.###
#.#/.#./... => ####/##.#/###./..##
###/.#./... => ..../...#/.###/.#..
.#./##./... => #.#./#..#/.##./.#.#
##./##./... => .###/#.../#..#/#.#.
..#/##./... => .###/####/..../#.##
#.#/##./... => ...#/.###/.###/.###
.##/##./... => ..##/..##/.###/##.#
###/##./... => ####/#..#/####/#.#.
.../#.#/... => #.##/..#./.###/#.#.
#../#.#/... => ####/##.#/##.#/....
.#./#.#/... => #.../...#/#.##/#..#
##./#.#/... => .#.#/##../##../....
#.#/#.#/... => ##.#/#.../##../.#..
###/#.#/... => ...#/###./.#.#/...#
.../###/... => .###/#.##/#.../###.
#../###/... => ..##/.#../.###/..#.
.#./###/... => ..../.##./#.##/#.##
##./###/... => .#.#/##.#/#.../#.#.
#.#/###/... => ..#./#.../#.#./.##.
###/###/... => ..##/.#.#/#..#/.##.
..#/.../#.. => ..##/.#../##.#/##..
#.#/.../#.. => ..#./..../#.../...#
.##/.../#.. => .##./..##/####/#...
###/.../#.. => #.##/..../##../#.##
.##/#../#.. => .###/...#/###./....
###/#../#.. => .#.#/#.#./#.##/..#.
..#/.#./#.. => ...#/..#./..##/.#.#
#.#/.#./#.. => #.../##.#/.###/#.#.
.##/.#./#.. => ###./####/#..#/##.#
###/.#./#.. => ..../..#./..../#...
.##/##./#.. => .#.#/.##./.#.#/#.##
###/##./#.. => ..../##../###./.#.#
#../..#/#.. => ...#/#.../#.##/.###
.#./..#/#.. => #..#/.#../###./#.#.
##./..#/#.. => #.#./..#./###./###.
#.#/..#/#.. => .#.#/##.#/##../####
.##/..#/#.. => ###./..../.#../...#
###/..#/#.. => #.#./.##./.#.#/#..#
#../#.#/#.. => #.#./##.#/.#../.###
.#./#.#/#.. => ##.#/#.#./#.../####
##./#.#/#.. => .#.#/#.../..#./#.##
..#/#.#/#.. => ##.#/.##./#.../.###
#.#/#.#/#.. => ..##/..../..../####
.##/#.#/#.. => ####/#.#./###./.#.#
###/#.#/#.. => #.##/..#./##../#...
#../.##/#.. => ..##/##.#/####/.#..
.#./.##/#.. => ..##/##../.#../..##
##./.##/#.. => ..##/.#.#/#..#/....
#.#/.##/#.. => #.../##../...#/.#.#
.##/.##/#.. => ##../...#/.###/.#.#
###/.##/#.. => ####/..#./.##./#.##
#../###/#.. => .#.#/##.#/#.#./#.#.
.#./###/#.. => .###/#..#/.#.#/###.
##./###/#.. => ##../.#../###./.#.#
..#/###/#.. => #.##/..../...#/..#.
#.#/###/#.. => #.../#..#/..../.#..
.##/###/#.. => ####/#..#/..#./.#.#
###/###/#.. => .##./##../.#../..#.
.#./#.#/.#. => #.#./.###/#.#./..##
##./#.#/.#. => .##./..../..##/##..
#.#/#.#/.#. => ...#/..../.#.#/..##
###/#.#/.#. => .#../####/#.#./#.##
.#./###/.#. => #..#/.#.#/#..#/#.#.
##./###/.#. => .#../##../#..#/..##
#.#/###/.#. => #.#./.##./##.#/.#.#
###/###/.#. => #.#./...#/..##/#...
#.#/..#/##. => ..#./..#./...#/#..#
###/..#/##. => #..#/###./..../##.#
.##/#.#/##. => #.##/.#.#/...#/..##
###/#.#/##. => #.##/...#/.##./.###
#.#/.##/##. => ..../##.#/..../...#
###/.##/##. => .###/#.../###./###.
.##/###/##. => #.../#.#./.###/..#.
###/###/##. => #.##/.#../..#./.#.#
#.#/.../#.# => .##./##../###./.###
###/.../#.# => ..##/...#/###./.#..
###/#../#.# => ##.#/..#./#.##/.#..
#.#/.#./#.# => .#../#.##/...#/###.
###/.#./#.# => ..#./..../####/####
###/##./#.# => ###./#..#/..../#..#
#.#/#.#/#.# => ##.#/###./..../#...
###/#.#/#.# => ##../.###/#..#/.#..
#.#/###/#.# => #.../###./.###/..#.
###/###/#.# => ..../.##./.#../###.
###/#.#/### => ##../#.../.###/#...
###/###/### => .###/###./#.##/..#.
"""

part1_test = ("""
.#/.. => ##./#../...
###/..#/.#. => #..#/..../..../#..#
""", 2, 12)

Rule = namedtuple("Rule", ("start", "end"))

# should be immutable
class Image:
  @classmethod
  def merge(cls, imgs):
    all_cells = [img.cells for img in imgs]
    chunk_size = int(sqrt(len(imgs)))
    arr = [all_cells[i*chunk_size:i*chunk_size+chunk_size] for i in range(chunk_size)]
    return Image(np.bmat(arr))

  def __init__(self, arr):
    self.cells = np.array(arr, str)
    self.size = len(self.cells)
    self.on_count = np.count_nonzero(self.cells == "#")

  def __eq__(self, other):
    return np.array_equal(self.cells, other.cells)

  def __repr__(self):
    return "/".join("".join(row) for row in self.cells)

  def split(self):
    cls = type(self)
    chunk_size = 2 if self.size % 2 == 0 else 3
    count = self.size // chunk_size
    result = []
    for row in range(count):
      for col in range(count):
        arr = self.cells[
          row*chunk_size:row*chunk_size+chunk_size,
          col*chunk_size:col*chunk_size+chunk_size,
        ]
        result.append(Image(arr))
    return result

  def enhance(self, rules):
    for rule in rules:
      if self.on_count == rule.start.on_count:
        for shape in self.shapes():
          if shape == rule.start:
            return rule.end
    raise Exception("could not enhance image", self)

  def shapes(self):
    c = np.rot90(self.cells)
    yield Image(c)
    yield Image(np.flip(c, 0))
    yield Image(np.flip(c, 1))

    c = np.rot90(c)
    yield Image(c)
    yield Image(np.flip(c, 0))
    yield Image(np.flip(c, 1))

    c = np.rot90(c)
    yield Image(c)
    yield Image(np.flip(c, 0))
    yield Image(np.flip(c, 1))

    c = np.rot90(c)
    yield Image(c)
    yield Image(np.flip(c, 0))
    yield Image(np.flip(c, 1))

def parse_str(str):
  return [list(s) for s in str.strip().split("/")]

start_img = Image(parse_str(".#./..#/###"))

def parse_rules(input):
  result = []
  for rule in input.strip().split("\n"):
    start_arr, end_arr = (parse_str(s) for s in rule.split("=>"))
    result.append(Rule(
      Image(start_arr),
      Image(end_arr),
    ))
  return result

def solve_part1(input, count):
  rules = parse_rules(input)
  img = start_img
  for _ in range(count):
    img = Image.merge([i.enhance(rules) for i in img.split()])
  return img.on_count

# print(solve_part1(part1_test[0], part1_test[1]), part1_test[2])
# print(solve_part1(input, 5))
# 133

# print(solve_part1(input, 18))
# 2221990