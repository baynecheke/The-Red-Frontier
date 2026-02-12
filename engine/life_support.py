def consume_resources(crew_count, food_stock, water_supply, oxygen_kg):
    water_required_k = 3.5
    calories_required = 3000
    oxygen_required_kg = 0.84

    required = crew_count * calories_required
    water_required = crew_count * water_required_k
    oxygen_required = crew_count * oxygen_required_kg
    #subtract the required from the stock
    water_supply -= water_required
    food_stock -= required
    oxygen_kg -= oxygen_required
    if food_stock < 0:
        return food_stock, water_supply, oxygen_kg, "STARVATION"
    if water_supply < 0:
        return food_stock, water_supply, oxygen_kg, "DEHYDRATION"
    if oxygen_kg < 0:
        return food_stock, water_supply, oxygen_kg,"OXYGEN_DEPLETION"
    else:
        return food_stock, water_supply, oxygen_kg, "OK"
    

    
