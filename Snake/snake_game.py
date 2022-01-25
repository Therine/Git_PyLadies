#Creates a 10x10 table with nest tuples [['.','.','.'],['.','.','.'],['.','.','.']]
#So essentially a matrix
#def draw_map():
#    print([['.','.','.'],['.','.','.'],['.','.','.']])

#draw_map()
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append((input())) 
    matrix.append(a) 