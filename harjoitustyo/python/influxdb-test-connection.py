from influxdb import InfluxDBClient

def InfluxDBTesting():

    client = InfluxDBClient(host='localhost', port=8086)

    client.create_database('pyexample')

    databases = client.get_list_database()

    print(*databases, sep = "\n") 
    print("\nSelect database\n")
    selectedDB = input(":")

    client.switch_database(selectedDB)

    json_body = [
        {
            "measurement": "brushEvents",
            "tags": {
                "user": "Carol",
                "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
            },
            "time": "2018-03-28T8:01:00Z",
            "fields": {
                "duration": 127
            }
        },
        {
            "measurement": "brushEvents",
            "tags": {
                "user": "Carol",
                "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
            },
            "time": "2018-03-29T8:04:00Z",
            "fields": {
                "duration": 132
            }
        },
        {
            "measurement": "brushEvents",
            "tags": {
                "user": "Carol",
                "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
            },
            "time": "2018-03-30T8:02:00Z",
            "fields": {
                "duration": 129
            }
        }
    ]

    choice = input("Write example data? (yes/no)\n:")
    if choice == "yes":
        client.write_points(json_body)
    else:
        pass

    choice = input("Print data? (yes/no)\n:")
    if choice == "yes":
        results = client.query('SELECT "duration" FROM "pyexample"."autogen"."brushEvents" GROUP BY "user"')
        rawResults = results.raw

        points = results.get_points(tags={'user':'Carol'})
        for point in points:
            print("Time: %s, Duration: %i" % (point['time'], point['duration']))
    else:
        pass

def main():
    InfluxDBTesting()

if __name__ == '__main__':
    print('InfluxDB testing...')
    main()