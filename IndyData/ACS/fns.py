
import requests
import pandas as pd


def get_data(year, 
             dsource, 
             dname, 
             variables, 
             state, 
             county, 
             tract,
            ):
    if variables:
        variable_names = [i for i,v in variables]
        variable_codes = [v for i,v in variables]
        codes = ',' + (',').join(variable_codes)
        
    if not variables:
        codes = ''
        
    codes = 'NAME' + codes

    base_url = f'https://api.census.gov/data/{year}/{dsource}/{dname}/'

    data_url = f'{base_url}?get={codes}&for=tract:{tract}&in=state:{state}&in=county:{county}'

    response = requests.get(data_url)
    data = pd.DataFrame(columns=response.json()[0], data=response.json()[1:])
    
    data['GEOID'] = data['state'] + data['county'] + data['tract']
    data['GEOID'] = data['GEOID'].astype(int)
    data = data.set_index('GEOID')
    
    if not variables:
        data['NAME'] = data['NAME'].str.split(',')
        data['tract_name'] = data['NAME'].apply(lambda row: row[0])
        data['tract_name'] = data['tract_name'].str.strip()
        data['county_name'] = data['NAME'].apply(lambda row: row[1])
        data['county_name'] = data['county_name'].str.strip()

    data = data.drop(columns =['NAME','state','county','tract'])
    
    if variables:
        data.columns = variable_names
        data = data.astype(int)
    
    data = data.sort_index()
    
    return data



def get_ACS(
    variable_dict,
    year = 2019,
    dsource = 'acs',
    dname = 'acs5',
    state = 18,
    county = '*',
    tract = '*'
):
    variables = [(i,v) for i,v in variable_dict.items()]
    
    if len(variables) > 15:
        groups = [variables[i:i + 15] for i in range(0, len(variables), 15)]
        df_list = []
        for grp in groups:
            tmp_data = get_data(
                year = year,
                variables = grp,
                dsource = dsource,
                dname = dname,
                state = state,
                county = county,
                tract = tract
            )
            df_list.append(tmp_data)
            
        data = pd.concat(df_list, axis=1)
        
    else:
        data = get_data(
            year = year,
            variables = variables,
            dsource = dsource,
            dname = dname,
            state = state,
            county = county,
            tract = tract
            )
        
    name_frame = get_data(
            year = year,
            variables = None,
            dsource = dsource,
            dname = dname,
            state = state,
            county = county,
            tract = tract
            )
    data = data.join(name_frame)
    data['year'] = year
    return data







