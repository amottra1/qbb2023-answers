Step 2.2
What is the “size” of this relationship? In your own words, what does this mean? Does this match what you observed in your plots in step 2.1?

The R-squared value for the maternal relationships is 0.226 which is a very low correlation. This means that size of the relationship is somewhat low but that ~23% of variations in dnm can be explained by age.

Is this relationship significant? How do you know?

The relationship between maternal age and the number of dnms is indeed significant since the p-value is very low (6.89e-24)



Step 2.3
What is the “size” of this relationship? In your own words, what does this mean? Does this match what you observed in your plots in step 2.1?

The R-squared value for the paternal relationships is 0.618 meaning there is a moderate correlation. This means that ~60% of variations in dnm can be explained by age.

Is this relationship significant? How do you know?

The relationship between paternal age and the number of dnms is very significant since the p-value is very low (1.55e-84)


Step 2.4

Answer: 78.7 ~79 dnms

I used the predict method in the statsmodels to predict the value of paternal_dnm based on a given Father age


Step 2.6

What statistical test did you choose? Why?
Was your test result statistically significant? Interpret your result as it relates 
to the number of paternally and maternally inherited DNMs."""

I chose to do a t test on scipy.stats which determines if 2 data sets are significantly different from each other. The p value is 2.2e-264 which is very low meaning that the number of inherited DNMs for paternally vs maternally is significantly different.






