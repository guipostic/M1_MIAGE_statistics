

dat2 = read.table("2.txt", h=F)
png("00002.png")
hist(dat2$V1, breaks=seq(min(dat2$V1),max(dat2$V1),1))
dev.off()

dat3 = read.table("3.txt", h=F)
png("00003.png")
hist(dat3$V1, breaks=seq(min(dat3$V1),max(dat3$V1),1))
dev.off()

dat4 = read.table("4.txt", h=F)
png("00004.png")
hist(dat4$V1, breaks=seq(min(dat4$V1),max(dat4$V1),1))
dev.off()

dat5 = read.table("5.txt", h=F)
png("00005.png")
hist(dat5$V1, breaks=seq(min(dat5$V1),max(dat5$V1),1))
dev.off()


dat10 = read.table("10.txt", h=F)
png("00010.png")
hist(dat10$V1, breaks=seq(min(dat10$V1),max(dat10$V1),1))
dev.off()


dat100 = read.table("100.txt", h=F)
png("00100.png")
hist(dat100$V1, breaks=seq(min(dat100$V1),max(dat100$V1),1))
dev.off()


