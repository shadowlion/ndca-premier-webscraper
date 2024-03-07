from dataclasses import dataclass
from typing import Self

import httpx


@dataclass
class NDCACompetition:
    event_id: int

    @property
    def _base_url(self: Self) -> str:
        return "https://www.ndcapremier.com"

    @property
    def event_url(self: Self) -> str:
        return f"{self._base_url}/heatlists/?cyi={self.event_id}"

    def get_competitor_url(self: Self, competitor_id: int) -> str:
        return f"{self._base_url}/feed/heatlists/?cyi={self.event_id}&id={competitor_id}&type=Attendee"

    def get_competitor_entries(self: Self, competitor_id: int) -> dict:
        with httpx.Client() as client:
            url = self.get_competitor_url(competitor_id)
            response = client.get(url)
            return response.json()
