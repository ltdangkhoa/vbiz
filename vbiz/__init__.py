"""
vbiz.py
"""
INPUT_PATH = '.'
TEMP_FILE = 'temp.txt'


def let_rock():
    """let_rock"""
    import os
    import subprocess

    result_file_name = os.path.basename(os.getcwd()) + '.txt'
    result_file = open("../" + result_file_name, "w")
    for filename in os.listdir(INPUT_PATH):
        print('📂 %s' % (filename))
        file_name, file_ext = os.path.splitext(filename)
        del file_name
        if file_ext == '.pdf':
            subprocess.check_output(
                ['pdf2txt.py', '-o', '../' + TEMP_FILE, filename])
            _f = open('../' + TEMP_FILE, 'r')
            inputs = _f.readlines()

            result = solution(inputs)
            len_result = len(result)
            if len_result > 0:
                str_line = ','.join(map(str, result))
                result_file.write(str_line + '\n')

    result_file.close()


def solution(arr):
    """solution"""
    bad_name = 'cid:'
    phone_key = ('(cid:264)(cid:76)(cid:1227)(cid:81)(cid:3)(cid:87)(cid:75)'
                 '(cid:82)(cid:1189)(cid:76)(cid:29) ')
    email_key = '@'
    results = []
    for i, line in enumerate(arr):
        line = line.replace('\n', '')
        if i == 0 and bad_name not in line:
            results.append(line)
        elif phone_key in line:
            results.append(line.replace(phone_key, ''))
        elif email_key in line:
            results.append(line)

    return results
