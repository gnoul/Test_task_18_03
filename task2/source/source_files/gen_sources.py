import json
"""
- 1-й источник: ID 1-10,31-40;
- 2-й источник: ID 11-20,41-50;
- 3-й источник: ID 21-30,51-60;
"""


def make_sources():
    sources = {1: (i for j in (range(1, 11), range(31, 41)) for i in j),
               2: (i for j in (range(11, 21), range(41, 51)) for i in j),
               3: (i for j in (range(21, 31), range(51, 61)) for i in j)}

    for i, val in sources.items():
        with open(f'source{i}.json', 'w') as f:
            res = [{"id": j, "Name": f'Test: {i}_{j}'} for j in val]
            json.dump(res, f)


if __name__ == '__main__':
    make_sources()
