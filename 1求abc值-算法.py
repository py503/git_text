#如果a+b+c=1000,且a^2+b^2 = c^2(a,b,c为自然数)，如何不求出所有a,b,c可能的组合？
#用枚举法
import time
begintime = time.time()
def match():
    for a in range(0,1001):
        for b in range(0,1001):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                #print("a,b,c:d%,%d,%d" % (a,b,c))
                print(a,b,c)
                
match()
endtime = time.time()

print("计算所用时间:%d" %(endtime-begintime))
print("finished")
print("*" * 50)
