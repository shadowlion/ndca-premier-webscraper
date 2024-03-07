import json

from project.classes import NDCACompetition
from project.helpers import find_all_competitors_for_event, write_to_file


def scaffold_competitor_entry_list(write_to: str):
    """
    On the NDCA Premier site, all competitions are marked by an ID (3-digit code?).
    This function will prompt the user to enter the ID of the event they want to
    scaffold the competitor entry list for to get all competitors for the event. The
    data will then be written to a file.

    Args:
        write_to (str): output filepath
    """

    event_id = input("Enter the ID of the event: ")
    comp = NDCACompetition(event_id)
    competitors = find_all_competitors_for_event(comp)
    write_to_file(write_to, competitors)


def find_competitors_for_event(read_from: str) -> list[str]:
    """Given a file with competitor entries, this function will prompt the user to
    enter the name of an event. The function will then return a list of competitors
    that are entered in the event.

    Args:
        read_from (str): filepath to the json file,
        created by the `scaffold_competitor_entry_list` function

    Returns:
        list[str]: list of competitors entered in the event
    """
    event_name = input("Enter the name of the event: ")

    competitors = set()

    with open(read_from, "r") as file:
        data: dict[str, list] = json.loads(file.read())

        for name, entries in data.items():
            for entry in entries:
                for event in entry["Events"]:
                    if event_name in event["Event_Name"]:
                        competitors.add(name)

    return competitors
