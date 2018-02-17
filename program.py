import numpy as np 
A = np.mat([
	[0,1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9,0],
	[2,3,4,5,6,7,8,9,0,1],
	[3,4,5,6,7,8,9,0,1,2]
	])

B = np.mat([
	[2,1],
	[1,1],
	[0,2],
	[3,1]
	])

C = np.mat([
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
	])

# baris A * baris B
baris_A = A [0:4]
print (baris_A)
kolom_B = B [:, 0:1]
print (kolom_B)

center = baris_A + kolom_B

print (center)

print ("github")

# baris = A [0:1]
# kolom = A [:, 0]
# Pilih baris dalam format a [start: end], jika start atau 
# end dihilangkan berarti semua range
# print(baris)
# Pilih kolom dalam format a [start: end, column_number]
# print(kolom)
