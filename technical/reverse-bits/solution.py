class Solution:
    def reverseBits(self, n: int) -> int:
        # The idea is using a left index and a right index, and on each iteration
        # take the value of each of those indexes, and if it's on, set the bit on
        # the opposite index. E.g: if the bit on the right index is on, the we set
        # set on the value on the left index; if it's off on the right index, we
        # set it off on the left index.
        left_index = 31
        right_index = 0
        while left_index > right_index:
            left_mask = (1 << left_index)
            right_mask = (1 << right_index)

            leftval = n & left_mask
            rightval = n & right_mask

            if rightval:
                # Set bit on left index if the value on the right index is on
                n |= left_mask
            else:
                # Clear it otherwise
                n &= ~left_mask

            if leftval:
                n |= right_mask
            else:
                n &= ~right_mask
            left_index -= 1
            right_index += 1
        return n
