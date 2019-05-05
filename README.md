### Dependencies

This package uses [pdfminer.six](https://pypi.org/project/pdfminer.six/) package for parsing pdf file

pip install pdfminer.six

pip install scrapy

### Usage

Change dir to folder which contains .pdf files downloaded from https://bocaodientu.dkkd.gov.vn/

Run command

```
vbiz
```

### Publish package

```
python setup.py sdist bdist_wheel
twine upload dist/*
```

### Install package

Locally
```
pip install .
```

PiPy
```
pip install vbiz
```
