library("jsonlite")

png(file = "genders.jpg")

data = read_json("../../data/censusPretty_newGeom.geojson", simplifyVector = TRUE)
genders <- c(data$totals$'male',data$totals$'fem')
colours <- c('#5555FF', '#FF6666')
pie(genders,
        labels = as.character(genders),
        radius = 1,
        main = "Gender distribution of children in Calgary",
        #col = rainbow(length(genders)))
        col = colours
)

legend(
        "bottomright",
        as.character(c('male', 'female')),
        cex = 0.8,
        fill = colours
)
dev.off()
