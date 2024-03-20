# task 3

import csv
from collections import defaultdict


def read_csv(filename):
    data = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
        return data


def annual_average(data):
    yearly_averages = defaultdict(float)
    yearly_counts = defaultdict(int)
    for row in data:
        year = row['Date'][:4]
        yearly_averages[year] += float(row['Average'])
        yearly_counts[year] += 1
    for year in yearly_averages:
        yearly_averages[year] /= yearly_counts[year]
    return yearly_averages


def overall_stats(data):
    co2_value = [float(row['Average']) for row in data]
    return {
        'Minimum': min(co2_value),
        'Maximum': max(co2_value),
        "Average": sum(co2_value) / len(co2_value)
    }


def seasonal_average(data):
    seasons = {
        'Spring': ('03', '04', '05'),
        'Summer': ('06', '07', '08'),
        'Autumn': ('09', '10', '11'),
        'Winter': ('12', '01', '02')
    }
    seasonal_averages = defaultdict(float)
    seasonal_counts = defaultdict(int)
    for row in data:
        month = row['Data'][5:7]
        co2 = float(row['Average'])
        for season, months in season.items():
            if month in months:
                seasonal_averages[season] += co2
                seasonal_counts[season] += 1
                break
    for season in seasonal_averages:
        seasonal_averages[season] /= seasonal_counts[season]
    return seasonal_averages


def calculate_anomaly(data):
    co2_values = [float(row['Average']) for row in data]
    overall_average = sum(co2_values) / len(co2_values)
    return [(float(row['Average']) - overall_average) for row in data]


def seasonal_average(data):
    pass


if __name__ == "__main__":
    filename = "co2-ppm-daily.csv"
    data = read_csv(filename)
    print("Annual Average:")
    print(annual_average(data))
    print("Overall Stats:")
    print(overall_stats(data))
    print("Seasonal Average:")
    print(seasonal_average(data))
    print("Anomaly:")
    print(calculate_anomaly(data))
