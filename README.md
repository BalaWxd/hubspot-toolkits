# Hubspot toolkits

A few command line for manipulating hubspot objects.

## Dependencies

- [hubspot3](https://github.com/jpetrucciani/hubspot3)
- [Click](http://click.pocoo.org/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [requests]()

## How to use

```
python contacts.py delete --file=path/to/data.txt
python contacts.py delete --vid=8888888
python contacts.py search --vid=8888888
```

## Configuration

- Create a .env file
- Adds below to the file

```
API_KEY=88888888888888888888888888888888
```
