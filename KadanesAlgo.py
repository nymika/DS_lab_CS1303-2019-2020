X = [-2,-3,4,-1,-2,1,5,-3]
maxc = maxg = X[0]
for i in range(1,len(X)) :
   if X[i] > maxc+X[i]:
       maxc = X[i]
   else:
       maxc = maxc+X[i]

   if maxc > maxg :
       maxg = maxc
print(maxg)
    

  

       
        