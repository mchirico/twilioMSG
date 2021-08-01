from TwilioLib.util.data import TW


def main():
    t = TW()
    result = t.GetList()
    for row in result:
        print(row)

        


if __name__ == "__main__":
    # execute only if run as a script
    main()



