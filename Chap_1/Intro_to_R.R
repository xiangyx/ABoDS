
# Variable & Type -----------------------------------------------------------

a <- 2
b <- 5.0
x <- "Hello World"

print(a)
print(b)
cat(x, "\n")

c <- a * 2 + b
print(c)

print(typeof(x))
print(typeof(c))

# Functions-----------------------------------------------
fun1 <- function(x) {
    x^x
}
cat(fun1(2), "\n")

fun2 <- function() {
    cat("Input and output are not needed here. \n")
}
fun2()

fun3 <- function(x, base = 10) {
    log(x, base)
}
cat("base: 10,", fun3(10), "\n")
cat("base: 2,", fun3(2, 2), "\n")
cat("base:", exp(1), ",", fun3(exp(1), exp(1)), "\n")
cat("base: 2,", fun3(base = 2, 2), "\n")

fun4 <- function(x) {
    if (x >= 0) 
        return(x)
    else
        return(-x) 
}
print(fun4(10))
print(fun4(-10))

fun5 <- function(x) {
    if (x > 0)
        return("positive")
    else if (x < 0)
        return("negative")
    else 
        return("zero")
}
cat(fun5(10), "\n")
cat(fun5(-10), "\n")
cat(fun5(0), "\n")

# For loop
for(i in 1:3) {
    print(i)
}
print(typeof(1:3))

# While loop
i <- 1
while(i <= 3) {
    print(i)
    i <- i + 1
}

# Next/Break
cat("-------\n")
for(i in 1:3) {
    if (i == 2) next
    print(i)
}
cat("-------\n")
for(i in 1:3) {
    if (i == 2) break
    print(i)
}
cat("-------\n")

# Built-in Data Structures-------------------------------
## Vectors
x = 1:5
y = "Another Hello World!"
print(length(x))
print(length(y))
print(nchar(y))
print(x[-1])
print(x[0])
print(x[length(x) + 1])
print(length(integer(0)))
print(length(NA))
print(rep(x, times = 5))
print(rep(x, each = 5))
cat("-------\n")

# Array
array1 <- array(1:9, c(3, 3))
array2 <- array(1:6, c(3, 2))
print(class(array1))
print(array2)
print(array1 %*% array2)
cat("-------\n")