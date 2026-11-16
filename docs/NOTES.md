# Developer Notes

## Scope

This tool is a read-only save file reader for Football Manager 27. It lists players with expiring contracts and wonderkid candidates.

## Save File Reader

The tool uses the `fmsave` library to open the `.fm` save file. No custom save parser is used.

## Contract Expiry

Contracts are filtered by the expiry date stored in the save file. The analysis window defaults to 12 months.

## Wonderkid Finder

Wonderkid candidates are players aged up to 21 with a high potential ability compared to the current ability.

## Limitations

Some field meanings may be unconfirmed for certain game builds.
