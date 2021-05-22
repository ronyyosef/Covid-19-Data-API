import numpy as np
import requests
import json
from datetime import datetime, timedelta

# The top 5 countries with most recovered per capital, in the last 10 days
# The average recovered cases per 100 square KM per country since the pandemic began
# The top 10 countries recovered cases in the last week


API_BASE = "https://covid-api.mmediagroup.fr/v1"
CASE_BASE = API_BASE + "/cases"
HISTORY_BASE = API_BASE + "/history"
VACCINES_BASE = API_BASE + "/vaccines"

today = datetime.today()
yesterday_date_str = str((today - timedelta(days=1)).date())


def respond(was_error, out_put_data=None):
    return {
        'statusCode': '400' if wasError else '200',
        'body': json.dumps("There was an Error") if wasError else json.dumps(outputData),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def Top_5_countries_with_most_recovered_per_capita_last_10_days(data_dict):
    data_list = []
    x_days_back_date_str = str((today - timedelta(days=10)).date())
    for country in data_dict:
        if country == 'Global':
            continue
        country_dict_date = data_dict[country]["All"]["dates"]
        recovered = country_dict_date[yesterday_date_str] - country_dict_date[x_days_back_date_str]
        try:
            population = data_dict[country]["All"]["population"]
            data_list.append((country, recovered / population))
        except:  # the field population is missing
            continue
    TOP_X = 5
    np_array = np.array(data_list, dtype=[('name', object), ('recovered_per_capital', float)])
    largest_x_index = np.sort(np.argpartition(np_array, -TOP_X, order='recovered_per_capital')[-TOP_X:])
    result_array = np.sort(np_array[largest_x_index], order='recovered_per_capital')[::-1].tolist()
    in_result = {}
    for i in range(TOP_X):
        in_result[i+1] = {
            "country": result_array[i][0],
            "recovered_per_capita": result_array[i][1],
        }
    return in_result


def Average_recovered_cases_per_100_square_KM_per_country(data_dict):
    in_result = {}
    for country in data_dict:
        try:
            sq_km_area = data_dict[country]["All"]["sq_km_area"]
            total_recovered_cases = data_dict[country]["All"]["dates"][yesterday_date_str]
            num_of_100_sq_km_area = sq_km_area/100
            recovered_cases_per_100_square_KM = total_recovered_cases / num_of_100_sq_km_area
            in_result[country] = {"recovered_cases_per_100_square_KM":recovered_cases_per_100_square_KM}
        except: # the field sq_km_area or population is missing
            continue
    return in_result

def The_top_10_countries_recovered_cases_in_the_last_week(data_dict):
    data_list = []
    x_days_back_date_str = str((today - timedelta(days=7)).date())
    for country in data_dict:
        if country == 'Global':
            continue
        country_dict_date = data_dict[country]["All"]["dates"]
        recovered = country_dict_date[yesterday_date_str] - country_dict_date[x_days_back_date_str]
        data_list.append((country, recovered))
    TOP_X = 10
    np_array = np.array(data_list, dtype=[('name', object), ('recovered', float)])
    largest_x_index = np.sort(np.argpartition(np_array, -TOP_X, order='recovered')[-TOP_X:])
    result_array = np.sort(np_array[largest_x_index], order='recovered')[::-1].tolist()
    in_result = {}
    for i in range(TOP_X):
        in_result[i+1] = {
            "country": result_array[i][0],
            "recovered_in_last_week": result_array[i][1],
        }
    return in_result

def lambda_handler(event, context):
    try:
        response = requests.get(HISTORY_BASE, params={"status": "Recovered"})
        data_dict = json.loads(json.dumps(response.json()))
        result_dict = {
            "Top_5_countries_with_most_recovered_per_capita_last_10_days": Top_5_countries_with_most_recovered_per_capita_last_10_days(data_dict),
            "The_average_recovered_cases_per_100_square_KM_per_country": Average_recovered_cases_per_100_square_KM_per_country(data_dict),
            "The_top_10_countries_recovered_cases_in_the_last_week":The_top_10_countries_recovered_cases_in_the_last_week(data_dict)}

        return respond(was_error=False, out_put_data=result_dict)
    except:
        return respond(was_error=True)
