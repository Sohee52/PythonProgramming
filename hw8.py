def buy(shopping_bag):
    print('[구입]')
    name = input('상품명? ')
    if name == '':
        return False
    num = int(input('수량은? '))
    print(f'장바구니에 {name} {num}개가 담겼습니다.\n')
    shopping_bag[name] = num

def show(shopping_bag):
    print(f'\n>>> 장바구니 보기: {shopping_bag}')

def find(shopping_bag):
    print('\n[검색]')
    f = input('장바구니에서 확인하고자 하는 상품은? ')
    if f in shopping_bag:
        print(f'{f}은(는) {shopping_bag[f]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {f}은(는) 없습니다.')

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
