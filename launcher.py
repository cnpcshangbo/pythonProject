import subprocess
import logging
import time
import threading


def thread_function(p, name):
    logging.info("Thread %s: starting", name)
    # get output from process "Something to print"
    while True:
        time.sleep(1)
        one_line_output = p.stdout.readline()
        logging.info("Thread %s: running", name)
        logging.info(one_line_output)
        if one_line_output == b"":
            logging.info("Thread %s: finishing", name)
            break


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    p = subprocess.Popen(["python", "1st.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    x = threading.Thread(target=thread_function, args=(p, 1,))
    x.start()
    time.sleep(2)
    # write 'a line\n' to the process
    p.stdin.write('a line\n'.encode())
    p.stdin.flush()  # not necessary in this case
    # get output from process "not time to break"
    # one_line_output = p.stdout.readline()
    # print(one_line_output)

    time.sleep(2)
    # write "n\n" to that process for if r=='n':
    p.stdin.write('n\n'.encode())
    p.stdin.flush()  # not necessary in this case

    # read the last output from the process  "Exiting"
    # one_line_output = p.stdout.read()
    # print(one_line_output)
