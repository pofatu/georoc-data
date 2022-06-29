# Releasing georoc-data

Install `pygeoroc`:
```shell
pip install pygeoroc==2.0.0
```

Download the GEOROC data
```shell
georoc download
```

Write a list of errata that will be corrected when importing the data into SQLite:
```shell
georoc check > errata.log
```

Create the SQLite database:
```shell
georoc createdb --force
```

Save some summary stats in the repos:
```shell
sqlite3 georoc.sqlite .schema > dbschema.sql 
georoc stats > dbstats.md
georoc ls --index --references --samples > INDEX.md
```

Update `README.md`, pasting in the citations for the current set of
datasets:
```shell
georoc ls --citations
``` 

Zip the database for upload:
```
gzip georoc.sqlite
```

Commit, tag, push and release - to Zenodo?.
