class Matrix:
    def __init__(self,array):
        self.array = array
        #self.new_matrix = new_matrix
    def __add__(self,other):
        #self.other = other
	'''
        if len(self.array) == len(other.array):
            row_len1 = self.array[0]
            row_len2 = other.array[1]
        for row in self.array:
            if row_len1 != len(row):
                return False
        for row in other.array:
            if row_len2 != len(row):
                return False
	'''
        new_matrix = []
        for i in range(len(self.array)):
            row = []
            for j in range (len(self.array[0])):
        	row.append((self.array[i][j])+ (other.array[i][j]))
        	new_matrix.append(row)
        return Matrix(new_matrix)
    def __str__(self):
        return str(self.array) 


num_row = int(input())
num_column = int(input())
matrix = []
for i in range(num_row):
    row = []
    for j in range(num_column):
        cell = int(input())
        row.append(cell)
    matrix.append(row)
m1 = Matrix(matrix)
m2 = Matrix(matrix)
m3 = Matrix(matrix)
m4 = Matrix(matrix)  
m5 = m1+m2
print m5

