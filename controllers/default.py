# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
	
    return dict(form=auth())

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    if auth.user: redirect(URL('main'))
    return dict()
    

def write():
    import datetime
    import gluon.contrib.rss2 as rss2
    import gluon.contrib.feedparser as feedparser
    d = feedparser.parse('http://rss.slashdot.org/Slashdot/slashdot/to')

    rss = rss2.RSS2(title=d.channel.title, link=d.channel.link,
                    description=d.channel.description,
                    lastBuildDate=datetime.datetime.now(),
                    items=[rss2.RSSItem(title=entry.title,
                    link=entry.link, description=entry.description,
                    pubDate=datetime.datetime.now()) for entry in
                    d.entries])
    response.headers['Content-Type'] = 'application/rss+xml'
    return rss.to_xml(encoding='utf-8')
    

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


def examples():
    return response.render()
def support():
    return response.render()

def xml():
    return dict(message=XML('<h1>text is not escaped</h1>'))
    """.strip(),language='web2py',link=URL('global','vars'),_class='boxCode')}}<b>and view: template_examples/xml.html</b>
    {{=CODE(open(os.path.join(request.folder,'views/template_examples/xml.html'),'r').read(),language='html',link=URL('global','vars'),_class='boxCode')}}
    <p>If you do not want to escape the argument of  &#123;&#123;=...&#125;&#125; mark it as XML.
    <br/>Try it here: <a class="btn" href="/{{=request.application}}/template_examples/xml">xml</a></p>

    <h3>Example {{=c}}{{c+=1}}</h3><b>In controller: template_examples.py </b>
    {{=CODE("""
	
	
def form():
    """ a simple entry form with various types of objects """

    form = FORM(TABLE(        
        TR('Proile', TEXTAREA(_name='profile',
           value='write something here')),
        TR('', INPUT(_type='submit', _value='SUBMIT')),
    ))
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form is invalid'
    else:
        response.flash = 'please fill the form'
    return dict(form=form, vars=form.vars)
# def next():
    # return dict()



def main():    
    pictures = db(db.picture).select(orderby=db.picture.name.upper())
    return dict(pictures=pictures)

def add_pictures():
 
    f = SQLFORM(db.picture).process()
    if f.accepted:
        session.flash = 'picture inserted'
        redirect(URL('main'))
    return dict(f=f)

	
	
def edit_picture():
    picture_id = request.args(0,cast=int)
   
    picture = db.picture(picture_id)
    if not picture:
        redirect(URL('main'))
    f = SQLFORM(db.picture,picture).process()
    if f.accepted:
        session.flash = 'picture edited'
        redirect(URL('main'))
    return dict(f=f)