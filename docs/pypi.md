# PyPI

## Requirements

```bash
pip install --upgrade setuptools wheel twine
```

## Generate distribution archive

```bash
python setup.py sdist bdist_wheel
``` 

## Upload to PyPI

### Testing

```bash
python -m twine upload --repository testpypi dist/*
```

### Production

```bash
python -m twine upload dist/*
```

## Resources

- https://packaging.python.org/tutorials/packaging-projects/
