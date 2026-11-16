"""Main window for the FM 27 Contract Hunter."""

from typing import List

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox,
)

from core.models import Contract, WonderkidResult
from core.save_reader import get_expiring_contracts, get_wonderkids, load_save
from utils.export import export_contracts_to_csv, export_wonderkid_results_to_csv


class MainWindow(QMainWindow):
    """Main application window with contract and wonderkid tabs."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("FM 27 Contract Hunter")
        self.resize(980, 660)

        self.contracts: List[Contract] = []
        self.wonderkid_results: List[WonderkidResult] = []
        self.status_label = QLabel("No save file selected.")

        self.tab_widget = QTabWidget()
        self.expiring_tab = QWidget()
        self.wonderkid_tab = QWidget()

        self._build_expiring_tab()
        self._build_wonderkid_tab()

        self.setCentralWidget(self.tab_widget)

    def _build_expiring_tab(self) -> None:
        layout = QVBoxLayout(self.expiring_tab)

        button_layout = QHBoxLayout()
        self.select_save_button = QPushButton("Select Save File")
        self.select_save_button.clicked.connect(self.select_save_file)
        self.export_button = QPushButton("Export CSV")
        self.export_button.clicked.connect(self.export_contracts_csv)
        button_layout.addWidget(self.select_save_button)
        button_layout.addWidget(self.export_button)
        button_layout.addStretch(1)
        layout.addLayout(button_layout)

        self.contracts_table = self._build_table(
            ["Player ID", "Player Name", "Club", "Expiry Date", "Months Remaining"]
        )
        layout.addWidget(self.contracts_table)
        layout.addWidget(self.status_label)

    def _build_wonderkid_tab(self) -> None:
        layout = QVBoxLayout(self.wonderkid_tab)

        self.wonderkid_table = self._build_table(
            ["Player ID", "Player Name", "Club", "Age", "PA", "CA", "Advantage", "Market Value"]
        )
        layout.addWidget(self.wonderkid_table)

        button_layout = QHBoxLayout()
        self.export_wonderkid_button = QPushButton("Export CSV")
        self.export_wonderkid_button.clicked.connect(self.export_wonderkid_results_csv)
        button_layout.addWidget(self.export_wonderkid_button)
        button_layout.addStretch(1)
        layout.addLayout(button_layout)

    def _build_table(self, columns: List[str]):
        table = QTableWidget(0, len(columns))
        table.setHorizontalHeaderLabels(columns)
        return table

    def _fill_contracts_table(self) -> None:
        self.contracts_table.setRowCount(len(self.contracts))

        for row, contract in enumerate(self.contracts):
            self.contracts_table.setItem(row, 0, QTableWidgetItem(str(contract.player_id)))
            self.contracts_table.setItem(row, 1, QTableWidgetItem(contract.player_name))
            self.contracts_table.setItem(row, 2, QTableWidgetItem(contract.club_name))
            self.contracts_table.setItem(row, 3, QTableWidgetItem(contract.expiry_date.isoformat()))
            self.contracts_table.setItem(row, 4, QTableWidgetItem(f"{contract.months_remaining:.2f}"))

    def _fill_wonderkid_table(self) -> None:
        self.wonderkid_table.setRowCount(len(self.wonderkid_results))

        for row, result in enumerate(self.wonderkid_results):
            self.wonderkid_table.setItem(row, 0, QTableWidgetItem(str(result.player_id)))
            self.wonderkid_table.setItem(row, 1, QTableWidgetItem(result.player_name))
            self.wonderkid_table.setItem(row, 2, QTableWidgetItem(result.club_name))
            self.wonderkid_table.setItem(row, 3, QTableWidgetItem(str(result.age)))
            self.wonderkid_table.setItem(row, 4, QTableWidgetItem(f"{result.potential_ability:.2f}"))
            self.wonderkid_table.setItem(row, 5, QTableWidgetItem(f"{result.current_ability:.2f}"))
            self.wonderkid_table.setItem(row, 6, QTableWidgetItem(f"{result.advantage:.2f}"))
            self.wonderkid_table.setItem(row, 7, QTableWidgetItem(f"{result.market_value:.2f}"))

    def select_save_file(self) -> None:
        path, _selected_filter = QFileDialog.getOpenFileName(
            self, "Select Football Manager Save", "", "Football Manager Saves (*.fm)"
        )

        if not path:
            return

        try:
            save = load_save(path)
            self.contracts = get_expiring_contracts(save)
            self.wonderkid_results = get_wonderkids(save)
            self._fill_contracts_table()
            self._fill_wonderkid_table()
            self.status_label.setText(
                f"Loaded save: {path}. Expiring contracts: {len(self.contracts)}. Wonderkid candidates: {len(self.wonderkid_results)}."
            )
        except (ValueError, OSError) as error:
            self.status_label.setText(f"Failed to read save file: {error}")

    def export_contracts_csv(self) -> None:
        path, _selected_filter = QFileDialog.getSaveFileName(self, "Export Contracts", "", "CSV Files (*.csv)")

        if not path:
            return

        export_contracts_to_csv(path, self.contracts)
        QMessageBox.information(self, "Export", f"Exported {len(self.contracts)} contracts to {path}.")

    def export_wonderkid_results_csv(self) -> None:
        path, _selected_filter = QFileDialog.getSaveFileName(self, "Export Wonderkid Results", "", "CSV Files (*.csv)")

        if not path:
            return

        export_wonderkid_results_to_csv(path, self.wonderkid_results)
        QMessageBox.information(self, "Export", f"Exported {len(self.wonderkid_results)} wonderkid results to {path}.")
