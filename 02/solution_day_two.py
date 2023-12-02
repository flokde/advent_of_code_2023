from typing import List

available_cubes = {"red": 12, "green": 13, "blue": 14}


def check_games(input_array: List[str]) -> int:

    sum = 0
    for game in input_array:
        game_possible = True
        game_id, outcome = game.split(": ")
        for draw in outcome.split("; "):
            for cubes in draw.split(", "):
                num, color = cubes.split()
                if int(num) > available_cubes[color]:
                    game_possible = False
        if game_possible:
            sum += int(game_id.split()[-1])

    return sum


def minimal_games(input_array: List[str]) -> int:

    sum = 0
    for game in input_array:
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        game_id, outcome = game.split(": ")
        for draw in outcome.split("; "):
            for cubes in draw.split(", "):
                num, color = cubes.split()
                min_cubes[color] = max(min_cubes[color], int(num))

        sum += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
    return sum


if __name__ == "__main__":
    with open("input", "r") as file:
        input_array = file.read().splitlines()

    result_1 = check_games(input_array)
    print(result_1)

    result_2 = minimal_games(input_array)
    print(result_2)
