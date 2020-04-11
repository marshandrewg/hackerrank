import unittest
import NewYearChaos
class test_swapString(unittest.TestCase):

    def test_swap(self):
        line = NewYearChaos.swapString(5)
        line.swap(4)
        print(line)
        self.assertEqual(line.string, "12354")
        line.swap(3)
        line.swap(2)
        line.swap(4)
        self.assertEqual(line.string, "15243")
    
    def test_minSwaps(self):
        line = NewYearChaos.swapString(5)
        line.string = "12537864"
        swaps = line.minSwaps()
        self.assertEqual(swaps, 7)

if __name__ == '__main__':
    unittest.main()