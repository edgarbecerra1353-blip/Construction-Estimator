# Construction Estimator - Project Notes

## Problem

Stone flowerbed estimates are currently created largely from experience and manual calculations.

The goal of this project is to create software that helps organize and calculate these estimates while still allowing the estimator to use their own judgment.

## Current Estimating Process

### Job Measurements
- Measure the total length of the flowerbed in feet.
- Determine the number of stone rows based on the customer's preference and what looks appropriate.
- Determine the stone or brick type.
- Determine the desired stone size/thickness.

### Materials
Common materials include:
- Stone
- Brick
- Portland cement
- Sand
- Gravel
- Rebar

Material quantities are currently estimated mainly from experience.

Stone may be estimated as a fraction of a pallet, such as:
- 1/4 pallet
- 1/2 pallet
- 3/4 pallet
- 1 pallet

Material prices are generally known approximately from experience with suppliers.

### Labor
The normal crew consists of:
- Maestro: $200 per day
- Chalan: $150 per day

The estimator determines approximately how many days the job will take.

Labor cost is based on:

(number of days) x (daily labor cost)

### Final Price

The basic estimate is:

materials + labor = customer price

The final price can sometimes be manually adjusted upward or downward based on judgment.

## V1 Goal

The first version should allow the user to:
- Enter job information
- Enter materials and their quantities
- Enter material prices
- Calculate material costs
- Enter workers and daily rates
- Enter estimated number of work days
- Calculate labor cost
- Calculate the total estimate
- Manually adjust the final price
- Clearly see how the total was calculated

Later versions can explore automatically suggesting material quantities using data from previous jobs.