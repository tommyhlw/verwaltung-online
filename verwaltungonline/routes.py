import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from verwaltungonline import app, db, bcrypt
from verwaltungonline.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, AddEinheit, AddGemeinschaft, AddKostenart, AddStockwerk, AddUmlageschluessel, AddVermietung, AddWohnung, AddZaehler, AddZaehlertyp
from verwaltungonline.models import User, Post, Einheiten, Gemeinschaft, Kostenarten, Stockwerke, Umlageschluessel, Vermietung, Wohnungen, Zaehler, Zaehlertypen
from flask_login import login_user, current_user, logout_user, login_required
from flask_oauthlib.client import OAuth2Client
from flask_oauthlib.provider import OAuth2Provider


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@oauth_provider.route('/login')
@oauth_provider.require_oauth('openid')
def login():
    return oauth_provider.authorize_redirect('https://login.wp472.de/auth/realms/your-realm-name/protocol/openid-connect/auth')


@oauth_provider.route('/oauth2/callback')
@oauth_provider.authorized_handler
def callback(resp):
    access_token = resp['access_token']
    # Use the access token to make requests to Keycloak API or protected resources
    return 'Authenticated successfully!'

@app.route("/ablesung")
@oauth_provider.require_oauth('openid')
def ablesung():
    bezeichnungen =Einheiten.query.all()
    return render_template('ablesung.html', title='Ablesung', bezeichnungen=bezeichnungen)


@app.route("/einheiten")
@oauth_provider.require_oauth('openid')
def einheiten():
    bezeichnungen =Einheiten.query.all()
    return render_template('einheiten.html', title='Einheiten', bezeichnungen=bezeichnungen)

@app.route("/einheiten/add_einheit", methods=['GET', 'POST'])
@oauth_provider.require_oauth('openid')
def add_einheit():
    form = AddEinheit()
    if form.validate_on_submit():
        post = Einheiten(bezeichnung=form.bezeichnung.data)
        db.session.add(post)
        db.session.commit()
        flash('Datensatz wurde angelegt.', 'success')
        return redirect(url_for('einheiten'))
    return render_template('add_einheit.html', title='Einheit hinzufügen', form=form, legend='Einheit hinzufügen')


@app.route("/gemeinschaft")
@oauth_provider.require_oauth('openid')
def gemeinschaft():
    bezeichnungen =Gemeinschaft.query.all()
    return render_template('gemeinschaft.html', title='Gemeinschaftsflächen', bezeichnungen=bezeichnungen)

@app.route("/gemeinschaft/add_gemeinschaft", methods=['GET', 'POST'])
@oauth_provider.require_oauth('openid')
def add_gemeinschaft():
    form = AddGemeinschaft()
    if form.validate_on_submit():
        post = Gemeinschaft(bezeichnung=form.bezeichnung.data)
        db.session.add(post)
        db.session.commit()
        flash('Datensatz wurde angelegt.', 'success')
        return redirect(url_for('gemeinschaft'))
    return render_template('add_gemeinschaft.html', title='Fläche hinzufügen', form=form, legend='Fläche hinzufügen')


@app.route("/kostenarten")
@oauth_provider.require_oauth('openid')
def kostenarten():
    bezeichnungen =Kostenarten.query.all()
    return render_template('gemeinschaft.html', title='Kostenarten', bezeichnungen=bezeichnungen)

@app.route("/kostenarten/add_kostenart", methods=['GET', 'POST'])
@oauth_provider.require_oauth('openid')
def add_kostenart():
    form = AddKostenart()
    if form.validate_on_submit():
        post = Kostenarten(bezeichnung=form.bezeichnung.data)
        db.session.add(post)
        db.session.commit()
        flash('Datensatz wurde angelegt.', 'success')
        return redirect(url_for('kostenarten'))
    return render_template('add_kostenart.html', title='Kostenart hinzufügen', form=form, legend='Kostenart hinzufügen')


@app.route("/stockwerke")
@oauth_provider.require_oauth('openid')
def stockwerke():
    bezeichnungen =Stockwerke.query.all()
    return render_template('stockwerke.html', title='Stockwerke', bezeichnungen=bezeichnungen)

@app.route("/stockwerke/add_stockwerk", methods=['GET', 'POST'])
@oauth_provider.require_oauth('openid')
def add_stockwerk():
    form = AddStockwerk()
    if form.validate_on_submit():
        post = Stockwerke(bezeichnung=form.bezeichnung.data)
        db.session.add(post)
        db.session.commit()
        flash('Datensatz wurde angelegt.', 'success')
        return redirect(url_for('stockwerke'))
    return render_template('add_stockwerk.html', title='Stockwerk hinzufügen', form=form, legend='Stockwerk hinzufügen')


