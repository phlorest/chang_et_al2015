# Releasing

- Install in editable mode:
  ```shell
  pip install -e .[test]
  ```
- Re-create the CLDF dataset:
  ```shell
  cldfbench makecldf --glottolog-version v4.7 cldfbench_chang_et_al2015.py --with-zenodo --with-cldfreadme
  ```
- Make sure the CLDF is valid:
  ```shell
  pytest
  ```
- Re-create the README:
  ```shell
  cldfbench readme cldfbench_chang_et_al2015.py
  ```
