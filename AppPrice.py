import sys
sys.set_int_max_str_digits(0)
def calc_total_price(apple_weight, APPLE_PRICE_KG):
	return apple_weight * APPLE_PRICE_KG

def calc_return(total_price,money_given):
	if money_given < total_price:
		return -1
	return money_given - total_price

def print_return_info(total): #can nhung to tien nao de thoi
 	#500 200 100 50 20 10 5 2 1
	a = [500,200,100,50,20,10,1]
	for i in a:
		count_info = int(total/(i*1000)) #dem so to tien
		total -= i*1000*count_info #so tien con lai
		if count_info != 0:
			print(str(i) + "k: " + str(int(count_info)) + " to")

def main():
	APPLE_PRICE_KG = 20000
	apple_weight = float(input("Enter weight of apples: ")) #So kg tao cua khach
	money_given = int(input("Total money customer give you: ")) #Tien khach hang dua
	
	total_price = calc_total_price(apple_weight, APPLE_PRICE_KG) #tong so tien
	money_return = calc_return(total_price, money_given) #Tien thoi khach

	if(money_return == -1):
		print("Not enough cash")
	else:		
		print("Tien thoi khach la: " + str(money_return))
		print_return_info(money_return)

main()


