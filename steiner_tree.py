from dijkstar import Graph, find_path
import pandas as pd
import numpy as np
steiner_network=[]


def steiner_tree(reader_cost,reader_od):
    matrix_cost=np.array(reader_cost)
    matrix_od=np.array(reader_od)
    graph=Graph()
# ایجاد گراف دایجسترا
    for item in range(matrix_cost.shape[0]):
        graph.add_edge(matrix_cost[item,0], matrix_cost[item,1], matrix_cost[item,2])
# ستون آخر ماتریس تقاضا(مجموع سفرهای تولید شده) را در لیست فرار بده
    list_max =[]
    for item in matrix_od[:,-1]:
        list_max.append(item)
# ماکزیمم اول و دوم را در لیست ایجاد شده شناسایی کن
    first_max=max(list_max[0],list_max[1])
    second_max=0
    for item in range(2,len(list_max)):
        if list_max[item]>first_max:
            second_max=first_max
            first_max=list_max[item] 
        elif list_max[item]>second_max:
            second_max=list_max[item]
# بین دو نقطه ماکزیمم، کوتاهترین مسیر را ایجاد کن
    steiner_outcome=find_path(graph, list_max.index(first_max), list_max.index(second_max))
    steiner_route=steiner_outcome.nodes
    steiner_network.append(steiner_route)
# مقدار نقطه های اول و دوم تقاضا را در ماتریس تقاضا برابر با صفر قرار بده
    matrix_od[list_max.index(first_max),-1]=0
    matrix_od[list_max.index(second_max),-1]=0
    #reader_cost=matrix_cost
    #reader_od=matrix_od
# مشخص کن که تمام نقاط ماتریس تقاضا بررسی شده و برابر صفر قرارداده شده
    # مشخص کن بیش از یک نقطه تقاضا برای ایجاد مسیر باقی مانده است
    if np.count_nonzero(matrix_od[:,-1])>1:
        steiner_tree(reader_cost,matrix_od)
    return steiner_network

    
reader_cost =pd.read_excel(r'C:\Users\sony\Anaconda3\envs\Mahyarenv\Mahyar\mandl_cost.xlsx')
reader_od =pd.read_excel(r'C:\Users\sony\Anaconda3\envs\Mahyarenv\Mahyar\mandl_od.xlsx')
print(steiner_tree(reader_cost,reader_od))   


        
    





    
    
 


     


    
    
    

    
        
        
        
        
        
   

    