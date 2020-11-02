""" BlackRock Problem 3 """
line = "Vodafone,STOCK,10|Google,STOCK,15|Microsoft,BOND,15:Vodafone,STOCK,15|Google,STOCK,10|Microsoft,BOND,15"

portfolio = line.split(':')[0]
benchmark = line.split(':')[1]

portfolios = portfolio.split('|')
benchmarks = benchmark.split('|')

portfolio_dict = {}
for asset in portfolios:
    company = asset.split(',')[0]
    assetType = asset.split(',')[1]
    key_portfolio = company + '_' + assetType
    value_portfolio = asset.split(',')[2]
    portfolio_dict[key_portfolio] = value_portfolio

benchmark_dict = {}
for asset in benchmarks:
    company = asset.split(',')[0]
    assetType = asset.split(',')[1]
    key_benchmark = company + '_' + assetType
    value_benchmark = asset.split(',')[2]
    benchmark_dict[key_benchmark] = value_benchmark

print('Portfolio dictionary:', portfolio_dict)
print('Benchmark dictionary:', benchmark_dict, '\n')
output_list = []

for key, value in portfolio_dict.items():
    if key in benchmark_dict.keys():
        diff_value = int(value) - int(benchmark_dict[key])
        if diff_value == 0:
            pass
        elif diff_value < 0:
            output_list.append('BUY,' + key.split('_')[0] + ',' + key.split('_')[1] + ',' + str(abs(diff_value)))
        else:
            output_list.append('SELL,' + key.split('_')[0] + ',' + key.split('_')[1] + ',' + str(abs(diff_value)))
    else:
        output_list.append('SELL,' + key.split('_')[0] + ',' + key.split('_')[1] + ',' + str(value))

for key, value in benchmark_dict.items():
    if key not in portfolio_dict.keys():
        output_list.append('BUY,' + key.split('_')[0] + ',' + key.split('_')[1] + ',' + str(value))

output_list.sort(key=lambda x: (x.split(',')[1], x.split(',')[2]))
for transaction in output_list:
    print(transaction)
