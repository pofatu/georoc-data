# georoc-data

This repository provides a zipped SQLite database created with 
[`pygeoroc`](https://pypi.org/project/pygeoroc/2.0.0/) from
precompiled datasets of [GEOROC data provided by DIGIS](https://data.goettingen-research-online.de/dataverse/digis).
See [`INDEX.md`](INDEX.md) for details.

Cite GEOROC as

> DIGIS Team, 2022, "GEOROC Compilation: Archaean Cratons", https://doi.org/10.25625/1KRR1P, GRO.data, V3

> DIGIS Team, 2022, "GEOROC Compilation: Complex Volcanic Settings", https://doi.org/10.25625/1VOFM5, GRO.data, V3

> DIGIS Team, 2022, "GEOROC Compilation: Continental Flood Basalts", https://doi.org/10.25625/WSTPOX, GRO.data, V3

> DIGIS Team, 2022, "GEOROC Compilation: Convergent Margins", https://doi.org/10.25625/PVFZCE, GRO.data, V3

> DIGIS Team, 2022, "GEOROC Compilation: Intraplate Volcanic Rocks", https://doi.org/10.25625/RZZ9VM, GRO.data, V3

> DIGIS Team, 2022, "GEOROC Compilation: Ocean Basin Flood Basalts", https://doi.org/10.25625/AVLFC2, GRO.data, V3

> DIGIS Team, 2022, "GEOROC Compilation: Ocean Island Groups", https://doi.org/10.25625/WFJZKY, GRO.data, V3

> DIGIS Team, 2022, "GEOROC Compilation: Oceanic Plateaus", https://doi.org/10.25625/JRZIJF, GRO.data, V3

> DIGIS Team, 2022, "GEOROC Compilation: Rift Volcanics", https://doi.org/10.25625/KAIVCT, GRO.data, V3

> DIGIS Team, 2022, "GEOROC Compilation: Seamounts", https://doi.org/10.25625/JUQK7N, GRO.data, V3

and `pygeoroc` as

> Robert Forkel. (2022). pofatu/pygeoroc: Programmatic access to GEOROC data (v2.0.0). Zenodo. https://doi.org/10.5281/zenodo.6778850


## Usage

After unzipping [the database](georoc.sqlite.gz), it can be queried using the
[SQLite command line shell](https://sqlite.org/cli.html):

```shell
$ sqlite3 georoc.sqlite
...
sqlite>
```

To look at the database schema, run `sqlite3 georoc.sqlite .schema` or look at [dbschema.sql](dbschema.sql).

We can - for example - list the 5 references with the highest number of samples running the following SQL query:

```sql
select
    count(c.sample_id) as samples, r.reference 
from
    citation as c, reference as r
where 
    r.id = c.reference_id
group by
    r.id, r.reference
order by samples desc limit 5;
```

Number of samples | Reference
 ---:| ---
3978|FONTIJN K., MCNAMARA K., TADESSE A. Z., PYLE D. M., DESSALEGN F., HUTCHISON W., MATHER T. A., YIRGU G.:    CONTRASTING STYLES OF POST-CALDERA VOLCANISM ALONG THE MAIN ETHIOPIAN RIFT: IMPLICATIONS FOR CONTEMPORARY VOLCANIC HAZARDS  J. VOLCANOL. GEOTHERM. RES. 356   [2018] 90-113    doi: 10.1016/j.jvolgeores.2018.02.001
3585|SCHINDLBECK-BELO J. C., KUTTEROLF S., STRAUB S. M., ANDREWS G. D. M., WANG KUO-LUNG, MLENECK-VAUTRAVERS M. J.:    ONE MILLION YEARS TEPHRA RECORD AT IODP SITES U1436 AND U1437: INSIGHTS INTO EXPLOSIVE VOLCANISM FROM THE JAPAN AND IZU ARCS  THE ISLAND ARC 27 (E12244)  [2018]    doi: 10.1111/iar.12244
2285|HARTLEY M. E., THORDARSON T., DE JOUX A.:    POSTGLACIAL ERUPTIVE HISTORY OF THE ASKJA REGION, NORTH ICELAND  BULL. VOLCANOL. 78 (28)  [2016]    doi: 10.1007/s00445-016-1022-7
2137|SANTACROCE R., CIONI R., MARIANELLI P., SBRANA A., SULPIZIO R., ZANCHETTA G., DONAHUE D. J., JORON J.-L.:    AGE AND WHOLE ROCK-GLASS COMPOSITIONS OF PROXIMAL PYROCLASTICS FROM THE MAJOR EXPLOSIVE ERUPTIONS OF SOMMA-VESUVIUS: A REVIEW AS A TOOL FOR DISTAL TEPHROSTRATIGRAPHY  J. VOLCANOL. GEOTHERM. RES. 177   [2008] 1-18    doi: 10.1016/j.jvolgeores.2008.06.009
2005|VASILENKO V. B., TOLSTOV A. V., KUZNETSOVA L. G., MININ V. A.:    CHEMICAL COMPOSITION AND DIAMOND POTENTIAL OF KIMBERLITES HAVING EXPERIENCED SECONDARY ALTERATION: NYURBINSKAYA PIPE, EAST SIBERIA  GEOCHEM. INT. 47   [2009] 1075-1082    doi: 10.1134/S0016702909110032


## Errata

Some [errata](errata.log) in the raw GEOROC data have been identified and `pygeoroc` provides a mechanism to fix these upon
loading the data into the SQLite database. This mechanism works with the configuration as specified in
[`converters.py`](converters.py).
