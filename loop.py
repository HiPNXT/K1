def calc_total_price(apple_weight, APPLE_PRICE_KG):
	pass

def calc_return(total_price,money_given):
	pass

def main():
	APPLE_PRICE_KG = 20000
	apple_weight = input("Enter weight of apples: ") #So kg tao cua khach
	money_given = input("Total money customer give you: ") #Tien khach hang dua

	total_price = calc_total_price(apple_weight, APPLE_PRICE_KG) #tong so tien
	money_returnn = calc_return(total_price, money_given) #Tien thoi khach
main()

