class Solution:
    table = {
        letter: index for index, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)
    }

    def title_to_number(self, column_title: str) -> int:
        # This is basically convert from base 26 to base 10, so the same logic should apply
        result = 0
        for position, letter in enumerate(reversed(column_title)):
            value = self.table[letter]
            result += value * 26 ** position
        return result
