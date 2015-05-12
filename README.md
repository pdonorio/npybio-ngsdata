# npybio-ngsdata

Notebook ipython to parse and handle NGS Data for variants.

## Input data

Upload of
[CSV](missing reference),
[TSV](missing reference),
or [VCF](missing reference)

formatted files, already annotated.

A suggested software for annotation is [ANNOVAR](missing reference).

All files should be inside an 'input/' directory available at the same level
of the running notebook.

```
# Clone repo
cd /tmp
git clone https://github.com/pdonorio/npybio-ngsdata.git nbs

# Launch notebook server
docker run -d --name ipy -p 80:8000 -v /tmp/nbs:/home/pydatanalysis/nbs pdonorio/ipynb_data_slides

# visit http://localhost
# username: pydatanalysis, password: workshop
```

## How it works

This notebooks examples help to parse, filter, plot and intersect
annotated variants via python commands.

## Debugging

Download the python code and the package from notebook and execute it via shell.
There will prompt logger prints.
