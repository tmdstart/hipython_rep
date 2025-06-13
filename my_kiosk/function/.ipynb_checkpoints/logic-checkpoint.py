
import time
menu_list = [
    {'name': '바나나', 'price': 4000},
    {'name': '딸기', 'price': 5000},
    {'name': '벌집꿀', 'price': 7000},
    {'name': '그레놀라', 'price': 7000},
    {'name': '초코쉘', 'price': 7000},
    {'name': '요거트 아이스크림', 'price': 3000}
]

membership_dict = {}

# 유효한 숫자 입력을 받기 위한 함수
def get_valid_number_input(msg, min_no = 1, max_no = 5):
    try:
        number = int(input(msg))
        if number < min_no:
            print(f"{min_no} 이상 숫자를 입력하세요")
            return None
        elif number > max_no:
            print(f"{max_no} 이하 숫자를 입력하세요")
            return None
        else:
            return number
    except ValueError:
        print("숫자를 입력하세요")
        return None
# 유효한 전화번호인지 확인하기 위한 함수
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 11 and phone.startswith('010')

# 장바구니 상태를 보여주는 함수
def display_cart(cart, total_price):
    print("\n" + "=" * 40)
    print("현재 장바구니")
    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
    print("-" * 40)
    print(f"Total = {total_price:,}원")

# 토핑을 장바구니에 추가하는 함수
def add_menu(cart, total_price):
    current_total = sum(item['quantity'] for item in cart)
    remaining = 16 - current_total  # 최대 15개까지 가능

    if remaining <= 0:
        print("장바구니에는 최대 16개까지만 담을 수 있습니다.")
        return total_price

    print("\n메뉴 목록:")
    for i, item in enumerate(menu_list, start=1):
        print(f"{i}. {item['name']} : {item['price']:,}원")
    idx = get_valid_number_input("추가할 토핑 번호를 골라주세요 : ", 1, len(menu_list))
    if idx:
        idx -= 1
        qty = get_valid_number_input(f"수량을 선택해주세요 (남은 수량: {remaining}) : ",1,remaining)
        if qty:
            selected_item = menu_list[idx]
            # 기존에 있던 토핑이면 수량만 증가
            for item in cart:
                if item['name'] == selected_item['name']:
                    item['quantity'] += qty
                    break
            else:
                # 새로운 항목 추가
                cart.append({'name': selected_item['name'], 'quantity': qty, 'price': selected_item['price']})
            total_price += selected_item['price'] * qty
    return total_price

# 장바구니에서 메뉴를 삭제하는 함수
def del_menu(cart, total_price):
    if not cart:
        print("장바구니가 비어 있어 삭제할 수 없습니다.")
        return total_price
    display_cart(cart, total_price)
    idx = get_valid_number_input("삭제할 메뉴의 번호를 골라주세요 : ",1,len(cart))
    if idx:
        idx -= 1
        item = cart[idx]
        print(f"'{item['name']}'의 현재 수량: {item['quantity']}")
        del_qty = get_valid_number_input("몇 개를 삭제하시겠습니까? : ", 1, item['quantity'])
        if del_qty:
            item['quantity'] -= del_qty
            if item['quantity'] == 0:
                cart.pop(idx)
            total_price -= item['price'] * del_qty
            print(f"'{item['name']}' {del_qty}개가 삭제되었습니다.")
    return total_price

# 사용자 명령 입력 받기
def select_pro():
    print("메뉴를 확정하려면 o")
    print("메뉴를 삭제하려면 d")
    print("메뉴를 추가하려면 a")
    print("메뉴를 취소하려면 c")
    return input("알파벳을 입력해주세요 : ").lower().strip()

# 결제 여부 확인
def pay_deci():
    return input("주문이 확정되었습니다. 결제를 하시겠습니까? (y/n): ").lower().strip()

# 결제 화면 및 포인트 처리
def pay_screen(total_price, num_order):
    phone = None
    used_point = 0

    while True:
        use_point = input("포인트를 사용하시겠습니까? (y/n): ").lower().strip()
        if use_point == 'y':
            total_price, used_point, phone = use_membership_point(total_price)
            break
        elif use_point == 'n':
            break
        else:
            print("y 또는 n을 입력해주세요.")
    
    print(f"{total_price:,}원 결제하겠습니다. 카드를 삽입해주세요.")
    print("결제가 완료되었습니다.")
    
    if used_point == 0:
        while True:
            mem = input("포인트 적립 하시겠습니까? (y/n): ").lower().strip()
            if mem == 'y':
                membership_point_save(total_price, phone)
                break
            elif mem == 'n':
                break
            else:
                print("y 또는 n을 입력해주세요.")
    else:
        print("포인트를 사용하셨기 때문에 이번 결제는 적립되지 않습니다.")
        
    print(f"주문번호는 {num_order}번 입니다.")

# 포인트를 적립할 때 사용하는 함수
def membership_point_save(total_price, phone=None):
    while not phone or not is_valid_phone(phone):
        phone = input("전화번호를 입력해주세요 (- 없이): ").replace(" ", "")
        if not is_valid_phone(phone):
            print("올바른 형식의 전화번호(예: 01012345678)를 입력해주세요.")
    points = int(total_price * 0.1)

    if phone in membership_dict:
        membership_dict[phone] += points
        print(f"{phone} 번호에 {points}포인트가 추가되어, 총 {membership_dict[phone]}포인트가 있습니다.")
    else:
        membership_dict[phone] = points
        print(f"{phone} 번호로 {points}포인트가 새로 적립되었습니다.")

# 포인트 사용 시 사용하는 함수 
def use_membership_point(total_price):
    while True:
        phone = input("전화번호를 입력해주세요 (- 없이): ").replace(" ", "")
        if not is_valid_phone(phone):
            print("올바른 형식의 전화번호(예: 01012345678)를 입력해주세요.")
            continue
        break
    if phone not in membership_dict:
        print("해당 번호로 적립된 포인트가 없습니다.")
        return total_price, 0, phone  # 사용된 포인트 없음

    available = membership_dict[phone]
    print(f"현재 {available}포인트가 있습니다.")
    while True:
        try:
            used_point = int(input("사용할 포인트를 입력해주세요: "))
            if used_point > available:
                print("포인트가 부족합니다.")
            elif used_point > total_price:
                print("결제 금액보다 많은 포인트는 사용할 수 없습니다.")
            elif used_point < 0:
                print("음수 포인트를 사용할 수 없습니다.")
            else:
                membership_dict[phone] -= used_point
                total_price -= used_point
                print(f"{used_point}포인트를 사용하여 {total_price}원을 결제합니다.")
                return total_price, used_point, phone
        except ValueError:
            print("숫자를 입력해주세요.")


# 초기화면으로 돌아가기 전 5초 대기
def end_screen_delay():
    print("초기화면으로 돌아갑니다.")
    for i in range(5, 0, -1):
        print(f"{i} ", end='\r', flush=True)
        time.sleep(1)
    print(" ", end='\r')