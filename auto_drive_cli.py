def run_cli():
    print("Welcome to Auto Driving Car Simulation!\n")

    width, height = map(int, input(
        "Please enter the width and height of the simulation field in x y format:\n"
    ).split())

    field = Field(width, height)
    cars = []

    while True:
        print("\nPlease choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")

        choice = input()

        if choice == "1":
            name = input("Please enter the name of the car:\n")

            x, y, d = input(
                f"Please enter initial position of car {name} in x y Direction format:\n"
            ).split()

            commands = input(f"Please enter the commands for car {name}:\n")

            cars.append(Car(name, int(x), int(y), d, commands))

        elif choice == "2":
            sim = Simulator(field, cars)
            result = sim.simulate()

            print("\nAfter simulation, the result is:")

            for c in result:
                if c.collision:
                    print(f"- {c.name}, collides at ({c.collision[0]},{c.collision[1]}) at step {c.collision[2]}")
                else:
                    print(f"- {c.name}, ({c.x},{c.y}) {c.direction}")

            break
