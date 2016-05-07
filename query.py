"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
brand_8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
corvette_chev = Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()
# Get all models that are older than 1960.
m_older_1960 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
b_after_1920 = db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
m_cor = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
b_founded_1903 = Brand.query.filter(Brand.founded=='1903', Brand.discontinued == None).alls()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
dc_f_before_1950 = Brand.query.filter((Brand.discontinued == None) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
not_Chev = db.session.query(Model).filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    all_from_yr = Model.query.filter(Model.year==year).all()

    for i in range(len(all_from_yr)):
        model = all_from_yr[i].name
        brand = all_from_yr[i].brand_name
        hq = all_from_yr[i].brand.headquarters  # If attribute is None, how do you account for it?

        print "Model: {}, Brand name: {}, Headquarters: {}".format(model, brand, hq)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands_models = db.session.query(Brand.name, Model.name).all() # list of brand, model tuples

    for i in range(len(brands_models)):
        tup = brands_models[i]
        for brand, model in tup:
            print 

    

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass