def consume_resources(crew_count, rations_available):
    # NASA Baseline: 0.62kg food per person/day
    required = crew_count * 0.62
    
    if rations_available >= required:
        new_stock = rations_available - required
        return new_stock, "Fed"
    else:
        # Starvation logic
        return 0, "STARVATION"