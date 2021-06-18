import json
import csv

if __name__ == '__main__':
    with open('data.json') as json_file:
        stores = json.load(json_file)["stores"]
    with open('stores.csv', 'w', newline='') as csvfile:
        check = False
        for s in stores:
            del s['isMyStore']
            del s['capuEnabled']
            del s['setStoreUrl']
            del s['custom']
            s['postalCode'] = str("=\"" + s['postalCode'] + "\"")
            s.pop('image', None)
            del s['gmbMapsURL']
            del s['distance']
            del s['inventoryListId']
            if 'storeHours' in s:
                del s['storeHours']

            if check is False:
                w = csv.DictWriter(csvfile, stores[0].keys())
                w.writeheader()
                check = True
            w.writerow(s)



