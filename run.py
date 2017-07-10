import percolate
import unittest
import test


if __name__ == '__main__':
    # runs the percolate app, check the result.out file in the data folder after
    # if result.out is already in the data folder prior to running the app, then delete the file first
    percolate.run_percolate_app()

    # runs the unittests in test.py
    # you should see the results of the tests in terminal
    suite = unittest.TestLoader().loadTestsFromModule(test)
    unittest.TextTestRunner(verbosity=2).run(suite)
