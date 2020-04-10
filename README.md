# California's Independenet Medical of Review
## Are arbitrators persuaded by elements other than the facts?

![Healthcare](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/Healthcare_workforce.jpg)

## Table of Contents

## Description
Uncovered statistical evidence to support that Titanic ethos of "women and children first", which aspiring data scientists know well, continues in the California healthcare system. By applying Bayesian inference and frequentist methods, one can conclude with a high level of certainty (98% CI) that arbitrators are more likely to overturn denial of insurance coverage of medical and health procedures for children (\leq 10 years) that patients of other ages.

## Data
The data is from the California Department of Managed Health Care (DMHC). It is comprised of more than 28,000 Independent Medical Reviews(IMR) of patients' appeals to their insurances' denial of coverage of medical treatment and/or healthcare service. The IMRs were administered by the DMHC since January 1, 2001. If an IMR decided in a patient's favor, i.e. overturned the decision, the insurer was obligated to authorize the requested service or treatment.

The dataset has a total of 14 features - numeric, categorical, and free form. Examples of features include patient age/gender, diagnosis and treatment categories and subcategories, and arbitrator' findings.

## Purpose
People should ask themselves if they are fine with such a bias in determining what is claimed to be an independent, scientific method. Assuming subjectivity is a significant contributor to the outcome of IMRs, it would not be a stretch that other proclaimed objective evaluations are comprised of some degree of partiality.

My intention is not to say that biases should not exist; however, I believe that the public should admit that partiality is real and account for it when making decisions, especially those judgements that apply to a public domain.

## Exploratory Data Analysis
In October 2013, California launched "Covered California" as its response to the Affordable Care Act. As expected, the data shows a significant uptick in IMRs starting in 2013.

A point of interest is what drove the increase in percentage of IMRs that resulted in an overturn ruling, i.e. 51% and 56% in 2015 and 2016, respectively. Excluding 2020, 16 out of 17 years have shows percentages ranging form 33 to 49% of the other years show the percentage. Both the mean and median of those 17 years are ~45%.

![Annual Plot](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/annual_trend.png)


During the exploratory data analysis, I searched for areas that potentially had bias. In one plot, I compared the likelihood of a case being overturned by the patient's age group. 
After discovering the difference in the "overturn rate" in the sample dataset, I decided totest the hypothesis that the a child's "overturn rate" is equal to that of patients
of other ages. (See chart below.)


![Age Plot](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/age.png)

## Hypothesis Testing
> $$ H_0: Child's expected overturn rate = Expected overturn rate of patients who are 11 years and older $$
> $$ H_A: Child's expected overturn rate \geq Expected overturn rate of patients who are 11 years and older $$

With ~98% level of confidence, one can conclude that the the the expected overturn rate of the population of the two observed groups 
- children who are 10 years and younger and people who are 11 years and older - are **not** equal. 
The below distribution shows the p-value to be approximately equal to a 1.0% significance level assuming a one-sided test.

![Sampling Distribution](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/p_val.png)

### Type 1 & 2 Error Rates and Statistical Power

The following plot displays the likelihood of incorrectly concluding that the expected overturn rate of children and remainder of the population are **not** equal,  when in fact they are.
The region labeled $\alpha$, which is know as the false positive rate and type I error, visualizes the probability. 

Additionally, the plot also shows the probability of mistakenly claiming the overturn rates of the two populations are equal when, in reality, the overturn rates are not equal.
The area labeled $\beta$, which is call the false negative and type II error, displays the probability.

![Alpha Beta](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/alpha_beta.png)