#!/usr/local/bin/python3

import os
import json
import argparse
import requests


# Request headers
headers = {"Content-Type": "text"}


def get_country_data(country):
    url = "https://api.covid19api.com/total/country/{}/status/confirmed?from=2021-06-01T00:00:00Z&to=2021-12-31T00:00:00Z".format(
        country)

    data = requests.get(url, headers=headers)

    return data.text


def get_data(output_dir, save_all=False):
    print("Pulling data from source ...")
    # Set list of countries
    countries = ['singapore', 'malaysia', 'thailand', 'lao', 'myanmar', 'china', 'viet-nam', 'mongolia', 'philippines']
    # Get last 6 months data for all listed countries
    all_data = []
    for country in countries:
        data = get_country_data(country)
        data = json.loads(data)

        for instance in data:
            all_data.append(instance)

    # Not all countries have data for this time period. Save only those with data.
    if data != []:
        out_path = os.path.join(output_dir, 'covid.json')
        with open(out_path, "w") as out_file:
            json.dump(all_data, out_file, ensure_ascii=True, indent=4)

        print("Pulled and saved data to %s" % out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', dest='out_dir', help='Output directory',
                        metavar='STR', default=os.path.join(os.path.dirname(os.path.realpath(__file__)), "data"))

    (opt_args, args) = parser.parse_known_args()

    get_data(opt_args.out_dir)

