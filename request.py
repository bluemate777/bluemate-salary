import requests

server.listen(port,()=>{  // do not add localhost here if you are deploying it
    console.log("server listening to port "+port);
});

'''
url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())
'''
