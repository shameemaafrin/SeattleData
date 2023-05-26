library(ggplot2)
install.packages("plotly")
library(plotly)

treedata <- read.csv(file = "trees.csv",as.is=TRUE, header=TRUE)
treedata

#1
str(treedata)
sort(treedata$GROWSPACE)

Growspace=treedata$GROWSPACE
hist(Growspace,col="darkgreen",main="GROWSPACE FOR TREES",xlim = c(0,300))                                   # Draw histogram
abline(v = mean(Growspace),                       
       lwd = 3)
abline(v = median(Growspace),                       
       col = "blue",
       lwd = 3)

mean(treedata$GROWSPACE)
median(treedata$GROWSPACE)
#2

CABLES<-treedata$CABLED
g<-ggplot(data.frame(treedata$CABLED), aes(x=CABLES)) +
  geom_bar(fill="darkblue")
WIRED<-treedata$WIRES
ggplot(data.frame(treedata$WIRES), aes(x=WIRED)) +
  geom_bar(fill="lightblue")
ggplot(treedata, aes(WIRES, CABLED,fill=Rec.no.)) +
  geom_bar(stat="identity", position = "dodge") +
  labs(title="WIRED VS CABLED")


#3
p = ggplot(treedata,aes(x=CONDITION_RATING,y=OWNERSHIP))  +
  ggtitle("CONDITION BASED ON OWNERSHIP") +
  xlab("Rating based on condition (0-5)") +
  ylab("Owner")
p1 = p + geom_point()
p2 = p + geom_point(alpha = 0.1, colour="red") +
  theme_bw()
plot(p2)

#4
names(treedata)
model1 <- lm(treedata$CONDITION_RATING~treedata$PRIMARYDISTRICTCD)
model1
summary(model1)











