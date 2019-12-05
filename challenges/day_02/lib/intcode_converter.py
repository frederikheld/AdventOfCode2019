def intcode_to_list(intcode):
    if intcode == "":
        return []

    return [int(x) for x in intcode.replace(" ", "").replace("\n", "").split(",")]


def list_to_intcode(lst):
    return ",".join(str(x) for x in lst)
