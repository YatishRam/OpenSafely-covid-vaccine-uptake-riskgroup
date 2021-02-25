args = commandArgs(trailingOnly=TRUE)

measures_folder <- "./output/measures/"
current_folder <- paste(measures_folder, args, sep="")

cohorts <- list.files(path = current_folder, pattern=glob2rx("input*.csv", trim.head = FALSE, trim.tail = TRUE), full.names=TRUE, recursive=FALSE, ignore.case = TRUE)

for (cohort in cohorts){
	df <- read.csv(cohort)
	
	df <- transform(df, unstated_first_dose= ifelse(first_dose==1 & az_first_dose==0 & pf_first_dose==0 & mo_first_dose==0 & nx_first_dose==0 & jn_first_dose==0 & gs_first_dose==0 & vl_first_dose==0, 1, 0))
	df <- transform(df, unstated_second_dose= ifelse(second_dose==1 & az_second_dose==0 & pf_second_dose==0 & mo_second_dose==0 & nx_second_dose==0 & jn_second_dose==0 & gs_second_dose==0 & vl_second_dose==0, 1, 0))

	write.csv(df, cohort)
}
