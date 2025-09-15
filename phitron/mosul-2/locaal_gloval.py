balance = 2000
def buy_t_shirt(t_shirt_size, t_shirt_price):
 global balance
 balance = balance - t_shirt_price
 return balance
reseve_money = buy_t_shirt("M", 200)
print(reseve_money)

    
