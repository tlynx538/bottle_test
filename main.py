from bottle import run,get,post,request

animals=[{'name':'Ellie','type':'Snake'},
        {'name':'Thomas','type':'Elephant'},
        {'name':'Phoebe','type':'Bear'}]
@get('/animal')
def getanimalist():
    return {'animals': animals}

@get('/animal/<name>')
def getnameanimal(name):
    ret_name=[i for i in animals if i['name'] == name]
    return { 'animal':ret_name[0]}

@post('/animal/sendreq')
def sendreq():
    new_animal={'name':request.json.get('name'),'type':request.json.get('type')}
    animals.append(new_animal)
    return {'animal':animals}

run(reloader=True)