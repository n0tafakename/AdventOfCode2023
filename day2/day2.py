import sys
import re


def is_game_possible(game):
    true_red = 12
    true_green = 13
    true_blue = 14

    for (r, g, b) in zip(game["reds"], game["greens"], game["blues"]):
        if r > true_red or g > true_green or b > true_blue:
            print(f"Game {game['id']} is NOT possible")
            return False

    print(f"Game {game['id']} IS possible")
    return True


def parse_game(game_str):
    game = {"id": None, "reds": [], "greens": [], "blues": []}

    id_str, rounds_str = game_str.split(":")
    game["id"] = int(re.match(r"^Game (\d+)", id_str).group(1))

    for round_str in rounds_str.split(";"):
        m_red = re.match(r"^.* (\d+) red.*", round_str)
        m_green = re.match(r"^.* (\d+) green.*", round_str)
        m_blue = re.match(r"^.* (\d+) blue.*", round_str)

        game["reds"].append(int(m_red.group(1)) if m_red else 0)
        game["greens"].append(int(m_green.group(1)) if m_green else 0)
        game["blues"].append(int(m_blue.group(1)) if m_blue else 0)

    return game


def part_one(lines):
    result = 0
    for game_str in lines:
        game = parse_game(game_str)

        if is_game_possible(game):
            result += game["id"]

    print(f"Result: {result}")
    return result


def part_two(lines):
    result = 0
    for game_str in lines:
        game = parse_game(game_str)

        result += (max(game["reds"]) * max(game["greens"])
                   * max(game["blues"]))

    print(f"Result: {result}")
    return result


def main():
    lines = None
    with open("./adventofcode.com_2023_day_2_input.txt") as f:
        lines = f.readlines()

    if len(sys.argv) < 2 or sys.argv[1] == "1":
        part_one(lines)
    else:
        part_two(lines)

    return 0


if __name__ == "__main__":
    main()
