for i in range(101):
    for j in range(101):
        for k in range(101):
            if 5*i+3*j+1/3*k ==100 and k%3 ==0 and i+j+k ==100:
                print("公鸡：{}只 母鸡：{}只 小鸡：{}只".format(i,j,k))