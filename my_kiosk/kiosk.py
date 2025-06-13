import time
from function import display_cart, select_pro, pay_deci, end_screen_delay, pay_screen, add_menu

def display_menu():
    print('*' * 40)
    print('어서오세요, ‘요렇게’에 오신 것을 환영합니다:)')
    print("Menu\t\t\t\tPrice")
    print("-" * 30)
    print("요거트 아이스크림(250g)\t3,000")
    print("-" * 30)
    print("\nNo. Topping\t\tPrice")
    print("-" * 30)
    for idx, item in enumerate(menu_list, start=1):
        print(f"{idx:<5} {item['name']:<10}\t{item['price']:,}")
    print("-" * 30)
    print("*" * 40)


# 멤버십 포인트 정보를 저장하는 딕셔너리
membership_dict = {}

# 메뉴 리스트: 이름과 가격 정보를 포함
menu_list = [
    {'name': '바나나', 'price': 4000},
    {'name': '딸기', 'price': 5000},
    {'name': '벌집꿀', 'price': 7000},
    {'name': '그레놀라', 'price': 7000},
    {'name': '초코쉘', 'price': 7000},
    {'name': '요거트 아이스크림', 'price': 3000}
]

def main(membership_dict):
    num_order = 1
    while True:
        display_menu()
        # 기본으로 요거트 아이스크림 1개가 장바구니에 들어감
        cart = [{'name': menu_list[5]['name'], 'price': menu_list[5]['price'], 'quantity': 1}]
        total_price = 3000
        while True:
            display_cart(cart, total_price)
            choice = select_pro()

            if choice == 'o':  # 주문 확정
                break
            elif choice == 'd':  # 메뉴 삭제
                total_price = del_menu(cart, total_price)
            elif choice == 'a':  # 메뉴 추가
                total_price = add_menu(cart, total_price)
            elif choice == 'c':  # 주문 취소
                print("주문이 취소됩니다.")
                end_screen_delay()
                break
            elif choice == '99':  # 관리자 중지 명령
                print("관리자 중지입니다.")
                return
            else:
                print("입력이 올바르지 않습니다.")

        # 주문 취소 or 중지 시 다음 루프로 이동
        if choice in ['c', '99']:
            continue

        # 장바구니 비었을 경우 처리
        if total_price == 0:
            print("장바구니가 비어있습니다.")
            end_screen_delay()
            continue

        # 결제 처리
        while True:
            pay = pay_deci()
            if pay == 'y':
                pay_screen(total_price, num_order)
                num_order += 1
                break
            elif pay == 'n':
                print("결제가 취소되었습니다.")
                break
            else:
                print("y 또는 n을 입력해주세요.")
        end_screen_delay()

# 프로그램 시작
main(membership_dict)