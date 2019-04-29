from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    page = requests.get(
        'https://dangkykinhdoanh.gov.vn/vn/Pages/NganhNghe.aspx', verify=False)
    # print(page.text)
    soup = BeautifulSoup(page.text, 'html.parser')
    tables = soup.find_all('table')
    tables_tr = tables[0].find_all('tr')

    result_file_name = 'category.csv'
    result_file = open(result_file_name, "w")
    result_file_delimeter = ','

    for row in tables_tr:
        tds = row.find_all('td')
        cat_id = tds[3].text.lstrip().rstrip()
        cat_name = tds[5].text.lstrip().rstrip()
        # print(cat_id, cat_name)
        if len(cat_id) == 4:
            print(cat_id, cat_name)
            result_file.write('"' + cat_id + '"' + result_file_delimeter +
                              '"' + cat_name + '"' + '\n')

    result_file.close()
