with open('test_7.txt', 'r', encoding='utf-8') as test:
    text = test.readlines()
    profitable = {'name': 'profitable'}
    profits = []
    unprofitable = {'name': 'unprofitable'}

    for subject in text:
        print(subject.split())
        subj_key = subject.split()[1]
        profit = int(subject.split()[2]) - int(subject.split()[3])
        if profit < 0:
            unprofitable.update({subj_key: profit})
        else:
            profits.append(profit)
            profitable.update({subj_key: profit})
    average_profit = {'average_profit': round(int(sum(profits) / len(profits)), 3)}
    total_dict = [profitable, unprofitable, average_profit]
print(total_dict)
