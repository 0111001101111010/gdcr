#!/usr/bin/env python

import unittest

class Cell():
    # postion(X, Y)
    def __init__(self, state=False, position=(0,0)):
        self.position = position

class Cell_Tests(unittest.TestCase):
    def test_cell_position_on_init(self):
        cell = Cell(state=True, position=(1,4))
        cell_new = Cell(state=True, position=(0,0))

        self.assertNotEqual(cell.position, cell_new.position)

    def test_cell_state_on_init(self):
        cell = Cell(state=True, position=(0,0))

        self.assertEqual(cell.state, True)


if __name__ == '__main__':
    unittest.main()
