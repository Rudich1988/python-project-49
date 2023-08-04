from random import randint
from brain_games.games.all_games import engine
from brain_games.cli import welcome_user


def progression():
    print('Welcome to the Brain Games!')
    hello = welcome_user()
    print('What number is missing in the progression?')
    count = 0
    for i in range(3):
        long_list = randint(5, 10)
        index = randint(0, long_list - 1)
        step = randint(1, 20)
        res_lst = []
        for j in range(long_list):
            if index == j:
                res_lst.append('..')
                continue
            elif j == 0 and index != 0:
                res_lst.append(randint(1,100))
            elif type(res_lst[j - 1]) == int:
                res_lst.append(res_lst[j - 1] + step)
            elif res_lst[j - 1] == '..' and j == 1:
                res_lst.append(randint(1, 100)),
            elif res_lst[j - 1] == '..' and j != 1:
                res_lst.append(res_lst[j - 2] + (step * 2))
        str_res_list = [str(res_lst[k]) for k in range(len(res_lst))]
        final_string = ' '.join(str_res_list)
        result = engine(final_string)
        if result == 'Correct!':
            print(result)
            count += 1
        else:
            print(result)
            print(f"Let's try again, {hello}!")
            break
    if count == 3:
        print(f'Congratulations, {hello}!')


if __name__ == '__main__':
    progression()            
