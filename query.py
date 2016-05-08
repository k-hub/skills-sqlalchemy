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
b_founded_1903 = Brand.query.filter(Brand.founded=='1903', Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
dc_f_before_1950 = Brand.query.filter((Brand.discontinued == None) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
not_Chev = db.session.query(Model).filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.

        >>> get_model_info(1958)
        Model: Corvette, Brand name: Chevrolet, Headquarters: Detroit, Michigan
        Model: 600, Brand name: BMW, Headquarters: Munich, Bavaria, Germany
        Model: Thunderbird, Brand name: Ford, Headquarters: Dearborn, MI

    '''

    all_from_yr = Model.query.filter(Model.year==year).all() # List of objects.

    for i in range(len(all_from_yr)):
        model = all_from_yr[i].name
        brand = all_from_yr[i].brand_name
        hq = all_from_yr[i].brand.headquarters  # If attribute is None, how do I account for it?

        print "Model: {}, Brand name: {}, Headquarters: {}".format(model, brand, hq)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''


    # brands_models = db.session.query(Brand.name).order_by(Brand.name).all() # List brand tuples in alpha order.

    # models = db.session.query(Model.name).distinct(Model.name).all() # List of model tuples in alpha order.


    brands = db.session.query(Brand).order_by(Brand.name).all() # List of brand objects in alpha order.

    b_m = {}

    for obj in brands:
        b_objs = obj.models  # List of objects. Same brand objects and their respective models.
        # print "\nTEST:\n", b_objs
        for i in range(len(obj.models)):
            # print "\nBRAND:\n", obj.models[i].brand_name
            brand = obj.models[i].brand_name
            # print "\nMOD:\n", obj.models[i].name
            model = obj.models[i].name
            b_m.setdefault(brand, set()).add(model)
    # print "DICTIONARY:\n", b_m

    for brand, models in b_m.items():
        models_joined = ", ".join(models)
        print "BRAND: {}\nMODELS: {}\n".format(brand, models_joined)





# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
    # <flask_sqlalchemy.BaseQuery object at 0x110c61b90>
    # [<Brand id=1 name=Ford>]

    # The datatype is a list.


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
    
    # An association table is a table that connects other tables via their primary key (which will be the foreign key in the association table) and is used to manage a many to many relationship. 

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    '''Find brand names that contain the input string.

    Returns a list of brand objects that contain the input string

        >>> search_brands_by_name('Tes')
        [<Brand id=15 name=Tesla>]


        >>> search_brands_by_name('Ford')
        [<Brand id=1 name=Ford>]
    '''

    contains_mystr = Brand.query.filter(Brand.name.like('%' + mystr + '%')).all()
    return contains_mystr


def get_models_between(start_year, end_year):
    '''Find models between start_year and end_year.

    Returns a list of model objects that contain the models that fall
    between start_year and end_year.

        >>> get_models_between(1960, 1963)
        [<Model id=18 brand_name=Chevrolet model_name=Corvair>, <Model id=19 brand_name=Chevrolet model_name=Corvette>, <Model id=20 brand_name=Fillmore model_name=Fillmore>, <Model id=21 brand_name=Fairthorpe model_name=Rockette>, <Model id=22 brand_name=Austin model_name=Mini Cooper>, <Model id=23 brand_name=Studebaker model_name=Avanti>, <Model id=24 brand_name=Pontiac model_name=Tempest>, <Model id=25 brand_name=Chevrolet model_name=Corvette>, <Model id=26 brand_name=Pontiac model_name=Grand Prix>, <Model id=27 brand_name=Chevrolet model_name=Corvette>, <Model id=28 brand_name=Studebaker model_name=Avanti>, <Model id=29 brand_name=Buick model_name=Special>]

        >>> get_models_between(1909, 1950)
        [<Model id=1 brand_name=Ford model_name=Model T>, <Model id=2 brand_name=Chrysler model_name=Imperial>]
    '''

    models = db.session.query(Model).filter(Model.year >= start_year, Model.year < end_year).all()

    return models






##########################################################################

if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
        print