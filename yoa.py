menu_list = [ 
    {'name': '요거트 아이스크림', 'price': 3000},
    {'name': '바나나', 'price': 4000},
    {'name': '딸기', 'price': 5000},
    {'name': '벌집꿀', 'price': 7000},
    {'name': '그레놀라', 'price': 7000},
    {'name': '초코쉘', 'price': 7000},
]

cart = []
default_item = menu_list[0]
cart.append({'name': default_item['name'], 'price': default_item['price'], 'quantity': 1})
total_price = 3000

while True:
    print("\n" + "=" * 40)
    print("현재 장바구니")
    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
    print("-" * 40)
    print(f"Total = {total_price:,}원")

    print("\n메뉴 목록:")
    for i, item in enumerate(menu_list, start=1):
        print(f"{i}. {item['name']} : {item['price']:,}원")

    choice = input("\n추가할 메뉴 번호를 입력하세요 (종료: 0): ").strip()

    if choice == "0":
        break

    if choice.isdigit() and 1 <= int(choice) <= len(menu_list):
        quantity = input("추가할 개수를 입력하세요: ").strip()
        if quantity.isdigit() and int(quantity) > 0:
            selected_item = menu_list[int(choice) - 1]
            qty = int(quantity)
            found = False

            for item in cart:
                if item['name'] == selected_item['name']:
                    item['quantity'] += qty
                    found = True
                    break

            if not found:
                cart.append({'name': selected_item['name'], 'price': selected_item['price'], 'quantity': qty})

            print(f"'{selected_item['name']}' {qty}개가 장바구니에 추가되었습니다.")
            total_price += selected_item["price"] * qty
        else:
            print("올바른 개수를 입력하세요.")
    else:
        print("올바른 메뉴 번호를 입력하세요.")

print("\n" + "=" * 40)
print("현재 장바구니")
for i, item in enumerate(cart, start=1):
    print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
print("-" * 40)
print(f"Total = {total_price:,}원")

print(" - 토핑 완료 1\n - 토핑을 삭제하려면 2\n - 토핑을 추가하려면 3\n")
select = int(input("번호를 입력해주세요 : "))

while True:
    if select == 1:
        print("\n" + "=" * 40)
        print("현재 장바구니")
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
        print("-" * 40)
        print(f"Total = {total_price:,}원")

        print("메뉴를 확정하려면 1")
        print("메뉴를 삭제하려면 2")
        print("메뉴를 추가하려면 3")
        select = int(input("번호를 입력해주세요 : "))
        if select == 1:
            break

    elif select == 2:
        print("\n" + "=" * 40)
        print("현재 장바구니")
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
        print("-" * 40)
        print(f"Total = {total_price:,}원")
        del_no = int(input("삭제할 메뉴의 번호를 골라주세요 : ")) - 1
        total_price -= cart[del_no]["price"] * cart[del_no]["quantity"]
        cart.pop(del_no)
        print("메뉴가 삭제되었습니다.")

        print("\n" + "=" * 40)
        print("현재 장바구니")
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
        print("-" * 40)
        print(f"Total = {total_price:,}원")

        print("이대로 유지하시겠습니까 : 1")
        print("토핑을 더 삭제하시겠습니까? : 2")
        print("메뉴를 추가하시겠습니까 : 3")
        select = int(input("번호를 입력해주세요 : "))

    elif select == 3:
        print("\n메뉴 목록:")
        for i, item in enumerate(menu_list, start=1):
            print(f"{i}. {item['name']} : {item['price']:,}원")
        add_topping = int(input('추가할 토핑 번호를 골라주세요 :')) - 1
        qty = int(input('수량을 선택해주세요 : '))

        selected_item = menu_list[add_topping]
        found = False

        for item in cart:
            if item['name'] == selected_item['name']:
                item['quantity'] += qty
                found = True
                break

        if not found:
            cart.append({'name': selected_item['name'], 'quantity': qty, 'price': selected_item['price']})

        total_price += selected_item['price'] * qty

        print("\n" + "=" * 40)
        print("현재 장바구니")
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
        print("-" * 40)
        print(f"Total = {total_price:,}원")

        print(" - 토핑 완료 1\n - 토핑을 삭제하려면 2\n - 토핑을 추가하려면 3\n")
        select = int(input("번호를 입력해주세요 : "))

print(f"{total_price:,}원 결제하겠습니다. 카드를 삽입해주세요.")