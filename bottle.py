# -*- coding: utf-8 -*-
__author__ = 'liebesu'


import sys


def buy():
    money=10
    price=2
    capchange=4
    bottlechange=2
    result=0
    bottle=0
    cap=0
    for num in range(1,50):
        print "第 " + str(num)+"操作"
        if money >= price :
            money=money-price
            result=result+1
            bottle=bottle+1
            cap=cap+1
            print "买 1 瓶"
            print "剩余钱 ："+str(money) +" 瓶子数量："+str(bottle)+"瓶盖数量："+str(cap)

        else:
            if bottle>=2:
                result=result+1
                bottle=bottle-1
                cap=cap+1
                print "瓶子换 1 瓶"
                print "剩余钱 ："+str(money) +" 瓶子数量："+str(bottle)+"瓶盖数量："+str(cap)
            else:
                if cap>=4:
                    result=result+1
                    bottle=bottle+1
                    cap=cap-3
                    print "瓶盖换 1 瓶"
                    print "剩余钱 ："+str(money) +" 瓶子数量："+str(bottle)+"瓶盖数量："+str(cap)
        if money<price and bottle<2 and cap <4:
            print "结果: "+str(result)
            print "剩余钱:"+str(money),"   剩余瓶子:"+str(bottle)," 剩余瓶盖:"+str(cap)
            sys.exit(0)
if __name__ =="__main__":
    buy()
