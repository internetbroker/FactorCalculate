#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: ??
@author: li
@file: __init__.py.py
@time: 2019-06-30 19:04
"""
from ultron.cluster.invoke.app_engine import create_app

app = create_app('factor', ['factor.factor_growth', 'factor.historical_value'])
