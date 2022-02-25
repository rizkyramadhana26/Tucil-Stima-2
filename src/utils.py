#visualisasi hasil ConvexHull
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from myConvexHull import *

def drawConvexHull(df,target_names,filename,mode):
    count=0
    for i in range(0,min(3,len(df.columns)-1)): #take 3 pairs for every dataset if possible
        for j in range(i+1,min(3,len(df.columns)-1)):
            plt.figure(figsize = (10, 6))
            colors = ['b','r','g','y','p','o']
            plt.xlabel(df.columns[i])
            plt.ylabel(df.columns[j])
            for k in range(len(target_names)):
                bucket = df[df['Target'] == k]
                bucket = bucket.iloc[:,[i,j]].values
                if(mode==0): #using myConvexHull
                    plt.title(f'{df.columns[j]} vs {df.columns[i]} (self-made)')
                    hull = myConvexHull(bucket)
                    plt.scatter(bucket[:, 0], bucket[:, 1], label=target_names[k])
                    for simplex in hull :
                        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[k])
                else : #using scipy's ConvexHull
                    plt.title(f'{df.columns[j]} vs {df.columns[i]} (scipy)')
                    hull = ConvexHull(bucket)
                    plt.scatter(bucket[:, 0], bucket[:, 1], label=target_names[k])
                    for simplex in hull.simplices:
                        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[k])

                
            plt.legend()
            plt.savefig('result/'+filename+'-'+str(count)+'.png')
            count+=1
