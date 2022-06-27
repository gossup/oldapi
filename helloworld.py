import sys
import json
import http.client
from collections import Counter

#
    # PARAMS
        # (required) token --- access token
        # ids --- literal ids of the playlists to get
        # postIds --- the postIds of the playlists to get
#

def main(args):
    
    depID = "crn:v1:bluemix:public:dashdb-for-transactions:us-south:a/67d1ffaa2c9c49f98661ec02c3f519a0:b7ad7d2c-f39a-49f4-acd6-c278dc16fa34::"
    hostName = "c1ogj3sd0tgtu0lqde00.db2.cloud.ibm.com"
    
    token = args.get('token')
    if not token:
        return { 'Error': "Missing token." }
        
    since = args.get('since')
    if not since:
        return { 'Error': "Missing since." }
        
    getPostsCommand = "SELECT p.parentId AS parentId, p.createdBy AS createdBy FROM GOSSUP.post p WHERE p.createdAt > {0} GROUP BY parentId, createdBy ORDER BY p.createdBy;".format(since)

    getPostsSqlCommand = {
        'commands': getPostsCommand,
        'limit': 1000,
        'separator': ";",
        'stop_on_error': "yes"
    }
    
    headers = {
    'accept': "application/json",
    'authorization': "Bearer {}".format(token),
    'content-type': "application/json",
    'x-deployment-id': "{}".format(depID)
    }
    
    conn = http.client.HTTPSConnection(hostName)
    
    conn.request("POST", "/dbapi/v4/sql_jobs", headers=headers, body=json.dumps(getPostsSqlCommand))

    postRes = conn.getresponse()
    postData = postRes.read()

    transactionID = json.loads(postData.decode("utf-8")).get('id')
    
    conn.request("GET", "/dbapi/v4/sql_jobs/{}".format(transactionID), headers=headers)
    
    getRes = conn.getresponse()
    getData = getRes.read()
    
    # status = json.loads(getData.decode("utf-8")).get('status')
    # return { 'HERE': json.loads(getData.decode("utf-8")) }
    rows = json.loads(getData.decode("utf-8")).get('results')[0]['rows']
    
    # if len(results) == 0:
    #     return { 'Error': "Missing rows from frist query." }
    
    if len(rows) == 0:
        return { 'Error': "Missing rows from first query." }
    
    createdByIds = []
    for row in rows:
        createdById = row[1]
        createdByIds.append(createdById)
        
    mostCommonUsers = Most_Common(createdByIds)
    
    if len(mostCommonUsers) == 0:
        return { 'Error': "No Trending Topics." }
        
    activeUsers = ""
    
    activeUserTopics = []
    
    if len(mostCommonUsers) == 5:
        
        first = mostCommonUsers[0][0]
        firstTopicIds = []
        
        second = mostCommonUsers[1][0]
        secondTopicIds = []
        
        third = mostCommonUsers[2][0]
        thirdTopicIds = []
        
        fouth = mostCommonUsers[3][0]
        fouthTopicIds = []
        
        fifth = mostCommonUsers[4][0]
        fifthTopicIds = []
        
        for row in rows:
            createdById = row[1]
            topicId = row[0]
            if createdById == first:
                firstTopicIds.append(topicId)
            elif createdById == second:
                secondTopicIds.append(topicId)
            elif createdById == third:
                thirdTopicIds.append(topicId)
            elif createdById == fouth:
                fouthTopicIds.append(topicId)
            elif createdById == fifth:
                fifthTopicIds.append(topicId)
                
        firstMostCommon = Most_Common_Topic(firstTopicIds)
        activeUserTopics.append({ "{0}".format(first): firstMostCommon[0][0] }).format(first)
        
        secondMostCommon = Most_Common_Topic(secondTopicIds)
        activeUserTopics.insert({ "{0}": secondMostCommon[0][0] }).format(second)
        
        thirdMostCommon = Most_Common_Topic(thirdTopicIds)
        activeUserTopics.insert({ "{0}": thirdMostCommon[0][0] }).format(third)
        
        fouthMostCommon = Most_Common_Topic(fouthTopicIds)
        activeUserTopics.insert({ "{0}": fouthMostCommon[0][0] }).format(fouth)
        
        fifthMostCommon = Most_Common_Topic(fifthTopicIds)
        activeUserTopics.insert({ "{0}": fifthMostCommon[0][0] }).format(fifth)
        
        activeUsers = "('{0}','{1}','{2}','{3}','{4}')".format(first, second, third, fouth, fifth)
            
    elif len(mostCommonUsers) == 4:
        
        first = mostCommonUsers[0][0]
        firstTopicIds = []
        
        second = mostCommonUsers[1][0]
        secondTopicIds = []
        
        third = mostCommonUsers[2][0]
        thirdTopicIds = []
        
        fouth = mostCommonUsers[3][0]
        fouthTopicIds = []
        
        for row in rows:
            createdById = row[1]
            topicId = row[0]
            if createdById == first:
                firstTopicIds.append(topicId)
            elif createdById == second:
                secondTopicIds.append(topicId)
            elif createdById == third:
                thirdTopicIds.append(topicId)
            elif createdById == fouth:
                fouthTopicIds.append(topicId)
                
        firstMostCommon = Most_Common_Topic(firstTopicIds)
        activeUserTopics.insert({ "{0}": firstMostCommon[0][0] }).format(first)
        
        secondMostCommon = Most_Common_Topic(secondTopicIds)
        activeUserTopics.insert({ "{0}": secondMostCommon[0][0] }).format(second)
        
        thirdMostCommon = Most_Common_Topic(thirdTopicIds)
        activeUserTopics.insert({ "{0}": thirdMostCommon[0][0] }).format(third)
        
        fouthMostCommon = Most_Common_Topic(fouthTopicIds)
        activeUserTopics.insert({ "{0}": fouthMostCommon[0][0] }).format(fouth)

        activeUsers = "('{0}','{1}','{2}','{3}')".format(first, second, third, fouth)
            
    elif len(mostCommonUsers) == 3:
        
        first = mostCommonUsers[0][0]
        firstTopicIds = []
        
        second = mostCommonUsers[1][0]
        secondTopicIds = []
        
        third = mostCommonUsers[2][0]
        thirdTopicIds = []
        
        for row in rows:
            createdById = row[1]
            topicId = row[0]
            if createdById == first:
                firstTopicIds.append(topicId)
            elif createdById == second:
                secondTopicIds.append(topicId)
            elif createdById == third:
                thirdTopicIds.append(topicId)
                
        firstMostCommon = Most_Common_Topic(firstTopicIds)
        activeUserTopics.insert({ "{0}": firstMostCommon[0][0] }).format(first)
        
        secondMostCommon = Most_Common_Topic(secondTopicIds)
        activeUserTopics.insert({ "{0}": secondMostCommon[0][0] }).format(second)
        
        thirdMostCommon = Most_Common_Topic(thirdTopicIds)
        activeUserTopics.insert({ "{0}": thirdMostCommon[0][0] }).format(third)

        activeUsers = "('{0}','{1}','{2}')".format(first, second, third)
            
    elif len(mostCommonUsers) == 2:
        
        first = mostCommonUsers[0][0]
        firstTopicIds = []
        
        second = mostCommonUsers[1][0]
        secondTopicIds = []
        
        for row in rows:
            createdById = row[1]
            topicId = row[0]
            if createdById == first:
                firstTopicIds.append(topicId)
            elif createdById == second:
                secondTopicIds.append(topicId)
                
        firstMostCommon = Most_Common_Topic(firstTopicIds)
        activeUserTopics.insert({ "{0}": firstMostCommon[0][0] }).format(first)
        
        secondMostCommon = Most_Common_Topic(secondTopicIds)
        activeUserTopics.insert({ "{0}": secondMostCommon[0][0] }).format(second)
        
        activeUsers = "('{0}', '{1}')".format(first, second)
            
    elif len(mostCommonUsers) == 1:
        
        first = mostCommonUsers[0][0]
        firstTopicIds = []
        for row in rows:
            createdById = row[1]
            topicId = row[0]
            if createdById == first:
                firstTopicIds.append(topicId)
                
        firstMostCommon = Most_Common_Topic(firstTopicIds)
        # return { 'HERE': firstMostCommon}
        # activeUserTopics["{0}"format(first)].append("{0}".format(firstMostCommon[0][0]))
        activeUserTopics.append({ '{}'.format(first): firstMostCommon })
        activeUsers = "('{0}')".format(first)

        
    activeUsersCommand = "SELECT u.id, u.displayName, u.email, u.isGold, u.isVerified, u.username, u.type, p.playCount FROM GOSSUP.user u, GOSSUP.profile p WHERE u.id=p.id AND u.id IN {0} GROUP BY u.id, u.displayName, u.email, u.isGold, u.isVerified, u.username, u.type, p.playCount ORDER BY p.playCount LIMIT 5 OFFSET 0;".format(activeUsers)

    getUsersSqlCommand = {
        'commands': activeUsersCommand,
        'limit': 5,
        'separator': ";",
        'stop_on_error': "yes"
    }
        
    conn.request("POST", "/dbapi/v4/sql_jobs", headers=headers, body=json.dumps(getUsersSqlCommand))
        
    userRes = conn.getresponse()
    userData = userRes.read()
    
    userTransactionID = json.loads(userData.decode("utf-8")).get('id')
        
    conn.request("GET", "/dbapi/v4/sql_jobs/{}".format(userTransactionID), headers=headers)
    
    userGetRes = conn.getresponse()
    userGetData = userGetRes.read()
    
    return { 'message': json.loads(userGetData.decode("utf-8")), 'activeUserTopics': activeUserTopics }
        
        
def Most_Common(lst):
    data = Counter(lst)
    return data.most_common(5)
    
def Most_Common_Topic(lst):
    data = Counter(lst)
    return data.most_common(1)