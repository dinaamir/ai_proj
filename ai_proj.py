import streamlit as st
import pandas as pd
from PIL import Image

# Image.open('mmu.png').con vert('RGB').save('mmu.jpeg')
mmuImg = Image.open('mmu.png')
st.image(mmuImg, width=300)
st.title("TIC3151 - AI Project")
st.text('Done by: \n Nur Adlina Marini Binti Amir Suharman \t 1181100317 \n Tala Maan Altaifi \t \t         1191302030 \n Pavitra A/P Sankar \t \t         1191303322')

# Create a sidebar page dropdown 
page = st.sidebar.selectbox("Choose your question number", ["Q1 - Vacation Planner", "Q2 - Vaccine Distribution Modelling", "Q3 - Loan Application Modeling"]) 

if page == "Q1 - Vacation Planner":
    st.markdown("# Q1 - Vacation Planner")
    st.write('The goal is to optimize the vacation experience with fixed amount of money and fixed duration using **Genetic Algorithm (GA)**')

    st.markdown("## Scenario")
    st.write('As for the scenario, the criteria or the parameters are as below:')
    dfParam = pd.DataFrame({'Parameter': [  'moneyOnHand', 
                            'vacDur', 
                            'hotelRatePerNight', 
                            'tourSpots', 
                            'oneTourSpots', 
                            'mealsPerDay', 
                            'foodPrice', 
                            'transFees', 
                            'transFreq'], 
            'Description': ['Fixed amont of money or budget for a vacation in RM',
                            'Fixed vacation duration in days',
                            'Hotel star rating per night in RM',
                            'Number of tourist spots visited',
                            'Price for one tourist spot in RM',
                            'Number of meals eaten per day',
                            'Food price per meal in RM',
                            'Transportation fees per trip',
                            'Transport frequency per day']})
    st.dataframe(dfParam)

    st.markdown("## Individuals & Population")
    st.write('We first get the suggested solution by creating an individual member of the population. In our current problem, the individual function will return the total spend for **hotel**, **tour**, **food**, and **transportation**.')
    code1 = '''
            def individual(vacDur,hotelRatePerNight,tourSpots,oneTourSpots,mealsPerDay,foodPrice,transFees,transFreq):
                hotel = randint(150, hotelRatePerNight) * vacDur      
                tour = randint(100, oneTourSpots) * tourSpots         
                food = randint(8, foodPrice) * mealsPerDay            
                transportation = randint(5, transFees) * transFreq    

                return [hotel, tour, food, transportation]
            '''
    st.code(code1, language='python')
    st.write('The collection of all individuals is referred to as our population.')
    code2 = '''
            def population(count,vacDur,hotelRatePerNight,tourSpots,oneTourSpots,mealsPerDay,foodPrice,transFees,transFreq):
                return [individual(vacDur,hotelRatePerNight,tourSpots,oneTourSpots,mealsPerDay,foodPrice,transFees,transFreq) for x in range(count)]
            '''
    st.code(code2, language='python')

    st.markdown("## Fitness Score")
    st.write('Next step is to assess or to evaluate the fitness of each individual. For our problem, we want the fitness score to be a function of the differences between the sum of spendings and the amount of money on-hand (balance money).')
    code3 = '''
            def fitness(individual, moneyOnHand):
                spent = sum(individual)
                return abs(moneyOnHand - spent) 
            '''
    st.code(code3, language='python')
    st.write('**0 difference** is the **best solution** that we aim to get (moneyOnHand - spent = RM0)')

    st.markdown("## Evolution")
    st.write('To advance the population from one generation to the next, we evolve the population by performing the selection, crossover, and mutation methods. The choices of value to be the *retain*, *random_select*, and *mutate* parameter will effect the evolution result.')
    st.write('***retain***         : The probability to get the top individuals in a population of count to be parents')
    st.write('***random_select***  : The probability to randomly select some lesser performing individuals to be parents')
    st.write('***mutate***         : The probability to randomly modify each individual')
    code4 = '''
            def evolve(pop, moneyOnHand, retain, random_select, mutate):
                ...
                return parents
            '''
    st.code(code4, language='python')

    st.markdown("## Testing it Out!")
    dfScenario1 = pd.DataFrame({
            'Parameter': [  'Number of generations',
                            'Money 0n-hand', 
                            'Vacation duration', 
                            'Hotel rate per night', 
                            'Tourist spots', 
                            'Price for one tourist spot', 
                            'Meals per day', 
                            'Food price', 
                            'Transportation fees', 
                            'Transportation frequency'], 
            'Value': ['100',
                            'RM5000',
                            '5',
                            'RM150 ~ RM250',
                            '6',
                            'RM100 ~ RM300',
                            '3',
                            'RM8 ~ RM20',
                            'RM5 ~ RM100',
                            '10']})
    st.write('Say, we have the scenario of:')
    st.dataframe(dfScenario1, None, 400)

    dfs1 = pd.read_csv (r'fitnessScore1.csv')   
    dfs2 = pd.read_csv (r'fitnessScore2.csv')   
    dfs3 = pd.read_csv (r'fitnessScore3.csv')   
    
    evoChoose = st.sidebar.radio("Choose the tweaked parameter set", ("Tweaked Parameter #1","Tweaked Parameter #2","Tweaked Parameter #3"))
    if evoChoose == "Tweaked Parameter #1":
        st.write('We set the *retain*, *random_select*, and *mutate* parameter as:')
        st.write('***retain***         : 0.2 (20%)')
        st.write('***random_select***  : 0.05 (5%)')
        st.write('***mutate***         : 0.01 (1%)')

        ## 1. PASTE THE DATAFRAME HERE
        st.dataframe(dfs1, None, 500)
        ## 2. CONCLUSION
        st.write('With 20% survival (plus an additional 5% of other individuals) and 1% mutation, it took 33 generations to reach an optimal solution of 24.00')

    elif evoChoose == "Tweaked Parameter #2":
        st.write('We set the *retain*, *random_select*, and *mutate* parameter as:')
        st.write('***retain***         : 0.3 (30%)')
        st.write('***random_select***  : 0.1 (10%)')
        st.write('***mutate***         : 0.05 (5%)')

        ## 1. PASTE THE DATAFRAME HERE
        st.dataframe(dfs2, None, 500)
        ## 2. CONCLUSION
        st.write('With 30% survival (plus an additional 10% of other individuals) and 5% mutation, it took 62 generations to reach an optimal solution of 0.38')
        

    elif evoChoose == "Tweaked Parameter #3":
        st.write('We set the *retain*, *random_select*, and *mutate* parameter as:')
        st.write('***retain***         : 0.4 (40%)')
        st.write('***random_select***  : 0.08 (8%)')
        st.write('***mutate***         : 0.03 (3%)')

        ## 1. PASTE THE DATAFRAME HERE
        st.dataframe(dfs3, None, 500)
        ## 2. CONCLUSION
        st.write('With 40% survival (plus an additional 8% of other individuals) and 3% mutation, it took 49 generations to reach an optimal solution of 0.22')
        
    
