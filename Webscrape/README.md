# Web Scraping Wikipedia getting data from a particular website to do further analysis.   
This project is getting data from Wikipedia using Python. Particularly, information market capitalization for top companies in the world. Why Wikipedia? Wikipedia is a great source of information and it is free. Besides,
knowing the market capitalization of companies is important for investors to adjust their portfolios.


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages.

NB. You can install the packages in a virtual environment or globally. We used python 3.10 for this example.

### Virtual Environment

```bash
pip install virtualenv
```
## Activate Virtual Environment

```bash
source venv/bin/activate
```

```bash
pip install requests pandas lxml matplotlib seaborn
```

## Usage
We use a Makefile to run the project. The Makefile contains the following commands:

```bash
make install
```
Activate the virtual environment and run the command.

```bash
. .venv/bin/activate
```

This command installs the required packages.

```bash
make run
```
This command runs the project.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
Creative Commons Zero v1.0 Universal

