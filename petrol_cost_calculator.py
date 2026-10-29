def monthly_fuel_cost(distance_per_day_km, days_per_month, mileage_km_per_litre, price_per_litre):
    monthly_km = distance_per_day_km * days_per_month
    litres = monthly_km / mileage_km_per_litre
    cost = litres * price_per_litre
    return monthly_km, litres, cost


if __name__ == "__main__":
    distance = float(input("Distance you drive daily (km): "))
    days = int(input("Days you drive per month (e.g. 30): "))
    mileage = float(input("Your car/bike mileage (km per litre): "))
    price = float(input("Petrol price per litre (PKR): "))
    km, litres, cost = monthly_fuel_cost(distance, days, mileage, price)
    print(f"Monthly distance: {km:,.0f} km")
    print(f"Petrol needed: {litres:,.1f} litres")
    print(f"Estimated monthly petrol cost: PKR {cost:,.0f}")
