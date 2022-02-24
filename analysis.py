import numpy as np
import pandas as pd
import matplotlib as plt

debug = False;

df = pd.read_excel('data\Heights.xlsx')

# Two questions we want to answer:
# 1. What are the top 5 tallest countries for males and females (top 5 for each),
#    and what are the shortest 5 countries for males and females?
# 2. What is the continent with the tallest males, and what contintent has the
#    tallest females?

''' Question 1: top 5 tallest and shortest countries '''
# Convert cm to meters and to make it easier to understand
df['Male Height in Meters'] = df['Male Height in Cm'] / 100.00
df['Female Height in Meters'] = df['Female Height in Cm'] / 100.00

# Sort by male height
sorted_male = df.sort_values(
    by='Male Height in Meters',
    ascending=False
)
# Select top 5 rows
top_5_male_countries = sorted_male.head(5).loc[:, 'Country Name'].tolist()
top_5_male_heights  = sorted_male.head(5).loc[:, 'Male Height in Meters'].round(2).tolist()
# Select bottom 5 rows
bottom_5_male_countries = sorted_male.tail(5).loc[:,'Country Name'].tolist()
bottom_5_male_heights = sorted_male.tail(5).loc[:, 'Male Height in Meters'].round(2).tolist()

# Sort by female height
sorted_female = df.sort_values(
    by='Female Height in Meters',
    ascending=False
)
# Select top 5 rows
top_5_female_countries = sorted_female.head(5).loc[:, 'Country Name'].tolist()
top_5_female_heights = sorted_female.head(5).loc[:,'Female Height in Meters'].round(2).tolist()
# Select bottom 5 rows
bottom_5_female_countries = sorted_female.tail(5).loc[:,'Country Name'].tolist()
bottom_5_female_heights = sorted_female.tail(5).loc[:,'Female Height in Meters'].round(2).tolist()


# Display the results for question 1
print("***Question 1: What are the top 5 tallest and shortest countries \n" +
      "in the world, for men and women's heights?")
print()
# Top 5 male countries
print("Top 5 countries with highest average male heights")
for i in range(0,5):
    country = top_5_male_countries[i]
    print(str(i + 1) + ". " + country + ": \t" + str(top_5_male_heights[i]))
print()
# Top 5 female countries
print("Top 5 countries with highest average female heights")
for i in range(0,5):
    country = top_5_female_countries[i]
    print(str(i + 1) + ". " + country + ": \t" + str(bottom_5_male_heights[i]))
print()
# Bottom 5 male countries
print("Top 5 countries with lowest average male heights")
for i in range(0,5):
    country = bottom_5_male_countries[i]
    print(str(i + 1) + ". " + country + ": \t" + str(top_5_female_heights[i]))
print()
# Bottom 5 female countries
print("Top 5 countries with lowest average female heights")
for i in range(0,5):
    country = bottom_5_female_countries[i]
    print(str(i + 1) + ". " + country + ": \t" + str(bottom_5_female_heights[i]))
print()
print()

'''Question 2: tallest continents for males and females'''
# List of all North American countries
na_countries = ["Puerto Rico", "Canada", "Barbados", "Jamaica", "United States",
                "Lucia", "Dominican Republic", "Bahamas", "Costa Rica", "Greenland",
                "Saint Kitts and Nevis", "Cuba", "Haiti", "El Salvador", "Belize",
                "Mexico", 'Honduras','Nicaragua','Panama', 'Antigua and Barbuda',
                'Saint Lucia']
# List of all European countries
eu_countries = ["Netherlands", "Montenegro", "Estonia", "Bosnia and Herzegovina",
                "Iceland", "Denmark", "Czech Republic", "Latvia", "Slovakia",
                "Slovenia", "Ukraine", "Croatia", "Serbia", "Lithuania",
                "Poland", "Finland", "Norway", "Sweden", "Germany", "Bermuda",
                "Greece", "Belgium", "Ireland", "Andorra",
                "Switzerland", "Belarus", "France", "Austria", "Lexembourg",
                "United Kingdom", "Romania", "Hungary", "North Macedonia",
                "Spain", "Moldova", "Italy", "Malta", "Portugal", "Bulgaria",
                "Albania", "Cyprus", "Luxembourg"]
