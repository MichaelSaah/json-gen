import random, string, time
from datetime import datetime


# building blocks - not exposed to API

class sampler:
    def __call__(self):
        return random.sample(self.values, 1)[0]
    def contains(self, x):
        return x in self.values

class integer_between:
    @staticmethod
    def __call__(l, u):
        if l > u:
            raise ValueError('The lower bound must be less than or equal to the upper bound')
        return random.sample(range(l, u+1), 1)[0]

class float_between:
    @staticmethod
    def __call__(l, u, k=None):
        width = u - l
        f =  random.random() * width + l
        if k:
            return round(f, k)
        else:
            return f

# tester

class _tester(sampler):
    values = ['hello', 'world']


# names

class firstNameMale(sampler):
    values = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Charles', 'Joseph', 'Thomas', 'Christopher', 'Daniel', 'Paul', 'Mark', 'Donald', 'George', 'Kenneth', 'Steven', 'Edward', 'Brian', 'Ronald', 'Anthony', 'Kevin', 'Jason', 'Matthew', 'Gary', 'Timothy', 'Jose', 'Larry', 'Jeffrey', 'Frank', 'Scott', 'Eric', 'Stephen', 'Andrew', 'Raymond', 'Gregory', 'Joshua', 'Jerry', 'Dennis', 'Walter', 'Patrick', 'Peter', 'Harold', 'Douglas', 'Henry', 'Carl', 'Arthur', 'Ryan', 'Roger', 'Joe', 'Juan', 'Jack', 'Albert', 'Jonathan', 'Justin', 'Terry', 'Gerald', 'Keith', 'Samuel', 'Willie', 'Ralph', 'Lawrence', 'Nicholas', 'Roy', 'Benjamin', 'Bruce', 'Brandon', 'Adam', 'Harry', 'Fred', 'Wayne', 'Billy', 'Steve', 'Louis', 'Jeremy', 'Aaron', 'Randy', 'Howard', 'Eugene', 'Carlos', 'Russell', 'Bobby', 'Victor', 'Martin', 'Ernest', 'Phillip', 'Todd', 'Jesse', 'Craig', 'Alan', 'Shawn', 'Clarence', 'Sean', 'Philip', 'Chris', 'Johnny', 'Earl', 'Jimmy', 'Antonio', 'Danny', 'Bryan', 'Tony', 'Luis', 'Mike', 'Stanley', 'Leonard', 'Nathan', 'Dale', 'Manuel', 'Rodney', 'Curtis', 'Norman', 'Allen', 'Marvin', 'Vincent', 'Glenn', 'Jeffery', 'Travis', 'Jeff', 'Chad', 'Jacob', 'Lee', 'Melvin', 'Alfred', 'Kyle', 'Francis', 'Bradley', 'Jesus', 'Herbert', 'Frederick', 'Ray', 'Joel', 'Edwin', 'Don', 'Eddie', 'Ricky', 'Troy', 'Randall', 'Barry', 'Alexander', 'Bernard', 'Mario', 'Leroy', 'Francisco', 'Marcus', 'Micheal', 'Theodore', 'Clifford', 'Miguel', 'Oscar', 'Jay', 'Jim', 'Tom', 'Calvin', 'Alex', 'Jon', 'Ronnie', 'Bill', 'Lloyd', 'Tommy', 'Leon', 'Derek', 'Warren', 'Darrell', 'Jerome', 'Floyd', 'Leo', 'Alvin', 'Tim', 'Wesley', 'Gordon', 'Dean', 'Greg', 'Jorge', 'Dustin', 'Pedro', 'Derrick', 'Dan', 'Lewis', 'Zachary', 'Corey', 'Herman', 'Maurice', 'Vernon', 'Roberto', 'Clyde', 'Glen', 'Hector', 'Shane', 'Ricardo', 'Sam', 'Rick', 'Lester', 'Brent', 'Ramon', 'Charlie', 'Tyler', 'Gilbert', 'Gene', 'Marc', 'Reginald', 'Ruben', 'Brett', 'Angel', 'Nathaniel', 'Rafael', 'Leslie', 'Edgar', 'Milton', 'Raul', 'Ben', 'Chester', 'Cecil', 'Duane', 'Franklin', 'Andre', 'Elmer', 'Brad', 'Gabriel', 'Ron', 'Mitchell', 'Roland', 'Arnold', 'Harvey', 'Jared', 'Adrian', 'Karl', 'Cory', 'Claude', 'Erik', 'Darryl', 'Jamie', 'Neil', 'Jessie', 'Christian', 'Javier', 'Fernando', 'Clinton', 'Ted', 'Mathew', 'Tyrone', 'Darren', 'Lonnie', 'Lance', 'Cody', 'Julio', 'Kelly', 'Kurt', 'Allan', 'Nelson', 'Guy', 'Clayton', 'Hugh', 'Max', 'Dwayne', 'Dwight', 'Armando', 'Felix', 'Jimmie', 'Everett', 'Jordan', 'Ian', 'Wallace', 'Ken', 'Bob', 'Jaime', 'Casey', 'Alfredo', 'Alberto', 'Dave', 'Ivan', 'Johnnie', 'Sidney', 'Byron', 'Julian', 'Isaac', 'Morris', 'Clifton', 'Willard', 'Daryl', 'Ross', 'Virgil', 'Andy', 'Marshall', 'Salvador', 'Perry', 'Kirk', 'Sergio', 'Marion', 'Tracy', 'Seth', 'Kent', 'Terrance', 'Rene', 'Eduardo', 'Terrence', 'Enrique', 'Freddie', 'Wade', 'Austin', 'Stuart', 'Fredrick', 'Arturo', 'Alejandro', 'Jackie', 'Joey', 'Nick', 'Luther', 'Wendell', 'Jeremiah', 'Evan', 'Julius', 'Dana', 'Donnie', 'Otis', 'Shannon', 'Trevor', 'Oliver', 'Luke', 'Homer', 'Gerard', 'Doug', 'Kenny', 'Hubert', 'Angelo', 'Shaun', 'Lyle', 'Matt', 'Lynn', 'Alfonso', 'Orlando', 'Rex', 'Carlton', 'Ernesto', 'Cameron', 'Neal', 'Pablo', 'Lorenzo', 'Omar', 'Wilbur', 'Blake', 'Grant', 'Horace', 'Roderick', 'Kerry', 'Abraham', 'Willis', 'Rickey', 'Jean', 'Ira', 'Andres', 'Cesar', 'Johnathan', 'Malcolm', 'Rudolph', 'Damon', 'Kelvin', 'Rudy', 'Preston', 'Alton', 'Archie', 'Marco', 'Wm', 'Pete', 'Randolph', 'Garry', 'Geoffrey', 'Jonathon', 'Felipe', 'Bennie', 'Gerardo', 'Ed', 'Dominic', 'Robin', 'Loren', 'Delbert', 'Colin', 'Guillermo', 'Earnest', 'Lucas', 'Benny', 'Noel', 'Spencer', 'Rodolfo', 'Myron', 'Edmund', 'Garrett', 'Salvatore', 'Cedric', 'Lowell', 'Gregg', 'Sherman', 'Wilson', 'Devin', 'Sylvester', 'Kim', 'Roosevelt', 'Israel', 'Jermaine', 'Forrest', 'Wilbert', 'Leland', 'Simon', 'Guadalupe', 'Clark', 'Irving', 'Carroll', 'Bryant', 'Owen', 'Rufus', 'Woodrow', 'Sammy', 'Kristopher', 'Mack', 'Levi', 'Marcos', 'Gustavo', 'Jake', 'Lionel', 'Marty', 'Taylor', 'Ellis', 'Dallas', 'Gilberto', 'Clint', 'Nicolas', 'Laurence', 'Ismael', 'Orville', 'Drew', 'Jody', 'Ervin', 'Dewey', 'Al', 'Wilfred', 'Josh', 'Hugo', 'Ignacio', 'Caleb', 'Tomas', 'Sheldon', 'Erick', 'Frankie', 'Stewart', 'Doyle', 'Darrel', 'Rogelio', 'Terence', 'Santiago', 'Alonzo', 'Elias', 'Bert', 'Elbert', 'Ramiro', 'Conrad', 'Pat', 'Noah', 'Grady', 'Phil', 'Cornelius', 'Lamar', 'Rolando', 'Clay', 'Percy', 'Dexter', 'Bradford', 'Merle', 'Darin', 'Amos', 'Terrell', 'Moses', 'Irvin', 'Saul', 'Roman', 'Darnell', 'Randal', 'Tommie', 'Timmy', 'Darrin', 'Winston', 'Brendan', 'Toby', 'Van', 'Abel', 'Dominick', 'Boyd', 'Courtney', 'Jan', 'Emilio', 'Elijah', 'Cary', 'Domingo', 'Santos', 'Aubrey', 'Emmett', 'Marlon', 'Emanuel', 'Jerald', 'Edmond']

class firstNameFemale(sampler):
    values = ['Mary', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Jennifer', 'Maria', 'Susan', 'Margaret', 'Dorothy', 'Lisa', 'Nancy', 'Karen', 'Betty', 'Helen', 'Sandra', 'Donna', 'Carol', 'Ruth', 'Sharon', 'Michelle', 'Laura', 'Sarah', 'Kimberly', 'Deborah', 'Jessica', 'Shirley', 'Cynthia', 'Angela', 'Melissa', 'Brenda', 'Amy', 'Anna', 'Rebecca', 'Virginia', 'Kathleen', 'Pamela', 'Martha', 'Debra', 'Amanda', 'Stephanie', 'Carolyn', 'Christine', 'Marie', 'Janet', 'Catherine', 'Frances', 'Ann', 'Joyce', 'Diane', 'Alice', 'Julie', 'Heather', 'Teresa', 'Doris', 'Gloria', 'Evelyn', 'Jean', 'Cheryl', 'Mildred', 'Katherine', 'Joan', 'Ashley', 'Judith', 'Rose', 'Janice', 'Kelly', 'Nicole', 'Judy', 'Christina', 'Kathy', 'Theresa', 'Beverly', 'Denise', 'Tammy', 'Irene', 'Jane', 'Lori', 'Rachel', 'Marilyn', 'Andrea', 'Kathryn', 'Louise', 'Sara', 'Anne', 'Jacqueline', 'Wanda', 'Bonnie', 'Julia', 'Ruby', 'Lois', 'Tina', 'Phyllis', 'Norma', 'Paula', 'Diana', 'Annie', 'Lillian', 'Emily', 'Robin', 'Peggy', 'Crystal', 'Gladys', 'Rita', 'Dawn', 'Connie', 'Florence', 'Tracy', 'Edna', 'Tiffany', 'Carmen', 'Rosa', 'Cindy', 'Grace', 'Wendy', 'Victoria', 'Edith', 'Kim', 'Sherry', 'Sylvia', 'Josephine', 'Thelma', 'Shannon', 'Sheila', 'Ethel', 'Ellen', 'Elaine', 'Marjorie', 'Carrie', 'Charlotte', 'Monica', 'Esther', 'Pauline', 'Emma', 'Juanita', 'Anita', 'Rhonda', 'Hazel', 'Amber', 'Eva', 'Debbie', 'April', 'Leslie', 'Clara', 'Lucille', 'Jamie', 'Joanne', 'Eleanor', 'Valerie', 'Danielle', 'Megan', 'Alicia', 'Suzanne', 'Michele', 'Gail', 'Bertha', 'Darlene', 'Veronica', 'Jill', 'Erin', 'Geraldine', 'Lauren', 'Cathy', 'Joann', 'Lorraine', 'Lynn', 'Sally', 'Regina', 'Erica', 'Beatrice', 'Dolores', 'Bernice', 'Audrey', 'Yvonne', 'Annette', 'June', 'Samantha', 'Marion', 'Dana', 'Stacy', 'Ana', 'Renee', 'Ida', 'Vivian', 'Roberta', 'Holly', 'Brittany', 'Melanie', 'Loretta', 'Yolanda', 'Jeanette', 'Laurie', 'Katie', 'Kristen', 'Vanessa', 'Alma', 'Sue', 'Elsie', 'Beth', 'Jeanne', 'Vicki', 'Carla', 'Tara', 'Rosemary', 'Eileen', 'Terri', 'Gertrude', 'Lucy', 'Tonya', 'Ella', 'Stacey', 'Wilma', 'Gina', 'Kristin', 'Jessie', 'Natalie', 'Agnes', 'Vera', 'Willie', 'Charlene', 'Bessie', 'Delores', 'Melinda', 'Pearl', 'Arlene', 'Maureen', 'Colleen', 'Allison', 'Tamara', 'Joy', 'Georgia', 'Constance', 'Lillie', 'Claudia', 'Jackie', 'Marcia', 'Tanya', 'Nellie', 'Minnie', 'Marlene', 'Heidi', 'Glenda', 'Lydia', 'Viola', 'Courtney', 'Marian', 'Stella', 'Caroline', 'Dora', 'Jo', 'Vickie', 'Mattie', 'Terry', 'Maxine', 'Irma', 'Mabel', 'Marsha', 'Myrtle', 'Lena', 'Christy', 'Deanna', 'Patsy', 'Hilda', 'Gwendolyn', 'Jennie', 'Nora', 'Margie', 'Nina', 'Cassandra', 'Leah', 'Penny', 'Kay', 'Priscilla', 'Naomi', 'Carole', 'Brandy', 'Olga', 'Billie', 'Dianne', 'Tracey', 'Leona', 'Jenny', 'Felicia', 'Sonia', 'Miriam', 'Velma', 'Becky', 'Bobbie', 'Violet', 'Kristina', 'Toni', 'Misty', 'Mae', 'Shelly', 'Daisy', 'Ramona', 'Sherri', 'Erika', 'Katrina', 'Claire', 'Lindsey', 'Lindsay', 'Geneva', 'Guadalupe', 'Belinda', 'Margarita', 'Sheryl', 'Cora', 'Faye', 'Ada', 'Natasha', 'Sabrina', 'Isabel', 'Marguerite', 'Hattie', 'Harriet', 'Molly', 'Cecilia', 'Kristi', 'Brandi', 'Blanche', 'Sandy', 'Rosie', 'Joanna', 'Iris', 'Eunice', 'Angie', 'Inez', 'Lynda', 'Madeline', 'Amelia', 'Alberta', 'Genevieve', 'Monique', 'Jodi', 'Janie', 'Maggie', 'Kayla', 'Sonya', 'Jan', 'Lee', 'Kristine', 'Candace', 'Fannie', 'Maryann', 'Opal', 'Alison', 'Yvette', 'Melody', 'Luz', 'Susie', 'Olivia', 'Flora', 'Shelley', 'Kristy', 'Mamie', 'Lula', 'Lola', 'Verna', 'Beulah', 'Antoinette', 'Candice', 'Juana', 'Jeannette', 'Pam', 'Kelli', 'Hannah', 'Whitney', 'Bridget', 'Karla', 'Celia', 'Latoya', 'Patty', 'Shelia', 'Gayle', 'Della', 'Vicky', 'Lynne', 'Sheri', 'Marianne', 'Kara', 'Jacquelyn', 'Erma', 'Blanca', 'Myra', 'Leticia', 'Pat', 'Krista', 'Roxanne', 'Angelica', 'Johnnie', 'Robyn', 'Francis', 'Adrienne', 'Rosalie', 'Alexandra', 'Brooke', 'Bethany', 'Sadie', 'Bernadette', 'Traci', 'Jody', 'Kendra', 'Jasmine', 'Nichole', 'Rachael', 'Chelsea', 'Mable', 'Ernestine', 'Muriel', 'Marcella', 'Elena', 'Krystal', 'Angelina', 'Nadine', 'Kari', 'Estelle', 'Dianna', 'Paulette', 'Lora', 'Mona', 'Doreen', 'Rosemarie', 'Angel', 'Desiree', 'Antonia', 'Hope', 'Ginger', 'Janis', 'Betsy', 'Christie', 'Freda', 'Mercedes', 'Meredith', 'Lynette', 'Teri', 'Cristina', 'Eula', 'Leigh', 'Meghan', 'Sophia', 'Eloise', 'Rochelle', 'Gretchen', 'Cecelia', 'Raquel', 'Henrietta', 'Alyssa', 'Jana', 'Kelley', 'Gwen', 'Kerry', 'Jenna', 'Tricia', 'Laverne', 'Olive', 'Alexis', 'Tasha', 'Silvia', 'Elvira', 'Casey', 'Delia', 'Sophie', 'Kate', 'Patti', 'Lorena', 'Kellie', 'Sonja', 'Lila', 'Lana', 'Darla', 'May', 'Mindy', 'Essie', 'Mandy', 'Lorene', 'Elsa', 'Josefina', 'Jeannie', 'Miranda', 'Dixie', 'Lucia', 'Marta', 'Faith', 'Lela', 'Johanna', 'Shari', 'Camille', 'Tami', 'Shawna', 'Elisa', 'Ebony', 'Melba', 'Ora', 'Nettie', 'Tabitha', 'Ollie', 'Jaime', 'Winifred', 'Kristie']

class firstName:
    male_name = firstNameMale()
    female_name = firstNameFemale()

    def __call__(self):
        if random.getrandbits(1):
            return self.male_name()
        else:
            return self.female_name()

class middleInit(sampler):
    values = list(string.ascii_uppercase)

class lastName(sampler):
    values = ['Pullin', 'Leverette', 'Carey', 'Larosa', 'Crosby', 'Freshwater', 'Bogue', 'Do', 'Strayhorn', 'Benedetto', 'Alldredge', 'Sundberg', 'Will', 'Bombardier', 'Brodt', 'Davin', 'Butter', 'Kardos', 'Barile', 'Remy', 'Brim', 'Holtsclaw', 'Delariva', 'Bissette', 'Garfinkel', 'Jerkins', 'Rosso', 'Nickel', 'Kriz', 'Vanwingerden', 'Viger', 'Geise', 'Kellough', 'Kimberling', 'Greenburg', 'Gressett', 'Wensel', 'Gurganus', 'Then', 'Scannell', 'Witherite', 'Piekarski', 'Heisey', 'Drews', 'Brocious', 'Schumaker', 'Fitton', 'Kehrer', 'Allison', 'Dorsey']

class suffix(sampler): # male only
    values = ['Jr.', 'Jr', 'Sr', 'Sr.', 'II', 'III', 'IV']

class prefixMale(sampler):
    values = ['Dr.', 'Mr.', 'Sir']

class prefixFemale(sampler):
    values = ['Dr.', 'Mrs.', 'Ms.', 'Miss', 'Madam']

class prefix:
    male_pf = prefixMale()
    fem_pf = prefixFemale()

    def __call__(self):
        if random.getrandbits(1):
            return self.male_pf()
        else:
            return self.fem_pf()

class fullName:
    male_name = firstNameMale()
    female_name = firstNameFemale()
    suffix = suffix()
    prefix_male = prefixMale()
    prefix_female = prefixFemale()
    last_name = lastName()

    def __call__(self):
        if random.getrandbits(1):
            return self.prefix_male() + ' ' + self.male_name() + ' ' \
               + self.male_name() + ' ' + self.last_name()
        else:
            return self.prefix_female() + ' ' + self.female_name() + ' ' \
               + self.female_name() + ' ' + self.last_name()


# person

class personAge(sampler):
    values = list(range(18, 80))

class personSex(sampler):
    values = ['Male', 'Female']


# phone numbers

class localNumber:
    l = 1000000000
    u = 9999999999
    ib = integer_between()
    def __call__(self):
        return str(self.ib(self.l, self.u))

class internationalCode:
    l = 1
    u = 999
    ib = integer_between()
    def __call__(self):
        return '+' + str(self.ib(self.l, self.u))

class areaCode:
    l = 100
    u = 999
    ib = integer_between()
    def __call__(self):
        return str(self.ib(self.l, self.u))

class phoneExtension:
    l = 10
    u = 9999
    ib = integer_between()
    def __call__(self):
        return 'x' + str(self.ib(self.l, self.u))

class internationalNumber:
    local = localNumber()
    code = internationalCode()
    def __call__(self):
        return code() + ' ' + local()

# email

class eMail_domain(sampler):
    values = ['hotmail.com', 'gmail.com', 'yahoo.com', 'comcast.net', 'verizon.net']

class eMail_number(sampler):
    values = list(map(str, range(100,1000)))

class eMail:
    names = firstName()
    domains = eMail_domain()
    numbers = eMail_number()
    def __call__(self):
        return self.names() + self.numbers() + '@' + self.domains()


# date/time

class time_formatter: # TODO: check source for possible exceptions
    def __call__(self, format, ts):
        return time.strftime(format, time.gmtime(ts))

class timeZone(sampler):
    values = ['UTC−12:00', 'UTC−11:00', 'UTC−10:00', 'UTC−09:30', 'UTC−09:00', 'UTC−08:00', 'UTC−07:00', 'UTC−06:00', 'UTC−05:00', 'UTC−04:00', 'UTC−03:30', 'UTC−03:00', 'UTC−02:00', 'UTC−01:00', 'UTC±00:00', 'UTC+01:00', 'UTC+02:00', 'UTC+03:00', 'UTC+03:30', 'UTC+04:00', 'UTC+04:30', 'UTC+05:00', 'UTC+05:30', 'UTC+05:45', 'UTC+06:00', 'UTC+06:30', 'UTC+07:00', 'UTC+08:00', 'UTC+08:45', 'UTC+09:00', 'UTC+09:30', 'UTC+10:00', 'UTC+10:30', 'UTC+11:00', 'UTC+12:00', 'UTC+12:45', 'UTC+13:00', 'UTC+14:00']

class timeUnix:
    def __call__(self):
        return int(time.time())

class timeNow:
    tf = time_formatter()
    def __call__(self, format='%H:%M:%S'):
        return self.tf(format, int(time.time()))

class timeRandom:
    tf = time_formatter()
    def __call__(self, format='%H:%M:%S'):
        rt = random.sample(range(-1262304000, int(time.time())), 1)[0] # start time is jan 1, 1930
        return self.tf(format, rt)


# numbers

class numberInt:
#TODO: test
    ib = integer_between()
    def __call__(self, l=-2**31, u=2**31):
        l = int(l)
        u = int(u)
        return self.ib(l, u)

class numberFloat:
#TODO: test
    fb = float_between()
    def __call__(self, l=-2**31, u=2**31, k=None):
        l = float(l)
        u = float(u)
        if k:
            k = int(k)
        return self.fb(l, u, k)


class database:
    _db = {
        # tester
        '_tester' : _tester(),

        # names
        'firstName' : firstName(), # random gender
        'lastName' : lastName(),
        'middleInit': middleInit(),
        'fullName': fullName(), # matching random gender
        'prefix' : prefix(), # random gender
        'suffix' : suffix(), # generally male

        # person
        'personAge' : personAge(),
        'personSex' : personSex(),

        # email
        'eMail' : eMail(),

        # phone
        'localNumber': localNumber(),
        'internationalCode': internationalCode(),
        'areaCode': areaCode(),
        'phoneExtension': phoneExtension(),
        'internationalNumber': internationalNumber(),

        # time
        'timeZone' : timeZone(),
        'timeNow' : timeNow(),
        'timeUnix' : timeUnix(),
        'timeRandom' : timeRandom(),

        # numbers
        'numberInt' : numberInt(),
        'numberFloat' : numberFloat(),
    }

    def __call__(self, args_str):
        args = args_str.split('|')

        if args[0] == 'array' and len(args) >= 3:
            args.pop(0) # throw away array keyword
            n = args.pop(0)
            try:
                n = int(n)
            except ValueError:
                return args_str
            if n < 0 or args[0] not in self._db:
                return args_str

            items = []
            
            try:
                for _ in range(n):
                    if len(args) == 1:
                        items.append(self._db[args[0]]())
                    else:
                        items.append(self._db[args[0]](*args[1:]))
            except ValueError:
                return args_str
                    
            return items

        elif args[0] in self._db:
            try:
                if len(args) == 1:
                    return self._db[args[0]]()
                else:
                    return self._db[args[0]](*args[1:])
            except ValueError:
                return args_str
        else:
            return args_str

