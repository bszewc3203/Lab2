import sys
import logging


def read_stdin_data():
    logging.info("Reading from standard input has started")
    largest_path = ""
    largest_size = 0
    fail_count = 0
    size_sum = 0
    req_count = 0

    # Iterating through std input
    for line in sys.stdin:
        str_arr = line.split(" ")
        if len(str_arr) < 6:
            sys.exit(1)
        # strArr[5] is request type
        # strArr[6] is path
        # strArr[8] is http code
        # strArr[9] is size
        req_type = str_arr[5]
        if req_type == "\"GET":
            path = str_arr[6]
            httpCode = str_arr[8]
            size = int(str_arr[9])

            size_sum += size
            if size > largest_size:
                largest_size = size
                largest_path = path

            if httpCode != "404":
                print(path)
            else:
                print(f"!{path}")
                fail_count += 1

            if len(path) > 64:
                logging.debug(f"{path} is a suspiciously long pathname")

            req_count += 1

    logging.info("All data was read successfully")
    return largest_path, largest_size, fail_count, size_sum, req_count


# printing the summary
def print_summary(data):
    logging.info("Printing summary")
    logging.debug(f"print_summary input data has {len(data)} arguments")

    largest_path = data[0]
    largest_size = data[1]
    fail_count = data[2]
    size_sum = data[3]
    req_count = data[4]
    print(f"""\nSUMMARY:
        Path of the largest file: {largest_path}
        Size of the largest file: {largest_size}
        Number of failed requests: {fail_count}
        Total number of bytes sent: {size_sum}
        Total number of kilobytes sent: {size_sum / 1024}
        Mean number of sent bytes: {size_sum / req_count}""")

    logging.info("Printing summary was successful")


if __name__ == '__main__':
    logging.basicConfig(filename='lab2.log', encoding='utf-8', level=logging.INFO)
    logging.info("Program has started executing")

    print_summary(read_stdin_data())

    logging.info("Program has finished executing")

# Logging documentation: https://docs.python.org/3/howto/logging.html
# Logging tutorial: https://docs.python.org/3/howto/logging.html (???)
# Logging cookbook: https://docs.python.org/3/howto/logging-cookbook.html
