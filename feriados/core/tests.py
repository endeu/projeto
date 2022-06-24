from core.FeriadosAPI import FeriadoAPI
from core.forms import FeriadoForm
from core.models import FeriadoModel
from datetime import datetime
from django.test import TestCase

class FeriadoTest(TestCase):    
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'feriado')
        
    def test_template_feriado(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')

class FeriadoModelTest(TestCase):
    def setUp(self):
        self.feriado = 'natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel(
            nome=self.feriado,
            dia=self.dia,
            mes=self.mes,
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)
        
    def test_nome_feriado(self):
        nome = self.cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, self.feriado)
        
    def test_dia_feriado(self):
        dia = self.cadastro.__dict__.get('dia', '')
        self.assertEqual(dia, self.dia)

class FeriadoFormTest(TestCase):
    def test_form_has_fields(self):
        form = FeriadoForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome='dia de são nunca')
        self.assertEqual('DIA DE SÃO NUNCA', form.cleaned_data['nome'])

    def test_must_be_capitalized(self):
        form = self.make_validated_form()
        self.assertEqual('TIRADENTES', form.cleaned_data['nome'])

    def make_validated_form(self, **kwargs):
        valid =  dict(
            nome='Tiradentes',
            dia=14,
            mes=4
        )
        data = dict(valid, **kwargs)
        form = FeriadoForm(data)
        form.is_valid()
        return form

class TestFeriadoAPI:

    def test_instanciar_objeto(self):
        objeto = FeriadoAPI(2022)
        assert objeto._ano, 2022
        assert type(objeto.feriados) == list
        assert len(objeto.feriados) == 11

    def test_str_repr(self):
        objeto = FeriadoAPI(2023)
        msg = 'Feriados de 2023'
        assert str(objeto) == msg
        assert repr(objeto) == msg

    def test_str_repr2(self):
        objeto = FeriadoAPI(2022)
        msg = 'Feriados de 2022'
        assert str(objeto) == msg
        assert repr(objeto) == msg

    def test_properties(self):
        objeto = FeriadoAPI(2022)
        assert objeto.ano == '2022'