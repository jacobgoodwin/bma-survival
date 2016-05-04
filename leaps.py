import fwleaps
import numpy as np
import pandas as pd

print(fwleaps.fwleaps.__doc__)

def leaps(info, coef, names, nbest):
	names = names
	# if not names:
	# 	names = '...'
	# if names.length < info.length
	# 	print("too few names")
	# 	exit
	print(coef)
	print(info)
	# bIb = pd.dot(coef, info, coef)
	bIb = coef.dot(info).dot(coef)
	print("bIB: ")
	print(bIb)
	# check ordering

	# number of cols of info
	# kx = info.shape.N
	kx=4
	# maxreg = nbest * 
	maxreg = nbest * 4
	if kx < 3:	
		print("too few individual variables")
		exit
	imeth = 1
	df = kx + 1

	Ib = info.dot(coef)

	rr = pd.concat([info, Ib], axis=1, ignore_index=1)
	print(rr)
	print(Ib)
	print(bIb)
	Ib = pd.Series(Ib)
	Ib = Ib.append(pd.Series(bIb)).transpose()
	print(rr)
	print(Ib)
	rr = pd.concat([rr, Ib], ignore_index=1)
	print(rr)
	# rr.columns = ['a', 'b']
	# rr = rr.concat(concatenate(['Ib', 'bIb']))
	

	it = 0
	ncols = kx + 1
	nv = kx + 1
	nf = 0
	no = 1e+05
	ib = 1
	mb = nbest
	nd = ncols
	nc = 4 * ncols
	rt = np.array([0] * (nd * nc)).reshape(-1, nc)
	rt.ix[:, 0:ncols] = rr
	iw = np.concatenate(range(1, kx+1), np.repeat(0, 4 * nd))
	nw = length(iw)
	rw = np.repeat(0, 2 * mb * kx + 7 * nd)
	nr = rw.length
	t1 = 2
	s2 = -1
	ne = 0
	iv = 0
	nret = mb * kx
	Subss = np.repeat(0, nret)
	RSS = Subss
	ans = fwleaps.fwleaps(int(nv), int(it), 
            int(kx), int(nf), int(no), int(1), 
            float(2), int(mb), float(rt), int(nd), 
            int(nc), int(iw), int(nw), float(rw), 
            int(nr), float(t1), float(s2), int(ne), 
            int(iv), float(Subss), float(RSS), 
            int(nret), PACKAGE = "BMA")
        # regid <- ans[[21]]/2
        # r2 <- ans[[20]]
        # nreg <- sum(regid > 0)
        # regid <- regid[1:nreg]
        # r2 <- r2[1:nreg]
        # which <- matrix(TRUE, nreg, kx)
        # z <- regid
        # which <- matrix(as.logical((rep.int(z, kx)%/%rep.int(2^((kx - 
        #     1):0), rep.int(length(z), kx)))%%2), byrow = FALSE, ncol = kx)
        # size <- which %*% rep(1, kx)
        # label <- character(nreg)
        # sep <- if (all(nchar(names.arg) == 1)) 
        #     ""
        # else ","
        # for (i in 1:nreg) label[i] <- paste(names.arg[which[i, 
        #     ]], collapse = sep)
        # ans <- list(r2 = r2, size = size, label = label, which = which)
 # print(ans)

coef = pd.Series([0.151, -0.513, -0.012, -0.002])
info = pd.DataFrame([[9.676660e-05, 5.395207e-05, 1.522390e-05, 2.459970e-06],
				[5.395207e-05, 3.041883e-02, -4.259301e-05, 3.346761e-05],
				[1.522390e-05, -4.259301e-05,  3.824660e-05, 8.321737e-06],
				[2.459970e-06, 3.346761e-05, 8.321737e-06, 4.041545e-05]])
names = pd.Series(['age', 'sex', 'ph_karno', 'wt_loss'])

leaps(info, coef, names, 150)


