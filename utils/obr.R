# maturity

pd <- read.csv('Vigna_-_VIR__Astrakhan_region_1910.csv', header = 1, stringsAsFactors = FALSE)

vdf_ast <- data.frame(cbind(pd[,3], pd[, 3], pd[,1], pd[,5],
		format.Date(as.Date("12.05.2018", format = "%d.%m.%Y"), format="'%Y-%m-%d'"),
		as.numeric(as.character(pd[, 30]))))

colnames(vdf_ast) <- c('name', 'geo_id', 'catnumber',  'origin_region', 'sowing', 'Dmaturity')

vdf_na <- is.na(vdf_ast$sowing) | is.na(vdf_ast$Dmaturity) | is.na(vdf_ast$catnumber)

vdf_ast <- vdf_ast[!vdf_na,]
vdf_ast$geo_id <- rep('Astrakhan', times = dim(vdf_ast)[1])
vdf_ast$sowing <- rep("'2018-05-12'", times = dim(vdf_ast)[1])
vdf_ast$Dmaturity <- as.numeric(as.character(vdf_ast$Dmaturity))

qqqq <- reshape(vdf_ast[,c(1,4,6)], idvar = "name", timevar = "origin_region", direction = "wide")
colnames(qqqq) <- gsub("Dmaturity.", "", gsub(" ", "_", colnames(qqqq), fixed = TRUE), fixed = TRUE)
rownames(qqqq) <- qqqq[,1]
qqqq <- qqqq[,-1]
for(i in 1:dim(qqqq)[2]) {
	q <- as.character(qqqq[,i])
	q[is.na(qqqq[,i])] <- 0
	q[!is.na(qqqq[,i])] <- 1
	qqqq[,i] <- as.numeric(q)
}

doy_ast <- as.numeric(format.Date(as.Date(vdf_ast$sowing, format="'%Y-%m-%d'"), format="%j"))
year_ast <- as.numeric(format.Date(as.Date(vdf_ast$sowing, format="'%Y-%m-%d'"), format="%Y"))
month_ast <- as.numeric(format.Date(as.Date(vdf_ast$sowing, format="'%Y-%m-%d'"), format="%m"))
response_ast <- as.numeric(vdf_ast$maturity)
geo_id_ast <- as.character(vdf_ast$geo_id)


pd <- read.csv('Vigna_-_VIR__Astrakhan_region_2014.csv', header = 1, stringsAsFactors = FALSE)

vdf_ast2 <- data.frame(cbind(pd[,4], pd[, 4], pd[,1], pd[,5],
		format.Date(as.Date("12.05.2018", format = "%d.%m.%Y"), format="'%Y-%m-%d'"),
		as.numeric(as.character(pd[, 6]))))

colnames(vdf_ast2) <- c('name', 'geo_id', 'catnumber',  'origin_region', 'sowing', 'Dmaturity')

vdf_na <- is.na(vdf_ast2$sowing) | is.na(vdf_ast2$Dmaturity) | is.na(vdf_ast2$catnumber)

vdf_ast2 <- vdf_ast2[!vdf_na,]
vdf_ast2$geo_id <- rep('Astrakhan', times = dim(vdf_ast2)[1])
vdf_ast2$sowing <- rep("'2018-05-12'", times = dim(vdf_ast2)[1])
vdf_ast2$Dmaturity <- as.numeric(as.character(vdf_ast2$Dmaturity))

qqqq <- reshape(vdf_ast2[,c(1,4,6)], idvar = "name", timevar = "origin_region", direction = "wide")
colnames(qqqq) <- gsub("Dmaturity.", "", gsub(" ", "_", colnames(qqqq), fixed = TRUE), fixed = TRUE)
rownames(qqqq) <- qqqq[,1]
qqqq <- qqqq[,-1]
for(i in 1:dim(qqqq)[2]) {
	q <- as.character(qqqq[,i])
	q[is.na(qqqq[,i])] <- 0
	q[!is.na(qqqq[,i])] <- 1
	qqqq[,i] <- as.numeric(q)
}

