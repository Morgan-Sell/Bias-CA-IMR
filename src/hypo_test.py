import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from src.import_process_eda import import_process_csv



def plot_sampling_distribution(mu_h_0, std_err)
    '''
    Plot the sampling distribution showing the 95%, 98%, and 99% CIs.
    Shows the region of the p-value associated with the null hypothesis.

    Parameters
    ----------
    mu_h_0 : float
        Mean of the sampling distribution.
    
    std_err : float
        Standard error of the sampling distribution

    Return
    ------

    '''

    # Calculate and plot p-value
    x_arr = np.linspace(-0.06, 0.06, 400)
    fig, ax = plt.subplots(figsize=(12,5))

    # Calculate and plot 95% CI
    up_95_lim = mu_h_0 + 1.96 * std_err
    low_95_lim = mu_h_0 - 1.96 * std_err
    ax.axvline(up_95_lim, c='grey', linestyle='-', label='95% CI')
    ax.axvline(low_95_lim, c='grey', linestyle='-')

    # Calculate and plot 98% CI
    up_98_lim = mu_h_0 + 2.326 * std_err
    low_98_lim = mu_h_0 - 2.326 * std_err
    ax.axvline(up_98_lim, c='blue', linestyle='--', label='98% CI')
    ax.axvline(low_98_lim, c='blue', linestyle='--')

    # Calculate and plot 99% CI
    up_99_lim = mu_h_0 + 2.58 * std_err
    low_99_lim = mu_h_0 - 2.58 * std_err
    ax.axvline(up_99_lim, c='blue', linestyle='-', label='99% CI')
    ax.axvline(low_99_lim, c='blue', linestyle='-')

    # Plot H0
    ax.plot(x_arr, h_0_dist.pdf(x_arr), c='green', label='$H_0$', linewidth=4)

    p_val = 1 - h_0_dist.cdf(mu_h_a)
    ax.fill_between(x_arr, h_0_dist.pdf(x_arr), where=(x_arr >= mu_h_a), color='green', alpha=0.5, 
                    label='P-Value Region')
    ax.fill_between(x_arr, h_0_dist.pdf(x_arr), where=(x_arr <= -mu_h_a), color='green', alpha=0.5)
    ax.set_title("Sampling Distribution under the $H_0$", fontsize=20, fontweight='bold')
    ax.legend(facecolor='white')
    ax.set_ylabel('PDF')

    # Formatting
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(color=None, linestyle='None')
    ax.set_facecolor('white')
    ax.set_xlim(-0.04, 0.04)
    ax.set_ylim(0, 50)
    plt.rcParams['font.family'] = 'arial'
    fig.tight_layout()
    plt.show()


def welch_t_test(sample_1, sample_2):
    num = np.mean(sample_1) - np.mean(sample_2)
    denom = (np.var(sample_1) / len(sample_1)) + (np.var(sample_2) / len(sample_2))
    return num / np.sqrt(denom)

def create_sig_lev_dict(mu_h_0, std_err):
    '''
    Develops a dictionary for difference CIs of 95%, 98%, and 99%.

    Parameters
    ----------
    mu_h_0 : float
        Mean of the sampling distribution.
    
    std_err : float
        Standard error of the sampling distribution

    Return
    ------
    sig_lev_dict : dict
        Key-value pairs of significance level and corresponding values for the specificed distribution.
    
    '''    
    lim_95 = mu_h_0 + 1.96 * std_err
    lim_98 = mu_h_0 + 2.326 * std_err
    lim_99 = mu_h_0 + 2.58 * std_err
    sig_lev_dict = {0.05: lim_95, 0.02: lim_98, 0.01: lim_99}
    return sig_lev_dict


def calc_plot_alpha_beta(mu_h_0, std_err, sig_lev, sig_lev_dict, h_0_dist, h_a_dist):
    '''
    Calculates and plots the alpha and beta based on the selected significance level.

    Parameters
    ----------
    mu_h_0 : float
        Mean of the sampling distribution.
    
    std_err : float
        Standard error of the sampling distribution

    sig_lev : float
        Significan level
    
    h_0_dist : class
        A instance of normal distribution for the null hypothesis instantiated by Scipy.

    h_a_dist : class
        A instance of normal distribution for the alternative hypothesis instantiated by Scipy.

    Return
    ------

    '''

    lim_95 = mu_h_0 + 1.96 * std_err
    lim_98 = mu_h_0 + 2.326 * std_err
    lim_99 = mu_h_0 + 2.58 * std_err
    sig_lev_dict = {0.05: lim_95, 0.02: lim_98, 0.01: lim_99}
    alpha = sig_lev / 2
    beta = h_a_dist.cdf(sig_lev_dict[sig_lev])

    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(x_arr, h_0_dist.pdf(x_arr), c='green', label='$H_0$', linewidth=3)

    #Plot alternative hypothesis
    ax.plot(x_arr, h_a_dist.pdf(x_arr), c='purple', label='$H_A$', linewidth=3)

    ax.axvline(sig_lev_dict[sig_lev], c='black', linestyle='--')
    ax.fill_between(x_arr, h_0_dist.pdf(x_arr), where=(x_arr >= sig_lev_dict[sig_lev]), color='green', alpha=0.3, label=r'$\alpha$')
    ax.fill_between(x_arr, h_a_dist.pdf(x_arr), where=(x_arr <= sig_lev_dict[sig_lev]), color='purple', alpha=0.3, label=r'$\beta$')

    ax.set_title('Distribution of the Difference in Overturn Rates - {:.2} Significance Level'.format(sig_lev), 
                fontsize=20, fontweight='bold')
    ax.set_ylabel('PDF')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(color=None, linestyle='None')
    ax.set_facecolor('white')
    ax.set_xlim([-0.04,0.06])
    ax.set_ylim([0,50])
    ax.legend(facecolor='white')
    plt.tight_layout()
    plt.show

    print('alpha = {:.3f}'.format(alpha))
    print('beta = {:.3f}'.format(beta))


