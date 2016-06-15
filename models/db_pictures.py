db.define_table('picture',
                Field('name',requires=IS_NOT_EMPTY()),
                Field('profile','text',length=1000),
                Field('picture','upload'))
