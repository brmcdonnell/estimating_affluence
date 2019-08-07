# Estimating Zip Code Wealth
Utilizing Yelp and Zillow data to estimating wealth in a zip code.

<i>**Authors:** Alex Bell, Nate Gunawan, Paolo Natividad, Ben Hamilton & Brendan McDonnell</i>

## Problem Statement From : Utilizing Yelp cost estimates for estimating neighborhood affluency

*Problem Statement:* This tool will estimate the affluence of a neighborhood based on the number of $ of businesses and services (according to Yelp) in a given neighborhood. ($, $$, $$$) This tool will expect to get, as an input, a list of zip codes or names of neighborhoods and will estimate the wealth of the locality. While traditional methods typically estimate wealth of a locality based on demographic characteristics (e.g. income or unemployment rate), the novelty of this approach is in its use of big data related to commercial activity and cost of product and services as an indicator for affluency.  

- [Github Link for DSI-DEN students' past work.](https://github.com/rbkim1990/yelp-client-project)
- [Github Link for DSI-LA students' past work.](https://github.com/jlian014/Clientproject_DSI_LA6)
- [Github Link for DSI-LA (2) students' past work.](https://github.com/hovikgas/hovieco)
- [Github Link for DSI-NYC students' past work.](https://github.com/twludlow/ga_project_4)
- Feel free to use this as a reference or to build on top of it. **Make sure to provide credit where credit is due!!**

## The Organization:

<a href="https://newlighttechnologies.com/" target="_blank">New Light Technologies</a> is a small, award-winning organization based in Washington, D.C. that provides solutions to government, commercial, and non-profit clients. NLT is a team of dedicated technologists, scientists, engineers, designers, and strategists working on some of the most interesting, challenging, and important assignments in the world, ranging from disaster response to enabling growing telecommunications networks to providing healthcare to Americans. Some of the organizations they work with include FEMA (the Federal Emergency Management Agency), USAID (the United States Agency for International Development), the U.S. Census Bureau, and The World Bank.

<a href="https://newlighttechnologies.com/staff/ran-goldblatt/" target="_blank">Ran Goldblatt</a>, our contact with NLT, is a remote sensing scientist and senior consultant. He has a strong background in geographic information systems (GIS) and leverages this knowledge when solving problems facing various agencies.

## Executive summary

In this case study, we'll be attempting to use social media to predict "affluence" of ZIP codes. Through doing this, organizations such as FEMA who focus on emergency management will we able to effectively identify which neighborhoods are high-need in a real time manner. Our data will be collected primarily through Yelp (through their Yelp Dataset Challenge) as well as augmented through Zillow data. This case aims to utilize various techniques: feature engineering, Pandas manipulation, and unsupervised learning to generate the best possible model.
 
Features were extracted from the yelp data include counts of review, 1 dollar sign, 2 dollar signs, 3, dollar signs, and 4 dollar signs locations. Aggregates of if the restaurant takes credit cards or has bike parking were also engineered. Zillow was also used as a source of features. Mean prices from 2018 and 2019 were used as features. Additional features include whether or not a Whole Foods is in the zip code, whether or not a Trader Joes is in the zip code, and whether or not a Core Power Yoga in in the zip code.
 
Regression and Classification models were created with this data. For the regression we used median household income as our target. We a linear regression model and a gradient boosting model. The linear regression model had a training R2 value of 0.44. The testing R2 value was 0.27. For the gradient boosting model, we had an R2 training value of 0.775 and a testing R2 value of 0.456. The baseline accuracy of the classification model was 60.3%. We used 3 models: logistic regression, a gradient boosted classifier, and a support vector classifier. The logistic regression training accuracy was 70.14% and its testing accuracy was 67.63%. For the gradient boosted classifier, the training accuracy was 100% and its test accuracy was 70.4%. For the support vector classifier, the training accuracy was 74.4% and the test accuracy was 66.1%

## Target Engineering

As far as target engineering goes, we started with economic data from a couple of primary sources; the <a href="https://www.psc.isr.umich.edu/dis/census/Features/tract2zip/" target="_blank">American Community Survey (ACS), as compiled by the Population Studies Center at U of M<a/> and the <a href="https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2016-zip-code-data-soi" target="_blank">Internal Revenue Service (IRS)<a/>. For the regression target, we used median household income from the ACS. This seemed fairly intuitive, and provides a fairly agreeable measure for <i>relative</i> affluence. After training a model with this as the target, we began testing and creating new targets to see if there was a more relevant target to be found in the data we had collected. We tried several different measures from the IRS data, such as average salaries and wages, average net capital gains, Adjusted Gross Income (AGI), and median household income, all weighted by the sum percentage of returns that featured capital gains, tax on investment income, or qualified dividends, believing that these might be correlated with affluence. Unfortunately, using these composite targets produced models that performed at or below baseline, so we resorted back to median household income. Little work was done on this target aside from normalizing the distribution with a boxcox transformation. For the classification model, we started by defaulting to the AGI classes defined by the IRS. Again, we attempted to find a better target. Namely, we took our normalized median household income distribution and divided it into six fairly balanced classes; 1: more than 1 standard deviation below the mean; 2: more than 0.5 but less than 1 standard deviation below the mean; 3: less than 0.5 standard deviations below the mean; 4: less than 0.5 standard deviations above the mean; 5: more than 0.5 but less than 1 standard deviation above the mean; and 6: more than 1 standard deviation above the mean. Again, this target performed notably worse than our original and was scrapped.
  
  ## Presentation Slides
  
  <a href="https://docs.google.com/presentation/d/1wh55Op-UXg36VAV6k9DAHs-9myA2-MPoeqJknqfOuUo/edit" target="_blank">View the presentation slides for more information.</a>

 