def power_analysis(h_a_dist, h_0_dist, sig_lev, sig_lev_dict):
    '''
    Calculates and plots the stastical power.

    Parameters
    ----------
    h_0_dist : class
        A instance of normal distribution for the null hypothesis instantiated by Scipy.

    h_a_dist : class
        A instance of normal distribution for the alternative hypothesis instantiated by Scipy.

    sig_lev : float
        Significan level
    
    sig_lev_dict : dict
        Key-value pairs of significance level and corresponding values for the specificed distribution.
    
    Return
    ------
    
    '''

    power = 1 - h_a_dist.cdf(sl_dict[sig_lev])

    fig, ax = plt.subplots(figsize=(12,5))

    # Plot null hypothesis.
    ax.plot(x_arr, h_0_dist.pdf(x_arr), c='green', label='$H_0$', linewidth=3)

    #Plot alternative hypothesis
    ax.plot(x_arr, h_a_dist.pdf(x_arr), c='purple', label='$H_A$', linewidth=3)
    ax.axvline(sl_dict[sig_lev], c='black', linestyle='--')
    ax.fill_between(x_arr, h_a_dist.pdf(x_arr), where=(x_arr >= sl_dict[sig_lev]), color='red', alpha=0.2, label='Power')
    ax.set_title('Power Analysis - {:.2} Significance Level'.format(sig_lev), fontsize=20, fontweight='bold')
    ax.set_ylabel('PDF')

    # Formatting
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(color=None, linestyle='None')
    ax.set_facecolor('white')
    ax.set_xlim([-0.04,0.06])
    ax.set_ylim([0,50])
    fig.tight_layout()
    ax.legend()
    plt.rcParams['font.family'] = 'arial'
    ax.legend(facecolor='white')
    plt.show()

    print('Power = {:.3f}'.format(power))



# code

imr = import_process_csv()
children = np.asarray(imr[imr['AgeRange'] == '11 to 20']['determination_encoded'])
others = np.asarray(imr[imr['AgeRange'] != '11 to 20']['determination_encoded'])

mu_h_0 = 0
n_child = len(children)
p_c = sum(children) / n_child

n_others = len(others)
p_o = sum(others) / n_others

p_shared = sum(imr['determination_encoded']) / len(imr['determination_encoded'])
var_shared = p_shared * (1 - p_shared) / n_child + p_shared * (1 - p_shared) / n_others
std_err_shared = np.sqrt(var_shared)
# mu for the alternative hypothesis
mu_h_a  = p_c - p_o

# Calculate alternative and null hypotheses distributions.
h_0_dist = stats.norm(mu_h_0, std_err_shared)
h_a_dist = stats.norm(mu_h_a, std_err_shared)

print('Probability for children: {:.4f}'.format(p_c))
print('Probability for all other age: {:.4f}'.format(p_o))
print("Difference in the sample probabilities: {:.4f}".format(mu_h_a))

plot_sampling_distribution(mu_h_0, std_err_shared)

# Apply Welch's T-test b/c significant difference in sample size between the two age group.
var_children = np.var(children)
var_others = np.var(others)

print("Children sample variance: {:.4f}".format(var_children))
print("Children sample size: {:.0f}".format(n_child))
print("Others sample variance: {:.4f}".format(var_others))
print("Others sample size: {:.0f}".format(n_others))

t_stat = welch_t_test(children, others)
scipy_t_stat, scipy_p_val =stats.ttest_ind(children, others, equal_var = False)
print("Welch's t-statistic: {:2.4f}".format(t_stat))
print("Scipy's Welch's t-statistic: {:2.4f}".format(scipy_t_stat))
print("Scipy's Welch's t-statistic: {:2.4f}".format(scipy_p_val))

# Calculate alpha and beta

sig_lev_dict = create_sig_lev_dict(mu_h_0, std_err_shared)
calc_plot_alpha_beta(mu_h_0, std_err, sig_lev, 0.05, h_0_dist, h_a_dist)
power_analysis(h_a_dist, h_0_dist, 0.5, sig_lev_dict):