# 사용자 정의 함수부
def get_integer(prompt):
    res = int(input(prompt))
    return res

def exchange(amount):
    num_500 = amount // 500
    amount = amount % 500
    
    num_100 = amount // 100
    amount = amount % 100
    
    num_50 = amount // 50
    amount = amount % 50
    
    num_10 = amount // 10
    
    print("500원 동전의 개수:", num_500)
    print("100원 동전의 개수:", num_100)
    print("50원 동전의 개수:", num_50)
    print("10원 동전의 개수:", num_10)


# 주 프로그램부
amount = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(amount)
