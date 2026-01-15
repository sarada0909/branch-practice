for i in range(16, 30+1):
    # 1-line fizzbuzz on branch rebase-test
    if i%3==0 or i%5==0:
        print('fizz'*(i%3==0)+'buzz'*(i%5==0))
    else:
        print(i)
