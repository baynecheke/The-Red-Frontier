import json

import engine

print("Simulation Starting...")

# 1. Open the file in 'read' mode ('r')
with open('data/items.json', 'r') as file:
    # 2. Parse the text into a Python Dictionary
    GAME_ITEMS = json.load(file)

# # 3. Now you can use it like a normal dictionary!
# print(GAME_ITEMS["water_recycler_mk1"]["mass_kg"])

# 1. SETUP PHASE
print("Initializing Simulation...")
max_payload_kg = 100_000.0
max_volume_m3 = 1_000.0
oxygen_kg = 5000.0

fuel = 120000 # kg
food_stock = 1000 # kg
crew_size = engine.crew.select_starting_crew_members(5, 20)
water_supply = 500 # kg

# Use the physics module
delta_v = engine.physics.calculate_thrust(max_payload_kg, fuel)
print(f"Potential Delta-V: {delta_v:.2f} m/s")

# 2. GAME LOOP (The Trip)



for day in range(1, 10): # Simulate 10 days
    print(f"--- Day {day} ---")
    
    # Use the life_support module
    food_stock, water_supply, oxygen_kg, status = engine.life_support.consume_resources(crew_size, food_stock, water_supply, oxygen_kg)
    
    if status == "STARVATION":
        print("Mission Failed: Crew died.")
        break
        
    print(f"Food Remaining: {food_stock:.2f} kg")