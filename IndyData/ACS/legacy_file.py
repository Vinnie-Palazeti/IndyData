# import pandas as pd

# def pop_condense(data, gender):
#     df = data.copy()
#     df[f'{gender} Pop Below 18'] = df.iloc[:,0:4].astype(int).sum(axis=1)
#     df[f'{gender} Pop 18 to 24'] = df.iloc[:,4:8].astype(int).sum(axis=1)
#     df[f'{gender} Pop 25 to 34'] = df.iloc[:,8:10].astype(int).sum(axis=1)
#     df[f'{gender} Pop 35 to 44'] = df.iloc[:,10:12].astype(int).sum(axis=1)
#     df[f'{gender} Pop 45 to 54'] = df.iloc[:,12:14].astype(int).sum(axis=1)
#     df[f'{gender} Pop 55 to 64'] = df.iloc[:,14:17].astype(int).sum(axis=1)
#     df[f'{gender} Pop 65+'] = df.iloc[:,17:23].astype(int).sum(axis=1)
#     return df

# def to_percent(data,total_data):
#     df = data.copy()
#     tots = total_data.copy()
    
#     vals = df.values / tots.values
    
#     return pd.DataFrame(vals, columns = df.columns, index = df.index)
    



# def query_data(state_code, vars_struct):
    
#     total_pop = vars_struct['Total Population']
#     year = '2019'
#     dsource = 'acs'
#     dname = 'acs5'
#     cols = 'NAME,' + total_pop
#     state = state_code
#     county = '*'
#     tract = '*'
#     rename = ['Total Population']
    
#     total_ = get_data(year, dsource, dname, cols, state, county, tract, rename)
    
#     cols = 'NAME'
#     names = get_name(year, dsource, dname, cols, state, county, tract)


#     # Male Population & Percent
#     col_names = ['Male ' + i for (i,v) in vars_struct['Population - Age']['Male'].items()]
#     col_codes = [v for (i,v) in vars_struct['Population - Age']['Male'].items()]

#     cols = 'NAME,' + ','.join(col_codes)
#     male_counts = get_data(year, dsource, dname, cols, state, county, tract, col_names)

#     male_counts = pop_condense(male_counts, 'Male')
#     male_perc = to_percent(male_counts, total_)

#     male_perc.columns = [i + ' Percent' for i in list(male_perc)]

#     # Female Population & Percent
#     col_names = ['Female ' + i for (i,v) in vars_struct['Population - Age']['Female'].items()]
#     col_codes = [v for (i,v) in vars_struct['Population - Age']['Female'].items()]

#     cols = 'NAME,' + ','.join(col_codes)
#     female_counts = get_data(year, dsource, dname, cols, state, county, tract, col_names)

#     female_counts = pop_condense(female_counts, 'Female')
#     female_perc = to_percent(female_counts,total_)

#     female_perc.columns = [i + ' Percent' for i in list(female_perc)]
    
    
#     total_population_by_age = pd.DataFrame(female_counts.values + male_counts.values, 
#                                            index = total_.index,
#                                            columns = male_counts.columns
#                                           )

#     total_population_by_age.columns = [i.replace('Male ',"Total ") for i in list(total_population_by_age)]

#     # Econ Cleaning

#     col_names = [i for (i,v) in vars_struct['Economic'].items()]
#     col_codes = [v for (i,v) in vars_struct['Economic'].items()]

#     cols = 'NAME,' + ','.join(col_codes)
#     econ_ = get_data(year, dsource, dname, cols, state, county, tract, col_names)

#     econ_['Income Below Poverty Line %'] = econ_['Income Below Poverty Line'] / econ_['Income Total Population']
#     econ_['Education: % Less than Highschool'] =  econ_['Education Attainment Less than Highschool'] / econ_['Education Attainment 18 to 64 Total']
#     econ_['Education: % Highschool Graduate'] =  econ_['Education Attainment Highschool Graduate'] / econ_['Education Attainment 18 to 64 Total']
#     econ_['Education: % Bachelors or Higher'] =  econ_['Education Attainment Bachelors Degree or Higher'] / econ_['Education Attainment 18 to 64 Total']

    
#     col_names = [i for (i,v) in vars_struct['Population - Race'].items()]
#     col_codes = [v for (i,v) in vars_struct['Population - Race'].items()]

#     cols = 'NAME,' + ','.join(col_codes)
#     pop_race = get_data(year, dsource, dname, cols, state, county, tract, col_names)
#     pop_race_percent = to_percent(pop_race,total_)
#     pop_race_percent.columns = [i + ' Percent' for i in list(pop_race_percent)]
    
#     # Population by sex
#     col_names = [i for (i,v) in vars_struct['Population - Sex'].items()]
#     col_codes = [v for (i,v) in vars_struct['Population - Sex'].items()]

#     cols = 'NAME,' + ','.join(col_codes)
#     pop_sex = get_data(year, dsource, dname, cols, state, county, tract, col_names)
#     pop_sex_percent = to_percent(pop_sex,total_)
#     pop_sex_percent.columns = [i + ' Percent' for i in list(pop_sex_percent)]
    
#     out_data = total_.join([female_counts,female_perc,male_counts,male_perc,total_population_by_age,econ_,pop_race,pop_race_percent,pop_sex,pop_sex_percent])
#     out_data = out_data.fillna(0.0)
    
#     out_data.to_csv(f'./data/storage/tabular_state_data/data_state_{state_code}.csv',compression='gzip')



#     