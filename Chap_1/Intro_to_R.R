
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

for (i in 1:10) {
    cat("This is ", i, "\n")
}