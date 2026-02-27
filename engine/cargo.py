class StarshipCargo:
    def __init__(self, max_mass, max_volume):
        self.max_mass = max_mass
        self.max_volume = max_volume
        
        self.current_mass = 0.0
        self.current_volume = 0.0
        self.power_generation = 0.0
        self.power_drain = 0.0
        
        self.inventory = {} # Keeps track of what we packed

    def pack_item(self, item_id, quantity, item_database):
        if item_id not in item_database:
            print(f"Error: {item_id} does not exist in the database.")
            return False
            
        item = item_database[item_id]
        total_mass = item['mass_kg'] * quantity
        total_volume = item['volume_m3'] * quantity
        
        # 1. Check Limits
        if self.current_mass + total_mass > self.max_mass:
            print(f"PACKING FAILED: Not enough weight capacity for {quantity}x {item['name']}.")
            return False
            
        if self.current_volume + total_volume > self.max_volume:
            print(f"PACKING FAILED: Not enough space (volume) for {quantity}x {item['name']}.")
            return False
            
        # 2. Add to ship
        self.current_mass += total_mass
        self.current_volume += total_volume
        
        # 3. Calculate Power
        power_impact = item.get('power_kw', 0) * quantity
        if power_impact > 0:
            self.power_generation += power_impact
        else:
            self.power_drain += abs(power_impact) # Store drain as a positive number for easy math
            
        # 4. Record in inventory
        if item_id in self.inventory:
            self.inventory[item_id] += quantity
        else:
            self.inventory[item_id] = quantity
            
        print(f"Packed {quantity}x {item['name']}.")
        return True

    def get_ship_status(self):
        power_net = self.power_generation - self.power_drain
        return f"""
        --- SHIP CARGO STATUS ---
        Mass:   {self.current_mass:,.1f} / {self.max_mass:,.1f} kg
        Volume: {self.current_volume:,.1f} / {self.max_volume:,.1f} m^3
        Power:  Generates {self.power_generation} kW | Consumes {self.power_drain} kW
        Net Power: {power_net} kW (Must be >= 0 for systems to run!)
        -------------------------
        """