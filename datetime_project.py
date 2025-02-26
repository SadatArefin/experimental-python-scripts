from datetime import datetime, timedelta

# For example, calling format_date(1514665153, "%d-%m-%Y") should output "30-12-2017".
def format_date(timestamp, datetime_format):
    return datetime.fromtimestamp(timestamp).strftime(datetime_format)

# For example, calling calculate_landing_time(datetime(2023, 2, 15), 20) should output "07-03-2023"
def calculate_landing_time(rocket_launch_dt, travel_duration):
    return (rocket_launch_dt + timedelta(days=travel_duration)).strftime("%d-%m-%Y")

# For example, calling days_until_delivery(datetime(2023, 2, 15), datetime(2023, 2, 5)) should output 10
def days_until_delivery(expected_delivery_dt, current_dt):
    return (expected_delivery_dt - current_dt).days

# test cases
print(format_date(1514665153, "%d-%m-%Y"))  # 30-12-2017
print(calculate_landing_time(datetime(2023, 2, 15), 20))  # 07-03-2023
print(days_until_delivery(datetime(2023, 2, 15), datetime(2023, 2, 5)))  # 10