find_pos <- function(v, x) {
    for (i in seq_along(v)) {
        cat("i = ", i, "\n")
        if (v[i] >= x) {
            return(i)
        }
    }
}

v <- c(1, 3, 5, 7)
print(find_pos(v, 8))