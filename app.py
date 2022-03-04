import csvparser

def main():
    try:
        with open('./data/vehicle_events.csv') as file:
            while True:
                row = csvparser.read_row(file)

                if row is None:
                    break

    except Exception as e:
        print({str(e)})
        exit(1)

if __name__ == '__main__':
    main()
