def load_dict(file_path):
    with open(file_path, "r") as file_in:
        my_dict = dict.fromkeys([line.strip() for line in file_in])
        return my_dict


