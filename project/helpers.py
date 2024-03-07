import json

from playwright.sync_api import sync_playwright

from .classes import NDCACompetition


def find_all_competitors_for_event(comp: NDCACompetition) -> list:
    output = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            print(f"Accessing {comp.event_url}...")
            page.goto(comp.event_url)
            heatlist_list = page.wait_for_selector("#heatlist-list")
            competitors = heatlist_list.query_selector_all("*")
            print(f"{len(competitors)} competitors found!")
            for competitor in competitors:
                # found = False

                if "competitor-A" not in competitor.get_attribute("id"):
                    continue

                id = competitor.get_attribute("id").removeprefix("competitor-A")
                data = comp.get_competitor_entries(id)

                key = f"{data["Result"]["Name"][1]}, {data["Result"]["Name"][0]}"
                print(f"Adding competitor {key}...")
                val = data["Result"]["Entries"]
                output.update({ key: val })

                # if data["Status"] != 1:
                #     raise Exception(f"Failed to get competitor data for {id}!")

                # for entry in data["Result"]["Entries"]:
                #     events = [e["Event_Name"] for e in entry["Events"]]
                #     if event_name in events:
                #         found = True

                # if found:

                #     output.add(f"{data["Result"]["Name"][1]}, {data["Result"]["Name"][0]}")
                #     print(f"Competitor {id} added to output!")
                # else:
                #     print(f"Competitor {id} not in the event. Next...")

            return output
        except Exception as e:
            print(e)
            browser.close()


def write_to_file(filename: str, data: dict):
    with open(filename, "w") as file:
        file.write(json.dumps(data, indent=2))