doy_ast2 <- as.numeric(format.Date(as.Date(vdf_ast2$sowing, format="'%Y-%m-%d'"), format="%j"))
year_ast2 <- as.numeric(format.Date(as.Date(vdf_ast2$sowing, format="'%Y-%m-%d'"), format="%Y"))
month_ast2 <- as.numeric(format.Date(as.Date(vdf_ast2$sowing, format="'%Y-%m-%d'"), format="%m"))
response_ast2 <- as.numeric(vdf_ast2$maturity)
geo_id_ast2 <- as.character(vdf_ast2$geo_id)

# flowering

pd <- read.csv('vigna_kuban_2018.csv', header = 1, stringsAsFactors = FALSE)

vdf_kub <- data.frame(cbind(pd[,3], pd[, 3], pd[,2], pd[,7],
		format.Date(as.Date("03.05.2018", format = "%d.%m.%Y"), format="'%Y-%m-%d'"),
		as.numeric(as.character(pd[, 18]))))

colnames(vdf_kub) <- c('name', 'geo_id', 'catnumber',  'origin_region', 'sowing', 'Dflowering50')

vdf_na <- is.na(vdf_kub$sowing) | is.na(vdf_kub$Dflowering50) | is.na(vdf_kub$catnumber)

vdf_kub <- vdf_kub[!vdf_na,]
vdf_kub$geo_id <- rep('Kuban', times = dim(vdf_kub)[1])
vdf_kub$sowing <- rep("'2018-05-03'", times = dim(vdf_kub)[1])
vdf_kub$Dflowering50 <- as.numeric(as.character(vdf_kub$Dflowering50))

pd <- read.csv('vigna_tainan_1984.csv', header = 1, stringsAsFactors = FALSE)

minicor <- read.csv('minicore_characterization.csv', header = 1, stringsAsFactors = FALSE)
minicor$VI.no. <- gsub("\t", "", minicor$VI.no., fixed = TRUE)
mmid <- match(pd$Pedigree, minicor$VI.no.)

pd <- cbind(pd[!is.na(mmid), ], minicor[mmid[!is.na(mmid)],])

pd$X[pd$characterization.year == "1984"] <- "28.08.1984"
pd$X[pd$characterization.year == "1985"] <- "17.09.1985"

vdf_tai <- data.frame(cbind(pd[,1], pd[, 1], pd[,1], pd[,16],
		format.Date(as.Date(pd[,10], format = "%d.%m.%Y"), format="'%Y-%m-%d'"),
		as.numeric(as.character(pd[, 6]))))

colnames(vdf_tai) <- c('name', 'geo_id', 'catnumber',  'origin_region', 'sowing', 'Dflowering50')

vdf_na <- is.na(vdf_tai$sowing) | is.na(vdf_tai$Dflowering50) | is.na(vdf_tai$catnumber)

vdf_tai <- vdf_tai[!vdf_na,]
vdf_tai$geo_id <- rep('Tainan', times = dim(vdf_tai)[1])

vdf_tai$Dflowering50 <- as.numeric(as.character(vdf_tai$Dflowering50))

pd <- read.csv('vigna_tainan_2018.csv', header = 1, stringsAsFactors = FALSE)

mmid <- match(pd$Pedigree,minicor$VI.no.)

pd <- cbind(pd[!is.na(mmid), ], minicor[mmid[!is.na(mmid)],])

vdf_tai2 <- data.frame(cbind(pd[,1], pd[, 1], pd[,1], pd[,12],
		format.Date(as.Date("21.09.2018", format = "%d.%m.%Y"), format="'%Y-%m-%d'"),
		as.numeric(as.character(pd[, 3]))))

colnames(vdf_tai2) <- c('name', 'geo_id', 'catnumber',  'origin_region', 'sowing', 'Dflowering50')

