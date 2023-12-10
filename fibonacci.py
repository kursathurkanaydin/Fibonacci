fibonacciList=list()
def fibonacci(n):
    sonuc=int()
    if(n>0):
        if(n>2):
            sonuc=fibonacci(n-1)+fibonacci(n-2)
            return sonuc
        else:
            return 1
def fibonacciEkle(x):
    if(x>1):
        fibonacciEkle(x-1)
    fibonacciList.append(fibonacci(x))
sayı=int(input("Dizinin kaç elemenalı olmasını istediğiniz giriniz: "))
fibonacciEkle(sayı)
print(fibonacciList)
