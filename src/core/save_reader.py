"""Read-only save file reader for the FM 27 Contract Hunter.

The module wraps the ``fmsave`` library and exposes small helpers that are
used by the UI to list expiring contracts and wonderkid candidates.
"""

from datetime import date
from typing import Any, List, Optional

import fmsave
from fmsave import UnsupportedGameError

from core.models import Contract, WonderkidResult

DEFAULT_EXPIRING_MONTHS = 12
DEFAULT_MAX_WONDERKID_AGE = 21


def load_save(path):
    """Open a Football Manager save file through the fmsave library."""
    try:
        return fmsave.open(str(path))
    except UnsupportedGameError as error:
        raise ValueError(f"Unsupported save file version: {error}") from error
    except (OSError, ValueError) as error:
        raise ValueError(f"Invalid save file: {error}") from error


def get_expiring_contracts(save, months: int = DEFAULT_EXPIRING_MONTHS) -> List[Contract]:
    """Return players whose contract expires within the given month window."""
    results: List[Contract] = []

    for player in _iter_players(save):
        expiry_date = _get_contract_expiry(player)

        if expiry_date is None:
            continue

        months_remaining = _months_between(date.today(), expiry_date)

        if months_remaining < 0 or months_remaining > months:
            continue

        results.append(
            Contract(
                player_id=_get_attribute(player, "player_id", 0),
                player_name=_get_attribute(player, "name", "Unknown"),
                club_name=_get_attribute(player, "club_name", "Unknown"),
                expiry_date=expiry_date,
                months_remaining=months_remaining,
            )
        )

    return results


def get_wonderkids(save, max_age: int = DEFAULT_MAX_WONDERKID_AGE) -> List[WonderkidResult]:
    """Return wonderkid candidates, sorted by potential advantage over current ability."""
    results: List[WonderkidResult] = []

    for player in _iter_players(save):
        age = int(_get_attribute(player, "age", 0))

        if age > max_age:
            continue

        potential = float(_get_attribute(player, "potential_ability", 0.0))
        current = float(_get_attribute(player, "current_ability", 0.0))
        advantage = potential - current

        if advantage <= 0:
            continue

        results.append(
            WonderkidResult(
                player_id=int(_get_attribute(player, "player_id", 0)),
                player_name=_get_attribute(player, "name", "Unknown"),
                club_name=_get_attribute(player, "club_name", "Unknown"),
                age=age,
                potential_ability=potential,
                current_ability=current,
                advantage=advantage,
                market_value=float(_get_attribute(player, "market_value", 0.0)),
            )
        )

    results.sort(key=lambda result: result.advantage, reverse=True)
    return results


def _iter_players(save) -> List[Any]:
    """Return the list of player records stored in the save."""
    players = getattr(save, "players", None)

    if players is None:
        return []

    results: List[Any] = []

    for player in players:
        results.append(player)

    return results


def _get_attribute(record: Any, name: str, default: Any = None) -> Any:
    """Read an attribute from a save record with a fallback value."""
    return getattr(record, name, default)


def _get_contract_expiry(player: Any):
    """Read the contract expiry date from a player record."""
    contract = _get_attribute(player, "contract", None)

    if contract is None:
        return None

    expiry = _get_attribute(contract, "expiry_date", _get_attribute(contract, "expiry", None))

    if expiry is None:
        return None

    if isinstance(expiry, date):
        return expiry

    return date.fromisoformat(str(expiry))


def _months_between(start: date, end: date) -> float:
    """Return the month difference between two dates."""
    return (end - start).days / 30.44
