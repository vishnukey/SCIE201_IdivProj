library("jsonlite")

png(file = "genders.jpg")

data = read_json("../../data/censusPretty_newGeom.geojson", simplifyVector = TRUE)
genders <- c(data$totals$'male',data$totals$'fem')
pie(genders,
        labels = as.character(genders),
        radius = 1,
        main = "Age distribution of children",
        #col = rainbow(length(genders)))
        col = c('#0000FF', '#FF0000')
)

legend(
        "bottomright",
        as.character(c('male', 'female')),
        cex = 0.8,
        fill = c('#0000FF', '#FF0000')
)
dev.off()
