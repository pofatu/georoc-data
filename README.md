# georoc-data

This repository provides a zipped SQLite database created with `pygeoroc` from
the downloads provided by the GEOROC database.
See [`INDEX.md`](INDEX.md) for details.

Cite GEOROC as

> Sarbas, B., U.Nohl: The GEOROC database as part of a growing geoinformatics network. In: Brady, S.R., Sinha, A.K., and Gundersen, L.C. (editors): Geoinformatics 2008—Data to Knowledge, Proceedings: U.S. Geological Survey Scientific Investigations Report 2008-5172 (2008), pp. 42/43.

and `pygeoroc` as

> Robert Forkel. (2020, April 9). pofatu/pygeoroc: Programmatic access to GEOROC data. Zenodo. http://doi.org/10.5281/zenodo.3744586


## Workflow

Install `pygeoroc`:
```shell
pip install pygeoroc
```

Download the GEOROC data
```shell
georoc download
```

Create the SQLite database:
```shell
georoc createdb
```

Write a list of errata that were corrected when importing the data into SQLite:
```shell
georoc check 2> errata.log
```

Zip the database for upload:
```
gzip georoc.sqlite
```


## Usage

After unzipping the database, it can be queried using the
[SQLite command line shell](https://sqlite.org/cli.html):

```
sqlite3 georoc.sqlite
...
sqlite>
```

We can - for example - list the 5 references with the highest number of samples:

```sql
select
    count(c.sample_id) as samples, r.reference 
from
    citation as c, reference as r
where 
    r.id = c.reference_id
group by
    r.id, r.reference
order by samples desc limit 5
```

Number of samples | Reference
 ---:| ---
3978|FONTIJN K., MCNAMARA K., TADESSE A. Z., PYLE D. M., DESSALEGN F., HUTCHISON W., MATHER T. A., YIRGU G.:    CONTRASTING STYLES OF POST-CALDERA VOLCANISM ALONG THE MAIN ETHIOPIAN RIFT: IMPLICATIONS FOR CONTEMPORARY VOLCANIC HAZARDS  J. VOLCANOL. GEOTHERM. RES. 356   [2018] 90-113    doi: 10.1016/j.jvolgeores.2018.02.001
3585|SCHINDLBECK-BELO J. C., KUTTEROLF S., STRAUB S. M., ANDREWS G. D. M., WANG KUO-LUNG, MLENECK-VAUTRAVERS M. J.:    ONE MILLION YEARS TEPHRA RECORD AT IODP SITES U1436 AND U1437: INSIGHTS INTO EXPLOSIVE VOLCANISM FROM THE JAPAN AND IZU ARCS  THE ISLAND ARC 27 (E12244)  [2018]    doi: 10.1111/iar.12244
2285|HARTLEY M. E., THORDARSON T., DE JOUX A.:    POSTGLACIAL ERUPTIVE HISTORY OF THE ASKJA REGION, NORTH ICELAND  BULL. VOLCANOL. 78 (28)  [2016]    doi: 10.1007/s00445-016-1022-7
2137|SANTACROCE R., CIONI R., MARIANELLI P., SBRANA A., SULPIZIO R., ZANCHETTA G., DONAHUE D. J., JORON J.-L.:    AGE AND WHOLE ROCK-GLASS COMPOSITIONS OF PROXIMAL PYROCLASTICS FROM THE MAJOR EXPLOSIVE ERUPTIONS OF SOMMA-VESUVIUS: A REVIEW AS A TOOL FOR DISTAL TEPHROSTRATIGRAPHY  J. VOLCANOL. GEOTHERM. RES. 177   [2008] 1-18    doi: 10.1016/j.jvolgeores.2008.06.009
2005|VASILENKO V. B., TOLSTOV A. V., KUZNETSOVA L. G., MININ V. A.:    CHEMICAL COMPOSITION AND DIAMOND POTENTIAL OF KIMBERLITES HAVING EXPERIENCED SECONDARY ALTERATION: NYURBINSKAYA PIPE, EAST SIBERIA  GEOCHEM. INT. 47   [2009] 1075-1082    doi: 10.1134/S0016702909110032
