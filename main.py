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
crew_size = engine.crew.select_starting_crew_members(5, 20)

fuel = 120000 # kg
food_stock = 1000 # kg
water_supply = 500 # kg
oxygen_kg = 5000.0




# 2. Setup Phase
print("Initializing Simulation...")
crew_size = engine.crew.select_starting_crew_members(5, 20)

# 3. Packing Phase
print("\n--- PACKING THE STARSHIP ---")
# Create our cargo hold using our new class
ship = engine.cargo.StarshipCargo(max_mass=100_000.0, max_volume=1_000.0)

# Let's pack some items using the IDs from our JSON file!
ship.pack_item("solar_array", 2, GAME_ITEMS)           # Generates 100 kW
ship.pack_item("water_recycler_mk1", 1, GAME_ITEMS)    # Drains 3.5 kW
ship.pack_item("hydroponics_bay", 2, GAME_ITEMS)       # Drains 30 kW

# Try to pack too many nuclear reactors to test the limits!
ship.pack_item("nuclear_kilopower", 100, GAME_ITEMS)   # Will fail due to weight!

# Print the final ship stats
print(ship.get_ship_status())
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
    if status == "DEHYDRATION":
        print("Mission Failed: Crew dehydrated.")
        break
    if status == "OXYGEN_DEPLETION":
        print("Mission Failed: Crew suffocated.")
        break
        
    print(f"Food Remaining: {food_stock:.2f} kg")
    print(f"Water Remaining: {water_supply:.2f} kg")
    print(f"Oxygen Remaining: {oxygen_kg:.2f} kg")