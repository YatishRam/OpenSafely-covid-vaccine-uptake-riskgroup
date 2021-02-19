args = commandArgs(trailingOnly=TRUE)

measures_folder <- "./output/measures/"
current_folder <- paste(measures_folder, args, sep="")

measures <- list.files(path = current_folder, pattern="*_stp.csv", full.names=TRUE, recursive=FALSE, ignore.case = TRUE)

filename = paste(paste(measures_folder, args, sep="/"), ".csv", sep="")

measure_count <- length(measures)

if (measure_count == 1){
	
	write.csv(read.csv(measures[1]), filename)

} else {
	
	library(plyr)
	import.list <- llply(measures, read.csv)	

	library(reshape)
	data <- merge_recurse(import.list)

	write.csv(data, filename)
}