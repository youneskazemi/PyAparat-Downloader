# PyAparat-Downloader

PyAparat-Downloader is a python app for downloading videos with desire quality from [Aparat](https://www.aparat.com).

## requirements

Before usage you need to install some requirements by pip

```commandline
pip install -r requirements.txt
```

## Usage

```python
from pyaparat import Main

m = Main('link', 'quality')
m.download()
```
