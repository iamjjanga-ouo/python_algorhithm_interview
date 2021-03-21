import sys
from datetime import datetime


if __name__ == '__main__':
    sys.stdin = open('Every_cloud_has_a_silver_lining/input.in', 'r')
    n = int(input())
    from_db = []
    to_db = []

    for _ in range(n):
        use_time = sys.stdin.readline().replace('\n','').split('~') # ['12:00 ', ' 23:59']

        from_time = datetime.strptime(use_time[0].strip(), '%H:%M')
        from_db.append(from_time)

        to_time = datetime.strptime(use_time[1].strip(), '%H:%M')
        to_db.append(to_time)

    max_from_time = max(from_db)
    min_to_time = min(to_db)

    if max_from_time > min_to_time:
        print(-1)
    else:
        print("%d:%02d ~ %d:%02d" % (max_from_time.hour, max_from_time.minute, min_to_time.hour, min_to_time.minute))
