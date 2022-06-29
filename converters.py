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
    "2022-06-PVFZCE_BISMARCK_ARC_NEW_BRITAIN_ARC.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.positive
    },
    "2022-06-PVFZCE_IZU-BONIN_ARC.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.positive
    },
    "2022-06-PVFZCE_KERMADEC_ARC.csv": {
        'latitude': CONVERTERS.negative,
    },
    "2022-06-PVFZCE_LUZON_ARC.csv": {
        'longitude': CONVERTERS.positive
    },
    "2022-06-PVFZCE_MARIANA_ARC.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.positive
    },
    "2022-06-PVFZCE_NEW_CALEDONIA.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': lambda old, data, _: 163.0
        if data['LOCATION'].startswith("NEW CALEDONIA / NEW CALEDONIA / POYA TERRANE")
           and int(old) == -21
        else CONVERTERS.positive(old)
    },
    "2022-06-PVFZCE_NEW_HEBRIDES_ARC_VANUATU_ARCHIPELAGO.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.positive,
    },
    "2022-06-PVFZCE_NEW_ZEALAND.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.positive
    },
    "2022-06-PVFZCE_SOLOMON_ISLAND_ARC.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.positive
    },
    "2022-06-PVFZCE_SULAWESI_ARC.csv": {
        'longitude': CONVERTERS.positive
    },
    "2022-06-PVFZCE_TONGA_ARC.csv": {
        'latitude': CONVERTERS.negative,
    },
    "2022-06-PVFZCE_YAP_ARC.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': lambda old, data, _: old
        if ("TONGA ARC / FIJI ISLANDS" in data['LOCATION'])
           or ("TONGA ARC / LAU BASIN" in data['LOCATION'])
        else CONVERTERS.positive(old)
    },
    "2022-06-WFJZKY_AUSTRAL-COOK_ISLANDS.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
    "2022-06-WFJZKY_CAROLINE_ISLANDS.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.positive
    },
    "2022-06-WFJZKY_EASTER_SEAMOUNT_CHAIN_SALAS_Y_GOMEZ_RIDGE.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
    "2022-06-WFJZKY_PITCAIRN-GAMBIER_CHAIN.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
    "2022-06-WFJZKY_HAWAIIAN_ISLANDS_part1.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.negative
    },
    "2022-06-WFJZKY_HAWAIIAN_ISLANDS_part2.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.negative
    },
    "2022-06-WFJZKY_HAWAIIAN-EMPEROR_CHAIN.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.negative
    },
    "2022-06-WFJZKY_HAWAIIAN_ARCH_VOLCANIC_FIELDS.csv": {
        'latitude': CONVERTERS.positive,
        'longitude': CONVERTERS.negative
    },
    "2022-06-WFJZKY_SOCIETY_ISLANDS.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
    "2022-06-JUQK7N_s_SAMOAN_ISLANDS.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
    "2022-06-WFJZKY_SAMOAN_ISLANDS.csv": {
        'latitude': CONVERTERS.negative,
        'longitude': CONVERTERS.negative
    },
}
