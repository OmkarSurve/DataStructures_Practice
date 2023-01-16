# Person with 2 is celebrity 
MATRIX = [ [ 0, 0, 1, 0], 
           [ 0, 0, 1, 0],
           [ 0, 0, 0, 0],
           [ 0, 0, 1, 0]]
           
           
  
def knows(a, b): 
      
  return MATRIX[a][b] 
  
# Returns id of celebrity 
def findCelebrity(n): 
    #Practise Yourself :  Write your code Here
    x = 0
    y = n - 1
    celeb = -1
    
    # Once x becomes greater than y, we have covered all the cases
    while (x<y):
        
        if knows(x, y) == 1:
            x += 1
            celeb = y
        else:
            y -= 1
            celeb = x 
    
    # At this point, we cannot be sure whether user x or y is celibrity, we only know he can be, so we do final
    # verification by checking against each of the user.
    for i in range(n):
        if celeb != i:
            if knows(celeb, i) == 1 or knows(i, celeb) == 0:
                celeb = -1
                break
        
            
    return celeb 
  
if __name__ == '__main__': 
      
    n = 4
    idx = findCelebrity(n) 
      
    if (idx == -1):   
      print("No celebrity Found")  
    else: 
      print("Celebrity ID is", idx) 
      
