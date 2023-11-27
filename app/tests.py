from django.test import TestCase

# Create your tests here.

class Test_forms(TestCase):
    def test_abcxyx(self):
        response = self.client.get('/string-2/xyz-there?word=abcxyz')
        self.assertContains(response, True)
    
    def test_abc_xyx(self):
        response = self.client.get('/string-2/xyz-there?word=abc.xyz')
        self.assertContains(response, False)

    def test_xyzabc(self):
        response = self.client.get('/string-2/xyz-there?word=xyz_abc')
        self.assertContains(response, True)

    def test_centered_average_1234100(self):
        response = self.client.get('/list-2/centered-average?n1=1&n2=2&n3=3&n4=4&n5=100&n6=&n7=')
        self.assertContains(response, 3)

    def test_centered_average_11551087(self):
        response = self.client.get('/list-2/centered-average?n1=1&n2=1&n3=5&n4=5&n5=10&n6=8&n7=7')
        self.assertContains(response, 5)

    def test_centered_average_negativenums(self):
        response = self.client.get('/list-2/centered-average?n1=-10&n2=-4&n3=-2&n4=-4&n5=-2&n6=0&n7=')
        self.assertContains(response, -3)
    
    def test_no_teen_sum_123(self):
        response = self.client.get('/logic-2/no-teen-sum?n1=1&n2=2&n3=3')
        self.assertContains(response, 6)

    def test_no_teen_sum_2114(self):
        response = self.client.get('/logic-2/no-teen-sum?n1=2&n2=1&n3=14')
        self.assertContains(response, 3)

    def test_no_teen_sum_2131(self):
        response = self.client.get('/logic-2/no-teen-sum?n1=2&n2=13&n3=1')
        self.assertContains(response, 3)

    def test_front_times_chochocho(self):
        response = self.client.get('/warmup-2/front_times?word=chocolate&length=3&times=3')
        self.assertContains(response, 'chochocho')

    def test_front_times_chocho(self):
        response = self.client.get('/warmup-2/front_times?word=chocolate&length=3&times=2')
        self.assertContains(response, 'chocho')

    def test_front_times_Abc(self):
        response = self.client.get('/warmup-2/front_times?word=Abc&length=3&times=3')
        self.assertContains(response, 'AbcAbcAbc')