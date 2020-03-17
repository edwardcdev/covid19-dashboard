# ©Brian Ruiz, @brianruizy
# Created: 03-15-2020
import numpy as np
import pandas as pd
import datetime

# Official general JHU CSSE data repository
daily_report_dir = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'

# Time series files
confirmed_time_series = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
deaths_time_series = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
recovered_time_series = 'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'


def file_date():
    # Returns file_date of most recent date
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime('%m-%d-%Y')
    file_date = yesterday+ '.csv'
    
    return file_date


def daily_report(date_string = None):
    #TODO: Implement date_string arg handling for dynamic daily reports
    raw_data = pd.read_csv(daily_report_dir + file_date())
    df = pd.DataFrame(raw_data)

    return df
