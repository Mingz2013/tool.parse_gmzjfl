# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os
import codecs


def do_line(line):
    items = line.split()
    # print items
    if (items[0] >= 'A') and (items[0] <= 'T'):
        # print len(items)
        if len(items) == 3:
            line = items[0] + "," + "," + "," + "," + items[1] + "," + items[2]
            # print line
        else:
            print "error..........."
    elif len(items[0]) == 2:
        # print len(items)
        if len(items) == 2:
            line = "," + items[0] + "," + "," + "," + items[1] + ","
            # print line
        elif len(items) == 3:
            line = "," + items[0] + "," + "," + "," + items[1] + "," + items[2]

            # print line
        else:
            print "error..........."
    elif len(items[0]) == 3:
        # print len(items)
        if len(items) == 2:
            line = "," + "," + items[0] + "," + "," + items[1] + ","
            # print line
        elif len(items) == 3:
            if len(items[1]) == 4 and ("0000" <= items[1] <= "9999"):
                line = "," + "," + items[0] + "," + items[1] + "," + items[2] + ","
            else:
                line = "," + "," + items[0] + "," + "," + items[1] + "," + items[2]
        elif len(items) == 4:
            line = "," + "," + items[0] + "," + items[1] + "," + items[2] + "," + items[3]
            # print line
        else:
            print "error..........."
    elif len(items[0]) == 4:
        # print len(items)
        if len(items) == 2:
            line = "," + "," + "," + items[0] + "," + items[1] + ","
            # print line
        elif len(items) == 3:
            line = "," + "," + "," + items[0] + "," + items[1] + "," + items[2]
            # print line
        # elif len(items) == 4:
        #     line = "," + "," + items[0] + "," + items[1] + "," + items[2] + "," + items[3]
        #     # print line
        else:
            print "error...........%s" % len(items)
    return line


def do_dir(path):
    out_str_csv = ""

    for file_name in os.listdir(path):
        file_path = path + '/' + file_name
        with codecs.open(file_path, encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                l = do_line(line)
                out_str_csv += l + "\n"
        pass
    return out_str_csv


def write_out_csv(path, out_str_csv):
    with codecs.open(path, mode="w", encoding='utf-8') as f:
        f.write(out_str_csv)
    pass


if __name__ == "__main__":
    out_str_csv = do_dir('data')
    write_out_csv("out/out.csv", out_str_csv)
    pass
