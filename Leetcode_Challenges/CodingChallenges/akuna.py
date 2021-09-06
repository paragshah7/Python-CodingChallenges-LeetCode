"""
You are inside question view of Trade Reconciliation - Parsing

3m 42s left

Skip to main content
ALL
1
2
3
1. Trade Reconciliation - Parsing
In order to verify records, Akuna compares information on its own trades against records from third-party exchanges - we call this reconciliation. As a simple example, consider this data. Akuna records show we bought 10 units of product A at 12:01:00, and that we sold 15 units of product B at 12:05:00.:



AKUNA,A,10,12:01:00

AKUNA,B,-15,12:05:00



If the exchange has the same record, that's a perfect reconciliation:



EXCHANGE,A,10,12:01:00

EXCHANGE,B,-15,12:05:00



We trade across multiple exchanges and in much larger volume than this, so sometimes there are missing records on one side called breaks. Breaks can occur on either side - e.g. Akuna has a trade not seen in the exchange's records, or vice versa.



You will be provided input as comma-separated lines of two types:

SOURCE,PRODUCT,QUANTITY,TIMESTAMP        # Represents a trade record.
RECONCILIATION,SOURCE,COUNTERPARTY       # Represents a reconciliation request.
The item's SOURCE is either Akuna or one of many exchanges, notated EXCHANGE#. The PRODUCT, QUANTITY, and TIMESTAMP represent trade information.

On lines representing a trade record (SOURCE,PRODUCT,QUANTITY,TIMESTAMP), return the quantity specified in the trade record.



On lines representing a reconciliation request, return the number of trades belonging to the given SOURCE that aren't matched by the given COUNTERPARTY.



Example 1

Input:

AKUNA,A,10,12:01:00
AKUNA,B,-15,12:05:00
RECONCILIATION,AKUNA,EXCHANGE1
RECONCILIATION,EXCHANGE1,AKUNA
EXCHANGE1,B,-15,12:05:00
EXCHANGE1,B,-20,12:07:00
RECONCILIATION,AKUNA,EXCHANGE1
RECONCILIATION,EXCHANGE1,AKUNA
RECONCILIATION,EXCHANGE2,AKUNA
Output:

10          # quantity 10
-15         # quantity -15
2           # AKUNA has 2 trades unmatched by EXCHANGE1 (input lines 1-2)
0           # EXCHANGE1 has 0 trades unmatched by AKUNA
-15         # quantity -15
-20         # quantity -20
1           # AKUNA has 1 trade unmatched by EXCHANGE1 (input line 1)
1           # EXCHANGE1 has 1 trade unmatched by AKUNA (input line 6)
0           # EXCHANGE2 has no trades, thus 0 unmatched by AKUNA


Language: Python 3
Autocomplete Ready



More
23456789101112131415161718192021222324
import fileinput

class TradeReconciliation:
    def __init__(self):
        super().__init__()
        self.aku = 0
        self.exc1 = 0
        self.exc2 = 0
        self.trade_map = {}

…            #     return int(list_line[2])






if __name__ == "__main__":
Line: 70 Col: 48

Test Results

Custom Input

Run Code

Run Tests

Submit
exc1
"""


import fileinput

class TradeReconciliation:
    def __init__(self):
        self.aku = 0
        self.exc1 = 0
        self.exc2 = 0
        self.trade_map = {}

    def process(self, line: str):
        if line:
            # print('line ----', line)
            list_line = line.split(',')
            if list_line[0] == 'AKUNA':
                if list_line[1] in self.trade_map and int(list_line[2]) == self.trade_map[list_line[1]][0] and list_line[3] == self.trade_map[list_line[1]][1]:
                    self.exc1 -= 1
                else:
                    self.trade_map[list_line[1]] = [int(list_line[2]),list_line[3]]
                    self.aku += 1
                return int(list_line[2])

            # if list_line[0] == 'RECONCILIATION' and list_line[1] == 'AKUNA':
            #     return self.aku
            if list_line[0] == 'RECONCILIATION':
                if list_line[1] == 'AKUNA':
                    return self.aku
                elif list_line[1] == 'EXCHANGE1':
                    return self.exc1
                elif list_line[1] == 'EXCHANGE2':
                    return self.exc2

            if list_line[0] == 'EXCHANGE1':
                if list_line[1] in self.trade_map and int(list_line[2]) == self.trade_map[list_line[1]][0] and list_line[3] == self.trade_map[list_line[1]][1]:
                    self.aku -= 1
                else:
                    self.trade_map[list_line[1]] = [int(list_line[2]),list_line[3]]
                    self.exc1 += 1
                return int(list_line[2])

            # if list_line[0] == 'RECONCILIATION' and list_line[1] == 'EXCHANGE1':
            #     val = self.exc
            #     self.exc = 0
            #     return val

            # if list_line[0] == 'RECONCILIATION' and list_line[1] != 'EXCHANGE1':
            #     return self.exc

            # if list_line[0] == 'EXCHANGE1':
            #     if list_line[1] in self.trade_map:
            #         if int(list_line[2]) == self.trade_map[list_line[1]]:
            #             self.aku -= 1
            #             return int(list_line[2])
            #         else:
            #             self.exc += 1
            #     else:
            #             self.exc += 1
            #     # print(int(list_line[2]))
            #     return int(list_line[2])






if __name__ == "__main__":