if (!"EnvStats" %in% rownames(installed.packages())) {
  install.packages("EnvStats")
}
library(EnvStats)


check_outlier <- function(df){
  outlier_indexs <- NULL
  for (i in 6:13){
    values <- strtoi(df[, i], 16L)
    if(sum(!is.na(values)) < 3){
      print(paste("There is NO Outliers for Column:", colnames(df)[i]))
    }
    else{
      outlier_num <- length(boxplot.stats(values)$out)
      if(length(outlier_num) == 0){
        print(paste("There is NO Outliers for Column:", colnames(df)[i]))
      }
      else if(outlier_num < 2){
        print(paste("There is NO Outliers for Column:", colnames(df)[i]))
      }
      else{
        r_test <- rosnerTest(values, k = outlier_num)
        outlier_info <- r_test$all.stats[r_test$all.stats$Outlier, ]
        if(nrow(outlier_info) > 0){
          print(paste("Result of Rosner Test for Column:", colnames(df)[i]))
          print(outlier_info)
          outlier_indexs <- c(outlier_indexs, row.names(df)[outlier_info$Obs.Num])
        }
        else{
          print(paste("There is NO Outliers for Column:", colnames(df)[i]))
        }
      }
    }
  }
  return(outlier_indexs)
}
data <- read.csv("combine_normal_attack.csv")
unique_ids <- unique(data$ID)

outlier_indexs <- NULL
for (id in unique_ids){
  print(paste("Check Outliers for ID:", id))
  id_data <- data[data$ID == id, ]
  outlier_index <- check_outlier(id_data)
  outlier_indexs <- c(outlier_indexs, outlier_index)
  print("")
}
data$Is_Outlier <- 0
data$Is_Outlier[as.numeric(outlier_indexs)] <- 1
write.csv(data, "new_data.csv", row.names = F)