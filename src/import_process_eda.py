import pandas as pd
import numpy as np
import matptlotlib.pyplot as plt
import seaborn as sns


def import_process_csv():
    '''
    Imports the California Department of Managed Health Care (DMHC) csv file.

    Resolves null values.
    Feature engineering.

    Parameters
    ----------
    
    Returns
    -------
    '''
    imr = pd.read_csv('../data/imr_trends.csv')
    imr2 = imr['DaysToReview'].fillna(imr['DaysToReview'].median())
    imr2['len_findings'] = imr2['Findings'].apply(len)
    imr2['determination_code'] = imr2['Determination'].map({'Upheld Decision of Health Plan' : 0, 'Overturned Decision of Health Plan' : 1})
    return imr2



def plot_imr_results_annual_trend(dataset):
    '''
    Create a dual-axis bar and line plot comparing the number of denial of services that were upheld and overturned by year

    Parameters
    ----------
    dataset : dataframe
        The dataset that is produced by the import_process_csv function.

    Returns
    -------
    '''
    yr_grpd_1 = dataset.groupby(['ReportYear', 'Determination']).agg({'Determination':'count'})
    yr_grpd_1.columns = ['count']
    yr_grpd_1.reset_index(inplace=True)
    yr_ovrtrnd = yr_grpd_1[yr_grpd_1['Determination'] == 'Overturned Decision of Health Plan']
    yr_upheld = yr_grpd_1[yr_grpd_1['Determination'] == 'Upheld Decision of Health Plan']

    # Total "Determinations" per year.
    yr_grpd_2 = dataset.groupby(['ReportYear']).agg({'Determination':'count'})
    yr_grpd_2.columns = ['count']
    yr_grpd_2.reset_index(inplace=True)

    # Merge
    det_yr = pd.merge(yr_grpd_2, yr_ovrtrnd, how='left', on='ReportYear')
    det_yr = pd.merge(det_yr, yr_upheld, how='left', on='ReportYear')
    det_yr.rename({'count_x':'total_reviewed', 'count_y':'num_overturned', 'count':'num_upheld'}, axis=1, inplace=True)
    det_yr.drop(['Determination_x', 'Determination_y'], inplace=True, axis=1)
    det_yr['percent_overturned'] = det_yr['num_overturned'] / det_yr['total_reviewed'].astype(np.float)
    det_yr.fillna(0, inplace=True)
    det_yr.drop(0, axis=0, inplace=True)

    pos = list(range(len(det_yr['ReportYear'])))
    width = 0.4

    fig, ax1 = plt.subplots(figsize=(12,6))

    ax1.bar(pos, det_yr['num_overturned'], width, alpha=0.5, color='g', label='Overturned')
    ax1.bar([p + width for p in pos], det_yr['num_upheld'], width, alpha=0.5, color='purple', label='Upheld')
    ax1.set_ylabel('Number of Reviews')
    ax1.set_xticks([p + 0.5 * width for p in pos])
    ax1.set_xticklabels(det_yr['ReportYear'])
    ax1.set_title('Independent Medical Review Outcomes by Report Year', fontsize=20, fontweight='bold')

    ax1.set_xlim(-0.5, 19)

    ax1.legend(loc='upper left', facecolor='white')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.grid(color=None, linestyle='None')
    ax1.set_facecolor('white')
    plt.rcParams['font.family'] = 'arial'

    # Share x-axis
    ax2=ax1.twinx()

    ax2.set_ylabel('% of Total Reviews that were Overturned')
    ax2.set_ylim(0,1)
    ax2.plot([p + width/2 for p in pos], det_yr['percent_overturned'], color='b', linestyle='--', linewidth=3, label='% - Overturned')

    ax2.legend(bbox_to_anchor=(0, 0, 0.167, 0.89), facecolor='white')
    ax2.grid(color=None, linestyle='None')
    plt.tight_layout()
    plt.show();


def plot_imr_results_by_age(dataset):
    '''
    Creates a clustered barplot comparing the IMR results by age group.

    Parameters
    ----------
    dataset : dataframe
        The dataset that is produced by the import_process_csv function.

    Returns
    -------
    '''
    fig, ax = plt.subplots(figsize=(12,6))
    age_order = ['0 to 10', '11 to 20', '21 to 30', '31 to 40', '41 to 50', '51 to 64', '65+']
    g = sns.countplot(x='AgeRange', data=dataset, order = age_order, hue='Determination', palette='Set1')
    g.legend().set_title(None)
    g.legend(['Overturned', 'Upheld'],facecolor='white', loc = 'upper left')
    g.set(xlabel='Age Range', ylabel='Count')
    g.set_title("Independent Medical Review Determinations by Patient Age", fontsize=20, fontweight='bold')
    sns.despine(top=True, bottom=True, left=True, right=True)
    sns.set(font='Arial')

    # Formatting hack to resolve "grey facecolor and grid lines" default setting.
    g.grid(color=None, linestyle='None')
    g.set_facecolor('white')
    plt.tight_layout()
    plt.show();

