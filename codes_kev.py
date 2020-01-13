"""
This is a guide of some usefull codes for data analysis

:: Index ::
- Slicing DataFrames

"""

# =============================================================================
# =============================================================================
# ==================     SLICING A DATAFRAME       ============================
# =============================================================================
# =============================================================================
# =============================================================================

# Droping values that does not met the condition using the index
df.drop(df[df['column'] != 'value'].index, inplace = True)

# Create DF with rows on a selected condition
df = df[df.column != 'value']  # Condition can be numeric or whatever
df = df[(df['League'] == 'LCK') | (df['League'] == 'NALCS') | (df['League'] == 'EULCS')] # Multiple conditions, where pipe "|" works as "or" to join each condition

# Using query as in sql to select rows base on Condition
df = df.query("Column != 'value'") # If the value is a string must be between quotes otherwise if it's number just put the values as it came on the DF
df = df.query("Column1 != 'value1' and Column2 == 54") # Example for multiple conditions
    """ .query() works as where in sql statement """

# =============================================================================
# =============================================================================
# ==================     GROUPING A DATAFRAME      ============================
# =============================================================================
# =============================================================================
# =============================================================================

# Using .groupby()

df.groupby('column').sum()

df.groupby(['Column1','Column2']).count()

df.groupby(['column0']).agg({'column1':'count','column2':'count'})

df.groupby('Season')['Year'].count() # Returns a series

df.groupby('Season')['Year','Season'].count() # Returns a DF with only the year and season
""" When we put a selection between brackets [] outside of the parentheses we tell the function that only return that selection in the grouped data """
df.groupby(['Season','Year']).count() # Return all the columns

# Using melting to group multiple columns into a single one
"""
Sometimes we have a DF where we want to group multiple columns in a single one. For example the Df below where we want ban_# columns as
one unique column, that's where we use .melt() from pandas.
	League	Year	Season	ban_1	ban_2	ban_3	   ban_4	ban_5
0	NALCS	2015	Spring	Rumble	Kassadin Lissandra	NaN	      NaN
1	NALCS	2015	Spring	Tristana Leblanc Nidalee	NaN	       NaN
2	NALCS	2015	Spring	Kassadin Sivir	Lissandra	NaN	       NaN
3	NALCS	2015	Spring	RekSai	Janna	Leblanc	    NaN	       NaN
4	NALCS	2015	Spring	JarvanIV Lissandra	Kassadin NaN	    NaN
"""
df = df.melt(id_vars=('Year','Season','League'), value_vars=['ban_1','ban_2','ban_3','ban_4','ban_5'])
"""
What the code above tries to do is setting columns in id_vars as index columns or key columns and the value_vars
is going to join the columns in it into a single one, returning in this case de next DF:
	Year	Season	League	variable	value
0	2015	Spring	NALCS	ban_1	  Rumble
1	2015	Spring	NALCS	ban_1     Tristana
2	2015	Spring	NALCS	ban_1     Kassadin
3	2015	Spring	NALCS	ban_1	  RekSai
4	2015	Spring	NALCS	ban_1	  JarvanIV

Droping the variable column and we stay with the following DF:
	Year	Season	League	value
0	2015	Spring	NALCS	Rumble
1	2015	Spring	NALCS	Tristana
2	2015	Spring	NALCS	Kassadin
3	2015	Spring	NALCS	RekSai
4	2015	Spring	NALCS	JarvanIV
"""

# =============================================================================
# =============================================================================
# ==========     REPLACE VALUES IN COLUMN BASE ON CONDITION      ==============
# =============================================================================
# =============================================================================
# =============================================================================
df['column'] = np.where(kills_info['column'] != 0, 1, 0)
"""
What we are telling is that where 'column' has a value different form 0 we'll sustitute for 1,
otherwise we sustitute for a 0.
We can use string or whatever value to set the conditions
"""
