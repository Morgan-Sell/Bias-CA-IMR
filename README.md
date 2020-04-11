# California's Independent Medical of Review
### *Are arbitrators persuaded by elements other than the facts?*

![Healthcare](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/Healthcare_workforce.jpg)

## Table of Contents

## Description
Evaluate if systemic bias exists when deciding to overturn or uphold an insurance company’s rejection of coverage of a medical procedure or health treatment.
By applying Bayesian inference and frequentist methods, one can conclude with a high level of certainty (98% CI) that arbitrators are more likely to overturn denial of coverage of medical and health procedures for children (\leq 10 years) than patients of other ages.

Throughout the summary the term **"overturn rate"** will be used. Overturn rate represents the probability that an independent reviewer repeals the insurer's denial of coverage.

## Purpose
People should ask themselves if they are fine with such a bias in determining what is claimed to be an independent, scientific method. Assuming subjectivity is a significant contributor to the outcome of IMRs, it would not be a stretch to conclude that other proclaimed objective evaluations are comprised of some degree of partiality.

My intention is not to claim that biases should/should not exist; however, I believe that the public should acknowledge that partiality is real and account for it when making decisions, especially those judgements that apply to a public domain.

## Data
In October 2013, California launched "Covered California" to follow the Affordable Care Act. As expected, the data shows a significant uptick in IMRs starting in 2013.

A point of interest is what drove the increase in percentage of IMRs that resulted in an overturn ruling, i.e. 51% and 56% in 2015 and 2016, respectively. In contrast, excluding 2020, 16 out of 17 years have percentages ranging from 33 to 49% of the other years show the percentage. Both the mean and median of those 17 years are ~45%.


## Exploratory Data Analysis
In October 2013, California launched "Covered California" as its response to the Affordable Care Act. As expected, the data shows a significant uptick in IMRs starting in 2013.

A point of interest is what drove the increase in percentage of IMRs that resulted in an overturn ruling, i.e. 51% and 56% in 2015 and 2016, respectively. Excluding 2020, 16 out of 17 years have shows percentages ranging form 33 to 49% of the other years show the percentage. Both the mean and median of those 17 years are ~45%.

![Annual Plot](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/annual_trend.png)


During the exploratory data analysis, I searched for areas that presented potential for bias. 
When I explored the overturn rate by age group, I noticed that children, who are ten years and younger in the sample set, 
showed a noticeably greater likelihood of their IMRs resulting in an overturn. 


![Age Plot](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/age.png)

## Hypothesis Testing
After discovering the difference in the higher overturn rate for children, I separated the sample population into children (10 years and younger) and the rest of 
the population and I developed the following null and alternative hypotheses:

> $$ H_0: Child's expected overturn rate = Expected overturn rate of patients who are 11 years and older $$

> $$ H_A: Child's expected overturn rate \geq Expected overturn rate of patients who are 11 years and older $$

With ~98% level of confidence, one can conclude that the expected overturn rate of the population of the two observed groups 
- children who are 10 years and younger and people who are 11 years and older - are **not** equal. 

By analyzing the sampling distribution under the null hypothesis, the p-value is approximately equal to a 1.0% significance level assuming a one-sided test.


![Sampling Distribution](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/p_val.png)

#### Type I & II Errors

The following plot displays the likelihood of incorrectly concluding that the expected overturn rate of children and remainder of the population are **not** equal, when in fact they are.
The region labeled $\alpha$, which is referred to as the false positive rate and type I error, visualizes the probability. 

Additionally, the plot also shows the probability of mistakenly claiming the overturn rates of the two populations are equal when, in reality, the overturn rates are not equal.
The area labeled $\beta$, which is called the false negative and type II error, displays the probability.


![Alpha Beta](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/alpha_beta.png)

#### Stasitical Power
It was slightly surprising that the power, under the given assumptions, resulted in 0.64, which is below the commonly used threshold of 0.80. I suspect that if the sample sizes were increased, 
specifically, for the children sample set, the power would increase.

![Power](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/power.png)

## Bayesian Inference
The results of Bayesian inference reinforced the conclusion to reject the $H_0. When 100,000 IMRs were simulated, the children's overturn rate was greater than the remainder of 
the population ~99%. Like the statistical power, I expect that if the children's sample size were increased, we would see less overlap of the two distributions in the plot below 
because of a decrease in the standard deviation of the children's overturn rate.

![Bayes Test](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/bayes_test.png)

