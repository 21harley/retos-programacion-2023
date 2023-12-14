def mostrar():
    #for i in range(1, 101):
        # print(
        #     "fizzbuzz" if i % 3 == 0 and i % 5 == 0 else ("fizz" if i % 3 == 0 else ("buzz" if i % 5 == 0 else i ) )
        # )
        
    for n in range(1,101):
        print("Fizz"*(n%3==0)+"Buzz"*(n%5==0) or n)

if __name__ == '__main__':
    mostrar()
