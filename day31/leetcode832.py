class Solution:
    def flipAndInvertImage(self, image):
        for row in image:
            # Flip the row and invert in one go using list comprehension
            for i in range((len(row) + 1) // 2):
                # Swap and invert at the same time
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return image
