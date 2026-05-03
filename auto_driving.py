from dataclasses import dataclass
from typing import List, Dict, Tuple

DIRECTIONS = ["N", "E", "S", "W"]

MOVE_MAP = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


@dataclass
class Car:
    name: str
    x: int
    y: int
    direction: str
    commands: str
    step_index: int = 0
    active: bool = True
    collision: Tuple[int, int, int] = None  # (x, y, step)


class Field:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def is_valid(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height


class Simulator:
    def __init__(self, field: Field, cars: List[Car]):
        self.field = field
        self.cars = cars

    def rotate_left(self, d):
        return DIRECTIONS[(DIRECTIONS.index(d) - 1) % 4]

    def rotate_right(self, d):
        return DIRECTIONS[(DIRECTIONS.index(d) + 1) % 4]

    def simulate(self):
        step = 0

        while any(c.active and c.step_index < len(c.commands) for c in self.cars):
            step += 1
            positions = {}

            for car in self.cars:
                if not car.active or car.step_index >= len(car.commands):
                    continue

                cmd = car.commands[car.step_index]
                car.step_index += 1

                if cmd == "L":
                    car.direction = self.rotate_left(car.direction)

                elif cmd == "R":
                    car.direction = self.rotate_right(car.direction)

                elif cmd == "F":
                    dx, dy = MOVE_MAP[car.direction]
                    new_x, new_y = car.x + dx, car.y + dy

                    if self.field.is_valid(new_x, new_y):
                        car.x, car.y = new_x, new_y

                # Track positions
                pos = (car.x, car.y)
                if pos not in positions:
                    positions[pos] = []
                positions[pos].append(car)

            # Detect collisions
            for pos, cars in positions.items():
                if len(cars) > 1:
                    for c in cars:
                        c.active = False
                        c.collision = (*pos, step)

        return self.cars
