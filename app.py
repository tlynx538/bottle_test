from bottle import run,route,template,request,error
@error(404)
def fouro(error):
    return template('error404')

@error(500)
def fiveo(error):
    return template('error500')

@route('/')
def index():
    var1=request.query.var1
    var2=request.query.var2
    return template('index',name='tlynx538',var1=var1,var2=var2)

@route('/home')
def home():
    return '<h1> Home </h1>'

@route('/user/<id>')
def user(id):
    return '<h1> You are now viewing '+id+' page </h1>'

@route('/postmec',method='POST')
def post_mec():
    return '<h1> POST SUCCESS </h1>'

@route('/json')
def jsonx():
    return {"name": "Bottle Website","test":"success"}    
    
run(reloader=True)    