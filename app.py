from flask import Flask, flash, session, redirect
from flask import render_template,request,send_file
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
import pathlib
import qrcode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

import ipfsapi
api = ipfsapi.Client(host='127.0.0.1', port=5001)



app = Flask(__name__)
 
app.config['UPLOADED_PHOTOS_DEST'] = 'static/files/'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

foldername='static/files/'

app.secret_key = 'any random string'



@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/index',methods=['POST','GET'])
def index1():
    return render_template('index.html') 

@app.route('/about',methods=['POST','GET'])
def about():
    return render_template('about.html')

@app.route('/register',methods=['POST','GET'])
def register():
    
    return render_template('register.html')

@app.route('/login',methods=['POST','GET'])
def login():
    return render_template('login.html')    

@app.route('/adminlogin',methods=['POST','GET'])
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/logout')
def logout():
    session.pop('name',None)
    return render_template('index.html') 

@app.route('/userregister',methods=['POST','GET'])
def userregister():
    return render_template('userregister.html') 

@app.route('/userlogin',methods=['POST','GET'])
def userlogin():
    return render_template('userlogin.html') 


@app.route('/main',methods=['POST','GET'])
def main():
    return render_template('index1.html') 

@app.route('/main2',methods=['POST','GET'])
def main2():
    return render_template('displayforuser.html') 

@app.route('/main1',methods=['POST','GET'])
def main1():
    return render_template('index2.html') 


@app.route('/SessionHandle',methods=['POST','GET'])
def SessionHandle():
    if request.method == "POST":
        details = request.form
        name = details['name']
        password = details['pass']
        session['name'] = name        
        session['pass'] = password
        strofuser = name
        print (strofuser.encode('utf8', 'ignore'))
        return strofuser 
    
@app.route('/SessionHandle2',methods=['POST','GET'])
def SessionHandle2():
    if request.method == "POST":
        details = request.form
        name = details['name']
        password = details['pass']
        session['name'] = name        
        session['pass'] = password
        strofuser = name
        print (strofuser.encode('utf8', 'ignore'))
        return strofuser 
    
@app.route('/SessionHandle1',methods=['POST','GET'])
def SessionHandle1():
    if request.method == "POST":
        details = request.form
        name = details['name']
        session['admin'] = name
        strofuser = name
        print (strofuser.encode('utf8', 'ignore'))
        return strofuser 





@app.route('/uploadProduct',methods=['POST','GET'])
def uploadProduct():
    if request.method == "POST":
        
        f2= request.files['filename'] 
        idofproduct = request.form['pid'] 
        name = request.form['pname'] 
        category = request.form.get('category')
        quantity = request.form.get('quantity')
        Price = request.form['pprice'] 
        
        user = session.get("name")
        passwww = session.get("pass")
        
        filename_secure = secure_filename(f2.filename)
        pathlib.Path(app.config['UPLOADED_PHOTOS_DEST'], user).mkdir(exist_ok=True)
        f2.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'],user, filename_secure))     
        
        filename55 = filename_secure
        
        ListOfFile = {'a':filename55,'b':idofproduct,'c':name,
                      'd':category,'e':Price,'f':user,'g':passwww,'h':quantity}
        return ListOfFile 
    return render_template('uploadProduct.html',data={})


@app.route('/displayInfo')
def displayInfo():
    return render_template('displayInfo.html') 


@app.route('/displayProduct',methods=['POST','GET'])
def displayProduct():
    if request.method == "POST":
        details = request.form
        fname = details['fname']
        data=fname.split('|')
        return render_template('displayProduct.html',data=data) 
    return render_template('displayProduct.html')




@app.route('/generateqrcode',methods=['POST','GET'])
def generateqrcode():
    if request.method == "POST":
        details = request.form
        username = details['username']
        imagename = details['imagename']
        idofp = details['idofp']
        pname = details['pname']
        pcat = details['pcat']
        pprice = details['pprice']        
        
        new_file1 = api.add("static/files/"+username+"/"+imagename)
        print(new_file1['Hash'])
        
        data = username+"|"+new_file1['Hash']+"|"+idofp+"|"+pname+"|"+pcat+"|"+pprice
        
        key = RSA.generate(2048)        
        
        pathlib.Path('static/keys/', username).mkdir(exist_ok=True)
        with open('static/keys/'+username+"/"+imagename.split('.', 1)[0]+'_private.pem', 'wb' ) as f:
            f.write( key.exportKey( 'PEM' ))        
        
        publicKey = PKCS1_OAEP.new( key )
        secret_message = bytes(data, 'utf-8')
        
        encMessage = publicKey.encrypt( secret_message ) 
        hexilify= binascii.hexlify(encMessage)
        strencry = str(hexilify.decode('UTF-8'))  
        
        dataofqr = strencry+","+'static/keys/'+username+"/"+imagename.split('.', 1)[0]+'_private.pem'
        img = qrcode.make(dataofqr)
        img.save('static/qrcode/'+imagename.split('.', 1)[0]+'_QR.png') 
        
        ListOfFile = {'a':idofp,'b':pname,'c':pcat,'d':pprice,'e':'static/qrcode/'+imagename.split('.', 1)[0]+'_QR.png'}
        return ListOfFile 
    return render_template('displayProduct.html')











@app.route('/getAllInfoOfImage',methods=['POST','GET'])
def getAllInfoOfImage():
    if request.method == "POST":   
        
        details = request.form
        data = details['data']
        parts = data.split("|")
        print ("dsdasdsadsadsad",parts)
        return render_template('qrcode.html',data=parts) 
    
    return render_template('qrcode.html',data={}) 
     
    
    
@app.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        print("GET")
        src = request.form.get("src")
        print("---------------------------------------------------------------")
        print(src)
        # try:
        parts = src.split(",")
        print(parts)
        
        with open(parts[1],'r' ) as f:
            key = RSA.importKey( f.read() )
        
        convertedtobyte = bytes(parts[0], 'utf-8')
        public_crypter =  PKCS1_OAEP.new( key )
        decrypted_data = public_crypter.decrypt(binascii.unhexlify(convertedtobyte))
        str1 = decrypted_data.decode('UTF-8') 
        print(type(str1))
        parts2 = str1.split("|")
        print(parts2) 
        
        # api.get(parts2[1])
        
        import urllib3
        url = 'http://127.0.0.1:8080/ipfs/'+parts2[1]
        connection_pool = urllib3.PoolManager()
        resp = connection_pool.request('GET',url )
        f = open("static/ipfs/"+parts2[1]+".jpg", 'wb')
        f.write(resp.data)
        f.close()
        resp.release_conn()
        
        # # creating a image object (main image) 
        # im1 = Image.open(parts2[1])
            
        # # save a image using extension
        # im1 = im1.save("static/ipfs/"+parts2[1]+".jpg")
        return str1
        # except:
        #     return "fail"


if __name__ == "__main__":
    app.run("0.0.0.0")
    # app.run(debug=True)