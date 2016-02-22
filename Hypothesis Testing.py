### Checking invariants
### Run experiment for 7 days. Unit of diversion: event.
### Total events control: 15,348. Total events experiment: 15,312.
### How would you figure out whether this difference is within expectation?

# 1. Compute standard deviation of binomial with probability 0.5 of success
import math

p = 0.5
sd = round(math.sqrt(p*(1-p)/(15348+15312)),4)
print "sd is:", sd

# 2. Multiple by z-score to get margin of error
m = round(1.96*sd,4)
print "margin of error is:", m

# 3. Compute confidence interval around 0.5
# Note: 95% of the time, the observed fraction of events should fall within this range
print "CI is:", p-m, p+m

# 4. Check whether observed fraction is within CI
p_hat = round(15348.0/(15348+15312),4)
if p-m <= p_hat <= p+m:
    print "Fell in the CI. p hat is:", p_hat
else:
    print "Fell outside of the CI. p hat is:", p_hat


### Analysis with a single metric
### Metric: click-through-rate. d-min=0.01. alpha = 0.05. 
### Empirical SE = 0.0062 with 5000 pageviews in each group. Is the effect significant?
### Note: Use empirical SE to calculate sample SE since CTR does not follow binomial distribution.

Xs_cont = [196, 200, 200, 216, 212, 185, 225, 187, 205, 211, 192, 196, 223, 192] 
Ns_cont = [2029, 1991, 1951, 1985, 1973, 2021, 2041, 1980, 1951, 1988, 1977, 2019, 2035, 2007] 
Xs_exp = [179, 208, 205, 175, 191, 291, 278, 216, 225, 207, 205, 200, 297, 299] 
Ns_exp = [1971, 2009, 2049, 2015, 2027, 1979, 1959, 2020, 2049, 2012, 2023, 1981, 1965, 1993]

# 1. Calculate difference in rates
Xs_cont_sum = sum(x for x in Xs_cont)
Ns_cont_sum = sum(x for x in Ns_cont)
Xs_exp_sum = sum(x for x in Xs_exp)
Ns_exp_sum = sum(x for x in Ns_exp)
rate_cont = round(1.0*Xs_cont_sum/Ns_cont_sum,4)
rate_exp = round(1.0*Xs_exp_sum/Ns_exp_sum,4)
d = rate_exp - rate_cont
print "difference in rate:", d

# 2. Calculate standard error
import math
SE = round(0.0062/math.sqrt(2.0/5000)*math.sqrt(1.0/Ns_cont_sum+1.0/Ns_exp_sum),4)
print "standard error:", SE

# 3. Calculate margin of error
m = round(SE*1.96,4)
print "margin of error:", m

# 4. Confidence interval
print "confidence interval:", d-m, d+m

# 5. Sanity check - calculate p-value using online calculator
# Note: n=14 is too small for binomial distrubtion to approximate normal distrubtion
# Online calculator for p-value: http://graphpad.com/quickcalcs/binomial1.cfm
list_rate_cont = [1.0*x/y for x,y in zip(Xs_cont,Ns_cont)]
list_rate_exp = [1.0*x/y for x,y in zip(Xs_exp,Ns_exp)]
print "total events:", len(Ns_cont)
print "total successes:", sum(1 for x, y in zip(list_rate_cont, list_rate_exp) if y>x)
