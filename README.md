# analysis
AI department for a company that is manufacturing T-shirts. the data collection team gathered information about N persons. For each person they got 5 features:
1. The Height
2. The Weight
3. The body mass index
4. The length between the shoulders
5. The length of the arms

the data shaped as an Nx5 matrix.this code will cluster the data into K clusters to manufacture K sizes of the T-shirt.For example, if the K= 3 then the N samples is clustered into  3 sizes; small, medium and large.If the K=5 then the data is clustered into XS, S, M, L and XL.
K-mean clustering algorithm to cluster the normalized normalized N samples into K groups. 
there is redundancy in the features; they can reduced and still preserve the same information.Principle Component Analysis (PCA) is used to reduce the features from 5 dimensions to 2.

#How to run the code 

**run main.py 
K=5 for example
the graph of the running time vs the number of samples N
![Figure_2](https://user-images.githubusercontent.com/83555471/151893393-8f197620-aaee-4307-9cd3-cd82c10dc87f.png)

**run main2.py 

the percentage of each cluster from the total N samples for k=5
{   1  =>  16.946
2  => 17.785
3  => 21.606
4  => 24.731
5  => 18.932
  }
![Figure_1](https://user-images.githubusercontent.com/83555471/151893004-cf40e194-e83a-4371-9ba3-e441cc2563ce.png)