elif page == "Q2 - Vaccine Distribution Modelling":
    st.markdown("# Q2 - Vaccine Distribution Modelling")

    ### ---------------------------------------------------- CSP ----------------------------------------------------- 
    st.markdown("## Introduction")
    st.write("The goal here is to be able to assign the right amount and type of vaccine for each center type in each. With constraints on the max capacity of vaccines for each center and state in mind, we performed Constraint Satisfaction Problem (CSP) to extarct the optimal solutions.")

    stateOption = st.sidebar.radio('Choose a state number:', ['State 1 (ST-1)', 'State 2 (ST-2)', 'State 3 (ST-3)', 'State 4 (ST-4)', 'State 5 (ST-5)'])
    ## 1. STATE 1
    if stateOption == 'State 1 (ST-1)':
        st.markdown("## State 1")
        st.write("Taking the max capacity of vaccines for the state in mind, we have added the needed constraints to finally get the optimal solutions for each center.")

        st.markdown("### Center 1")
        ST1CR1 = Image.open('ST1CR1.png')
        st.image(ST1CR1)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")
        
        st.markdown("### Center 2")
        ST1CR2 = Image.open('ST1CR2.png')
        st.image(ST1CR2)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 3")
        ST1CR3 = Image.open('ST1CR3.png')
        st.image(ST1CR3)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 4")
        ST1CR4 = Image.open('ST1CR4.png')
        st.image(ST1CR4)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 5")
        ST1CR5 = Image.open('ST1CR5.png')
        st.image(ST1CR5)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

    ## 2. STATE 2
    elif stateOption == 'State 2 (ST-2)':
        st.markdown("## State 2")
        st.write("Taking the max capacity of vaccines for the state in mind, we have added the needed constraints to finally get the optimal solutions for each center.")

        st.markdown("### Center 1")
        ST2CR1a = Image.open('ST2CR1a.png')
        ST2CR1b = Image.open('ST2CR1b.png')
        st.image(ST2CR1a)
        st.image(ST2CR1b)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 2")
        ST2CR2 = Image.open('ST2CR2.png')
        st.image(ST2CR2)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 3")
        ST2CR3 = Image.open('ST2CR3.png')
        st.image(ST2CR3)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 4")
        ST2CR4 = Image.open('ST2CR4.png')
        st.image(ST2CR4)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 5")
        ST2CR5 = Image.open('ST2CR5.png')
        st.image(ST2CR5)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

    ## 3. STATE 3
    elif stateOption == 'State 3 (ST-3)':
        st.markdown("## State 3")
        st.write("Taking the max capacity of vaccines for the state in mind, we have added the needed constraints to finally get the optimal solutions for each center.")

        st.markdown("### Center 1")
        ST3CR1 = Image.open('ST3CR1.png')
        st.image(ST3CR1)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 2")
        ST3CR2 = Image.open('ST3CR2.png')
        st.image(ST3CR2)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 3")
        ST3CR3 = Image.open('ST3CR3.png')
        st.image(ST3CR3)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 4")
        ST3CR4 = Image.open('ST3CR4.png')
        st.image(ST3CR4)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 5")
        ST3CR5 = Image.open('ST3CR5.png')
        st.image(ST3CR5)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

    ## 4. STATE 4
    elif stateOption == 'State 4 (ST-4)':
        st.markdown("## State 4")
        st.write("Taking the max capacity of vaccines for the state in mind, we have added the needed constraints to finally get the optimal solutions for each center.")

        st.markdown("### Center 1")
        ST4CR1 = Image.open('ST4CR1.png')
        st.image(ST4CR1)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 2")
        ST4CR2 = Image.open('ST4CR2.png')
        st.image(ST4CR2)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 3")
        ST4CR3 = Image.open('ST4CR3.png')
        st.image(ST4CR3)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 4")
        ST4CR4 = Image.open('ST4CR4.png')
        st.image(ST4CR4)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 5")
        ST4CR5 = Image.open('ST4CR5.png')
        st.image(ST4CR5)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

    ## 5. STATE 5
    elif stateOption == 'State 5 (ST-5)':
        st.markdown("## State 5")
        st.write("Taking the max capacity of vaccines for the state in mind, we have added the needed constraints to finally get the optimal solutions for each center.")

        st.markdown("### Center 1")
        ST5CR1 = Image.open('ST5CR1.png')
        st.image(ST5CR1)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 2")
        ST5CR2 = Image.open('ST5CR2.png')
        st.image(ST5CR2)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 3")
        ST5CR3 = Image.open('ST5CR3.png')
        st.image(ST5CR3)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 4")
        ST5CR4 = Image.open('ST5CR4.png')
        st.image(ST5CR4)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

        st.markdown("### Center 5")
        ST5CR5 = Image.open('ST5CR5.png')
        st.image(ST5CR5)
        st.write("To extarct the optimal solution, we filtered through the solutions and extract the outcomes where Vac-A < Vac-C < Vac-B. This logic follows the age grouping population since some certain age groups are more populated than others, and in this case, the population assigned to Vac-B are the majority, followed by Vac-C and lastly Vac-A.")

    
