# Python-challenge
-----------------------------------------------------
Financial Analysis
-----------------------------------------------------
File has a header. Needed to skip using next(csvreader)
Tracker was established to retrieve total months.
Calculation for profit loss starting in column2, index 1
Track profit loss change, starting with integer in column2, index1 and subtracting the previous profit loss. Used append to track profit loss changes. Used .pop in average calclation removing 0 index. This helped in calculating average. 
Conditionals used to retrieve greatest increase in profits and greatest decrease in losses.
Used print text to capture key financial data points including total months, total amount, average change, Greatest increase and decrease in profits. 

-----------------------------------------------------
PyPoll
-----------------------------------------------------
File has a header. Needed to skip using next(csvreader).
Established candidate list and added tracker using .append taking index 2 and making it last element of the candidate list, resulting in 3 candidates.
Established 3 different sets by assigning letter values (x, y, z) and assinged them to unique candidate, vote count and vote percent respectively.
Used a max function to retrieve candidate with the highest total vote count.
Used print text to capture total votes, votes for each candidate, and announcing the winner. For loop (i) was used to capture all 3 candidates along with their respective totals, and the % of the total vote count.