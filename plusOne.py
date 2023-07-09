class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ""

        for i in digits:
            number += str(i)

        new_number = int(number) + 1

        arr = []

        for i in str(new_number):
            arr.append(int(i))

        return arr
