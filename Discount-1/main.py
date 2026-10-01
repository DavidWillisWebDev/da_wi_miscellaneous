"""
Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

Examples
dis(1500, 50) ➞ 750

dis(89, 20) ➞ 71.2

dis(100, 75) ➞ 25
Notes
Your answer should be rounded to two decimal places.
"""

originalPrice = 1500
discount = 50

def getFinalPrice(o, d):
  discountAmount = d / 100 * o
  finalPrice = o - discountAmount
  return finalPrice



print(getFinalPrice(originalPrice, discount))
