mport unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_init(self):
        rx, ry = a_star_planning(sx, sy, gx, gy, ox, oy, grid_size, robot_size)
        self.assertFalse(rx)
        self.assertFalse(ry)
        

    def test_calc_heuristic(self):
        s = a_star_planning(4.0, , 2.0, 0.8, 4.4, 8.2, 20, 3.4)
        self.assertEqual(8, 4)

    def test_verity_node(self):
        s = a_star_planning(4.0, , 2.0, 0.8, 4.4, 8.2, 20, 3.4)
        
        self.assertFalse(s)

    def test_calc_obstacle_map(self):
        s  = a_star_planning(8.0, , 2.4, 0.8, 4.8, 8.2, 20, 3.4)
        
        self.assertEqual("8, 5, 6", s)
       
if __name__ == '__main__':
    unittest.main()
