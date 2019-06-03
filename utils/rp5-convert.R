
corrds <- data.frame(
    locname = c("Floreat", "Mt. Barker", "Ankara", "Urfa", "Kuban", "Astrakan", "Tainan", "Hyderabad"),
    locabbr = c("per", "bar", "ank", "urf", "kub", "ast", "tai", "hyd"),
    lat = c(-31.935988, -34.629784, 39.920777, 37.215282, 45.43333333, 46.25000000, 23.11388889, 17.50777778),
    lon = c(115.780192, 117.666196, 32.854058, 38.737966, 40.56666667, 48.01666667, 120.29861111, 78.26944444)
)
59° 43' с.ш., 30° 25' в.д

frps <- list.files(path = "rp5", full.names = TRUE, include.dirs = FALSE, pattern="*csv")

qw <- lapply(frps, FUN=function(frp) {
	rpstn <- substr(frp, 5, 7)

	drp <- read.csv(frp, sep = ";", stringsAsFactors = FALSE, comment.char = "#", row.names = NULL)
	crp <- colnames(drp)
	colnames(drp) <- crp[-1]

	#strptime(drp[1,1], format = "%d.%m.%Y%t%R")
	drp_y <- format.Date(as.Date(drp[,1], format = "%d.%m.%Y%t%R"), format="%Y")
	drp_m <- format.Date(as.Date(drp[,1], format = "%d.%m.%Y%t%R"), format="%m")
	drp_d <- format.Date(as.Date(drp[,1], format = "%d.%m.%Y%t%R"), format="%d")
	drp_doy <- lubridate::yday(as.Date(drp[,1], format = "%d.%m.%Y%t%R"))

	list_y <- unique(drp_y)
	cat(rpstn, sum(drp$RRR == "No precipitation", na.rm = TRUE), sum(drp$RRR == "Trace of precipitation", na.rm = TRUE), sum(drp$RRR == "", na.rm = TRUE), '\n')
	if (sum(drp$RRR == "No precipitation", na.rm = TRUE) > 0) {drp[drp$RRR == "No precipitation",]$RRR = 0}
	if (sum(drp$RRR == "Trace of precipitation", na.rm = TRUE) > 0) drp[drp$RRR == "Trace of precipitation",]$RRR = 0
	cat(rpstn, sum(drp$RRR == "Осадков нет", na.rm = TRUE), sum(drp$RRR == "Следы осадков", na.rm = TRUE), sum(drp$RRR == "", na.rm = TRUE), '\n')
	if (sum(drp$RRR == "Осадков нет", na.rm = TRUE) > 0) {drp[drp$RRR == "Осадков нет",]$RRR = 0}
	if (sum(drp$RRR == "Следы осадков", na.rm = TRUE) > 0) drp[drp$RRR == "Следы осадков",]$RRR = 0
	if (sum(drp$RRR == "", na.rm = TRUE) > 0) drp[drp$RRR == "",]$RRR = 0

	dat_rpstn <- do.call("rbind", lapply(list_y, FUN=function(y) {
			idx = drp_y == y
			list_doy <- unique(drp_doy[idx])
			dat_y <- do.call("rbind", lapply(list_doy, FUN=function(oy) {
				drp_y_oy = drp[idx & drp_doy == oy,]
#				cat(oy, '\n')
				txc <- max(as.numeric(drp_y_oy$T), na.rm = TRUE)
				tmc <- min(as.numeric(drp_y_oy$T), na.rm = TRUE)
				tc <- mean(as.numeric(drp_y_oy$T), na.rm = TRUE)
				p <- max(as.numeric(drp_y_oy$RRR), na.rm = TRUE)
				year <- y
				mo <- mean(as.numeric(drp_m[idx & drp_doy == oy]), na.rm = TRUE)
				da <- mean(as.numeric(drp_d[idx & drp_doy == oy]), na.rm = TRUE)
				dl <- geosphere::daylength(corrds[corrds$locabbr == rpstn, 3], oy)
				return(data.frame(year, mo, da, p, tc, txc, tmc, dl))
			}))
			return(dat_y)
	}))

	write.csv(file = paste0("rp5_d/", rpstn, ".csv"), quote = FALSE, row.names = FALSE, dat_rpstn)
})


nfrps <- list.files(path = "noaa", full.names = TRUE, include.dirs = FALSE, pattern="*txt")

qw <- lapply(nfrps, FUN=function(frp) {
	rpstn <- substr(frp, 6, 8)

	drp <- read.csv(frp, sep = ",", stringsAsFactors = FALSE, comment.char = "#", row.names = NULL)
	crp <- colnames(drp)

	drp_y <- format.Date(as.Date(substr(drp[,3],1,4), format = "%Y"), format="%Y")
	drp_m <- substr(drp[,3],5,6)
	drp_d <- format.Date(as.Date(substr(drp[,3],7,8), format = "%d"), format="%d")
	drp_doy <- lubridate::yday(as.Date(paste0(substr(drp[,3],1,4), "-", substr(drp[,3],5,6), "-", substr(drp[,3],7,8)), format = "%Y-%m-%d"))
	p <- substr(drp[,20],1,4)
	tc <- drp[,4]
	txc <- gsub("*", "", drp[,18], fixed = TRUE)
	tmc <- gsub("*", "", drp[,19], fixed = TRUE)
	dl <- geosphere::daylength(corrds[corrds$locabbr == rpstn, 3], drp_doy)

	dat_rpstn <- data.frame(drp_y, drp_m, drp_doy, p, tc, txc, tmc, dl)
	for (i in 1:dim(dat_rpstn)[2]) dat_rpstn[,i] <- as.numeric(as.character(dat_rpstn[,i]))
	dat_rpstn$p = dat_rpstn$p * 25.4
	dat_rpstn$tc = 5.0 * (dat_rpstn$tc - 32.0) / 9.0
	dat_rpstn$txc = 5.0 * (dat_rpstn$txc - 32.0) / 9.0
	dat_rpstn$tmc = 5.0 * (dat_rpstn$tmc - 32.0) / 9.0
	write.csv(file = paste0("rp5_d/", rpstn, ".csv"), quote = FALSE, row.names = FALSE, dat_rpstn)
})

