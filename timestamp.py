import time


def add_timestamp(input_str):
    current_time = time.ctime()

    sep_time = time.strptime(current_time)

    timestamp = time.asctime(sep_time)

    return "[" + timestamp + "] " + input_str


def main():
    print(add_timestamp("test string."))


if __name__ == '__main__':
    main()
