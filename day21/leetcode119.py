class Solution:
    def getRow(self, rowIndex: int):
        row = [1]
        for i in range(1, rowIndex + 1):
            new_row = [1]
            for j in range(1, len(row)):
                new_row.append(row[j - 1] + row[j])
            new_row.append(1)
            row = new_row
        return row
