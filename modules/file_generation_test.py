from file_generation import read_input_file, filter_asin_from_url_list

test_file_path = './sources/books_url_test.csv'

def test_read_input_file():
    assert read_input_file(test_file_path, 5) == ['https://www.amazon.com/Americana-400-Year-History-American-Capitalism/dp/0399563792', 'https://www.amazon.com/American-Popular-Song-Innovators-1900-1950/dp/0195014456', 
    'https://www.amazon.com/Apprenticeship-Duddy-Kravitz-Mordecai-Richler/dp/0671028472/?tag=ryanholnet-20',
    'https://www.amazon.com/gp/product/0735213658', 'https://www.amazon.com/gp/product/0743249275'
    ]

def test_filter_asin_from_url_list():
    batch = read_input_file(test_file_path, 5)
    assert filter_asin_from_url_list(batch) == ['0399563792', '0195014456', '0671028472', '0735213658', '0743249275']