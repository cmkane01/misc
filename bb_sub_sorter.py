import os, sys, shutil

def main(dst_dir):

    source_dir = '.'
    os.mkdir("./" + dst_dir)
    netid_set = set()
    file_records = []
    text_files = []
    for fn in os.scandir(source_dir):
        file_record = dict()
        if fn.is_file():
            if fn.name[-3:] == "txt":
                text_files.append(fn.name)
            elif fn.name[-2:] == "py" and fn.name != "bb_sub_sorter.py":
                split_name = fn.name.split("_")
                #print(split_name)
                file_record['fn'] = fn.name
                file_record['aname'] = split_name[0]
                file_record['netid'] = split_name[1]
                netid_set.add(split_name[1])
                file_record['timestamp'] = split_name[3]
                file_record['basename'] = "_".join(split_name[4:])
                #print(file_record)
                file_records.append(file_record)
    print(netid_set)
    print(text_files)
    #print(file_records)
    attempt_records = dict()
    for netid in list(netid_set):
        tf = [fn for fn in text_files if netid in fn].pop()
        files = [f for f in file_records if f['netid'] == netid]
        attempt_records[netid] = (tf, files)
        #print(files)
    for netid in attempt_records.keys():
        print(attempt_records[netid])
        tfd = open(attempt_records[netid][0], 'r')
        lines = tfd.readlines()
        tfd.close()
        full_name = lines[0][6:lines[0].find('(')]
        print(full_name)
        fns = full_name.split()
        print(fns)
        reverse_name = fns[-1] + "".join(fns[:-1])
        print(reverse_name)
        print()
        os.mkdir("./" + dst_dir + "/" + reverse_name)
        for f in attempt_records[netid][1]:
            shutil.copyfile(f['fn'], './' + dst_dir + "/" + reverse_name + "/" + f['basename'])
    print("DONE")
# end def main()

if __name__ == "__main__":
    dst_dir = sys.argv[1] if len(sys.argv) > 1 else "all_attempts"
    main(dst_dir)
