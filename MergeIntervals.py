X = [[1,3],[2,6],[8,10],[15,18]]
X = sorted(X,key=lambda X: X[0])
print(X)
m =[X[0]]
for i in range(1,len(X)):
    if m[len(m)-1][1]>=X[i][0]:
        x = m[len(m)-1][0]
        y = max(m[len(m)-1][1],X[i][1])
        m.remove(m[len(m)-1])
        m.append([x,y])
        
    else :
        m.append(X[i])
print(m)
