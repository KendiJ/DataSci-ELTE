from dataclasses import dataclass
from typing import List


# 1️⃣ Function that takes a value and returns a name as a string
def get_name(value: int) -> str:
    names = {
        1: "Sedan",
        2: "SUV",
        3: "Truck",
        4: "Coupe"
    }
    return names.get(value, "Unknown")


# 2️⃣ Structure State (id, state)
@dataclass
class State:
    id: int
    state: str  # e.g., "good", "flat"


# 3️⃣ Structure Wheel (id, state)
@dataclass
class Wheel:
    id: int
    state: State


# 4️⃣ Structure Car
@dataclass
class Car:
    car_type: str
    wheels: List[Wheel]
    number_of_passengers: int
    passenger_ids: List[int]
    consumption: float  # fuel consumption (e.g., liters per 100km)

if __name__ == "__main__":
    # Create states
    good_state = State(id=1, state="good")
    flat_state = State(id=2, state="flat")

    # Create wheels
    wheel1 = Wheel(id=101, state=good_state)
    wheel2 = Wheel(id=102, state=good_state)
    wheel3 = Wheel(id=103, state=good_state)
    wheel4 = Wheel(id=104, state=flat_state)

    wheels = [wheel1, wheel2, wheel3, wheel4]

    # Create car
    car = Car(
        car_type=get_name(1),
        wheels=wheels,
        number_of_passengers=3,
        passenger_ids=[201, 202, 203],
        consumption=6.5
    )

    print(car)


# The course outline
# The root function