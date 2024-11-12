from typing import List, Dict


def employee_statistics_for_list(worker_and_hours: List) -> Dict:
    result = {}
    for i in worker_and_hours:
        name = " ".join(i.split(" ")[:-1])
        hours = i.split(" ")[-1]
        if name in result:
            result[name] += ", " + hours
        else:
            result[name] = hours
    return result


list_worker = ["Андрей В 9", "Василий 11", "Роман 7", "Андрей В 6", "Роман 11"]

if __name__ == "__main__":
    var = 0
    employee_statistics = employee_statistics_for_list(list_worker)
    for k, v in employee_statistics.items():
        print(f"{k}: {v}; sum: {sum([int(i) for i in v.split(", ")])}")
