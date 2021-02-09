import pandas as pd
import pathlib

DATA_DIR_NAME = "data"
INPUT_FILE_BASE = 'waste'
INPUT_FILE_SUFFIX = 'orig'
OUTPUT_FILE_SUFFIX = 'processed'

# %%
def read_input_file():
    # get relative data folder
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath(DATA_DIR_NAME).resolve()
    
    return pd.read_csv(
        DATA_PATH.joinpath(f"{INPUT_FILE_BASE}_{INPUT_FILE_SUFFIX}.csv"))

def write_output_file():
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath(DATA_DIR_NAME).resolve()
    
    return df.to_csv(
        DATA_PATH.joinpath(f"{INPUT_FILE_BASE}_{OUTPUT_FILE_SUFFIX}.csv"))

# %%
df = read_input_file()

# %%  Adding true datetime column
# need to remove extraneous spaces from some month entries
df['month'] = df['month'].str.strip()
df['year'] = df['year'].astype(str)
df['date'] = pd.to_datetime(df[['year', 'month']].agg('-'.join, axis=1),
                            format='%Y-%B')
df.sort_values(by='date', inplace=True)
df.set_index('date', inplace=True)


# %%  formatting issues preventing certain columns from automatically importing
#     as numeric
df['waste_this_month'] = df['waste_this_month'].str.strip()
df['waste_this_month'] = pd.to_numeric(
    df['waste_this_month'], errors='coerce')

df['share_of_commingled_volume'] = \
    df['share_of_commingled_volume'].str.strip('% ')
df['share_of_commingled_volume'] = pd.to_numeric(
    df['share_of_commingled_volume'], errors='coerce')


# %% clean up the 'bill_description' and 'description' columns.  Canonicalize values.
#    also couldn't resist fixing some typos (generally in 'bill_description',
#    tweaking to match 'description')

# copy existing columns for reference purposes
df['bill_desc_original'] = df['bill_description'].copy()
df['desc_original'] = df['description'].copy()

# the "from" (key) is the one with fewer instances in the dataset,
# being mapped into the "to" (value) which generally has more instances
# also took 'description' into account and matched that where it seemed to make sense
bill2canonical = {
    '102 Cresap/Russian/Slevic': '108 Cresap House',
    '108 Cresap/Russian/Slevic': '108 Cresap House',
    '108 Cresap/Russian/Slev': '108 Cresap House',
    'Aerospace Res. Lab': 'Aerospace Research Lab',
    'Aerospace Research Laborat': 'Aerospace Research Lab',
    'Aerospace Research Labory': 'Aerospace Research Lab',
    'Aerospace Research Laboratory': 'Aerospace Research Lab',
    'Balz-Dobie House': 'Balz-Dobie',
#    'Bice House Container': 'Bice House',   # not certain about this one
    'Bookstore/Central Grounds Parking': 'Bookstore/Central Grounds',
    'CafãÂÃÂ© N @ Law School': 'Cafe N @ Law School',
    'CafãÂÃÂ© N. @ Law School': 'Cafe N @ Law School',
    "Carr's Hill/Pres Hou": "Carr's Hill/Pres House",
    "Carr's Hill/Pres Housese": "Carr's Hill/Pres House",
    'Casa Bolivar/Spanish': 'Casa Bolivar Spanish',
    'Chemistry Bldg': 'Chemistry Building',
    'Chemistry': 'Chemistry Building',
    'Collanande Alley': 'Collanade Alley',
    'Copeely Apts 510 Seymour': 'Copeley Apts 510 Seymour',
    'Copeley 1 285 Peyton': 'Copeley Apts 285 Peyton',
    'Copeley 1 304 Peyton': 'Copeley Apts 304 Peyton',
    'Copeley 1 410Seymour': 'Copeley Apts 410 Seymour',
    'Copeley 1 448Seymour': 'Copeley Apts 443 Seymour',  # probably
    'Copeley 1 475Seymour': 'Copeley Apts 475 Seymour',
    'Copeley 1 499Seymour': 'Copeley Apts 499 Seymour',
    'Copeley 1 510Seymour': 'Copeley Apts 510 Seymour',
    'Copeley 1 547Seymour': 'Copeley Apts 547 Seymour',
    'Copely Seymour 210': 'Copeley Apts 210 Seymour',
    'Copeley Seymour 210': 'Copeley Apts 210 Seymour',
    'Dillard&Gooch Dorms': 'Gooch Dillard Dorms',
    'Dillard Gooch Dorms': 'Gooch Dillard Dorms',
    'East Lawn Green Alley Pav Iv': 'East Lawn Green Alley Pav',
    'East Lawn Rotunda Alley Pav II': 'East Lawn Rotunda Alley Pa',
    'Env. Health & Safety': 'Env Health & Safety',
    'Fontainer Res. Park': 'Fontaine Rsch Park',
    'Fontana Food Ctr': 'Fontana Food Center',
    'Gooch': 'Gooch 382',
    'Hereford Colleg Low': 'Hereford College Low',
    'High Energy Physics Lab': 'High Energy Lab',
    'Humprhreys & Echols': 'Humphreys & Echols',
    'Interntational House': 'International House',
    'Intranural Sports': 'Intramural Sports',
    'Jag School': 'JAG School',
    'Jag School Addition': 'JAG School Addition',
    'John P Jones': 'JPJ',
    'John Paul Jones': 'JPJ',
    'Jpj': 'JPJ',
    'Kcrc Cochran House': 'KCRC Cochran House',
    'Kcrc Commwlth Ct': 'KCRC Commonwealth Court',
    'Kcrc': 'KCRC',
    'Kcrc Commonwealth Court': 'KCRC Commonwealth Court',
    'Kellogg Dorm': 'Kellogg House',
    'Klockner Stadium UVA': 'Klockner Stadium',
    'Law/ Withers-Brown': 'Law/Withers-Brown',
    'Mccormick Observ.': 'Mccormick Observatory',
    'Mccue Center': 'Frank C McCue Ctr',
    'Frank C Mccue Ctr': 'Frank C McCue Ctr',
    'Mcguffey Alley': 'McGuffey Alley',
    'Mcleod Hall': 'McLeod Hall',
    'Metcalf/ Lefevre Hse': 'Metcalf/Lefevre House',
    'Metcalf Lefevre House': 'Metcalf/Lefevre House',
    'Move In Fl': 'Move In (Front Load)',
    'Mr4 - West': 'Mr4 West',
    'New Child Care Ctr': 'New Child Care Center',
    'New Childcare Center': 'New Child Care Center',    
    'Ollson Hall': 'Olsson Hall',
    'Outdoor Rec Center': 'Outdoor Rec. Center',
    'Physics': 'Physics Building',
    'Physics Bldg': 'Physics Building',
    'Polic Bldg': 'Police Building',
    'Police Bldg': 'Police Building',
    'Police Headquarters': 'Police Building',
    'Printing Services': 'Printing Service Center',
    'Reactor': 'Reactor Building',
    'Reactor Bldg': 'Reactor Building',
    'Seig Building': 'Sieg Warehouse',
    'Sponsors Hall': "Sponsor's Hall",
    'Student Activities': 'Student Activities Building',
    'Student Activities Buildin': 'Student Activities Building',
    'The Park - Support Facilit': 'The Park',
    'Transitionalcarehosp': 'Transitional Care Hospital',
    'University Garden': 'University Gardens',
    }

