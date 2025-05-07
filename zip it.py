s1={2,3,4}
s2={'d','z','a'}
s3=list(zip(s1,s2))
print(s3,"\n")

list3=[10,20,30,40]
list4=[400,300,200,100]
for x,y in zip(list3,list4[::-1]):
    print(x,y)

stocks=["reliance","infosys","tcs"]
prices=[2175,1127,2750]
newdic={stocks:prices for stocks,prices in zip(stocks,prices)}
print("\n{}".format(newdic))