vdf_na <- is.na(vdf_tai2$sowing) | is.na(vdf_tai2$Dflowering50) | is.na(vdf_tai2$catnumber)
vdf_tai2 <- vdf_tai2[!vdf_na,]

vdf_tai2$sowing <- rep("'2018-09-21'", times = dim(vdf_tai2)[1])
vdf_tai2$geo_id <- rep('Tainan', times = dim(vdf_tai2)[1])

vdf_tai2$Dflowering50 <- as.numeric(as.character(vdf_tai2$Dflowering50))

pd <- read.csv('vigna_hyderabad_2016.csv', header = 1, stringsAsFactors = FALSE)

mmid <- match(pd$Pedigree,minicor$VI.no.)

pd <- cbind(pd[!is.na(mmid), ], minicor[mmid[!is.na(mmid)],])

vdf_hyd <- data.frame(cbind(pd[,1], pd[, 1], pd[,1], pd[,9],
		format.Date(as.Date("16.06.2016", format = "%d.%m.%Y"), format="'%Y-%m-%d'"),
		as.numeric(as.character(pd[, 2]))))

colnames(vdf_hyd) <- c('name', 'geo_id', 'catnumber',  'origin_region', 'sowing', 'Dflowering50')

vdf_na <- is.na(vdf_hyd$sowing) | is.na(vdf_hyd$Dflowering50) | is.na(vdf_hyd$catnumber)
vdf_hyd <- vdf_hyd[!vdf_na,]

vdf_hyd$sowing <- rep("'2016-06-16'", times = dim(vdf_hyd)[1])
vdf_hyd$geo_id <- rep('Hyderabad', times = dim(vdf_hyd)[1])

vdf_hyd$Dflowering50 <- as.numeric(as.character(vdf_hyd$Dflowering50))

vdf <- rbind(vdf_kub, vdf_tai, vdf_tai2, vdf_hyd)

vdf$name <- as.character(vdf$name)
vdf$catnumber <- as.character(vdf$catnumber)
vdf$origin_region <- as.character(vdf$origin_region)
vdf$origin_region <- gsub("Tyrkey", "Turkey", vdf$origin_region)
vdf$origin_region <- gsub("Tailand", "Thailand", vdf$origin_region)
vdf$origin_region <- gsub("Korea,_Republic_of", "Korea", vdf$origin_region)
vdf$origin_region <- gsub("Korea, Republic of", "Korea", vdf$origin_region)
vdf$origin_region <- gsub("Brasil", "Brazil", vdf$origin_region)
vdf$origin_region <- gsub("United_States_of_America", "USA", vdf$origin_region)
vdf$origin_region <- gsub("United States of America", "USA", vdf$origin_region)

qqqq <- reshape(vdf[,c(1,4,6)], idvar = "name", timevar = "origin_region", direction = "wide")
colnames(qqqq) <- gsub("Dflowering50.", "", gsub(" ", "_", colnames(qqqq), fixed = TRUE), fixed = TRUE)
rownames(qqqq) <- qqqq[,1]
qqqq <- qqqq[,-1]
for(i in 1:dim(qqqq)[2]) {
	q <- as.character(qqqq[,i])
	q[is.na(qqqq[,i])] <- 0
	q[!is.na(qqqq[,i])] <- 1
	qqqq[,i] <- as.numeric(q)
}

doy <- as.numeric(format.Date(as.Date(vdf$sowing, format="'%Y-%m-%d'"), format="%j"))
year <- as.numeric(format.Date(as.Date(vdf$sowing, format="'%Y-%m-%d'"), format="%Y"))
month <- as.numeric(format.Date(as.Date(vdf$sowing, format="'%Y-%m-%d'"), format="%m"))
response <- as.numeric(vdf$Dflowering50)
geo_id <- as.character(vdf$geo_id)

