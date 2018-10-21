import random

class sampler:
    def __call__(self):
        return random.sample(self.values, 1)[0]

class firstName(sampler):
    values = ['Oma', 'Shasta', 'Nickie', 'Micha', 'Olin', 'Jerry', 'Bernadette', 'Maryland', 'Caroline', 'Kelsie', 'Dana', 'Torie', 'Shara', 'Janay', 'Ashli', 'Kerrie', 'Margot', 'Stephan', 'Nigel', 'Trenton', 'Hildred', 'Toi', 'Mercedes', 'Rodolfo', 'Len', 'Yessenia', 'Kimberli', 'Jerrie', 'Janene', 'Wes', 'Toshia', 'Robert', 'Tari', 'Concetta', 'Wesley', 'Brett', 'Lita', 'Lorrine', 'Ozell', 'Dahlia', 'Noe', 'Sanora', 'Lino', 'Sara', 'Jasper', 'Cherilyn', 'Etha', 'Laurena', 'Piper', 'Luann']

class lastName(sampler):
    values = ['Pullin', 'Leverette', 'Carey', 'Larosa', 'Crosby', 'Freshwater', 'Bogue', 'Do', 'Strayhorn', 'Benedetto', 'Alldredge', 'Sundberg', 'Will', 'Bombardier', 'Brodt', 'Davin', 'Butter', 'Kardos', 'Barile', 'Remy', 'Brim', 'Holtsclaw', 'Delariva', 'Bissette', 'Garfinkel', 'Jerkins', 'Rosso', 'Nickel', 'Kriz', 'Vanwingerden', 'Viger', 'Geise', 'Kellough', 'Kimberling', 'Greenburg', 'Gressett', 'Wensel', 'Gurganus', 'Then', 'Scannell', 'Witherite', 'Piekarski', 'Heisey', 'Drews', 'Brocious', 'Schumaker', 'Fitton', 'Kehrer', 'Allison', 'Dorsey']

class personAge(sampler):
    values = list(range(18, 80))

class database:
    _db = {
        'firstName' : firstName(),
        'lastName' : lastName(),
        'personAge' : personAge()
    }
    def __call__(self, name_str):
        if name_str in self._db:
            return self._db[name_str]()
        else:
            return None
