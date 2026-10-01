# To find the decimal of a percentage, divide by 100. It should be something like "x.0." This is how we get our tip.
# Then, multiply the original price by the tip (being the first digit).
# Finally, add it to the final price.


originalPrice = 73
tip = 20

def getTip(o, t):
  tipAmount = t / 100 * o
  finalPrice = o + tipAmount
  return finalPrice



print(getTip(originalPrice, tip))
