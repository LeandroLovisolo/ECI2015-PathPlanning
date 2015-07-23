class Quadcopter:
  def __init__(self, pos):
    self.pos = pos
    self.V = []
    self.E = []



  def update(self, new_pos):
    return [2, 2, 0.5]
    # new_pos[0] = new_pos[0] + .01
    # return new_pos