geo_id[geo_id == 'Floreat'] = 0
geo_id[geo_id == 'Mt. Barker'] = 1
geo_id[geo_id == 'Ankara'] = 2
geo_id[geo_id == 'Urfa'] = 3
geo_id[geo_id == 'Kuban'] = 4
geo_id[geo_id == 'Astrakhan'] = 5
geo_id[geo_id == 'Hyderabad'] = 6
geo_id[geo_id == 'Tainan'] = 7
geo_id <- as.numeric(geo_id)

#"Floreat"    "Mt. Barker" "Ankara"     "Urfa" "Kuban" "Astrakhan" "Hyderabad" "Tainan"

library(h5)

dfile <- paste0("vigna-sdm-loc-full", ".h5")
file.remove(dfile)
file <- h5file(dfile)

file["doy"] <- as.matrix(doy)
file["year"] <- as.matrix(year)
file["month"] <- as.matrix(month)
file["response"] <- as.matrix(response)
file["species"] <- as.character(vdf$name)
file["geo_id"] <- as.matrix(geo_id)

csminds <- match(vdf$name, rownames(qqqq))
qqqtab = qqqq[csminds,]
file["gr_names"] <- colnames(qqqtab)
file["gr_covar"] <- as.matrix(qqqtab)
h5close(file)

nasa_srad <- read.csv('nasa-srad', header = FALSE, skip = 12, sep = ' ', stringsAsFactors = FALSE)
nasa_srad$V31[is.na(nasa_srad$V31)] <- nasa_srad$V30[is.na(nasa_srad$V31)]
nasa_srad$V31[nasa_srad$V31 < 0] = 0

meteo_kub <- read.csv('rp5_d/kub.csv', header = 1, stringsAsFactors = FALSE)
doy_kub <- as.numeric(format.Date(as.Date(paste0(meteo_kub$year, "-", meteo_kub$mo, "-", meteo_kub$da), format="%Y-%m-%d"), format="%j"))
geo_id_kub <- rep(4, dim(meteo_kub)[1])

ord <- order(doy_kub)
doy_kub <- doy_kub[ord]
meteo_kub <- meteo_kub[ord,]

srad <- nasa_srad$V31
doy <- doy_kub
meteo <- meteo_kub
geo_id <- geo_id_kub

nasa_srad <- read.csv('nasa-srad-ast', header = FALSE, skip = 12, sep = ' ', stringsAsFactors = FALSE)
nasa_srad$V17[is.na(nasa_srad$V17)] <- nasa_srad$V16[is.na(nasa_srad$V17)]
nasa_srad$V17[nasa_srad$V17 < 0] = 0

meteo_ast <- read.csv('rp5_d/ast.csv', header = 1, stringsAsFactors = FALSE)
doy_ast <- as.numeric(format.Date(as.Date(paste0(meteo_ast$year, "-", meteo_ast$mo, "-", meteo_ast$da), format="%Y-%m-%d"), format="%j"))
geo_id_ast <- rep(5, dim(meteo_ast)[1])

ord <- order(doy_ast)
doy_ast <- doy_ast[ord]
meteo_ast <- meteo_ast[ord,]

srad <- c(srad, nasa_srad$V17)
doy <- c(doy, doy_ast)
meteo <- rbind(meteo, meteo_ast)
geo_id <- c(geo_id, geo_id_ast)

nasa_srad <- read.csv('nasa-srad-hyd-16', header = FALSE, skip = 12, sep = ' ', stringsAsFactors = FALSE)
nasa_srad$V31[is.na(nasa_srad$V31)] <- nasa_srad$V30[is.na(nasa_srad$V31)]
nasa_srad$V31[nasa_srad$V31 < 0] = 0

meteo_hyd <- read.csv('rp5_d/hyd.csv', header = 1, stringsAsFactors = FALSE)
doy_hyd <- as.numeric(format.Date(as.Date(paste0(meteo_hyd$year, "-", meteo_hyd$mo, "-", meteo_hyd$da), format="%Y-%m-%d"), format="%j"))
geo_id_hyd <- rep(6, dim(meteo_hyd)[1])

