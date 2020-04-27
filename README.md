# California's Independent Medical of Review
### *Are arbitrators persuaded by elements other than the facts?*

![Healthcare](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/Healthcare_workforce.jpg)

## Table of Contents

1) Executive Summary
3) Data
4) Exploratory Data Analysis
5) Hypothesis Testing
6) Bayesian Inference


## Executive Summary
Evaluated if systemic bias exists when an arbitrator determines to overturn or uphold an insurer’s rejection of coverage of a medical procedure or health treatment. To test for age bias, this project compares the likelihood of a child (10 years or younger) and older-aged patient’s denials of service being overturned during an independent medical review (IMR) in California.

Throughout this document, the term **“overturn rate”** will be used to represent the probability that an insurer’s denial of coverage is repealed during the IMR. Also, **“other patient(s)”** will represent patients/people who are not children, i.e. older than ten years of age.

The results of the hypothesis testing demonstrate that the probability that the children and other patient’s overturn rates are equal is 2.0%. As the null hypothesis – children and other patient’s overturn rates are equal – is rejected at a 98% confidence interval.

## Data
The data is from the California Department of Managed Health Care (DMHC). It contains over 28,000 decisions from IMRs administered by the DMHC since January 1, 2001. An IMR is an independent review of a denied, delayed, or modified health care service that the health plan has determined to be not medically necessary, experimental/investigational, or non-emergent/urgent. If the IMR is decided in an enrollee’s favor, the health plan must authorize the service or treatment requested. 


## Exploratory Data Analysis
In the earlier years of the dataset, we see a gradual increase in the number of annual IMRs and the percentage of IMRs that resulted in an overturn decision is, more or less, constant. Meanwhile, starting in 2014, the number of annual IMRs begin to increase at a significantly greater rate than the one between 2002 and 2012. This increase in IMR is more than likely caused by the increase in the number of insured Californian residents because of the implementation of Covered California in October 2013. Covered California is the state’s health insurance marketplace that resulted from the Affordable Care Act.

According to Peter Lee, Executive Director of Covered California, the number of uninsured residents decreased from 17.3% at the end of 2013 to 7.2% in 2019. And, according to the U.S. Census, California’s population has increased every year since 2013, ranging from 0.10% to 0.90%. Coalescing the two facts validate that the raw number of total insured California citizens has increased.

The outliers to note in the bar chart below is that in 2015, 2016, and 2019 more than 50% of the cases reviewed favored the enrollee. Meanwhile, the unweighted average overturn rate from 2003 to 2019 is less than 45%.
We also see a steady decrease in the annual number of IMRs starting in 2017. According to Peter Lee, starting in 2017, the federal government refused to reimburse insurers for discounts that the companies were required to offer on deductibles and copayments. Therefore, the insurers increased prices of insurance plans listed on Covered California. The rate hikes coincided with 170,000 people, who were previously insured via Covered California, to discontinue their insurance. 


![Annual Plot](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/annual_trend.png)


While studying the data to identify areas that warranted further investigation, I discovered a meaningful difference in the overturn rate of children and other patients. We observe in the bar chart below that a negation of a child’s insurance coverage is two times more likely to be overturned. In contrast, all other age groups’ overturn rates are less than 50%.


![Age Plot](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/age.png)

## Hypothesis Testing
After recognizing the noticeable difference in the overturn rate between children and the other patients, I evaluted if age bias is systemic in the arbitrators’ decisions by testing for statistical significance.

<p align="center">
 Null Hypothesis: Child's expected overturn rate = Expected overturn rate of patients who are 11 years and older <br>
Alternative Hypothesis: Child's expected overturn rate != Expected overturn rate of patients who are 11 years and older
</p>

As the p-value for the experiment is ~2.0%, the null hypothesis  can be rejected – a child’s overturn rate does not equal the other patient’s overturn rate – at a 98% confidence interval.

By analyzing the sampling distribution under the null hypothesis, the p-value is approximately equal to a 1.0% significance level assuming a one-sided test.


![Sampling Distribution](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/p_val.png

#### Type I & II Errors

The distribution plot below displays the likelihood of incorrectly concluding that the expected overturn rate of children and remainder of the patient population are not equal, when in fact they are. The region labeled *alpha*, which is referred to as the false positive rate (FPR) and type I error, visualizes the probability which demonstrates the possibility of this error is relatively minor.
 
The visualization also shows the probability of mistakenly claiming the overturn rates of the two populations are equal when, in reality, the overturn rates are inequal. The shaded area labeled *beta*, which is called the false negative rate (FNR) and type II error displays the probability. Assuming a significance level equal to 0.05, *beta* equals 0.36.



![Alpha Beta](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/alpha_beta.png)

#### Stasitical Power
In this project, power represents the probability that the test rejects the proposal that a child and other patient’s overturn rates are equal (Ho) when the inverse of the proposal (Ha) is true – the overturn rates of the two groups are not equal. Under the provided assumptions, power equals 0.64, which is the equivalent to 1 – *beta*. 

![Power](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/power.png)

## Bayesian Inference
By applying the Beta function/distribution, the posterior probability, which accounts for the consideration of background information, I derived the distributions below. To quantify the likelihood that a child’s overturn rate is greater than the overturn rate of other patients, I simulated 100,000 IMRs. Under the assumptions stated throughout this analysis, the probability that the child’s overturn rate is greater is 99%.

![Bayes Test](https://github.com/Morgan-Sell/CA-Indepedent-Medical-Review/blob/individual/images/bayes_test.png)

