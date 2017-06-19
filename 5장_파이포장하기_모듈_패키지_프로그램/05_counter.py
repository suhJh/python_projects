from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)

print('breakfast: ', breakfast_counter)
print('breakfast sort: ', breakfast_counter.most_common())  # 내림차순으로 반환

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

print('union', breakfast_counter + lunch_counter) # 카운터끼리는 합칠 수 있다. 단, 서로 공통으로 가진 것 중에서 낮은 숫자가 나온다.
print('minus', breakfast_counter - lunch_counter) # 카운터끼리는 뺄 수 있다.
print('intersection', breakfast_counter & lunch_counter)
