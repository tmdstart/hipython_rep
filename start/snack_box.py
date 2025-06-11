#간식박스 관리 프로그램
snack_box = ['초보파이', '홈런볼', '하리보젤리']
new_snack=input("먹고싶은 간식을 추가하세요. 단, 쉼표(,)로 연결하세요").split(',')
snack_box += new_snack

snack_box

qty=int(input("간식박스를 몇 세트로 포장할까요? 예2->2box"))
snack_box=snack_box*qty


print(f'주문하신 간식상자는 {snack_box[0]}, {snack_box[1]}, {snack_box[3]} 등입니다 확인하세요')

msg = f'혹시 빼고싶은 간식이 있으면 번호를 입력하세요 (0~{len(snack_box)-1})'
snack_no=int(input(msg))

del snack_box[snack_no]
 
#간식박스프로그램 4
#찾고 싶은 간식번호를 입력하세요
msg = f'찾고싶은 간식 이름을 입력하세요 (0~)'
name=input(msg)
name in snack_box

#간식박스 관리프로그램
snack_name = input('혹시 찾고싶은 간식을 입력하세요')
if snack_name in snack_box : 
    print("있어요")
else:
    print('없어요')

#간식박스 프로그램
print("주문하신 간식박스는 뒤어세버터 다음과 같다.")
print(f'{snack_box[::-1]}, 총 {len(snack_box)} 입니다 ')