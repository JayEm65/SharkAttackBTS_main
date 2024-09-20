Team Update on Code Refinement & Next Steps (v0.5)
Hey team,
I've gone through our code once more to streamline and restructure our workflow, bringing in some changes and updates based on our last discussions and findings. Here's a quick recap of what's been adjusted in v0.5:
Setup Enhancements:
Included import re to aid in the 'time' column cleaning, prepping for regex applications.
Overview Update:
Renamed our initial overview cell to "Preview of raw DataFrame:" for better clarity before cleaning process.
Added a columns printout step to quickly visualize the available data points.
DataFrame Prep:
Removed "Species " from our columns-to-drop list as part of our DF cleaning prep.
Created a copy of the DataFrame (df_copy) earlier in the process for cleaner handling.
'Type' Column Cleaning:
Optimized our approach here by moving the df.copy() operation directly into our initial data cleaning preparation for efficiency, as mentioned.
'Time' Column Adjustments:
Made minor adjustments to comments for consistency across our documentation style.
'Age' Column Refinement:
Ensured uniform tonality in comments, providing a clearer guide through the cleaning steps implemented.
Added a "Subsequent overview" cell at the bottom of the code, to highlight the current state of the DataFrame.
Given these adjustments, here's where we currently stand cleaning-wise and what's left for cleanup:
Columns Pending Further Cleaning
'date'
'year'
'activity'
'country'
'state'
Particular Note on 'country' and 'state':
We considered merging 'country' and 'state' into a singular 'location' column. This aims to enhance our geographic data precision without risking data loss from dropping NaNs.
Missing values:
'country': 37 missing
'state': 398 missing
Next Steps:
As soon as they're ready I'll integrate the cleaning strategies for 'date', 'year', and 'type', as well as our approach to creating a 'location' column (depending on our solution), in the upcoming v0.6.
A Note on Uniformity in Commentary:
As we advance, I'd like to ask for maintaining a uniform tonality across our cell commentary. This consistency not only enhances readability but also ensures our documentation remains clear and accessible to all team members and future reviewers. Let's keep an eye on this as we make further updates and revisions.
Looking forward to our discussion and your insights as we finish our cleaning process.
Marc