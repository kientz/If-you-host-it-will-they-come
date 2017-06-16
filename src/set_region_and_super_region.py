import pandas as pd


def define_regions():
    regions = {}
    regions['Great Lakes']=['IL','IN','MI','MN','OH','WI']
    regions['Central Midwest']=['IA','KS','MO','ND','OK','NE','SD']
    regions['Mid-Atlantic']=['DC','DE','KY','MD','VA','WV']
    regions['Mountain States']=['CO','MT','UT','WY']
    regions['Northwest']=['AK','ID','OR','WA']
    regions['South-Central']=['AR','LA','MS','TX']
    regions['Southeast']=['AL','FL','GA','NC','SC','TN']
    regions['Northeast']=['CT','MA','ME','NH','NJ','NY','PA','RI','VT']
    regions['Southwest']=['AZ','CA','HI','NV','NM']
    regions['Eastern Canada']=['NB','NL','NS','ON','PE','QC']
    regions['Northern Canada']=['NT','NU','YT']
    regions['Western Canada']=['AB','BC','MB','SK']
    regions['Mexico/Caribbean']=['PR','VI']

    #Define the Super regions as a dictionary
    superregions={}
    superregions['Northeast']=['CT','ME','MA','NJ','NH','NY','PA','RI','VT']
    superregions['Midwest']=['IL','IN','IA','KS','MI','MN','MO','OH','NE','ND','SD','WI']
    superregions['South']=['FL','GA','NC','SC','VA','WV','MD','DE','AL','KY','MS','TN','AR','LA','OK','TX','DC']
    superregions['West']=['AK','AZ','CA','CO','HI','ID','MT','NV','NM','OR','UT','WA','WY']
    superregions['Eastern Canada']=['NB','NL','NS','ON','PE','QC']
    superregions['Northern Canada']=['NT','NU','YT']
    superregions['Western Canada']=['AB','BC','MB','SK']
    superregions['Mexico/Caribbean']=['PR','VI']


    state_to_code = {'Alabama' : 'AL', 'Alaska' : 'AK', 'Arizona' : 'AZ',
    'Arkansas' : 'AR', 'California' : 'CA', 'Colorado' : 'CO',
    'Connecticut' : 'CT', 'Delaware' : 'DE', 'District of Columbia' : 'DC',
    'Florida' : 'FL', 'Georgia' : 'GA', 'Hawaii' : 'HI',
    'Idaho' : 'ID', 'Illinois' : 'IL', 'Indiana' : 'IN',
    'Iowa' : 'IA', 'Kansas' : 'KS', 'Kentucky' : 'KY',
    'Louisiana' : 'LA', 'Maine' : 'ME', 'Maryland' : 'MD',
    'Massachusetts' : 'MA', 'Michigan' : 'MI', 'Minnesota' : 'MN',
    'Mississippi' : 'MS', 'Missouri' : 'MO', 'Montana' : 'MT',
    'Nebraska' : 'NE', 'Nevada' : 'NV', 'New Hampshire' : 'NH',
    'New Jersey' : 'NJ', 'New Mexico' : 'NM', 'New York' : 'NY',
    'North Carolina' : 'NC', 'North Dakota' : 'ND', 'Ohio' : 'OH',
    'Oklahoma' : 'OK', 'Oregon' : 'OR', 'Pennsylvania' : 'PA',
    'Rhode Island' : 'RI', 'South Carolina' : 'SC', 'South Dakota' : 'SD',
    'Tennessee' : 'TN', 'Texas' : 'TX', 'Utah' : 'UT',
    'Vermont' : 'VT', 'Virginia' : 'VA', 'Washington' : 'WA',
    'West Virginia' : 'WV', 'Wisconsin' : 'WI', 'Wyoming' : 'WY'}

    #Set up the postal code to State Dictionary as well
    code_to_state = {y:x for x,y in state_to_code.items()}


    regions2 = {}
    regions2['Great Lakes']=['Illinois','Indiana','Minnesota','Michigan','Ohio','Wisconsin']
    regions2['Central Midwest']=['Iowa','Kansas','Missouri','North Dakota','Oklahoma','Nebraska','South Dakota']
    regions2['Mid-Atlantic']=['District of Columbia','Delaware','Kentucky','Maryland','Virginia','West Virginia']
    regions2['Mountain States']=['Colorado','Montana','Utah','Wyoming']
    regions2['Northwest']=['Alaska','Idaho','Oregon','Washington']
    regions2['South-Central']=['Arkansas','Louisiana','Mississippi','Texas']
    regions2['Southeast']=['Alabama','Florida','Georgia','North Carolina','South Carolina','Tennessee']
    regions2['Northeast']=['Connecticut','Massachusetts','Maine','New Hampshire','New Jersey','New York','Pennsylvania','Rhode Island','Vermont']
    regions2['Southwest']=['Arizona','California','Hawaii','Nevada','New Mexico']
    #regions2['Eastern Canada']=['NB','NL','NS','ON','PE','QC']
    #regions2['Northern Canada']=['NT','NU','YT']
    #regions2['Western Canada']=['AB','BC','MB','SK']
    #regions2['Mexico/Caribbean']=['PR','VI']

    #Define the Super regions as a dictionary
    superregions2={}
    superregions2['Northeast']=['Connecticut','Maine','Massachusetts','New Jersey','New Hampshire','New York','Pennsylvania','Rhode Island','Vermont']
    superregions2['Midwest']=['Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Ohio','Nebraska','North Dakota','South Dakota','Wisconsin']
    superregions2['South']=['Florida','Georgia','North Carolina','South Carolina','Virginia','West Virginia','Maryland','Delaware','Alabama','Kentucky','Mississippi','Tennessee','Arkansas','Louisiana','Oklahoma','Texas','District of Columbia']
    superregions2['West']=['Alaska','Arizona','California','Colorado','Hawaii','Idaho','Montana','Nevada','New Mexico','Oregon','Utah','Washington','Wyoming']
    #superregions2['Eastern Canada']=['NB','NL','NS','ON','PE','QC']
    #superregions2['Northern Canada']=['NT','NU','YT']
    #superregions2['Western Canada']=['AB','BC','MB','SK']
    #superregions2['Mexico/Caribbean']=['PR','VI']

    return superregions2, superregions, regions, regions2, state_to_code, code_to_state

def set_regions(df):
    '''This function will take in a data frame and classify each user
    into a few predetermined regions.
    We've defined 14 Regions (geographically) and 8 Super Regions (larger)
    Two columns are added to the data frame and populated with the region classifier
    '''

    #Define the regions as a dictionary
    superregions2, superregions, regions, regions2, state_to_code, code_to_state = define_regions()





    def find_key(input_dict, value):
        ''' Function to determine the region (key) based on the value in the dictionary
        '''
        return next((k for k, v in input_dict.items() if value in v), 'International')

    #Add columns to data frame
    df['regions']=''
    df['superregions']=''

    print("setting region data for each row")
    for i in range(len(df)):
        '''step though all rows
        get region and super region based on postal code
        '''

        df['regions'][i]=find_key(regions,df['state'][i])
        df['superregions'][i]=find_key(superregions,df['state'][i])

    return df

    #write new dataframe with region data


if __name__ == '__main__':
    df = pd.read_excel('../data/ConferenceStates.xlsx')
    df3 = set_regions(df)
    print("Writing CSV file with regions identified")
    df3.to_csv('conferencestates_with_regions.csv')
