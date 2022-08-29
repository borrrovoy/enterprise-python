# Copyright (C) 2021-present CompatibL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

if __name__ == "__main__":

    # Execute fastapi_intro.py before running this code

    # Query all trades
    api_url = "http://localhost:50301/query_trades"  # Port used by fastapi_blotter.py
    trades = requests.post(api_url)
    print(f"All trades: {trades.json()}")

    # Query trades that have GBP for at least one leg
    api_url = "http://localhost:50301/query_trades"  # Port used by fastapi_blotter.py
    gbp_trades = requests.post(api_url, params={"leg_ccy": "GBP"})
    print(f"Trades where leg_ccy=GBP for at least one leg: {gbp_trades.json()}")

    # Get one specific trade
    api_url = "http://localhost:50301/get_trade"  # Port used by fastapi_blotter.py
    t3_trade = requests.post(api_url, params={"trade_id": "T3"})
    print(f"Trade with trade_id=T3: {t3_trade.json()}")

    # Query by notional without min_notional specified
    # Just like copy of all trades query
    api_url = "http://localhost:50301/query_by_notional"  # Port used by fastapi_blotter.py
    no_min_notional_trades = requests.post(api_url)
    print(f"All trades: {no_min_notional_trades.json()}")

    # Query by notional with min_notional specified
    api_url = "http://localhost:50301/query_by_notional"  # Port used by fastapi_blotter.py
    # For example, let's specify min_notional with value of 101
    trades_with_notional_gte_101 = requests.post(api_url, params={"min_notional": 101})
    print(f"Trades with notional >= 101: {trades_with_notional_gte_101.json()}")
