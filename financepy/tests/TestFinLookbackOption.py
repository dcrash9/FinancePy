# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:51:05 2016

@author: Dominic O'Kane
"""

from financepy.finutils.FinTestCases import FinTestCases, globalTestCaseMode
from financepy.products.equities.FinFloatStrikeLookbackOption import FinFloatStrikeLookbackOption, FinFloatStrikeLookbackOptionTypes
from financepy.products.equities.FinFixedStrikeLookbackOption import FinFixedStrikeLookbackOption, FinFixedStrikeLookbackOptionTypes
from financepy.finutils.FinDate import FinDate
import time
import sys
sys.path.append("..//..")


testCases = FinTestCases(__file__, globalTestCaseMode)


def test_FinLookBackOption():
    valueDate = FinDate(2015, 1, 1)
    expiryDate = FinDate(2016, 1, 1)
    stockPrice = 100.0
    volatility = 0.3
    interestRate = 0.05
    dividendYield = 0.01
    numPathsRange = [10000]
    stockPriceRange = range(90, 110, 2)
    numStepsPerYear = 252

###############################################################################

    testCases.header(
        "NUMPATHS",
        "OPTION_TYPE",
        "S",
        "SMIN",
        "VALUE",
        "VALUE_MC",
        "DIFF",
        "TIME")

    optionType = FinFloatStrikeLookbackOptionTypes.FLOATING_CALL
    for stockPrice in stockPriceRange:
        for numPaths in numPathsRange:
            option = FinFloatStrikeLookbackOption(expiryDate, optionType)
            stockMin = stockPrice
            value = option.value(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMin)
            start = time.time()
            valueMC = option.valueMC(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMin,
                numPaths,
                numStepsPerYear)
            end = time.time()
            timeElapsed = round(end - start, 3)
            diff = valueMC - value
            testCases.print(
                numPaths,
                optionType,
                stockPrice,
                stockMin,
                value,
                valueMC,
                diff,
                timeElapsed)

    testCases.header(
        "NUMPATHS",
        "OPTION_TYPE",
        "S",
        "SMIN",
        "VALUE",
        "VALUE_MC",
        "DIFF",
        "TIME")

    optionType = FinFloatStrikeLookbackOptionTypes.FLOATING_CALL
    for stockPrice in stockPriceRange:
        for numPaths in numPathsRange:
            option = FinFloatStrikeLookbackOption(expiryDate, optionType)
            stockMin = stockPrice - 10
            value = option.value(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMin)
            start = time.time()
            valueMC = option.valueMC(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMin,
                numPaths,
                numStepsPerYear)
            end = time.time()
            timeElapsed = round(end - start, 3)
            diff = valueMC - value
            testCases.print(
                numPaths,
                optionType,
                stockPrice,
                stockMin,
                value,
                valueMC,
                diff,
                timeElapsed)

    testCases.header(
        "NUMPATHS",
        "OPTION_TYPE",
        "S",
        "SMAX",
        "VALUE",
        "VALUE_MC",
        "DIFF",
        "TIME")

    optionType = FinFloatStrikeLookbackOptionTypes.FLOATING_PUT
    for stockPrice in stockPriceRange:
        for numPaths in numPathsRange:
            option = FinFloatStrikeLookbackOption(expiryDate, optionType)
            stockMax = stockPrice
            value = option.value(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMax)
            start = time.time()
            valueMC = option.valueMC(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMax,
                numPaths,
                numStepsPerYear)
            end = time.time()
            timeElapsed = round(end - start, 3)
            diff = valueMC - value
            testCases.print(
                numPaths,
                optionType,
                stockPrice,
                stockMax,
                value,
                valueMC,
                diff,
                timeElapsed)

    testCases.header(
        "NUMPATHS",
        "OPTION_TYPE",
        "S",
        "SMAX",
        "VALUE",
        "VALUE_MC",
        "DIFF",
        "TIME")

    optionType = FinFloatStrikeLookbackOptionTypes.FLOATING_PUT
    for stockPrice in stockPriceRange:
        for numPaths in numPathsRange:
            option = FinFloatStrikeLookbackOption(expiryDate, optionType)
            stockMax = stockPrice + 10
            value = option.value(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMax)
            start = time.time()
            valueMC = option.valueMC(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMax,
                numPaths,
                numStepsPerYear)
            end = time.time()
            timeElapsed = round(end - start, 3)
            diff = valueMC - value
            testCases.print(
                numPaths,
                optionType,
                stockPrice,
                stockMax,
                value,
                valueMC,
                diff,
                timeElapsed)

###############################################################################
###############################################################################

    stockPriceRange = range(90, 110, 2)
    numStepsPerYear = 252

    testCases.header(
        "NUMPATHS",
        "OPTION_TYPE",
        "S",
        "K",
        "SMAX",
        "VALUE",
        "VALUE_MC",
        "DIFF",
        "TIME")

    optionType = FinFixedStrikeLookbackOptionTypes.FIXED_CALL
    k = 95.0
    for stockPrice in stockPriceRange:
        for numPaths in numPathsRange:
            option = FinFixedStrikeLookbackOption(expiryDate, optionType, k)
            stockMax = stockPrice
            value = option.value(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMax)
            start = time.time()
            valueMC = option.valueMC(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMax,
                numPaths,
                numStepsPerYear)
            end = time.time()
            timeElapsed = round(end - start, 3)
            diff = valueMC - value
            testCases.print(
                numPaths,
                optionType,
                stockPrice,
                k,
                stockMax,
                value,
                valueMC,
                diff,
                timeElapsed)

    testCases.header(
        "NUMPATHS",
        "OPTION_TYPE",
        "S",
        "K",
        "SMAX",
        "VALUE",
        "VALUE_MC",
        "DIFF",
        "TIME")

    optionType = FinFixedStrikeLookbackOptionTypes.FIXED_CALL
    k = 100.0
    for stockPrice in stockPriceRange:
        for numPaths in numPathsRange:
            option = FinFixedStrikeLookbackOption(expiryDate, optionType, k)
            stockMax = stockPrice
            value = option.value(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMax)
            start = time.time()
            valueMC = option.valueMC(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMax,
                numPaths,
                numStepsPerYear)
            end = time.time()
            timeElapsed = round(end - start, 3)
            diff = valueMC - value
            testCases.print(
                numPaths,
                optionType,
                stockPrice,
                k,
                stockMax,
                value,
                valueMC,
                diff,
                timeElapsed)

    testCases.header(
        "NUMPATHS",
        "OPTION_TYPE",
        "S",
        "K",
        "SMAX",
        "VALUE",
        "VALUE_MC",
        "DIFF",
        "TIME")

    optionType = FinFixedStrikeLookbackOptionTypes.FIXED_CALL
    k = 105.0
    for stockPrice in stockPriceRange:
        for numPaths in numPathsRange:
            option = FinFixedStrikeLookbackOption(expiryDate, optionType, k)
            stockMax = stockPrice + 10.0
            value = option.value(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMax)
            start = time.time()
            valueMC = option.valueMC(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMax,
                numPaths,
                numStepsPerYear)
            end = time.time()
            timeElapsed = round(end - start, 3)
            diff = valueMC - value
            testCases.print(
                numPaths,
                optionType,
                stockPrice,
                k,
                stockMax,
                value,
                valueMC,
                diff,
                timeElapsed)

    testCases.header(
        "NUMPATHS",
        "OPTION_TYPE",
        "S",
        "K",
        "SMIN",
        "VALUE",
        "VALUE_MC",
        "DIFF",
        "TIME")

    optionType = FinFixedStrikeLookbackOptionTypes.FIXED_PUT
    k = 95.0
    for stockPrice in stockPriceRange:
        for numPaths in numPathsRange:
            option = FinFixedStrikeLookbackOption(expiryDate, optionType, k)
            stockMin = stockPrice
            value = option.value(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMin)
            start = time.time()
            valueMC = option.valueMC(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMin,
                numPaths,
                numStepsPerYear)
            end = time.time()
            timeElapsed = round(end - start, 3)
            diff = valueMC - value
            testCases.print(
                numPaths,
                optionType,
                stockPrice,
                k,
                stockMin,
                value,
                valueMC,
                diff,
                timeElapsed)

    testCases.header(
        "NUMPATHS",
        "OPTION_TYPE",
        "S",
        "K",
        "SMIN",
        "VALUE",
        "VALUE_MC",
        "DIFF",
        "TIME")

    optionType = FinFixedStrikeLookbackOptionTypes.FIXED_PUT
    k = 100.0
    for stockPrice in stockPriceRange:
        for numPaths in numPathsRange:
            option = FinFixedStrikeLookbackOption(expiryDate, optionType, k)
            stockMin = stockPrice
            value = option.value(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMin)
            start = time.time()
            valueMC = option.valueMC(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMin,
                numPaths,
                numStepsPerYear)
            end = time.time()
            timeElapsed = round(end - start, 3)
            diff = valueMC - value
            testCases.print(
                numPaths,
                optionType,
                stockPrice,
                k,
                stockMin,
                value,
                valueMC,
                diff,
                timeElapsed)

    testCases.header(
        "NUMPATHS",
        "OPTION_TYPE",
        "S",
        "K",
        "SMIN",
        "VALUE",
        "VALUE_MC",
        "DIFF",
        "TIME")

    optionType = FinFixedStrikeLookbackOptionTypes.FIXED_PUT
    k = 105.0
    for stockPrice in stockPriceRange:
        for numPaths in numPathsRange:
            option = FinFixedStrikeLookbackOption(expiryDate, optionType, k)
            stockMin = stockPrice - 10.0
            value = option.value(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMin)
            start = time.time()
            valueMC = option.valueMC(
                valueDate,
                stockPrice,
                interestRate,
                dividendYield,
                volatility,
                stockMin,
                numPaths,
                numStepsPerYear)
            end = time.time()
            timeElapsed = round(end - start, 3)
            diff = valueMC - value
            testCases.print(
                numPaths,
                optionType,
                stockPrice,
                k,
                stockMin,
                value,
                valueMC,
                diff,
                timeElapsed)

###############################################################################


test_FinLookBackOption()
testCases.compareTestCases()