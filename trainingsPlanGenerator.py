from prettytable import PrettyTable

MAX = input("Max: ")

table = PrettyTable()
table.field_names = ["Week 1", "Week 2", "Week 3"]

def calculate_cycle(max):
    working_weight = 0.9 * float(max)
    data = [
        "{} x 5\n{} x 5\n{} x 5+\n".format(round(working_weight * 0.65, 2), round(working_weight * 0.75, 2), round(working_weight * 0.85, 2)),
        "{} x 3\n{} x 3\n{} x 3+\n".format(round(working_weight * 0.70, 2), round(working_weight * 0.80, 2), round(working_weight * 0.90, 2)),
        "{} x 5\n{} x 3\n{} x 1+\n".format(round(working_weight * 0.75, 2), round(working_weight * 0.85, 2), round(working_weight * 0.95, 2)),
    ]
    return data

table.add_rows([
    calculate_cycle(MAX),
])

print(table)