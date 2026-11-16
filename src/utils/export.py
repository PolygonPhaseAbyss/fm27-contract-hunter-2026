"""Export helpers for the FM 27 Contract Hunter."""

import csv
from typing import List

from core.models import Contract, WonderkidResult


def export_contracts_to_csv(file_path: str, contracts: List[Contract]) -> None:
    """Write expiring contracts to a CSV file."""
    with open(file_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Player ID", "Player Name", "Club", "Expiry Date", "Months Remaining"])
        for contract in contracts:
            writer.writerow(
                [
                    contract.player_id,
                    contract.player_name,
                    contract.club_name,
                    contract.expiry_date.isoformat(),
                    f"{contract.months_remaining:.2f}",
                ]
            )


def export_wonderkid_results_to_csv(file_path: str, results: List[WonderkidResult]) -> None:
    """Write wonderkid candidates to a CSV file."""
    with open(file_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Player ID", "Player Name", "Club", "Age", "PA", "CA", "Advantage", "Market Value"])
        for result in results:
            writer.writerow(
                [
                    result.player_id,
                    result.player_name,
                    result.club_name,
                    result.age,
                    f"{result.potential_ability:.2f}",
                    f"{result.current_ability:.2f}",
                    f"{result.advantage:.2f}",
                    f"{result.market_value:.2f}",
                ]
            )
