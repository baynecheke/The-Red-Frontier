def select_starting_crew_members(minimum, maximum):
    print("--- CREW SELECTION ---")
    
    while True:
        try:
            # 1. Get input as a string
            user_input = input(f"Enter the number of crew members: {minimum}-{maximum}: ")
            
            # 2. Try to convert to integer
            number_of_crew = int(user_input)
            
            # 3. Add logic checks (optional but recommended)
            if number_of_crew < minimum:
                print(f"You need at least {minimum} crew members!")
                continue # Skip the rest and loop again
            
            if number_of_crew > maximum: # Example limit
                 print(f"That's too many people for one ship! Maximum is {maximum}.")
                 continue

            # 4. If we get here, it's a valid number. Break the loop.
            return number_of_crew

        except ValueError:
            # 5. This runs if they type "five" or "obsidian"
            print(f"Invalid input. Please enter a whole number (e.g., {minimum}-{maximum}).")