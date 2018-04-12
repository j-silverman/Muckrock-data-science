import csv

def overlap(x, y):
    return bool(set(x) & set(y))

terms = ["Gun", "gun", "Guns", "guns", "shooting", "shooter", "shootings", "Shooting", "#GunControl", "#gunsafety", "#nra", "#shooting", "#gunviolence", "#guns", "#gun", "NRA", "nra", "school violence"]

dateCount = {}
tweetCount = {}
termsCount = {}
stateCount = {}

users = {}

cStates = {}
sStates = {}
stateUsers = {}

with open("115th-Congress-House-seeds.csv", 'rU') as csvfile:
    agencies = csv.DictReader(csvfile)
    for agency in agencies:
        cStates[agency["Handle"]] = agency["State"]



with open("115th-Congress-Senate-seeds.csv", 'rU') as csvfile:
    agencies = csv.DictReader(csvfile)
    for agency in agencies:
        sStates[agency["Handle"]] = agency["State"]

with open("senatetweets.csv", 'rU') as csvfile:
    agencies = csv.DictReader(csvfile)
    for agency in agencies:
        try:
            if overlap(terms,agency["tweets"].split()):
                date = agency["time"].split()[0]
                if date not in dateCount:
                    dateCount[date] = 1
                else:
                    dateCount[date] += 1
                if agency["username"] not in tweetCount:
                    tweetCount[agency["username"]] = 1
                else:
                    tweetCount[agency["username"]] += 1
                if sStates[agency["username"]] not in stateCount:
                    stateCount[sStates[agency["username"]]] = 1
                else:
                    stateCount[sStates[agency["username"]]] += 1
                if sStates[agency["username"]] not in stateUsers:
                    stateUsers[sStates[agency["username"]]] = []
                if agency["username"] not in stateUsers[sStates[agency["username"]]]:
                    stateUsers[sStates[agency["username"]]] += [agency["username"]]

        except:
            pass

with open("congresstwitterdata.csv", 'rU') as csvfile:
    agencies = csv.DictReader(csvfile)
    for agency in agencies:
        try:
            if overlap(terms,agency["tweets"].split()):
                date = agency["time"].split()[0]
                if date not in dateCount:
                    dateCount[date] = 1
                else:
                    dateCount[date] += 1
                if agency["username"] not in tweetCount:
                    tweetCount[agency["username"]] = 1
                else:
                    tweetCount[agency["username"]] += 1
                if cStates[agency["username"]] not in stateCount:
                    stateCount[cStates[agency["username"]]] = 1
                else:
                    stateCount[cStates[agency["username"]]] += 1
                if cStates[agency["username"]] not in stateUsers:
                    stateUsers[cStates[agency["username"]]] = []
                if agency["username"] not in stateUsers[cStates[agency["username"]]]:
                    stateUsers[cStates[agency["username"]]] += [agency["username"]]
        except:
            pass



with open('stateCount.csv', 'w') as myfile:
    writer = csv.writer(myfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(['agencyTwitter', 'gunCount'])
    # for i in [1,2,3]:
    #     if i != 2:
    #         j = 31
    #     if i == 2:
    #         j = 28
    #     for k in range(1,j+1):
    #         s = str(i) + "/" + str(k) + "/18"
    #         t = "2018-0" + str(i) + "-" + str(k)
    #         if s in dateCount and t in dateCount:
    #             writer.writerow([s, str(int(dateCount[s]) + int(dateCount[t]))])
    #         elif s in dateCount:
    #             writer.writerow([s, dateCount[s]])
    #         elif t in dateCount:
    #             writer.writerow([s, dateCount[t]])
    #         else:
    #             writer.writerow([s, 0])
    keylist = stateCount.keys()
    keylist.sort()
    for key in keylist:
        writer.writerow([key, str(float(stateCount[key])/float(len(stateUsers[key])))])


keylist = stateUsers.keys()
keylist.sort()
for key in keylist:
    print "%s: %s" % (key, len(stateUsers[key]))


