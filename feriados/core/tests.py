from django.test import TestCase
class NatalTest(TestCase):
    
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'feriado')
        
    def test_template_feriado(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')