ord <- order(doy_hyd)
doy_hyd <- doy_hyd[ord]
meteo_hyd <- meteo_hyd[ord,]

srad <- c(srad, nasa_srad$V31)
doy <- c(doy, doy_hyd)
meteo <- rbind(meteo, meteo_hyd)
geo_id <- c(geo_id, geo_id_hyd)

nasa_srad <- read.csv('nasa-srad-tai-18', header = FALSE, skip = 12, sep = ' ', stringsAsFactors = FALSE)
nasa_srad$V31[is.na(nasa_srad$V31)] <- nasa_srad$V30[is.na(nasa_srad$V31)]
nasa_srad$V31[nasa_srad$V31 < 0] = 0

meteo_tai <- read.csv('rp5_d/tai.csv', header = 1, stringsAsFactors = FALSE)
doy_tai <- as.numeric(format.Date(as.Date(paste0(meteo_tai$year, "-", meteo_tai$mo, "-", meteo_tai$da), format="%Y-%m-%d"), format="%j"))
geo_id_tai <- rep(7, dim(meteo_tai)[1])

ord <- order(doy_tai)
doy_tai <- doy_tai[ord]
meteo_tai <- meteo_tai[ord,]

srad <- c(srad, nasa_srad$V31)
doy <- c(doy, doy_tai)
meteo <- rbind(meteo, meteo_tai)
geo_id <- c(geo_id, geo_id_tai)

nasa_srad <- read.csv('nasa-srad-tai-84', header = FALSE, skip = 12, sep = ' ', stringsAsFactors = FALSE)
nasa_srad$V31[is.na(nasa_srad$V31)] <- nasa_srad$V30[is.na(nasa_srad$V31)]
nasa_srad$V31[nasa_srad$V31 < 0] = 0

srad <- c(srad, nasa_srad$V31)

nasa_srad <- read.csv('nasa-srad-tai-85', header = FALSE, skip = 12, sep = ' ', stringsAsFactors = FALSE)
nasa_srad$V31[is.na(nasa_srad$V31)] <- nasa_srad$V30[is.na(nasa_srad$V31)]
nasa_srad$V31[nasa_srad$V31 < 0] = 0

srad <- c(srad, nasa_srad$V31)

meteo_tai <- read.csv('noaa_d/tai.csv', header = 1, stringsAsFactors = FALSE)
colnames(meteo_tai) <- colnames(meteo)
#doy_tai <- as.numeric(format.Date(as.Date(paste0(meteo_tai$year, "-", meteo_tai$mo, "-", meteo_tai$da), format="%Y-%m-%d"), format="%j"))
doy_tai <- meteo_tai$da
geo_id_tai <- rep(7, dim(meteo_tai)[1])

ord <- order(meteo_tai$year, doy_tai)
doy_tai <- doy_tai[ord]
meteo_tai <- meteo_tai[ord,]

doy <- c(doy, doy_tai)
meteo <- rbind(meteo, meteo_tai)
geo_id <- c(geo_id, geo_id_tai)

ord <- order(meteo$year, doy)
doy <- doy[ord]
meteo <- meteo[ord,]

mfile <- 'vigna-meteo-full.h5'
file.remove(mfile)
file <- h5file(mfile)
file["doy"] <- as.matrix(doy)
file["year"] <- as.matrix(meteo$year)
file["month"] <- as.matrix(meteo$mo)
file["dl"] <- as.matrix(meteo$dl)
file["tmin"] <- as.matrix(meteo$tmc)
file["tmax"] <- as.matrix(meteo$txc)
file["rain"] <- as.matrix(meteo$p)
file["srad"] <- as.matrix(as.numeric(srad))
file["geo_id"] <- as.matrix(geo_id)
h5close(file)


