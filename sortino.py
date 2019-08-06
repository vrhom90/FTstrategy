#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:14:53 2019

@author: vrhom90
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:06:58 2019

@author: vrhom90
"""

# --- Do not remove these libs ---
from freqtrade.strategy.interface import IStrategy
from typing import Dict, List
from hyperopt import hp
from functools import reduce
from pandas import DataFrame
# --------------------------------
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
from typing import Dict, List
from hyperopt import hp
from functools import reduce
from pandas import DataFrame, DatetimeIndex, merge
# --------------------------------
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
import numpy  # noqa
#-------------------------------------------
import numpy as np
from empyrical import sortino_ratio, calmar_ratio, omega_ratio

class Sortino(IStrategy):
    """
        this strategy is based around the idea of generating a lot of potentatils buys and make tiny profits on each trade
        we recommend to have at least 60 parallel trades at any time to cover non avoidable losses
    """

    # Minimal ROI designed for the strategy.
    # This attribute will be overridden if the config file contains "minimal_roi"
    minimal_roi = {
        "0": 0.01
    }
    # Optimal stoploss designed for the strategy
    # This attribute will be overridden if the config file contains "stoploss"
    # should not be below 3% loss

    stoploss = -0.5
    # Optimal ticker interval for the strategy
    # the shorter the better
    ticker_interval = '1m'
    

  
def _reward(self):
      length = min(self.current_step, self.reward_len)
      returns = np.diff(self.net_worths)[-length:]

      if self.reward_func == 'sortino':
          reward = sortino_ratio(returns)
      elif self.reward_func == 'calmar':
          reward = calmar_ratio(returns)
      elif self.reward_func == 'omega':
          reward = omega_ratio(returns)
      else
          reward = np.mean(returns)

      return reward if abs(reward) != inf and not np.isnan(reward) else 0