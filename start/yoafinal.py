import time

menu_list = [ 
    {'name': '바나나', 'price': 4000},
    {'name': '딸기', 'price': 5000},
    {'name': '벌집꿀', 'price': 7000},
    {'name': '그레놀라', 'price': 7000},
    {'name': '초코쉘', 'price': 7000},
    {'name': '요거트 아이스크림', 'price': 3000}
]

num_order = 1

def show_menu():
    print('*' * 40)
    print("어서오세요, ‘요렇게’에 오신 것을 환영합니다:)\n")
    print("Menu\t\t\tPrice\n" + "-" * 30)
    print("요거트 아이스크림(250g)\t3,000")
    print("-" * 30 + "\nNo.  Topping\t\tPrice\n" + "-" * 30)
    for i, item in enumerate(menu_list[:-1], start=1):
        print(f"{i:<5} {item['name']:<10}\t{item['price']:,}")
    print("-" * 30 + "\n" + "*" * 40)

def show_cart(cart, total_price):
    print("\n" + "=" * 40)
    print("현재 장바구니")
    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
    print("-" * 40)
    print(f"Total = {total_price:,}원")

def add_item(cart, total_price):
    show_menu()
    idx = int(input("추가할 토핑 번호를 골라주세요 : ")) - 1
    qty = int(input("수량을 선택해주세요 : "))
    item = menu_list[idx]
    for c in cart:
        if c['name'] == item['name']:
            c['quantity'] += qty
            break
    else:
        cart.append({'name': item['name'], 'price': item['price'], 'quantity': qty})
    return total_price + item['price'] * qty

def delete_item(cart, total_price):
    show_cart(cart, total_price)     
    idx = int(input("삭제할 메뉴 번호를 입력해주세요 : ")) - 1
    if 0 <= idx < len(cart):
        item = cart[idx]
        qty = int(input(f"{item['name']}의 삭제할 수량 : "))
        if qty >= item['quantity']:
            total_price -= item['price'] * item['quantity']
            cart.pop(idx)
        else:
            item['quantity'] -= qty
            total_price -= item['price'] * qty
    return total_price

def countdown():
    for i in range(5, 0, -1):
        print(f"{i}   ", end='\r', flush=True)
        time.sleep(1)
    print("   ", end='\r')

def process_payment(total_price, order_num):
    print(f"{total_price:,}원 결제하겠습니다. 카드를 삽입해주세요.")
    print("결제가 완료되었습니다.")
    print(f"주문번호는 {order_num}번 입니다.")
    return order_num + 1


actions = {
    'a': lambda cart, total_price: add_item(cart, total_price),
    'd': lambda cart, total_price: delete_item(cart, total_price),
    'c': lambda cart, total_price: (print("주문이 취소되었습니다."), countdown(), "break"),
    'o': lambda cart, total_price: (
        print("장바구니가 비어있습니다.") if total_price == 0 else (
            process_payment(total_price, num_order) if input("결제하시겠습니까? (y/n) : ").lower() == 'y' else None,
            countdown(),
            "break"
        )
    ),
    '99': lambda cart, total_price: (print("관리자 종료입니다."), "return")
}




def main():
    global num_order
    while True:
        show_menu()
        cart = [{'name': '요거트 아이스크림', 'price': 3000, 'quantity': 1}]
        total_price = 3000

        while True:
            show_cart(cart, total_price)
            action = input("추가(a) / 삭제(d) / 확정(o) / 취소(c) / 종료(99) : ").lower()
            if action in actions:
                 result = actions[action](cart, total_price)
                 if result == "break":
                       break
                 elif result == "return":
                      return
            else:
                 print("올바른 입력을 해주세요.")

main() 