elif page == "Q3 - Loan Application Modeling":
    st.markdown("# Q3 - Loan Application Modeling")
    st.write()

    ### ----------------------------------------------------- Data Exploration ----------------------------------------------------- 
    st.markdown("## Data Exploration")
    st.markdown("### Descriptive Analysis")

    st.write("Before attempting to perform anything on the dataset, we first checked if there was any missing data to deaal with, and we came up with none.")

    st.write("We looked into the maximum monthly salary for each type of employee to see if there is any observable pattern.")
    emp_salary = Image.open('employee_salary.png')
    st.image(emp_salary)
    st.write("Based on the figure above, the distribution of the salary each employment type recieves is fairy equal amongst them all with the maximum amount ranging from 12,500RM to 13,000RM.")

    st.write("We also checked on the average loan amount for each type of employee.")
    loan_per_emp = Image.open('loan_per_emp.png')
    st.image(loan_per_emp)
    st.write("According to the plot, all types of employments seem to request similar amounts for a loan.")

    st.write("As for some areas of interest such as where the credit card months exceeded for each person is no more than one.")
    cc_exceed = Image.open('cc_exceed.png')
    st.image(cc_exceed)
    st.write("What we can see from the output above, it seems that employers and fresh graduates,coming from varied loan amounts and monthly salary, are the only types of employments who have not exceeded a month from not paying thier due amounts. ")

    st.write("Another area that peaked our interest was the worst performing employment type. To extract that we looked into the credit score, credit card exceeded months, and years to financial freedom for each person.")
    worst = pd.read_csv (r'worst_emp.csv')  
    dfCluster1 = pd.DataFrame(worst)
    st.write("After extraction, it shows the worst performing employment type is often the fresh graduate. We can make the assumption that due to the person just graduating, they may not have a solid job or a good paying job because of their lack of experience. this could explain their bad credit score, long overdue payment for the credit card, and many years left till they are debt free. ")

    st.markdown("### Outlier Detection")

    st.write("For detecting if there is any outliers in the attributes of our interest, we plotted box plots. ")
    out1 = Image.open('out1.png')
    st.image(out1)
    st.write("Based on the box plot above, there are no outliers for the attribute Loan_Amount in any of the employment types.")

    out2 = Image.open('out2.png')
    st.image(out2)
    st.write("According to the box plot, there are no outliers detected for the attribute Loan_Tenure_Year in any of the employment types.")

    out3 = Image.open('out3.png')
    st.image(out3)
    st.write("And according to the box plot for the attribute Montly_Salary, there seems to also lack any outliers here as well.")

    out4 = Image.open('out4.png')
    st.image(out4)
    st.write("As for the final attribute, Number_of_Properties, there are a few outliers detected employment types: government, employee, and fresh graduate, but due to its minority, we won't be doing anything to deal with the outliers.")


    st.markdown("### Correlation")
    st.write("Now, we are looking at possible relationships between attributes that fall under our area of interest.")

    corr1 = Image.open('corr1.png')
    st.image(corr1)
    st.write("When looking at the figure above, we can conclude that there is no correlation between the monthly salary and loan amounts requested.")
    
    corr2 = Image.open('corr2.png')
    st.image(corr2)
    st.write("We also thought there could potentially be a relationship between the loan tenure and the decision to accept or reject a loan, but there seems to be no correlation that can be found.")
    
    corr3 = Image.open('corr3.png')
    st.image(corr3)
    st.write("Based on the scatterplot, a conclusion can be formed that there is no relationship between the type of employment and their monthly salary, which was slightly hinted at in an above plot where almost all employment types' salaries are around the same amount.")
    
    corr4 = Image.open('corr4.png')
    st.image(corr4)
    st.write("According to the scatterplot above, there seems to also be no correlation between the number of properties the person owns and the decision to accept or reject the loan.")


    
    
    ### ----------------------------------------------------- Cluster Analysis ----------------------------------------------------- 
    st.markdown("## Cluster Analysis - KPrototype")
    st.write("For cluster analysis, K-Prototype Clustering algorithm will be chosen to cluster categorical as well as numerical variables. Instead of calculating within the sum of squares errors (WSSE) with Euclidian distance, K-Prototype provides the cost function that combines the calculation for numerical and categorical variables.")
    st.write("Based on the Bank Credit Score dataset, we aim to group them based on the ‘Employment_Type', 'State', and ‘Decision’ as categorical variables, 'Loan_Amount', 'Monthly_Salary', and 'Score' as numerical variable. ")

    # reading cluster centroids result
    dfc1 = pd.read_csv (r'dfCluster1.csv')   
    dfc3 = pd.read_csv (r'dfCluster3.csv')   
    dfc5 = pd.read_csv (r'dfCluster5.csv')   
    dfcost = pd.read_csv (r'dfCost.csv')   
    dfCluster1 = pd.DataFrame(dfc1, columns= ['Segment','Employment_Type','State','Decision','Loan_Amount','Monthly_Salary','Score'])
    dfCluster3 = pd.DataFrame(dfc3, columns= ['Segment','Employment_Type','State','Decision','Loan_Amount','Monthly_Salary','Score'])
    dfCluster5 = pd.DataFrame(dfc5, columns= ['Segment','Employment_Type','State','Decision','Loan_Amount','Monthly_Salary','Score'])
    dfCost = pd.DataFrame(dfcost, columns= ['Number of Clusters','Cost'])

    st.markdown("### Elbow Curve Method")
    st.write("Firstly, an optimal number of clusters, K, must be found. This can be done by plotting the Elbow Curve plot where K is selected when you observe an elbow-like bend with a lesser cost value. ")

    elbowImg = Image.open('elbow.png')
    st.image(elbowImg)
    st.write("If the plot looks like an arm, then the elbow on the arm is optimal k. In this case, 3 is the optimal number as clusters.")

    st.markdown("### Displaying Cluster Centroids")
    cost1 = "96639676873150.219"
    cost3 = "10715117234554.281"
    cost5 = "3855829605062.772"
    kChoose = st.sidebar.select_slider("Choose the number of clusters (k)", ("1","3","5"))
    if kChoose == "1":
        dfCluster1
        st.write('Cost score for k=1 :', cost1)

    elif kChoose == "3":
        dfCluster3
        st.write('Cost score for k=1 :', cost3)
        st.write('While all cluster groups are more likely to live in Kuala Lumpur, there is a split between all cluster groups when we look at the loan amount value. The people in cluster 3 has the least loan amount than the rest, however they (cluster 3) has the highest monthly salary among all clusters.')
        st.write("Fresh graduate, employer, and government as well as the 'Rejected' decision does not seem to be the majority in any of the cluster groups. ")

    elif kChoose == "5":
        dfCluster5
        st.write('Cost score for k=1 :', cost5)
        st.write("While all cluster groups are more likely to live in Kuala Lumpur, there is a split between all cluster groups when we look at the loan amount value. The people in Group 3 has the highest loan amount than the rest, however they (cluster 3) has the least monthly salary among all clusters.")
        st.write("Fresh graduate, employer, and government as well as the 'Rejected' decision does not seem to be the majority in any of the cluster groups. ")

    st.markdown("### Comparing The Cost Score")
    dfCost
    st.write("As number of clusters, k, increases, the cost score is approaching zero. Imagine if we set k to its maximum value n (where n is number of samples,) each sample will form its own cluster meaning that the cost value is equal to zero.")

    ### ------------------------------------------------------ Classification ------------------------------------------------------ 
    dfaccuracy = pd.read_csv (r'accuracy.csv')   
    dfprediction = pd.read_csv (r'Prediction.csv')  

    st.markdown("## Classification")
    st.write("For classification, we decided on predicting two attributes; *Decision* and *Employment_Type*. The algorithms chosen were decided based on training and testing multiple types of algorithms and extracting the the best performing two for each attribute predicted.")
    st.write("For the sake of accuracy and performance, we used LabelEncoder to encode the categorical data into numerical. Doing so has shown positive affects in the accuracy of the models later on.")

    attribute_Choose = st.sidebar.radio("Choose an attribute to predict ", ("Decision","Employement_Type"))
    if attribute_Choose == "Decision":
        st.markdown("### Predicting the *Decision*")
        st.write("For predicting the attribute *Decision*, the two best performing algorithms were **Decision Tree Classifier** and **K Neighbors Classifier**, so they were chosen to predict the decision.")

        st.markdown("### Decision Tree Classifier")
        st.write("The only parameter that made the overall accuracy higher for is *ccp_alpha* for the Decision Tree.")

        st.write('**Accuracy for score for the attribute *Decision*** :', dfaccuracy.loc[0,'Accuracy'])
        st.write('**Prediction 1 for *Decision*** :', dfprediction.loc[0,'Prediction'])
        st.write('**Prediction 2 for *Decision*** :', dfprediction.loc[1,'Prediction'])

        st.markdown("### K Neighbors Classifier")
        st.write("For K Neighbors Classifier, *n_neighbors* was the only parameter that highly affected the accuracy score.")

        st.write('**Accuracy for score for the attribute *Decision*** :', dfaccuracy.loc[1,'Accuracy'])
        st.write('**Prediction 1 for *Decision*** :', dfprediction.loc[2,'Prediction'])
        st.write('**Prediction 2 for *Decision*** :', dfprediction.loc[3,'Prediction'])
        
    elif attribute_Choose == "Employement_Type":
        st.markdown("### Predicting the *Employment_Type*")
        st.write("As for predicting the attribute *Decision*, the top two algorithms were **Decision Tree Classifier** and **Support Vector Machines (SVM)**, so they were decided upon to predict the type of employment.")

        st.markdown("### Decision Tree Classifier")
        st.write("To get the best parameters for the classifier, **GridSearchCV** was used. It helps to loop through predefined hyperparameters and fit our estimator (model) on our training set. So, in the end, we can select the best parameters from the listed hyperparameters.")

        st.write('**Accuracy for score for the attribute *Employement_Type*** :', dfaccuracy.loc[2,'Accuracy'])
        st.write('**Prediction 1 for *Employement_Type*** :', dfprediction.loc[4,'Prediction'])
        st.write('**Prediction 2 for *Employement_Type*** :', dfprediction.loc[5,'Prediction'])

        st.markdown("### Support Vector Machines (SVM)")
        st.write("The same concept was applied here. GridSearchCV was used to extract the best performing parameters that had made a positive influence on the accuracy.")

        st.write('**Accuracy for score for the attribute *Employement_Type*** :', dfaccuracy.loc[3,'Accuracy'])
        st.write('**Prediction 1 for *Employement_Type*** :', dfprediction.loc[6,'Prediction'])
        st.write('**Prediction 2 for *Employement_Type*** :', dfprediction.loc[7,'Prediction'])

