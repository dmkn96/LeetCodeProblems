class Solution:

    def __init__(self, number):
        self.intToRoman(number)

    @staticmethod
    def intToRoman(num: int) -> str:
        if 1 <= num <= 3999:
            return 'error'

        romanDigitDict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }

        return 'None'


if __name__ == '__main__':
    Solution(50)
