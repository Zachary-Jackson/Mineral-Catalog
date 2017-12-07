from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTests(TestCase):
    '''This tests to see if the Mineral model works.'''
    def test_model_creation(self):
        # The following mineral does not contain correct charactiristics
        mineral = Mineral.objects.create(
            name='Abelsonite',
            image_filename='240px-Abelsonite.jpg',
            image_caption='Abelsonite from the Green River Formation',
            category='Organic',
            formula='C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni',
            strunz_classification='10.CA.20',
            color='Pink-purple',
            crystal_system='Tetragonal',
            unit_cell='a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β',
            crystal_symmetry='Space group: P1',
            cleavage='Probable on {111}',
            mohs_scale_hardness='2-3',
            luster='Adamantine, sub-metallic',
            streak='Pink',
            diaphaneity='Semitransparent',
            optical_properties='Biaxial',
            refractive_index='',
            crystal_habit='',
            specific_gravity='7.20 - 7.22',
            group='Sulfides'
        )
        self.assertEqual(mineral.name, 'Abelsonite')


class MineralViewsTests(TestCase):
    '''This tests to see if the mineral views work.'''
    def setUp(self):
        '''This sets up a Mineral instance to test.'''
        self.mineral = Mineral.objects.create(
            name='Abelsonite',
            image_filename='240px-Abelsonite.jpg',
            image_caption='Abelsonite from the Green River Formation',
            category='Organic',
            formula='C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni',
            strunz_classification='10.CA.20',
            color='Pink-purple',
            crystal_system='Tetragonal',
            unit_cell='a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β',
            crystal_symmetry='Space group: P1',
            cleavage='Probable on {111}',
            mohs_scale_hardness='2-3',
            luster='Adamantine, sub-metallic',
            streak='Pink',
            diaphaneity='Semitransparent',
            optical_properties='Biaxial',
            refractive_index='',
            crystal_habit='',
            specific_gravity='7.20 - 7.22',
            group='Sulfides'
        )
        self.mineral2 = Mineral.objects.create(
            name='Salt',
            image_filename='240px-Salt.jpg',
            image_caption='Salt from the Green River Formation',
            category='Organic',
            formula='C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni',
            strunz_classification='10.CA.20',
            color='Pink-purple',
            crystal_system='Tetragonal',
            unit_cell='a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β',
            crystal_symmetry='Space group: P1',
            cleavage='Probable on {111}',
            mohs_scale_hardness='2-3',
            luster='Adamantine, sub-metallic',
            streak='Pink',
            diaphaneity='Semitransparent',
            optical_properties='Biaxial',
            refractive_index='',
            crystal_habit='',
            specific_gravity='7.20 - 7.22',
            group='Sulfides'
        )

    def test_mineral_list_view(self):
        '''This tests the main homepage for minerals.'''
        resp = self.client.get(reverse('minerals:home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)
        self.assertContains(resp, self.mineral2.name)

    def test_mineral_detail_view(self):
        '''This tests the detail view for minerals.'''
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertContains(resp, self.mineral.name)
        self.assertContains(resp, self.mineral.color)

    def test_random_mineral_detail_view(self):
        '''This tests the random view for minerals.'''
        resp = self.client.get(reverse('minerals:random_mineral'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        # The following two self.assertContains user mineral charactiristics
        # common to both mineral and mineral2
        self.assertContains(resp, self.mineral.optical_properties)
        self.assertContains(resp, self.mineral.diaphaneity)
