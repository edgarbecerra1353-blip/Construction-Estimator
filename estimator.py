

#Basic estimator variables
maistro_day_rate = 200
chalan_day_rate = 150



#Estimator arithmetic
daily_labor_cost = maistro_day_rate + chalan_day_rate

#Prompting user for the sake of calculations
days_to_finish = int(input("Cuantos dias se llevara para acabar el trabajo?\n"))

total_labor_cost = days_to_finish * daily_labor_cost

print(total_labor_cost)



#Materials info, starting w/ cement
number_of_bags = int(input("Cuantos bolsas de cemento se ocupan?\n"))

price_per_bag = float(input("Cuanto cuesta cada bolsa de cemento?\n"))

cement_total_cost = number_of_bags * price_per_bag

print("El precio total de cemento es: ", cement_total_cost)