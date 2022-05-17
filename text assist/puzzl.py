from datetime import datetime

def dt_convert(dt_str, fmt_from='%Y-%m-%d %H:%M:%S', fmt_to='%m/%d %a %H:%M'):
    return datetime.strptime(dt_str, fmt_from).strftime(fmt_to)

today = datetime.now().strftime('%Y-%m-%d')

forecast_today = \
['{} - {}°C'.format(dt_convert(x['dt_txt']), round(x['main']['temp']))
 for x in data['list']
 if x['dt_txt'].startswith(today)
]