@app.route("/umlageschluessel")
@oauth_provider.require_oauth('openid')
def umlageschluessel():
    bezeichnungen =Umlageschluessel.query.all()
    return render_template('umlageschluessel.html', title='Umlageschlüssel', bezeichnungen=bezeichnungen)

@app.route("/umlageschluessel/add_umlageschluessel", methods=['GET', 'POST'])
@oauth_provider.require_oauth('openid')
def add_umlageschluessel():
    form = AddUmlageschluessel()
    if form.validate_on_submit():
        post = Umlageschluessel(bezeichnung=form.bezeichnung.data)
        db.session.add(post)
        db.session.commit()
        flash('Datensatz wurde angelegt.', 'success')
        return redirect(url_for('umlageschluessel'))
    return render_template('add_umlageschluessel.html', title='Umlageschlüssel hinzufügen', form=form, legend='Umlageschlüssel hinzufügen')


@app.route("/vermietung")
@oauth_provider.require_oauth('openid')
def vermietung():
    bezeichnungen = Vermietung.query.all()
    return render_template('vermietung.html', title='Mieter*innen', bezeichnungen=bezeichnungen)

@app.route("/vermietung/add_vermietung", methods=['GET', 'POST'])
@oauth_provider.require_oauth('openid')
def add_vermietung():
    form = AddVermietung()
    if form.validate_on_submit():
        post = Vermietung(weid=form.weid.data, wohnung=form.wohnung.data, vorname=form.vorname.data, nachname=form.nachname.data, strasse=form.strasse.data,
                          hausnummer=form.hausnummer.data, plz=form.plz.data, ort=form.ort.data, mietbeginn=form.mietbeginn.data, mietende=form.mietende.data,
                          personen=form.personen.data)
        db.session.add(post)
        db.session.commit()
        flash('Datensatz wurde angelegt.', 'success')
        return redirect(url_for('vermietung'))
    return render_template('add_vermietung.html', title='Neue Mieter*in hinzufügen',
                           form=form, legend='Neue Mieter*in hinzufügen')


@app.route("/wohnungen")
@oauth_provider.require_oauth('openid')
def wohnungen():
    bezeichnungen =Wohnungen.query.all()
    return render_template('wohnungen.html', title='Wohnungen', bezeichnungen=bezeichnungen)

@app.route("/wohnungen/add_wohnung", methods=['GET', 'POST'])
@oauth_provider.require_oauth('openid')
def add_wohnung():
    form = AddWohnung()
    if form.validate_on_submit():
        post = Wohnungen(bezeichnung=form.bezeichnung.data)
        db.session.add(post)
        db.session.commit()
        flash('Datensatz wurde angelegt.', 'success')
        return redirect(url_for('wohnungen'))
    return render_template('add_wohnung.html', title='Wohnung hinzufügen', form=form, legend='Wohnung hinzufügen')


@app.route("/zaehler")
@oauth_provider.require_oauth('openid')
def zaehler():
    bezeichnungen =Zaehler.query.all()
    return render_template('zaehler.html', title='Zähler', bezeichnungen=bezeichnungen)

@app.route("/stockwerke/add_zaehler", methods=['GET', 'POST'])
@oauth_provider.require_oauth('openid')
def add_zaehler():
    form = AddZaehler()
    if form.validate_on_submit():
        post = Zaehler(bezeichnung=form.bezeichnung.data)
        db.session.add(post)
        db.session.commit()
        flash('Datensatz wurde angelegt.', 'success')
        return redirect(url_for('zaehler'))
    return render_template('add_zaehler.html', title='Zähler hinzufügen', form=form, legend='Zähler hinzufügen')


@app.route("/zaehlertypen")
@oauth_provider.require_oauth('openid')
def zaehlertypen():
    bezeichnungen =Zaehlertypen.query.all()
    return render_template('zaehlertypen.html', title='Zählertypen', bezeichnungen=bezeichnungen)

@app.route("/zaehlertypen/add_zaehlertyp", methods=['GET', 'POST'])
@oauth_provider.require_oauth('openid')
def add_zaehlertyp():
    form = AddZaehlertyp()
    if form.validate_on_submit():
        post = Zaehlertypen(bezeichnung=form.bezeichnung.data)
        db.session.add(post)
        db.session.commit()
        flash('Datensatz wurde angelegt.', 'success')
        return redirect(url_for('zaehlertypen'))
    return render_template('add_zaehlertyp.html', title='Zählertyp hinzufügen', form=form, legend='Zählertyp hinzufügen')


@app.route("/stammdaten")
def stammdaten():
    return render_template('stammdaten.html', title='Stammdaten')

@app.route("/verwaltung")
def verwaltung():
    return render_template('verwaltung.html', title='Verwaltung')

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    return oauth_provider.unauthorized_response()

@app.route("/post/new", methods=['GET', 'POST'])
@oauth_provider.require_oauth('openid')
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@oauth_provider.require_oauth('openid')
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@oauth_provider.require_oauth('openid')
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))

