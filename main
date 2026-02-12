import json

# --- CONNECTING THE MODULES ---
# From the 'engine' folder, import the 'physics' file
import engine.physics as physics 
# From the 'engine' folder, import the 'life_support' file
import engine.life_support as life_support

# 1. SETUP PHASE
print("Initializing Simulation...")
ship_mass = 50000 # kg
fuel = 120000 # kg

# Use the physics module
delta_v = physics.calculate_thrust(ship_mass, fuel)
print(f"Potential Delta-V: {delta_v:.2f} m/s")

# 2. GAME LOOP (The Trip)
food_stock = 1000 # kg
crew_size = 6

for day in range(1, 10): # Simulate 10 days
    print(f"--- Day {day} ---")
    
    # Use the life_support module
    food_stock, status = life_support.consume_resources(crew_size, food_stock)
    
    if status == "STARVATION":
        print("Mission Failed: Crew died.")
        break
        
    print(f"Food Remaining: {food_stock:.2f} kg")