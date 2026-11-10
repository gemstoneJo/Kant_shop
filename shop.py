# 영수증 출력 전체루프
def main():
    show_title()
    
    while True:
        choice = menu_choice()
        
        if choice == "1":
            show_products()
            
        elif choice == "2":
            add_product()
        
        elif choice == "3":
            remove_product()
        
        elif choice == "4":
            show_cart()
             
        elif choice == "q":
            break
        
        print()

#상품 클래스
class Product:
    def __init__(self, name, price, stock): #부모 클래스 (가격, 수량, 재고)
        self.name = name
        self.price = price
        self.stock = stock
    
product1 = Product("무선이어폰", 89000, 3)
product2 = Product("텀블러", 15000, 10)
product3 = Product("보조배터리", 32000, 5)
product4 = Product("마우스패드", 9000, 0)
product5 = Product("USB 허브", 18000, 3)

#쿠폰 클래스
# class Discount:
#   def discount_amount(self, total):
#         return 0

#  class RateDiscount(Discount):
#     def 
#  class FixedDiscoount(Discount):
#     def        

# 상품
products = [
    product1,
    product2,
    product3,
    product4,
    product5
]

#장바구니 생성
cart = {}
# 메뉴 
MENUS = {
    "1" : "상품목록",
    "2" : "담기",
    "3" : "빼기",
    "4" : "장바구니",
    "5" : "쿠폰",
    "6" : "결제",
    "q" : "종료",
}

# 첫 화면

def show_title():
    print("-"*56)
    
    for number, menu in MENUS.items():
        print(f"{number}.{menu}",end=" ")     
    print()       
    print("-"*56)
    
# 상품 리스트 출력
def show_products():
    for item in products:
        print(f"{item.name}.{item.price}원 (재고 {item.stock}개)")     
     

# 장바구니 담기
def add_product():
    number = int(input("상품 번호: "))
    item = products[number -1]
    
    if item.stock == 0:
        print("품절된 상품입니다.")
        return
    
    qty = int(input("수량: "))
    
    if qty < 0:
        print("수량은 1개 이상을 입력하세요.")
        return
    # 장바구니에 담은 수량
    already_qty = cart.get(number, 0)
    
    # 추가로 담을 수 있는 수량
    available_qty = item.stock - already_qty
    
    if qty > available_qty:
        print(f"재고가 부족합니다. (담을 수 있는 수량 {available_qty}개)")
        return
        
    # 장바구니 수량 누적
    cart[number] = already_qty + qty
    
    print(f"{item.name} {qty}개를 담았습니다.")
    
    
    print(f"선택한 상품: {item.name}")
    

# 장바구니 빼기
def remove_product():
    number = int(input("뺄 상품 번호: "))
    
    if number not in cart:
        print("장바구니에 없는 상품입니다.")
        return
        
    item = products[number -1]
    
    # 현재 장바구니 수량
    already_qty = cart[number]
    
    print(f"현재 담긴 수량 : {already_qty}개")
    #뺄 수량    
    qty = int(input("뺄 수량: "))
    
    if qty < 0:
        print("뺄 수량은 1개 이상 입력해주세요.")
        return 
    
    if qty > already_qty:
        print(f"수량이 부족합니다. (장바구니에 담긴 수량: {already_qty}개)") 
        return
        
    # 장바구니 수량 차감
    cart[number] = already_qty - qty
    
    print(f"{item.name} {qty}개를 뺐습니다.")
    
    

    
#장바구니 조회
def show_cart():
    if not cart:
        print("장바구니가 비어있습니다.")
        return
    
    total = 0
    
    print("-"*56)
    
    for number, qty in cart.items():
        item = products[number -1]
        
        price = item.price * qty
        total += price
        
        print(f"{item.name} x {qty} = {price:,}원")
    print("-"*56)
    print(f"상품합계 {total:,}원")
        # print(f"할인 )
        # print(f"배송비)
        # print(f"결제 금액 )
    
    
# 메뉴 선택
def menu_choice():
    while True:
        choice = input("선택: ").strip().lower()
        
        
        if choice in ("1", "2", "3", "4", "5", "6", "q"):
            return choice
        
        print("1~6 또는 q를 입력하세요.")
        
        


main()

