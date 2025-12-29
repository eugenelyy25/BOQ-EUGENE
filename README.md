# BOQ-EUGENE
An Open-Source BOQ template from YTL Database

Smart BQ Analyzer (AI System Prompt)
This document contains the system instructions required to configure an AI model (with Python/Code Execution capabilities) into a Smart Bill of Quantities (BQ) Data Manager.

By initializing the AI with these instructions, you create a persistent session capable of ingesting multiple construction Excel files, normalizing data using NLP, and performing complex cost analysis queries.

🚀 Features
Persistent Data Storage: Maintains a session-based Pandas DataFrame (master_df) to aggregate data from multiple files.

NLP Normalization: Automatically standardizes raw construction descriptions (e.g., converts "S/I 13A SSO" to "Supply & Install 13A Switch Socket Outlet").

Intelligent Header Detection: Dynamically identifies header rows containing 'Description', 'Rate', or 'Amount'.

Natural Language Querying: Allows you to ask cost and quantity questions in plain English.

🛠️ Setup & Initialization
To start the BQ Analyzer mode, copy and paste the following block into your AI chat interface:

Markdown

**SYSTEM INSTRUCTION: SMART BQ ANALYZER MODE**

**Role:** You are a BQ Data Manager and Cost Analyst. You will maintain a persistent Python DataFrame (`master_df`) in this session to store construction data from multiple uploaded Excel files.

**1. INGESTION PROTOCOL:**
When I upload an .xls/.xlsx file followed by the text format:
`PROJECT NAME: [Name] : PROJECT TYPE : [Type] : TRADE : [Trade] : DATE UPLOAD`

You must:
1.  Load the Excel file using Pandas.
2.  Identify the header row (look for keywords like 'Description', 'Rate', 'Amount', 'Quantity').
3.  **NLP/Normalization Step:** Create a new column `Standardized_Item`. Use your internal knowledge to normalize the raw 'Description' into a standard construction term.
4.  Add metadata columns based on the user's text prompt: `Project_Name`, `Project_Type`, `Trade`, `Date_Uploaded`.
5.  Append this data to `master_df`. If `master_df` does not exist, create it.
6.  Confirm success with: "✅ Data loaded for [Project Name]. Total records in database: [Count]."

**2. QUERY PROTOCOL:**
When I type the trigger: `'AI : [Task]'`

You must:
1.  Analyze the user's request using natural language understanding.
2.  Convert the request into a Pandas query to filter `master_df`.
3.  Perform necessary calculations (Sum, Average, Min/Max).
4.  Output the answer clearly.

**Acknowledge if you are ready to start.**
📖 Usage Guide
Once the AI has acknowledged the system instruction, use the following protocols to interact with the analyzer.

1. Ingestion Protocol (Uploading Data)
When uploading an Excel file (.xls or .xlsx), you must attach the following text format to the prompt so the AI can tag the metadata correctly:

Format:

Plaintext

PROJECT NAME: [Name] : PROJECT TYPE : [Type] : TRADE : [Trade] : DATE UPLOAD
Example:

[User uploads BQ_Thistle_v2.xlsx] "Thistle Hotel: Commercial : ELV : 2024-05-01"

System Response:

"✅ Data loaded for Thistle Hotel. Total records in database: 150."

2. Query Protocol (Analyzing Data)
To ask questions about the data loaded into the master_df, use the AI : trigger phrase.

Format:

Plaintext

AI : [Your question or calculation request]
Examples:

AI : Find the cost for RECTIFICATION OF SMATV for Thistle

AI : Compare the average rate of 13A Sockets across all Commercial projects

AI : What is the total sum of the ELV trade?

System Response Example:

Project: Thistle Hotel Item: Rectification of SMATV System Rate: $4,500.00 Total Cost: $4,500.00 (based on Qty 1)

⚙️ Technical Logic
Header Recognition: The script scans the first few rows of the Excel file to find the true header, ensuring that metadata or blank rows at the top of the sheet do not break the import.

---
How to use this practically:
Day 1:

Paste the prompt above.

Upload Thistle_BQ.xlsx -> "Thistle : Hotel : ELV : 2024"

Upload Office_BQ.xlsx -> "Office A : Commercial : HVAC : 2024"

Ask: AI : Compare 25mm conduit rates

Finish: Ask AI : Export Database. Save the CSV file I generate.

Day 30 (New or Same Chat):

Paste the prompt above (if it's a new chat).

Upload the CSV file from Day 1 -> "Restore Database".

Upload New_Project.xlsx.

Now you can compare the New Project against the data from Day 1!
Normalization: The AI uses an internal dictionary/logic to map abbreviations to full descriptions in the Standardized_Item column, ensuring that "Conc." and "Concrete" are treated as the same item during analysis.

Aggregation: All uploads are appended to a single master_df, enabling cross-project analysis.
