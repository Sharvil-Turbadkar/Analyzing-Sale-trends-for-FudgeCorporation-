# Analyzing-Sale-trends-for-FudgeCorporation-
Constructed a Robust Model using ETL to make  business  decisions by analyzing Sale trends for Fudge Corporation  
The goal of the project is to integrate information from FudgeMart & FudgeFlix, analyze & identify patterns in Sales to 
improve Sales of FudgeCorporation and provide recommendations to boost business.

In order to extract insights from the data a set of rubrics were followed before vieweing the data on a  BI Tool

1)Data profiling was the first step where the requirements of the user were understood and business processes were identified accoridngly
Business processes are the operational activities performed by your organization. 
Business process events generate or capture performance metrics that translate into facts
in a fact table. Most fact tables focus on the results of a single business process

2)High Level Dimensional Modelling was done to turn functional business requirements into dimensional data warehouse (DDS)
specifications based on the Kimball technical architecture

3)Detailed Level Dimensional Modelling was done to create a formal table design for our FudgeFlix and FudgeMart DDS, including tables, keys, data types and indexes so we can create tables and indexes required for our star schemas (ROLAP)
4)Created a ROLAP schema using T-SQL that follows all the rules mentioned under High Level and Detailed Level Dimension Modelling  

5)Performed ETL using SSIS Tool

6)Performed Multidimensional data analysis by craeting MOLAP cubes using SSAS
Using ROLAP would require querying data from multiple tables. 
On the contrary, MOLAP has all possible combinations of data already stored in a multidimensional array
MOLAP can access this data directly. Hence, MOLAP is faster compared to Relational Online Analytical Processing (ROLAP)

7) Made Visualizations on Power-BI after brainstorming with teammates to make recommendations on how Fudge Corporation can increase its sales   
