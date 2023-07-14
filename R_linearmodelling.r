dataset = read.csv("regrex1.csv")
# Here are the import statements
library(ggplot2)

# Fitting Linear Regression to the Dataset

model = lm(formula = y ~ x,
               data = dataset)

# Visualizing the scatter plot. 
#png ("R_scatterplot.png")
ggplot() +
    geom_point(aes(x = dataset$x, y = dataset$y),
                   colour = 'red') +
    ggtitle('y vs x') +
    xlab('x') +
    ylab('y')
#dev.off()

#Visualizing the Linear Regression results
#png ("R_linearmodelling.png")
library(ggplot2)
ggplot() +
    geom_point(aes(x = dataset$x, y = dataset$y),
             colour = 'red') +
    geom_line(aes(x = dataset$x, y = predict(model, newdata = dataset)),
            colour = 'blue') +
    ggtitle('y vs x') +
    xlab('x') +
    ylab('y')
#dev.off()

summary(model)