df['bill_description'] = df['bill_description'].str.strip()
# Attempt to canonicize capitalization
df['bill_description'] = df['bill_description'].str.title()
# many instances where rows have '[name]' vs. similar others with 'UVA [same name]'.
# Easiest to remove the 'UVA ' (which is now 'Uva' from the call to title() )
df['bill_description'] = df['bill_description'].str.replace('^Uva ', '', regex=True)
# some instances where rows have '[name]' vs. similar others with 'UVA RL [same name]'.
# Removing the 'UVA RL ' (which is now 'Rl ' from previous substitutions )
df['bill_description'] = df['bill_description'].str.replace('^Rl ', '', regex=True)
# Restore any remaining (interior) 'Uva' to glory as 'UVA'
df['bill_description'] = df['bill_description'].str.replace('Uva', 'UVA', regex=False)
# also undo the capital 'S' after apostrophe side effect from str.title()
df['bill_description'] = df['bill_description'].str.replace("'S", "'s", regex=False)
# once more for the roman numerals
df['bill_description'] = df['bill_description'].str.replace("Ii", "II", regex=False)
df['bill_description'] = df['bill_description'].str.replace("iii", "III", regex=False)
df['bill_description'] = df['bill_description'].str.replace("ii", "II", regex=False)
df['bill_description'] = df['bill_description'].str.replace("IIi", "III", regex=False)

for from_name, to_name in bill2canonical.items():
    df.loc[df['bill_description'] == from_name, 'bill_description'] = to_name

# 'description' column is in much better shape
desc2canonical = {
    'Balze-Dobie': 'Balz-Dobie',
    'CafãÂÃÂ© N @ Law School': 'Cafe N @ Law School',
    'CafãÂÃÂ© N. @ Law School': 'Cafe N @ Law School',
    }

for from_name, to_name in desc2canonical.items():
    df.loc[df['description'] == from_name, 'description'] = to_name

# Try again to clean up one particular pesky value
df.description = df.description.replace(
    regex={r'Caf.*Law School': 'Cafe N @ Law School'})

# for convenience in examining results
dfb = df['bill_description'].value_counts()
dfd = df['description'].value_counts()

print(f"bill_description value_counts Before: {len(df['bill_desc_original'].value_counts())}")
print(f"bill_description value_counts After: {len(df['bill_description'].value_counts())}")

print(f"description value_counts Before: {len(df['desc_original'].value_counts())}")
print(f"description value_counts After: {len(df['description'].value_counts())}")

# %%  Reorder columns

df = df[['building_number', 'month', 'year', 'container_type', 'service_type',
       'bill_description', 'description', 'bill_desc_original', 'desc_original',
       'container_quantity',
       'volume_per_container', 'weekly_pickups', 'volume_collected_per_week',
       'total_volume_per_week', 'waste_stream', 'share_of_commingled_volume',
       'total_commingled_waste', 'waste_this_month',
       ]]

# %%  Final output
write_output_file()
