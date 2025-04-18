# 2~5단 출력
for i in range(1, 10):
    for dan in range(2, 6):
        print(f"{dan} x {i} = {dan * i:2}", end='\t')
    print()

print()  # 한 줄 띄우기

# 6~9단 출력
for i in range(1, 10):
    for dan in range(6, 10):
        print(f"{dan} x {i} = {dan * i:2}", end='\t')
    print()
