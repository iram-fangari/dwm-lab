import numpy as np
N=int (input("\n enter how many number of pages :"))
print("\n please eneter the adjacency matrix for the number")
links=[]
for i in range(0,N):
    L=[]
    for j in range(0,N):
        L.append(int(input('type 1 if there is a link from page'+(i+1)+' to page '+str(j+1)+':')))
        links.append(L)
outboundL=np.zeros((N,),dtype=int)
for i in range(0,N):
    for j in range(0,N):
        if(Links[i][j]==1):
            outboundL[i]+=1