import yfinance as yf
from prettytable import PrettyTable
from datetime import datetime, timedelta
import matplotlib.pyplot as plt




date=datetime.today()
hoje=str(date.year)+'-'+str(date.month)+'-'+str(date.day)
ontem=str(date.year)+'-'+str(date.month)+'-'+str(date.day-1)
inicio_mes=str(date.year)+'-'+str(date.month)+'-'+str(1)
print(hoje)

f=open("stocks_list.txt","r")
f2=open("stocks2_list.txt","w")

#stock=yf.download('IRBR3.SA',start=inicio_mes,end=hoje,progress=False)
tickers=[];
#tickers.append("IRBR3.SA")
#tickers.append("CIEL3.SA")

"""
returns:
              Open    High    Low    Close      Volume  Dividends  Splits
Date
1986-03-13    0.06    0.07    0.06    0.07  1031788800        0.0     0.0
1986-03-14    0.07    0.07    0.07    0.07   308160000        0.0     0.0
...
2019-04-15  120.94  121.58  120.57  121.05    15792600        0.0     0.0
2019-04-16  121.64  121.65  120.10  120.77    14059700        0.0     0.0
"""
def up5d(tickers):#procura subida constante de 5 dias seguidos
        table=PrettyTable(['Stock','Inicio','Fim'])
        for t in tickers:
                stock=yf.Ticker(t)
                hist=stock.history(period='5d')
                i=0
                ant=0;
                low=0
                high=0
                #print(stock)
                for t2 in hist.Close:
                        close=t2
                        #print(close)
                        if ant<=close:
                                i=i+1
                        ant=close
                if i==5:
                        #print(t+" | "+str(hist.Close[0])+" | "+str(hist.Close[4]))
                        table.add_row([t,round(hist.Close[0],2),round(hist.Close[4],2)])
        print(table)

def var100(tickers):#procura variação de 100% ou mais nos ultimos 30 dias
        table=PrettyTable(['Stock','low','high','Close'])
        for t in tickers:
                stock=yf.Ticker(t)
                hist=stock.history(period='30d')
                high=0
                low=999999
                l=999999999
                h=0
                #print(stock)
                for i in range(0,hist.Low.size):
                        #if hist.Low[i].size > 0:
                        l=hist.Low[i]
                        h=hist.High[i]
                        if low<l:
                                low=l
                        if high>h:
                                high=h
                var=((high-low)/low)*100
                if var>=100:
                        #print(t+" | "+low+" | "+high+" | "+str(hist.Close[29]))
                        table.add_row([t,round(low,2),round(high,2),str(round(hist.Close[29],2))])
        print(table)


def var30d(tickers):
        table=PrettyTable(['Stock','low','high','Close'])
        for t in tickers:
                stock=yf.Ticker(t)
                hist=stock.history(period='1d')
                high=0
                low=999999
                #print(stock)
                high=(hist.High)
                low=(hist.Low)
                if(low>0):
                        var=((high-low)/low)*100.00
                else:
                        var=1
                if var>=30:
                        table.add_row([t,round(low,2),round(high,2),str(round(hist.Close[0],2))])
        print(table)

def queda5d(tickers):
        table=PrettyTable(['Stock','Inicio','Fim'])
        for t in tickers:
                stock=yf.Ticker(t)
                hist=stock.history(period='5d')
                i=0
                ant=0;
                low=0
                high=0
                #print(stock)
                for t2 in hist.Close:
                        close=t2
                        #print(close)
                        if ant>=close:
                                i=i+1
                        ant=close
                if i==5:
                        #print(t+" | "+str(hist.Close[0])+" | "+str(hist.Close[4]))
                        table.add_row([t,round(hist.Close[0],2),round(hist.Close[4],2)])
        print(table)

def queda30(tickers):
        table=PrettyTable(['Stock','low','high','Close'])
        for t in tickers:
                stock=yf.Ticker(t)
                hist=stock.history(period='30d')
                high=0
                low=999999
                l=999999999
                h=0
                #print(stock)
                for i in range(0,hist.Low.size):
                        #if hist.Low[i].size > 0:
                        l=hist.Low[i]
                        h=hist.High[i]
                        if low<l:
                                low=l
                        if high>h:
                                high=h
                var=((high-low)/low)*100
                if var>=100 and hist.Close[0] > hist.Close[29]:
                        #print(t+" | "+low+" | "+high+" | "+str(hist.Close[29]))
                        table.add_row([t,round(low,2),round(high,2),str(round(hist.Close[29],2))])
        print(table)


for st in f:
        tickers.append(st.strip('\n'))

menu=0
while menu!=-1:
        if menu==1:
                print("5 dias de subida seguida:")
                up5d(tickers)
        if menu==2:
                print("variacao de 100%")
                var100(tickers)
        if menu==3:
                print("variacao 30% ")
                var30d(tickers)
        if menu==4:
                print("variação de queda 5d: ")
                queda5d(tickers)
        if menu==8:
            for stock in tickers:
                kp=yf.Ticker(stock)
                aux=kp.history(period="5d")
                if aux.empty == False:
                    f2.write(stock+'\n')

        print("5 dias de subida: 1")
        print("variacao de 100 em 30 dias: 2")
        print("variacao de 30 em 1 dia: 3")
        print("variação de queda 5d: 4")
        print("valida stocks: 8")

        menu=int(input("escolha sua opção\n"))

f.close()
f2.close()