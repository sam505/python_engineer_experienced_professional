The instructions below should work on a linux based OS.

## Setting up Virtual Environment

```bash
python3 -m venv venv
```

## Activate the virtual environment
```bash
source venv/bin/activate
```

## Installing required packages to run the program
```bash
pip3 install -r requirements.txt
```

## Running the program
Before running the program, the values of the data folders can be changed on line `25` and `26` of the `main.py` to match the directories on your PC.

```bash
python3 main.py
```