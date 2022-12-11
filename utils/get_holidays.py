from utils.get_base_dir import BASE_DIR

def get_holidays():
    with open(f"{BASE_DIR}/extras/holidays.dat", "r") as f:
        holidays = f.readlines()
        return {holidays.index(line): line.split("\n")[0] for line in holidays}
    