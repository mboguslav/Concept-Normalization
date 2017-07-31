##Baseline to pre-processing
CHEBI_pre = matrix(c(2934,1795,2931,1550),nrow=2,ncol=2,byrow=TRUE)

chisq.test(CHEBI_pre) #significant

##Baseline to Case post-processing
CL = matrix(c(1359,120,126,3),nrow=2,ncol=2,byrow=TRUE)
CHEBI = matrix(c(2943,1795,172,33),nrow=2,ncol=2,byrow=TRUE)
NCBITAXON= matrix(c(4149,2202,94,264),nrow=2,ncol=2,byrow=TRUE)
PR = matrix(c(8320,6357,7457,2661),nrow=2,ncol=2,byrow=TRUE)
SO = matrix(c(7840,3495,1141,122),nrow=2,ncol=2,byrow=TRUE)
GO_BP = matrix(c(3234,1088,393,69),nrow=2,ncol=2,byrow=TRUE)
GO_CC = matrix(c(5515,451,455,78),nrow=2,ncol=2,byrow=TRUE)
GO_MF = matrix(c(337,139,89,17),nrow=2,ncol=2,byrow=TRUE)

##chi-squared = all significant
chisq.test(CL) #sig
chisq.test(CHEBI) #sig
chisq.test(NCBITAXON) #sig
chisq.test(PR) #sig
chisq.test(SO) #sig
chisq.test(GO_BP) #sig
chisq.test(GO_CC) #sig
chisq.test(GO_MF) #sig


##Baseline to Frequency post-processing
CL_2 = matrix(c(1359,120,1340,116),nrow=2,ncol=2,byrow=TRUE)
CHEBI_2 = matrix(c(2943,1795,2611,1274),nrow=2,ncol=2,byrow=TRUE)
NCBITAXON_2= matrix(c(4149,2202,2740,918),nrow=2,ncol=2,byrow=TRUE)
PR_2 = matrix(c(8320,6357,5593,1858),nrow=2,ncol=2,byrow=TRUE)
SO_2 = matrix(c(7840,3495,6311,2628),nrow=2,ncol=2,byrow=TRUE)
GO_BP_2 = matrix(c(3234,1088,2413,525),nrow=2,ncol=2,byrow=TRUE)
GO_CC_2 = matrix(c(5515,451,4319,227),nrow=2,ncol=2,byrow=TRUE)
GO_MF_2 = matrix(c(337,139,284,104),nrow=2,ncol=2,byrow=TRUE)

##chi-squared
chisq.test(CL_2) #not sig
chisq.test(CHEBI_2) #sig
chisq.test(NCBITAXON_2) #sig
chisq.test(PR_2) #sig
chisq.test(SO_2) #sig
chisq.test(GO_BP_2) #not sig
chisq.test(GO_CC_2) #sig
chisq.test(GO_MF_2) #not sig


##Zipf like distribution of top 20 concepts for each ontology
install.packages("igraph")
library(igraph)
zCL = c(0.444504751,0.055796743,0.049169905,0.037819555,0.036000554,0.032013877,0.031685949,0.030848726,0.028176442,0.028139633,0.026814534,0.02634941,0.022898127,0.021494057,0.020828161,0.017342077,0.015345058,0.015286165,0.012954524,0.012475347)
zCHEBI = c(0.911513445,0.535444748,0.504435404,0.416304216,0.337042498,0.337042498,0.295993848,0.250295972, 0.245937197,0.200629489,
           0.189643876,0.189518728,0.154465821,0.154417635,0.147893192,0.141252969,0.138464236, 0.136995918,0.13222422,0.120700536)
zNCBITaxon = c(0.43750916,0.434525678,0.372614067,0.267324175,0.234140462,0.231985502,0.144996041,0.119143209,0.108170981,0.09349115,0.078853481,0.069255876,0.06677031,0.065740346,0.064529017,0.061848032,0.061354132,0.059302904,0.054578053,0.046944005)
zPRO = c(0.783617215,0.51739662,0.512762117,0.50300791,0.415316414,0.394708435,0.373783903,0.336928726,0.313352657,0.297817534,0.27734541,0.223182957,0.208195274,0.171571655,0.15853883,0.153613206,0.152164296,0.135902376,0.127522793,0.121337655)
zSO = c(0.477931399,0.429941368,0.386087254,0.332327016,0.319580626,0.312087119,0.258978054,0.254136754,0.197782532,0.186315065,0.184690813,0.179085239,0.172082287,0.170046452,0.160342438,0.156767345,0.153439872,0.144403093,0.140696159,0.133809655)
zGO_BP = c(0.465970699,0.442214603,0.442027215,0.331193989,0.321757002,0.317111791,0.229616384,0.225695293,0.219579087,0.216973726,0.210444598,0.203921493,0.198063614,0.185222861,0.176657228,0.153681469,0.150445682,0.149416387,0.148431932,0.147775405)
zGO_CC = c(0.55728748,0.449352742,0.447901825,0.447897809,0.447896471,0.447896471,0.273434358,0.270419421,0.236855578,0.231372476,0.228071103,0.227997486,0.209424672,0.202356135,0.156695736,0.14049271,0.12817865,0.116490332,0.103474907,0.096650643)
zGO_MF = c(0.949877763,0.701090932,0.503947526,0.503946857,0.3718083,0.279392622,0.273240947,0.266487622,0.261303001,0.238339958,0.207901477,0.207728812,0.199098263,0.143227903,0.099816159,0.096367553,0.094446158,0.093930173,0.089221383,0.087756412)


##Power law fit to get p-values: ideally want p-value > 0.05 to show that they fit

fit_power_law(zCL, xmin = NULL, start = 2, force.continuous = FALSE,
              implementation = c("plfit", "R.mle")) #KS.p = 0.9924492
fit_power_law(zCHEBI, xmin = NULL, start = 2, force.continuous = FALSE,
              implementation = c("plfit", "R.mle")) #KS.p = 0.9609383
fit_power_law(zNCBITaxon, xmin = NULL, start = 2, force.continuous = FALSE,
              implementation = c("plfit", "R.mle")) #KS.p = 0.8561492
fit_power_law(zPRO, xmin = NULL, start = 2, force.continuous = FALSE,
              implementation = c("plfit", "R.mle")) #KS.p = 0.9163666
fit_power_law(zSO, xmin = NULL, start = 2, force.continuous = FALSE,
              implementation = c("plfit", "R.mle")) #KS.p = 0.8824374
fit_power_law(zGO_BP, xmin = NULL, start = 2, force.continuous = FALSE,
              implementation = c("plfit", "R.mle")) #KS.p = 0.8261036
fit_power_law(zGO_CC, xmin = NULL, start = 2, force.continuous = FALSE,
              implementation = c("plfit", "R.mle")) #KS.p = 0.2323271
fit_power_law(zGO_MF, xmin = NULL, start = 2, force.continuous = FALSE,
              implementation = c("plfit", "R.mle")) #KS.p = 0.9501458


