#Section: Define city and timeline

#set city variable
city_name = "Instanbul, Turkey"
#set start year
pop_1927 = 691000
#set end year
pop_2017 = 15029231

#Section: calculate annual percentage growth rate

#calculate population change
pop_change = pop_2017 - pop_1927
#print(pop_change)
#calculate percentage change
percentage_gr = ((pop_2017 - pop_1927)/pop_1927) * 100
#print(percentage_gr)
#calculate annual percentage growth
annual_gr = percentage_gr / (2017 - 1927)
#print(annual_gr)
#annual percentage growth function
def population_growth(year_one,year_two,population_one,population_two):
  growth_rate = (((population_two - population_one) / population_one)*100) / (year_two - year_one)
  return(growth_rate)

#Section: call functions

#call function for 1927 and 2017
set_one = round(population_growth(1927,2017,pop_1927,pop_2017),2)
#print(set_one)

#call function for 1950 and 2000
set_two = round(population_growth(1950,2000,983000,8831800),2)
#print(set_two)

#Section: final report out
report = "Istanbul grew by " + str(pop_change) + " from " + str(pop_1927) + " in 1927 to " + str(pop_2017) + "2017 - a rapid annual population growth rate of " +str(set_one) + "% - due to eastern expansion from Europe. Between 1950 and 2000, the annual growth rate slowed down to " + str(set_two) + "% as a result of war and famine."
print(report)