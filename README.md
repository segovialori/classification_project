# Let's Predict Churn!
  
## Project Description: 
### Goals 
Customers are churning at an alarming rate at a telco company and they need our help finding out why!  Since it is more cost effective to keep our current customers, than recruit new ones, we will focus on determining what is driving our current customers away.  Our goal is to use machine learning to determine which customers have a higher probability of leaving us.  It is important to find which customers might leave us because by retaining our current customers we can increase our revenue.  

### Background
What is customer churn?
> "Churn rate (sometimes called attrition rate), in its broadest sense, is a measure of the number of individuals or items moving out of a collective group over a specific period. It is one of two primary factors that determine the steady-state level of customers a business will support." [https://en.wikipedia.org/wiki/Churn_rate]
> 
### Deliverables
1. Jupyter notebook report
2. README.md file
3. CSV file
4. Individula modules, .py files
5. Notebook presentation

### Data Dictionary:

| Feature               | Definition                                                                                                                                 | Data Type |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| customer_id           | unique identification number assigned to identify each customer                                                                            | string    |
| gender                | male or female                                                                                                                             | int       |
| senior_citizen        | 0 = not a senior citizen, 1 = is a senior citizen                                                                                          | int       |
| partner               | no = no partner, yes = has a partner                                                                                                       | int       |
| dependents            | no = no dependents, yes = has dependents                                                                                                   | int       |
| tenure                | The number of months the customer has had service (total_charges/monthly_charges)                                                          | int       |
| phone_service         | no = no phone service with current company, yes = phone service with company                                                               | int       |
| multiple_lines        | no = one phone line, yes = more than one phone line, no phone service = does not have phone service with current company                   | int       |
| internet_service_type | Internet service type the customer has: 0 = no service, 1 = DSL, 2 = Fiber Optic                                                           | int       |
| online_security       | no = has internet, but no online security service, yes = security service, no internet service = does not have internet service            | int       |
| online_backup         | no = has internet, but no online backup service, yes = online backup service, no internet service = does not have internet service         | int       |
| device_protection     | no = has internet, but no device protection service, yes = device protection service, no internet service = does not have internet service | int       |
| tech_support          | no = has internet, but no tech support serive, yes = tech support, no internet service = does not have internet service                    | int       |
| streaming_tv          | no = does not stream tv, yes = streams tv                                                                                                  | int       |
| streaming_movies      | no = does not stream movies, yes = streams movies                                                                                          | int       |
| contract_type         | 0 = month-to-month contract, 1 = 1 year contract, 2 = 2 year contract                                                                      | int       |
| paperless_billing     | no = no paperless billing, yes = paperless billing                                                                                         | int       |
| payment_type          | 1 = electronic check, 2 = mailed check, 3 = bank transfer (automatic), 4 = credit card (automatic)                                         | int       |
| monthly_charges       | Average monthly charges customer pays per month (total_charges/tenure)                                                                     | float     |
| total_charges         | Sum of all charges customer has incurred throughout lifetime of account                                                                    | float     |
| churn                 | no = has not left company, yes = has left company                                                                                          | int       |
| tenure                | number of months customer has been with company                                                                                            | float     |

## Hypotheses
1. Hypothesis 1: Does having fiber internet have any effect on customer churn?
2. Hypothesis 2: Does tech support have any effect on customer churn?

## Project Planning
### Acquire
- get data from codeup database using sql
### Prepare
- clean and prep data with a function so that it is ready for exploration
### Explore
- visualize relationships features have with the target (churn)
### Model
- establish baseline and test against 3 different models
### Conclusions
- determine the best model and key takeaways

## Reproduce
### Steps
1.  Fork or clone repo
2.  Download all modules into working directory
3.  Run the telco_churn_project notebook
