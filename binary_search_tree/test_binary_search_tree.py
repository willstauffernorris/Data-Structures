import unittest
import random
import sys
import io
from binary_search_tree import BSTNode

class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = BSTNode(5)

    def test_insert(self):
        self.bst.insert(2)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(6)
        self.assertEqual(self.bst.left.right.value, 3)
        self.assertEqual(self.bst.right.left.value, 6)
        
    def test_handle_dupe_insert(self):
        self.bst2 = BSTNode(1)
        self.bst2.insert(1)
        self.assertEqual(self.bst2.right.value, 1)

    def test_contains(self):
        self.bst.insert(2)
        self.bst.insert(3)
        self.bst.insert(7)
        self.assertTrue(self.bst.contains(7))
        self.assertFalse(self.bst.contains(8))

    def test_get_max(self):
        self.assertEqual(self.bst.get_max(), 5)
        #print("~~~PASS NICE JOB, 5 is the max")
        self.bst.insert(30)
        self.assertEqual(self.bst.get_max(), 30)
        #print("~~~PASS NICE JOB")
        #print(f'self value 1{self.value}')
        self.bst.insert(300)
        #print(f'self value {self.value}')
        self.bst.insert(3)
        final = self.bst.get_max()
        #print(final)
        self.assertEqual(final, 300)
        #print("~~~PASS NICE JOB")

    def test_for_each(self):
        arr = []
        cb = lambda x: arr.append(x)

        v1 = random.randint(1, 101)
        #print(v1)
        v2 = random.randint(1, 101)
        #print(v2)
        v3 = random.randint(1, 101)
        #print(v3)
        v4 = random.randint(1, 101)
        #print(v4)
        v5 = random.randint(1, 101)
        #print(v5)

        self.bst.insert(v1)
        self.bst.insert(v2)
        self.bst.insert(v3)
        self.bst.insert(v4)
        self.bst.insert(v5)
        #print("---------")
       # print("MANAGED TO INSERT")
        #print("---------")

        self.bst.for_each(cb)
        #print(f'length of array: {len(arr)}')

        self.assertTrue(5 in arr)
        #print("5 is in the array")
        self.assertTrue(v1 in arr)
        #print("~~~v1 in array PASS NICE JOB")
        self.assertTrue(v2 in arr)
        #print("~~~v2 in array PASS NICE JOB")
        self.assertTrue(v3 in arr)
        #print("~~~v3 in array PASS NICE JOB")
        self.assertTrue(v4 in arr)
        #print("~~~v4 in array PASS NICE JOB")
        self.assertTrue(v5 in arr)
        #print("~~~v5 in array PASS NICE JOB")

    def test_print_traversals(self):
        # WARNING:  Tests are for Print()
        # Debug calls to Print() in functions will cause failure

        stdout_ = sys.stdout  # Keep previous value
        sys.stdout = io.StringIO()

        self.bst = BSTNode(1)
        self.bst.insert(8)
        self.bst.insert(5)
        self.bst.insert(7)
        self.bst.insert(6)
        self.bst.insert(3)
        self.bst.insert(4)
        self.bst.insert(2)

        self.bst.in_order_print(self.bst)
        

        output = sys.stdout.getvalue()
        self.assertEqual(output, "1\n2\n3\n4\n5\n6\n7\n8\n")

        sys.stdout = io.StringIO()
        self.bst.bft_print(self.bst)
        output = sys.stdout.getvalue()
        self.assertTrue(output == "1\n8\n5\n3\n7\n2\n4\n6\n" or
                        output == "1\n8\n5\n7\n3\n6\n4\n2\n")

        sys.stdout = io.StringIO()
        self.bst.dft_print(self.bst)
        output = sys.stdout.getvalue()
        self.assertTrue(output == "1\n8\n5\n7\n6\n3\n4\n2\n" or
                        output == "1\n8\n5\n3\n2\n4\n7\n6\n")

        # sys.stdout = io.StringIO()
        # self.bst.pre_order_dft(self.bst)
        # output = sys.stdout.getvalue()
        # self.assertEqual(output, "1\n8\n5\n3\n2\n4\n7\n6\n")

        # sys.stdout = io.StringIO()
        # self.bst.post_order_dft(self.bst)
        # output = sys.stdout.getvalue()
        # self.assertEqual(output, "2\n4\n3\n6\n7\n5\n8\n1\n")

        print()
        sys.stdout = stdout_  # Restore stdout

if __name__ == '__main__':
    unittest.main()
