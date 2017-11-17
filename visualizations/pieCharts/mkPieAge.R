library("jsonlite")

png(file = "ages.jpg")

data = read_json("../../data/censusPretty_newGeom.geojson", simplifyVector = TRUE)
ages <- c(data$totals$'15_19',data$totals$'5_14')
colours <- c("#55FF55", "#5555FF")
pie(ages,
        labels = as.character(ages),
        radius = 1,
        main = "Age distribution of children in Calgary",
        col = colours
)

legend(
        "bottomright",
        as.character(c('14_19', '5_14')),
        cex = 0.8,
        fill = colours
)
dev.off()
