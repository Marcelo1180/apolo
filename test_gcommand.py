import unittest
from gcommand import GCommand


class TestAdd(unittest.TestCase):
    def test_command(self):
        result = GCommand.generate('jarvis, actualiza todos los repositorios')
        print(result)
        self.assertEqual(result, '(accion:actualiza)')


if __name__ == '__main__':
    unittest.main()