def calc_prcnt_overturned_by_age(dataset):
    '''
    Calculates the percentage of IMRs that resulted in an "overturned" decision by age group.

    Parameters
    ----------
    dataset : dataframe
        The dataset that is produced by the import_process_csv function.

    Returns
    -------
    age_grpd : dataframe
        A dataframe summarizing the results of the reviewers' decisions by age group.

    '''


    age_grpd = dataset.groupby(['AgeRange', 'Determination']).agg({'Determination':'count'}).unstack()

    age_grpd.rename({'Overturned Decision of Health Plan': 'overturned', 'Upheld Decision of Health Plan':'upheld'},
                axis=1, inplace=True)
    age_grpd.reset_index(inplace=True, col_level=1)
    age_grpd = age_grpd.droplevel(0, axis=1)
    age_grpd['prcnt_overturned'] = age_grpd['overturned'] / (age_grpd['overturned'] + age_grpd['upheld'])
    return age_grpd

def plot_imr_results_by_gender(dataset):
    '''
    Creates a clustered barplot comparing the IMR results by gender.

    Parameters
    ----------
    dataset : dataframe
        The dataset that is produced by the import_process_csv function.

    Returns
    -------
    '''

    fig, ax = plt.subplots(figsize=(12,5))
    g = sns.countplot(x='PatientGender', data=imr2, hue='Determination')
    ax.set_title('IMR Results by Patient Gender', fontsize=20, fontweight='bold')
    g.legend().set_title(None)
    sns.despine(top=True, bottom=True, left=True, right=True)
    sns.set(font='Arial')
    plt.tight_layout();
    ax.grid(color=None, linestyle='None')
    ax.set_facecolor('white')
    plt.tight_layout()
    plt.show();

def plot_imr_results_by_reason_for_procedure(dataset):
    '''
    Creates a clustered barplot comparing the IMR results by reason for procedure.

    Parameters
    ----------
    dataset : dataframe
        The dataset that is produced by the import_process_csv function.

    Returns
    -------
    '''

    plt.figure(figsize=(12,5))
    sns.countplot(x='Type', data=dataset, hue='Determination')
    plt.title('IMR Results by Reason for Procedure', fontsize=20, fontweight='bold')
    plt.tight_layout()
    plt.show()

def plot_imr_results_by_patient_diagnosis(dataset):
    '''
    Creates a clustered barplot comparing the IMR results by patient diagnosis.

    Parameters
    ----------
    dataset : dataframe
        The dataset that is produced by the import_process_csv function.

    Returns
    -------
    '''
    fig, ax = plt.subplots(figsize=(14,7))
    g = sns.countplot(x='DiagnosisCategory', data=imr2, hue='Determination')
    ax.set_title('Determination Results by Patient Diagnosis Category', fontsize=20, fontweight='bold')
    ax.tick_params(labelrotation=90)
    plt.tight_layout()
    plt.show()

def plot_imr_results_by_treatment_category(dataset):
    '''
    Creates a clustered barplot comparing the IMR results by treatment category.

    Parameters
    ----------
    dataset : dataframe
        The dataset that is produced by the import_process_csv function.

    Returns
    -------
    '''
    fig, ax = plt.subplots(figsize=(14,7))
    g = sns.countplot(x='TreatmentCategory', data=imr2, hue='Determination')
    ax.set_title('Determination Results by Treatment Category', fontsize=20, fontweight='bold')
    ax.tick_params(labelrotation=90)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    imr = import_process_csv()

    # Product EDA
    plot_imr_results_annual_trend(imr)
    plot_imr_results_by_age(imr)
    plot_imr_results_by_gender(imr)
    plot_imr_results_by_patient_diagnosis(imr)
    plot_imr_results_by_reason_for_procedure(imr)
    plot_imr_results_by_treatment_category(imr)

    results_by_age = calc_prcnt_overturned_by_age(imr)
    print(results_by_age)
