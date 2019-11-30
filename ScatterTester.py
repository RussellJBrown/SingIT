EnglishSums = np.array([2531, 1894, 1942, 1816, 1638, 1510, 1211, 1050, 1069, 1110, 1017, 1100, 1420])/90
FrenchSums = np.array([2233, 1830, 2065, 1753, 1698, 1364, 1150, 1130, 1104, 1022, 1131, 1199, 1494])/90
GermanSums = np.array([2318, 1899, 1898, 1693, 1587, 1395, 1265, 1312, 1359, 1464, 1565, 1628, 2200])/90
JapaneseSums = np.array([2546, 2021, 1838, 1886, 2132, 1930, 1454, 1056, 866, 815, 864, 897, 1163])/90
xaxis13 = np.arange(13)+1

# inputarr is where you put the numbers you want to test for a single song.
inputarr = np.array([11,9,12,4,2,17,2,22,13,12,4,5,53])

plt.scatter(xaxis13,EnglishSums) # Blue
plt.scatter(xaxis13,FrenchSums) # Orange
plt.scatter(xaxis13,JapaneseSums) # Green
plt.scatter(xaxis13,GermanSums) # Red
plt.scatter(xaxis13,inputarr) # Purple
plt.figure()
plt.scatter(xaxis13,EnglishSums)
plt.scatter(xaxis13,FrenchSums)
plt.figure()
plt.scatter(xaxis13,EnglishSums)
plt.scatter(xaxis13,JapaneseSums)
