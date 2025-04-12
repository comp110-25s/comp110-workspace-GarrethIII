"""This program is designed to calculate the resources needed for a tea party"""

__author__: str = "730745029"


def tea_bags(people: int) -> int:
    """Determines the number of teabags needed."""
    return people * 2


def treats(people: int) -> int:
    """Determines the number of treats needed."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Determines the cost of the tea and treats."""
    return float(0.5 * (tea_count)) + (0.75 * (treat_count))


def main_planner(guests: int) -> None:
    """Displays information regarding tea, treats, and total cost."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
