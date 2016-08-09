import sys
sys.path.append('/home/fenrir/Coding/Games/Reflections')

import unittest
import source.level

class ReflectTest(unittest.TestCase):
    def testNavigation(self):
        forest_obj = source.level.Forest()

        self.assertEqual(forest_obj.area_map[4], "x", "Invalid start location")

        # Move Up
        source.level.navigate(forest_obj, 0)
        self.assertEqual(forest_obj.area_map[1], "x", "Player moved to the wrong space")

        # Move down
        source.level.navigate(forest_obj, 2)
        self.assertEqual(forest_obj.area_map[4], "x", "Player moved to the wrong space")

        # Move left
        source.level.navigate(forest_obj, 1)
        self.assertEqual(forest_obj.area_map[3], "x", "Player moved to the wrong space")

        # Move right
        source.level.navigate(forest_obj, 3)
        self.assertEqual(forest_obj.area_map[4], "x", "Player moved to the wrong space")

        # Move test borders
        source.level.navigate(forest_obj, 3)
        return_obj = source.level.navigate(forest_obj, 3)
        self.assertTrue(return_obj[1], "Border Not Crossed")

obj = ReflectTest()
obj.testNavigation()
