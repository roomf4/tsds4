# moy_hist.r

# This script should sum pctlead and groupby month of year
# This script should sum pctlead and groupby day   of week
# Demo:
# R -f moy_hist.r
# or
# source('moy_hist.r')

csv_l  = read.csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
summary(csv_l)

# I should convert my list into a Data Frame:
csv_df = data.frame(csv_l)

# For 30 years, I should get Date and Close:
df10 = csv_df[c(1:(252*30)), c("Date","Close")]

lead_v = c(c(df10$Close[1]), df10$Close)[1:length(df10$Close)]
df10$leadp = lead_v

df10$pctlead = 100.0*(df10$leadp - df10$Close)/df10$Close

df10$moy = format(as.Date(df10$Date),"%m")
df10$dow = format(as.Date(df10$Date),"%w")

head(df10)

agg_moy = aggregate(pctlead ~ moy, df10, sum)
print('Sum of pctlead groupby month of year:')
print(agg_moy)

agg_dow = aggregate(pctlead ~ dow, df10, sum)
print('Sum of pctlead groupby day of week:')
print(agg_dow)

# I should create a plot window of 2 rows and one col:
par(mfrow = c(2,1))

plot(agg_moy$pctlead ~ agg_moy$moy, type="h", col="blue", lwd=10)
grid()

plot(agg_dow$pctlead ~ agg_dow$dow, type="h", col="darkgreen", lwd=10)
grid()

