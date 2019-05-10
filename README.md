# Amazon Books Web Scraper using Python and Pandas
This program will scrape books **from a list of Amazon links (spreadsheet)**. It will generate a **csv** file with book data such as: 
- ASIN
- Name
- Author
- Stars
- ISBN10 and ISBN13 number
- Item category, subcategory and specific category
- Item availability
- Original price and sale price

<!-- ## Table of Contents
- [Usage Example](#usage-example)
- [Getting Started](#getting-started)
- [Running the tests](#running-the-tests)
- [Built With](#built-with)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Acknowledgements](#acknowledgements) -->

---

## Usage Example
**Input links:**

![](./docs/input.jpg)

**Usage:**

![](./docs/usage_new.jpg)

**Repeated links:**
The program can detect if there are repeated books based on its *ASIN number*, these repeated books won't be scraped.

![](./docs/usage_repeated.jpg)

**Output data:**

![](./docs/output.jpg)


## Getting Started
### Prerequisites
- You will need Python

> **IMPORTANT:** To scrape your own Amazon links you have to create a .csv file **with a column header of url** and place it inside the `data` folder with the name of `input.csv`

### Installing


### Running
Run the command line:
```sh
PYTHON_PATH/python.exe "FOLDER_PATH/python-web-scrapper/modules/main.py"
```

<!-- ## Running the tests -->

<!-- 
## Development setup

## Deployment -->

## Important Considerations
- Check out *variables.py* file to modify the desired behavior of the program such as:
    - **Number of desired books to scrape**.
    - Change the name of the input and output files and its directory
- [REGEX filtering queries](./docs/FILTERING.md)
- [Useful web scraping resources](./docs/USEFUL_RESOURCES.md)
- [XPATHS for web scraping Amazon](./docs/xpaths_for_amazon.txt)

## Built With
- Python 3.7
- Pandas

<!-- ## Versioning -->

<!-- ## Release History -->

## Contributing
Please read [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors
- Guido Santillan Arias - [guidosantillan01@gmail.com](guidosantillan01@gmail.com) - [www.guidosantillan.com](www.guidosantillan.com)

## Licence
This project is licensed under the **MIT license** - see the [LICENSE](./LICENSE.txt) file for details.

<!-- ## Acknowledgements
- abc
- abc -->
