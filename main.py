def main():
    set1 = {1,2,4}  # create set
    # set2 = {2,4,3,5,11,13}
    # un = set1.difference(set2)
    # print(un) # 2,3,4
    # ^ XOR true ^ false =>true
    # set1.add(2)
    # print(set1)
    d2 = dict(name="Tom", surname="Due")
    d2["name"] = "Bob"
    for item in d2.items():
        print(item)


if __name__ == '__main__':
    main()