# List of all South American countries
sa_countries = ["Dominica", "Angigua and Barbuda", "Grenada",
                "Saint Vincent and the Grenadines", "Trinidad and Tobago", "Brazil",
                "Argentina", "Suriname", "Uruguay", "Paraguay", "Venezuela", "Chile",
                "Guyana", "Colombia", 'Guatemala','Peru','Ecuador', 'Bolivia']
# List of all Asian countries
asian_countries = ["Russia", "Turkey", "Israel", "Lebanon", "Georgia", "China",
                   "Iran", "South Korea", "Kazakhstan", "Palestine", "Kuwait",
                   "Jordan", "Hong Kong", "North Korea", "Turkmenistan",
                   "United Arab Emirates", "Azerbaijan", "Iraq", "Armenia", "Taiwan",
                   "Singapore", "Qatar", "Bahrain", "Japan", "Oman", "Kyrgyzstan",
                   "Syria", "Thailand", "Uzbekistan", "Mongolia", "Saudi Arabia",
                   'Timor-Leste', 'Laos', 'Nepal','Yemen','Bangladesh','Madagascar',
                   'Philippines','Cambodia','Brunei', 'India', 'Myanmar','Tanzania',
                   'Bhutan', 'Pakistan', 'Maldives', 'Sri Lanka','Tajikistan',
                   'Afghanistan','Vietnam', 'Malaysia', "Indonesia"]
# List of all African countries
african_countries = ["Tunisia", "Libya", "Morocco", "Senegal", "Seychelles",
                     "Algeria", "Mali", "Egypt", "Botswana", "Mauritius", "Cameroon",
                     "Sudan", "Burkina Faso", "Chad", "Nigeria", "Republic of the Congo",
                     "Somalia", "Djibouti", "Guinea", "Zimbabwe", "Eritrea", "Gabon",
                     "Kenya", "Sao Tome and Principe", "Ghana", 'Mozambique',
                     "Niger", "Togo", "Namibia", "South Africa","Eswatini",
                     "Central African Republic", "Ethiopia", "Uganda", "Angola",
                     "Benin", "Gambia", "Ivory Coast", "Equatorial Guinea",
                     "Guinea-Bissau", "Lesotho", "Comoros", "Zambia", "Burundi",
                     "Sierra Leone", "Rwanda", "Malawi", "Mauritania", "Liberia",
                     "DR Congo"]
# List of all Australia/Oceania countries
aus_countries = ["Australia", "Cook Islands", "French Polynesia", "New Zealand",
                 "Niue", "American Samoa", "Tokelau", "Tonga", "Samoa", "Fiji",
                 "Tuvalu", "Palau", 'Solomon Islands', 'Papua New Guinea',
                 'Marshall Islands', 'Vanuatu', 'Nauru','Micronesia', 'Kiribati']

# Sort heights by their continent
def sort_continent(country):
    if country in na_countries:
        return 'North America'
    elif country in eu_countries:
        return 'Europe'
    elif country in sa_countries:
        return 'South America'
    elif country in asian_countries:
        return 'Asia'
    elif country in african_countries:
        return 'Africa'
    elif country in aus_countries:
        return 'Australia/Oceania'
    return '?'

df["Continent"] = df['Country Name'].apply(sort_continent)
# Filter to average heights
male_continent_means = df.groupby('Continent').mean().round(2).sort_values(
    by="Male Height in Meters",
    ascending=False
).loc[:,'Male Height in Meters'].to_string()
female_continent_means = df.groupby('Continent').mean().round(2).sort_values(
    by="Female Height in Meters",
    ascending=False
).loc[:,'Female Height in Meters'].to_string()

# Display results
print("***Question 2: What continents have the highest average height \n" +
      "for males and females?")
print()
print("\t\tContinent means: ")
print()
print('Average male heights in meters based on continent:')
print()
print(male_continent_means)
print()
print()
print('Average female heights in meters based on continent:')
print()
print(female_continent_means)
