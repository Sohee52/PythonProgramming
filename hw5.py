# 사용자 정의 함수
def read_single_digit(digit):
    korean_digits = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    print(korean_digits[int(digit)], end=" ")

def read_number(number):
    length = len(number)
    
    if length == 1:
        read_single_digit(number[0])
    elif length == 2:
        read_single_digit(number[0])
        read_single_digit(number[1])
    elif length == 3:
        read_single_digit(number[0])
        read_single_digit(number[1])
        read_single_digit(number[2])

# 주 프로그램부
num = input("세 자리 수 정수 입력: ")

if num.isdigit() and len(num) <= 3:
    read_number(num)
else:
    print("세 자리 수 이하의 10진 정수를 입력해주세요.")
