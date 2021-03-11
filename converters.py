"""
This python module specifies conversions of raw GEOROC data, when read by pygeoroc.

Two sets of converters can be specified:
- "FIELDS": a `dict` mapping field names (i.e. column names in GEOROC CSV) to converters.
- "COORDINATES": a `dict` mapping CSV file names to a `dict` specifying converters for
  "latitude" and/or "longitude".

A "converter" is a Python callable with the following signature:

    def conv(old, data, fname):
        new = ...
        return new

where
- "old": old value for the respective field in the sample data
- "data": full `dict` of the sample data in one row in the GEOROC CSV
- "fname": name of the GEOROC CSV file containing the row
- return: the new value for "field" in "data"

Some common converters are available from `pygeoroc.errata.CONVERTERS`:
- `pygeoroc.CONVERTERS.upper`: Convert a value to uppercase.
- `pygeoroc.CONVERTERS.positive`: Make sure a value has positive sign.
- `pygeoroc.CONVERTERS.negative`: Make sure a value has negative sign.
"""
from pygeoroc.errata import CONVERTERS

FIELDS = {
    'LAND_OR_SEA': CONVERTERS.upper,
}

COORDINATES = {
    "Convergent_Margins_comp__BISMARCK_ARC_-_NEW_BRITAIN_ARC.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.positive
    },
    "Convergent_Margins_comp__IZU-BONIN_ARC.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.positive
    },
    "Convergent_Margins_comp__KERMADEC_ARC.csv": {
        'latitude': CONVERTERS.negative,
    },
    "Convergent_Margins_comp__LUZON_ARC.csv": {
        'longitude': CONVERTERS.positive
    },
    "Convergent_Margins_comp__MARIANA_ARC.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.positive
    },
    "Convergent_Margins_comp__NEW_CALEDONIA.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': lambda old, data, _: 163.0
        if data['LOCATION'].startswith("NEW CALEDONIA / NEW CALEDONIA / POYA TERRANE")
           and int(old) == -21
        else CONVERTERS.positive(old)
    },
    "Convergent_Margins_comp__NEW_HEBRIDES_ARC_-_VANUATU_ARCHIPELAGO.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.positive,
    },
    "Convergent_Margins_comp__NEW_ZEALAND.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.positive
    },
    "Convergent_Margins_comp__SOLOMON_ISLAND_ARC.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.positive
    },
    "Convergent_Margins_comp__SULAWESI_ARC.csv": {
        'longitude': CONVERTERS.positive
    },
    "Convergent_Margins_comp__TONGA_ARC.csv": {
        'latitude': CONVERTERS.negative,
    },
    "Convergent_Margins_comp__YAP_ARC.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': lambda old, data, _: old
        if ("TONGA ARC / FIJI ISLANDS" in data['LOCATION'])
           or ("TONGA ARC / LAU BASIN" in data['LOCATION'])
        else CONVERTERS.positive(old)
    },
    "Ocean_Island_Groups_comp__AUSTRAL-COOK_ISLANDS.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
    "Ocean_Island_Groups_comp__CAROLINE_ISLANDS.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.positive
    },
    "Ocean_Island_Groups_comp__EASTER_SEAMOUNT_CHAIN_-_SALAS_Y_GOMEZ_RIDGE.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
    "Ocean_Island_Groups_comp__PITCAIRN-GAMBIER_CHAIN.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
    "Ocean_Island_Groups_comp__HAWAIIAN_ISLANDS_part1.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.negative
    },
    "Ocean_Island_Groups_comp__HAWAIIAN_ISLANDS_part2.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.negative
    },
    "Ocean_Island_Groups_comp__HAWAIIAN-EMPEROR_CHAIN.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.negative
    },
    "Ocean_Island_Groups_comp__HAWAIIAN_ARCH_VOLCANIC_FIELDS.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.negative
    },
    "Ocean_Island_Groups_comp__SOCIETY_ISLANDS.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
    "Seamounts_comp__s_SAMOAN_ISLANDS.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
    "Ocean_Island_Groups_comp__SAMOAN_ISLANDS.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
}
