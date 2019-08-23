# `maddata`

The function of this module is simply to download the Maddison dataset in `pandas.DataFrame`. No more than that.

### How to Use
```
import maddata
```
The following will download the dataset in a plain `DataFrame`.
```
maddata.load()
```
There are two options:
* `multi_index=True` (default is `False`) returns a `DataFrame` with `MultiIndex` (`countrycode` and `year` as hierarchical row labels):
```
maddata.load(multi_index=True)
```
* `description=True` (default is `False`) shows variable definitions, irrespective of the value of `multi_index`.
```
maddata.load(description=True)
```

### How to Install
```
$ pip install git+https://github.com/spring-haru/maddata.git
```
or
```
git clone https://github.com/spring-haru/maddata.git
pip install .
```
<br>

**Note:**
Part of this module is built on [this `pyPWT`](https://github.com/jonduan/penn-world-tables), which is forked from the [original `pyPWT`](https://github.com/davidrpugh/penn-world-tables).
