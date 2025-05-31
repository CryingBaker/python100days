from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name","Pokemon Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Charmander","Fire"])
table.align["Pokemon Name"] = "l"

print(table)