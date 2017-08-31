from flask import Blueprint, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.utils import secure_filename
import os

from models.ads import AdsModel

UPLOAD_FOLDER = os.path.dirname(__file__)+'/assets/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

application = Blueprint('application', __name__, template_folder='templates', static_folder='assets')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@application.route('/index')
@application.route('/')
def index():
    return 'Under Constructions!!!'

@application.route('/about')
def about():
    return 'About'

@application.route('/ads', methods=['GET', 'POST'])
def ads():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        desc = request.form['description']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            new_ads = AdsModel(file.filename, desc)
            new_ads.save_to_db()
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('application.ads'))

    data = AdsModel.query.all()
    return render_template('ads.html', data=data)

@application.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER,filename)