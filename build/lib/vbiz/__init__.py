"""
vbiz.py
"""

INPUT_PATH = '.'
TEMP_FILE = 'temp.txt'


def let_rock():
    """let_rock"""
    import os
    import subprocess
    import json
    import pkg_resources

    ciddict_file = 'ciddict.json'
    ciddict_filepath = pkg_resources.resource_filename(__name__, ciddict_file)
    with open(ciddict_filepath) as json_file:
        ciddict = json.load(json_file)

    result_file_name = os.path.basename(os.getcwd()) + '.csv'
    result_file = open("../" + result_file_name, "w")

    result_file.write('biz_name,biz_phone,biz_email' + '\n')

    for filename in os.listdir(INPUT_PATH):
        print('📂 %s' % (filename))
        file_name, file_ext = os.path.splitext(filename)
        del file_name
        if file_ext == '.pdf':
            subprocess.check_output(
                ['pdf2txt.py', '-o', '../' + TEMP_FILE, filename])
            _f = open('../' + TEMP_FILE, 'r')
            inputs = _f.readlines()

            result = solution(inputs, ciddict)
            len_result = len(result)
            if len_result > 0:
                str_line = ','.join(map(str, result))
                result_file.write(str_line + '\n')

    result_file.close()


def solution(arr, ciddict):
    """solution"""
    # bad_name = 'cid:'
    phone_key = ('(cid:264)(cid:76)(cid:1227)(cid:81)(cid:3)(cid:87)(cid:75)'
                 '(cid:82)(cid:1189)(cid:76)(cid:29) ')
    email_key = '@'
    results = []
    biz_name = ''
    biz_phone = ''
    biz_email = ''
    for i, line in enumerate(arr):
        line = line.replace('\n', '')
        if i == 0:
            for key in ciddict.keys():
                line = line.replace(key, ciddict[key])
            biz_name = line

        if phone_key in line:
            biz_phone = line.replace(phone_key, '')

        if email_key in line:
            biz_email = line

    if biz_phone != '' or biz_email != '':
        results.extend([biz_name, biz_phone, biz_email])

    return results
