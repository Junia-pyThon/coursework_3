import utils

operations = utils.selection(utils.operations)

sort_operation = sorted(operations, key=lambda operation: operation["date"], reverse=True)

utils.print_last(sort_operation)

