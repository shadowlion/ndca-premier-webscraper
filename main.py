import sys

from project.scripts import find_competitors_for_event, scaffold_competitor_entry_list


def main():
    initial_action = input(
        "Which action would you like to perform?\n"
        "1. Scaffold competitor entry list\n"
        "2. Search for all competitors in an event\n"
        "3. Exit\n",
    )
    filepath = "./output/entries.json"
    match initial_action:
        case "1":
            scaffold_competitor_entry_list(filepath)
            sys.exit(0)
        case "2":
            competitors = find_competitors_for_event(filepath)
            for c in competitors:
                print(c)
            sys.exit(0)
        case "3":
            sys.exit(0)
        case _:
            print("Invalid action!")
            sys.exit(1)


if __name__ == "__main__":
    main()
