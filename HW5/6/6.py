import re

with open('test_6.txt', 'r', encoding='utf-8') as test:
    schedule = {}
    text = test.readlines()

    for subject in text:
        subj_key = subject.split(':')[0]
        print(subj_key)
        hours = re.findall('\d+', subject)
        subj_val = sum(list(map(lambda x: int(x), hours)))
        schedule.update({subj_key: subj_val})

print(schedule)