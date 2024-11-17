import unittest
import EX1
import EX2

run_test = unittest.TestSuite()
run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(EX1.RunnerTest))
run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(EX2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_test)