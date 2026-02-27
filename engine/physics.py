def calculate_thrust(mass_kg, fuel_kg):
    # Tsiolkovsky rocket equation simplified
    exhaust_velocity = 3500 # m/s for Raptor engine (approx)
    import math
    delta_v = exhaust_velocity * math.log((mass_kg + fuel_kg) / mass_kg)
    return delta_v

def check_weight_limit(current_mass, max_limit):
    if current_mass > max_limit:
        return False, f"OVERWEIGHT: {current_mass - max_limit}kg too heavy!"
    return True, "Weight OK"

def check_volume_limit(current_volume, max_limit):
    if current_volume > max_limit:
        return False, f"OVERVOLUME: {current_volume - max_limit}m³ too much!"
    return True, "Volume OK"