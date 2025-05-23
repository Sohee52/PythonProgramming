import os
import pickle

filename = 'score.bin'

def input_scores():
    scores = []
    i = 1
    while True:
        score = int(input(f'#{i}? '))
        if score < 0:
            break
        scores.append(score)
        i += 1
    return scores

def get_average(scores):
    total = 0
    for score in scores:
        total += score
    avg = total/len(scores)
    return avg

def show_scores(scores, avg):
    print('\n[점수 출력]')
    print(f'개인 점수: ', end = '')
    for i in range(len(scores)):
        print(f'{scores[i]}', end = ' ')
    print(f'\n평균: {avg:.1f}')

def save_data(scores):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_data():
    with open(filename, 'rb') as file:
        return pickle.load(file)

if os.path.exists(filename):
    scores = load_data()
    avg = get_average(scores)
    print('[파일 읽기]')
    show_scores(scores, avg)
else:
    scores = input_scores()
    avg = get_average(scores)
    show_scores(scores, avg)
    save_data(scores)
    



