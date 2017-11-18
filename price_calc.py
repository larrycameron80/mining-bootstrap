import re
import sys

if len(sys.argv) < 2:
    print("Improper invocation")
    print("python3.5 price_calc.py <coin-name>")

coin_name = sys.argv[1]
input_csv = 'output.csv'
input_prices = 'prices.txt'
report_file = 'report.txt'
vtcPerDay = {}
usdPerDay = {}

with open(input_csv) as fh:
    for line in fh.readlines():
        if re.search('2017', line):
            date, vtc, _ = line.split(',')
            vtcPerDay[date] = vtc

with open(input_prices) as fh:
    for line in fh.readlines():
        if re.search('2017', line):
            date, price = line.split(',')
            usdPerDay[date] = price

template_message_header = "DATE\t\tVTC-MINED\t%s-VALUE-PER-COIN\tTOTAL-USD-VALUE" % coin_name
template_message_barrier = "====\t\t=========\t==================\t==============="
template_message = "{date}\t{vtcmined}\t\t{usdvaluepercoin}\t\t\t{usdvaluetotal}"
message_list = []

for date in vtcPerDay.keys():
    vtc_mined = vtcPerDay[date]
    vtc_mined = float(vtc_mined)
    usd_value_per_vtc = usdPerDay[date]
    total_usd_value = float(vtc_mined) * float(usd_value_per_vtc)
    usd_value_per_vtc = float(usd_value_per_vtc)
    total_usd_value = float(total_usd_value)
    msg = template_message.format(date=date, vtcmined='%0.2f' %vtc_mined, usdvaluepercoin='%0.2f' % usd_value_per_vtc,usdvaluetotal='%0.2f' % total_usd_value)
    message_list.append(msg)

with open(report_file, 'a') as fh:
    fh.write('%s\n' % template_message_header)
    fh.write('%s\n' % template_message_barrier)
    for i in message_list:
        fh.write('%s\n' % i)