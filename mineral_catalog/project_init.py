import json, os, sys

# Much of this file was written by chrisrh. chrisrh helped me with
# some unicode errors that this file fixed. I modified some
# of the information to fit my specific program.

# Uses this script file, to find the directory we are currently in.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# First we need the path to the project
# This can be hardcoded, but to be OS capatible
# The 'os' module is what we need
project_path = os.path.join(BASE_DIR)

# This environ variable is so Django module itself can find all our project stuff.
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MYPROJECT.settings")
# notice i changed MYPROJECT to the package that has the settings.py file.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mineral_catalog.settings")

# We want to append our project path to the system so Django can find it.
sys.path.append(project_path)

# This is so my local_settings.py gets loaded.
# os.chdir(proj_path)

# This will ensure our project models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.utils import timezone
from minerals.models import Mineral

current_location = os.path.dirname(os.path.abspath(__file__))
file_location = os.path.join(current_location, 'minerals/fixtures/minerals_json.json')

def minerals_dictionary():
    with open(file_location, encoding="utf-8") as jsonfile:
        minerals = json.load(jsonfile)
        return minerals


def populate_database():
    # I can use my app models now...
    mineral_json = minerals_dictionary()
    for item in mineral_json:
        alpha = Mineral()
        alpha.name = item['name']
        alpha.image_filename = item['image filename']
        alpha.image_caption = item['image caption']
        alpha.category = item['category']
        try:
            alpha.formula = item['formula']
        except KeyError:
            pass
        try:
            alpha.strunz_classification = item['strunz classification']
        except KeyError:
            pass
        try:
            alpha.color = item['color']
        except KeyError:
            pass
        try:
            alpha.crystal_system = item['crystal system']
        except KeyError:
            pass
        try:
            alpha.cleavage = item['cleavage']
        except KeyError:
            pass
        try:
            alpha.mohs_scale_hardness=item['mohs scale hardness']
        except KeyError:
            pass
        try:
            alpha.luster=item['luster']
        except KeyError:
            pass
        try:
            alpha.streak=item['streak']
        except KeyError:
            pass
        try:
            alpha.diaphaneity=item['diaphaneity']
        except KeyError:
            pass
        try:
            alpha.optical_properties=item['optical properties']
        except KeyError:
            pass
        try:
            alpha.refractive_index=item['refractive index']
        except KeyError:
            pass
        try:
            alpha.crystal_habit=item['crystal habit']
        except KeyError:
            pass
        try:
            alpha.specific_gravity=item['specific gravity']
        except KeyError:
            pass
        alpha.group=item['group']
        alpha.save()


if __name__ == '__main__':
    populate_database() # run our script and we can use our django apps now.
