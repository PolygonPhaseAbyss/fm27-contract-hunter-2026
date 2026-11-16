"""Data models for the FM 27 Contract Hunter."""

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Contract:
    """A player contract that expires within the analysed window."""

    player_id: int
    player_name: str
    club_name: str
    expiry_date: date
    months_remaining: float


@dataclass
class Player:
    """A football player loaded from the save file."""

    player_id: int
    name: str
    age: int
    position: str
    current_ability: float
    potential_ability: float
    contract_expiry: Optional[date]
    market_value: float


@dataclass
class WonderkidResult:
    """A wonderkid candidate found in the save file."""

    player_id: int
    player_name: str
    club_name: str
    age: int
    potential_ability: float
    current_ability: float
    advantage: float
    market_value: float
